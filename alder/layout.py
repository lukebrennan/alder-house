"""Document shell: <head>, header, mobile menu, footer."""
from __future__ import annotations

from .images import EXT, TERR, ENT, BRK, BATH, BATHV, COCK, LAMB, REST, FISH, STP, WINE, AUT, EVE, WALK, JET, VIL, WTF, SUITE, CORN, FELL, GARD, HOUSE, LAKE  # noqa: F401

import json
from html import escape

from . import config as C
from .config import url, abs_url
from .images import og_image, srcset
from .ui import icon, newsletter_form, button

FONTS = (
    "https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,500;1,400"
    "&family=Montserrat:wght@400;500;600&family=Playfair+Display:ital,wght@0,400;0,500;1,400&display=swap"
)

NAV = [("Stay", "stay/"), ("Dining", "dining/"), ("Explore", "explore/"),
       ("Our Story", "our-story/"), ("Journal", "journal/"), ("Contact", "contact/")]


def ld(data) -> str:
    return f'<script type="application/ld+json">{json.dumps(data, ensure_ascii=False, separators=(",", ":"))}</script>'


def breadcrumb_ld(items) -> dict:
    """items: [(label, path)] from home down to the current page."""
    return {
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": name, "item": abs_url(path)}
            for i, (name, path) in enumerate(items)
        ],
    }


def logo(cls="") -> str:
    return (f'<a class="logo {cls}" href="{url()}" aria-label="The Alder House, Boutique Hotel. Home">'
            '<span class="logo__the" aria-hidden="true">The</span>'
            '<span class="logo__name" aria-hidden="true">Alder House</span>'
            '<span class="logo__sub" aria-hidden="true">Boutique Hotel</span></a>')


def _nav_links(path, cls="") -> str:
    out = []
    for label, p in NAV:
        cur = ' aria-current="page"' if path.startswith(p) else ""
        out.append(f'<li><a class="{cls}" href="{url(p)}"{cur}>{label}</a></li>')
    return "".join(out)


def header(path, overlay) -> str:
    mode = "overlay" if overlay else "solid"
    return f'''<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header" data-header data-mode="{mode}">
  <div class="site-header__inner">
    {logo()}
    <nav class="primary-nav" aria-label="Primary"><ul>{_nav_links(path, "nav-link")}</ul></nav>
    <div class="site-header__actions">
      {button("Book Your Stay", url("book/"), "primary", cls="btn--small site-header__cta")}
      <button class="menu-toggle" type="button" aria-haspopup="dialog" aria-controls="menu" aria-expanded="false" data-menu-open>
        <span class="menu-toggle__label">Menu</span><span class="menu-toggle__bars" aria-hidden="true"><i></i><i></i></span>
      </button>
    </div>
  </div>
</header>
<dialog class="menu" id="menu" aria-label="Main menu" data-menu>
  <div class="menu__inner">
    <div class="menu__top">
      {logo("logo--light")}
      <button class="menu__close" type="button" data-menu-close aria-label="Close menu">{icon("close", "icon", 26)}</button>
    </div>
    <nav class="menu__nav" aria-label="Main menu"><ul>{_nav_links(path, "menu__link")}</ul></nav>
    <div class="menu__foot">
      {button("Book Your Stay", url("book/"), "light", arrow=True)}
      <p class="menu__meta">Boutique Hotel · Lake District<br><a href="tel:{C.PHONE_HREF}">{C.PHONE}</a></p>
    </div>
  </div>
</dialog>'''


def footer() -> str:
    links = "".join(f'<li><a href="{url(p)}">{l}</a></li>' for l, p in NAV)
    second = "".join(f'<li><a href="{url(p)}">{l}</a></li>' for l, p in
                     [("FAQs", "faqs/"), ("Accessibility", "accessibility/"), ("Privacy", "privacy/"), ("Terms", "terms/")])
    return f'''<footer class="site-footer">
  <div class="site-footer__inner">
    <div class="site-footer__brand">
      {icon("mountain", "site-footer__mark", 44)}
      <p class="site-footer__name">The Alder House</p>
      <p class="site-footer__sub">Boutique Hotel · Lake District</p>
      <p class="site-footer__tag">Stay a little longer.</p>
    </div>
    <nav class="site-footer__col" aria-label="Footer"><h2 class="site-footer__heading">The House</h2><ul>{links}</ul></nav>
    <nav class="site-footer__col" aria-label="Information"><h2 class="site-footer__heading">Information</h2><ul>{second}</ul>
      <h2 class="site-footer__heading site-footer__heading--spaced">Follow</h2>
      <ul class="social">
        <li><a href="https://www.instagram.com/" rel="noopener" aria-label="Instagram">{icon("instagram", "icon", 20)}<span>Instagram</span></a></li>
        <li><a href="https://www.pinterest.com/" rel="noopener" aria-label="Pinterest">{icon("pinterest", "icon", 20)}<span>Pinterest</span></a></li>
      </ul>
    </nav>
    <div class="site-footer__col site-footer__news">
      <h2 class="site-footer__heading">Notes from The Alder House</h2>
      <p>Occasional stories, seasonal escapes and reasons to return to the Lakes.</p>
      {newsletter_form()}
    </div>
  </div>
  <div class="site-footer__legal">
    <p>&copy; 2026 The Alder House. Photography from <a href="https://unsplash.com/" rel="noopener">Unsplash</a> contributors.</p>
    <p class="site-footer__credit">Website designed and developed by Luke Brennan</p>
  </div>
</footer>'''


def book_bar(sticky) -> str:
    """Mobile-only booking bar that slides in once the visitor has scrolled past the hero."""
    if sticky is None:
        return ""
    strong, small, href, label = sticky
    return (f'<div class="book-bar" data-book-bar><div class="book-bar__text"><strong>{strong}</strong><span>{small}</span></div>'
            f'{button(label, href, "primary")}</div>')


LIGHTBOX = f'''<dialog class="lightbox" aria-label="Photograph viewer" data-lightbox-dialog>
  <button class="lightbox__close" type="button" data-lb-close aria-label="Close photograph viewer">{icon("close", "icon", 26)}</button>
  <button class="lightbox__nav lightbox__nav--prev" type="button" data-lb-prev aria-label="Previous photograph">{icon("prev", "icon", 28)}</button>
  <figure class="lightbox__figure"><img class="lightbox__img" alt="" data-lb-img><figcaption class="lightbox__caption" data-lb-caption></figcaption></figure>
  <button class="lightbox__nav lightbox__nav--next" type="button" data-lb-next aria-label="Next photograph">{icon("next", "icon", 28)}</button>
</dialog>'''


def page(path, title, description, body, *, overlay=False, og_key=EXT, og_type="website",
         schema=None, noindex=False, lightbox=False, preload=None, body_class="", crumbs=None,
         full_title=None, extra_head="", extra_body="", sticky="default") -> str:
    full = full_title or (f"{title} | The Alder House" if path else title)
    canonical = abs_url(path)
    schema = list(schema or [])
    if crumbs:
        schema.append(breadcrumb_ld([("Home", "")] + crumbs))
    robots = "noindex, follow" if noindex else "index, follow, max-image-preview:large"
    preload_tag = ""
    if preload:  # an image key: preload the AVIF rendition that matches the viewport and pixel density
        preload_tag = f'<link rel="preload" as="image" type="image/avif" imagesrcset="{srcset(preload, "avif")}" imagesizes="100vw" fetchpriority="high">'
    og = og_image(og_key)
    if sticky == "default":
        sticky = ("Stay a little longer", "Breakfast included in every room", url("book/"), "Check availability")
    return f'''<!doctype html>
<html lang="en-GB" data-base="{C.BASE}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(full)}</title>
<meta name="description" content="{escape(description, quote=True)}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="#F6F2EA">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="The Alder House">
<meta property="og:locale" content="en_GB">
<meta property="og:title" content="{escape(full, quote=True)}">
<meta property="og:description" content="{escape(description, quote=True)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og}">
<meta property="og:image:alt" content="Sunset over Windermere in the English Lake District">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{url("favicon.ico")}" sizes="48x48">
<link rel="icon" href="{url("favicon-32x32.png")}" type="image/png" sizes="32x32">
<link rel="apple-touch-icon" href="{url("apple-touch-icon-180x180.png")}">
<link rel="manifest" href="{url("manifest.webmanifest")}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preconnect" href="https://images.unsplash.com" crossorigin>
{preload_tag}
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="{url(C.CSS_PATH)}">
<script>document.documentElement.classList.add("js")</script>
<script type="module" src="{url(C.JS_PATH)}"></script>
{"".join(ld(s) for s in schema)}
{extra_head}
</head>
<body class="{body_class}">
{header(path, overlay)}
<main id="main" tabindex="-1">
{body}
</main>
{footer()}
{LIGHTBOX if lightbox else ""}
{book_bar(sticky)}
{extra_body}
</body>
</html>
'''
