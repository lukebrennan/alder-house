#!/usr/bin/env python3
"""Build the static site into dist/.

    python3 build.py           # build
    python3 build.py --serve   # build, then preview at http://localhost:8000

Environment:
    SITE_ORIGIN  e.g. https://username.github.io   (canonical/OG URLs and the sitemap)
    BASE_PATH    e.g. /alder-house                  (blank for a custom domain or user site)
"""
from __future__ import annotations

import functools
import http.server
import re
import shutil
import socketserver
import sys
import json
from pathlib import Path

from alder import config as C
from alder.pages import book, contact, dining, explore, home, journal, legal, notfound, stay, story

ROOT = Path(__file__).parent
DIST = ROOT / "dist"
STATIC = ROOT / "static"
CSS_ORDER = ["00-tokens", "10-base", "20-layout", "30-components", "40-sections", "50-pages", "90-motion"]


def minify_css(css: str) -> str:
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    css = re.sub(r"\s+", " ", css)
    css = re.sub(r"\s*([{};,>])\s*", r"\1", css)
    css = re.sub(r":\s+", ":", css)
    return css.replace(";}", "}").strip()


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

    pages = collect_pages()
    sitemap = []
    for path, html in pages:
        out = DIST / path / "index.html" if not path.endswith(".html") else DIST / path
        if path == "":
            out = DIST / "index.html"
        write(out, html)
        if 'content="noindex' not in html:
            sitemap.append(path)

    # CSS: concatenate in a fixed order, then minify
    css = "\n".join((STATIC / "css" / f"{n}.css").read_text() for n in CSS_ORDER)
    write(DIST / "assets" / "css" / "main.css", minify_css(css))

    # JS (native ES modules, served as-is) and other static files
    shutil.copytree(STATIC / "js", DIST / "assets" / "js")
    shutil.copytree(STATIC / "img", DIST / "assets" / "img")
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
    print(f"Built {len(pages)} pages into {DIST.relative_to(ROOT)}/ (origin {C.ORIGIN}, base '{C.BASE or '/'}')")


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
