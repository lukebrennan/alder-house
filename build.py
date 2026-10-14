#!/usr/bin/env python3
"""Build the static site into dist/.

    python3 build.py           # build
    python3 build.py --serve   # build, then preview at http://localhost:8000

Environment:
    SITE_ORIGIN  e.g. https://username.github.io   (canonical/OG URLs and the sitemap)
    BASE_PATH    e.g. /alder-house                  (blank for a custom domain or user site)

Performance work done here: CSS is concatenated, pruned of rules no page uses and minified; the ES modules in
static/js are bundled into one deferred script; CSS and JS URLs carry a content hash so deploys are never stale.
"""
from __future__ import annotations

import functools
import hashlib
import http.server
import json
import re
import shutil
import socketserver
import sys
from pathlib import Path

from alder import config as C
from alder.pages import book, contact, dining, explore, home, journal, legal, notfound, stay, story

ROOT = Path(__file__).parent
DIST = ROOT / "dist"
STATIC = ROOT / "static"
CSS_ORDER = ["00-tokens", "10-base", "20-layout", "30-components", "40-sections", "50-pages", "90-motion"]
JS_ORDER = ["curtain", "split", "header", "reveal", "accordion", "lightbox", "datepicker", "forms", "map",
            "filter", "booking", "prefetch"]
CSS_VERSION_TOKEN = "__CSS_VERSION__"


# ------------------------------------------------------------------ CSS ----
def minify_css(css: str) -> str:
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    css = re.sub(r"\s+", " ", css)
    css = re.sub(r"\s*([{};,>])\s*", r"\1", css)
    css = re.sub(r":\s+", ":", css)
    return css.replace(";}", "}").strip()


def _split_top(s: str, sep: str = ",") -> list[str]:
    """Split on `sep` outside parentheses/brackets."""
    out, depth, cur = [], 0, ""
    for ch in s:
        if ch in "([":
            depth += 1
        elif ch in ")]":
            depth -= 1
        if ch == sep and depth == 0:
            out.append(cur)
            cur = ""
        else:
            cur += ch
    out.append(cur)
    return out


def _blocks(css: str):
    """Yield (prelude, body) for each top-level block in a CSS string."""
    i, n = 0, len(css)
    while i < n:
        j = css.find("{", i)
        if j == -1:
            break
        depth, k = 1, j + 1
        while k < n and depth:
            depth += {"{": 1, "}": -1}.get(css[k], 0)
            k += 1
        yield css[i:j].strip(), css[j + 1:k - 1]
        i = k


def prune_css(css: str, words: set[str]) -> str:
    """Drop rules whose class selectors never appear in any page or script. Classes inside :not() are ignored
    so a selector like `a:not(.x)` is never removed."""
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)

    def keep_selector(sel: str) -> bool:
        probe = re.sub(r":not\((?:[^()]|\([^()]*\))*\)", "", sel)
        return all(c in words for c in re.findall(r"\.([A-Za-z_][\w-]*)", probe))

    out = []
    for prelude, body in _blocks(css):
        if prelude.startswith("@"):
            if prelude.startswith(("@font-face", "@keyframes", "@view-transition", "@property")):
                out.append(f"{prelude}{{{body}}}")
            else:  # @media, @supports, @starting-style, ...
                inner = prune_css(body, words)
                if inner.strip():
                    out.append(f"{prelude}{{{inner}}}")
        else:
            sels = [s.strip() for s in _split_top(prelude) if s.strip()]
            kept = [s for s in sels if keep_selector(s)]
            if kept:
                out.append(f"{','.join(kept)}{{{body}}}")
    return "\n".join(out)


# ------------------------------------------------------------------- JS ----
def bundle_js() -> str:
    """Bundle static/js/*.js (ES modules) into one classic deferred script. Each module becomes an IIFE that
    returns its exports; main.js imports are rewritten into destructuring from those."""
    parts, names_by_mod = [], {}
    for mod in JS_ORDER:
        code = (STATIC / "js" / f"{mod}.js").read_text()
        exported = re.findall(r"export\s+(?:async\s+)?(?:function|const|let)\s+(\w+)", code)
        names_by_mod[mod] = exported
        code = re.sub(r"^import .*$\n?", "", code, flags=re.M)
        code = re.sub(r"\bexport\s+", "", code)
        parts.append(f"const M_{mod} = (() => {{\n{code}\nreturn {{ {', '.join(exported)} }};\n}})();")
    main = (STATIC / "js" / "main.js").read_text()
    main = re.sub(r'^import \{([^}]*)\} from "\./(\w+)\.js";\s*$', lambda m: f"const {{{m.group(1)}}} = M_{m.group(2)};", main, flags=re.M)
    return '(() => {\n"use strict";\n' + "\n".join(parts) + "\n" + main + "\n})();\n"


# ---------------------------------------------------------------- pages ----
def write(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def collect_pages():
    pages = []
    for mod in (home, stay, dining, explore, story, journal, contact, legal, book, notfound):
        pages.extend(mod.build())
    return pages


def build():
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()

    # JS first (it does not depend on the pages), then pages with a CSS version placeholder
    js = bundle_js()
    js_hash = hashlib.sha1(js.encode()).hexdigest()[:10]
    write(DIST / "assets" / "js" / "app.js", js)
    C.JS_PATH = f"assets/js/app.js?v={js_hash}"
    C.CSS_PATH = f"assets/css/main.css?v={CSS_VERSION_TOKEN}"

    pages = collect_pages()

    # CSS: concatenate, prune against the real pages and scripts, minify, then fingerprint
    css = "\n".join((STATIC / "css" / f"{n}.css").read_text() for n in CSS_ORDER)
    corpus = " ".join(html for _, html in pages) + " " + js
    words = set(re.findall(r"[A-Za-z_][\w-]*", corpus))
    pruned = minify_css(prune_css(css, words))
    css_hash = hashlib.sha1(pruned.encode()).hexdigest()[:10]
    write(DIST / "assets" / "css" / "main.css", pruned)

    sitemap = []
    for path, html in pages:
        html = html.replace(CSS_VERSION_TOKEN, css_hash)
        out = DIST / path / "index.html" if not path.endswith(".html") else DIST / path
        if path == "":
            out = DIST / "index.html"
        write(out, html)
        if 'content="noindex' not in html:
            sitemap.append(path)

    shutil.copytree(STATIC / "img", DIST / "assets" / "img")
    shutil.copytree(STATIC / "fonts", DIST / "assets" / "fonts")
    for f in (STATIC / "favicons").iterdir():
        shutil.copy(f, DIST / f.name)

    manifest = {
        "name": "The Alder House", "short_name": "Alder House", "start_url": C.url(), "display": "browser",
        "background_color": "#F6F2EA", "theme_color": "#55624B",
        "icons": [{"src": C.url("favicon-512x512.png"), "sizes": "512x512", "type": "image/png"},
                  {"src": C.url("apple-touch-icon-180x180.png"), "sizes": "180x180", "type": "image/png"}],
    }
    write(DIST / "manifest.webmanifest", json.dumps(manifest, indent=2))
    write(DIST / "robots.txt", f"User-agent: *\nAllow: /\nDisallow: {C.url('book/summary/')}\n\nSitemap: {C.abs_url('sitemap.xml')}\n")
    urls = "".join(f"  <url><loc>{C.abs_url(p)}</loc></url>\n" for p in sitemap)
    write(DIST / "sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
    write(DIST / ".nojekyll", "")
    size = lambda p: f"{p.stat().st_size / 1024:.0f} KB"
    print(f"Built {len(pages)} pages into {DIST.relative_to(ROOT)}/ (origin {C.ORIGIN}, base '{C.BASE or '/'}')")
    print(f"  CSS {len(css) // 1024} KB -> {size(DIST / 'assets/css/main.css')} after pruning and minifying; JS bundle {size(DIST / 'assets/js/app.js')}")


def serve(port=8000):
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(DIST))
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"Serving http://localhost:{port}  (Ctrl-C to stop)")
        httpd.serve_forever()


if __name__ == "__main__":
    build()
    if "--serve" in sys.argv:
        serve()
