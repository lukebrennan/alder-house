"""Reusable HTML components. Each returns a string of markup."""
from __future__ import annotations

import datetime as dt
from html import escape

from . import config as C
from .images import img, src, alt_for
from .config import url
from .rooms import amenity_list, key_amenities

# ---------------------------------------------------------------- icons ----
_ICONS = {
    "bed": "M3 18v-7a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2v7M3 15h18M3 18v2M21 18v2M7 9V7.5A1.5 1.5 0 0 1 8.5 6h3A1.5 1.5 0 0 1 13 7.5V9",
    "shower": "M6 10a6 6 0 0 1 12 0zM8 14v1M12 14v2M16 14v1M10 18v1M14 18v1",
    "bath": "M3 12h18v2a4 4 0 0 1-4 4H7a4 4 0 0 1-4-4zM6 12V7a2 2 0 0 1 4 0M7 18l-1 2M17 18l1 2",
    "radio": "M4 8h16v11H4zM4 8l12-4M8 13h4M17 13.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0",
    "wifi": "M2 9a15 15 0 0 1 20 0M5 12.5a10 10 0 0 1 14 0M8.5 16a5 5 0 0 1 7 0M12 19.5h.01",
    "tv": "M3 6h18v11H3zM8 21h8M12 17v4",
    "cup": "M5 9h11v6a4 4 0 0 1-4 4H9a4 4 0 0 1-4-4zM16 10h2a2 2 0 0 1 0 4h-2M8 4v2M12 4v2",
    "robe": "M8 3l4 3 4-3 3 4-3 2v12H8V9L5 7zM12 6v15",
    "drop": "M12 3c3 4 6 7 6 10.5a6 6 0 0 1-12 0C6 10 9 7 12 3z",
    "breakfast": "M4 12h16a8 6 0 0 1-16 0zM8 8c0-1.5 1.500-1.500 1.500-3M12 8c0-1.500 1.500-1.500 1.500-3M16 8c0-1.500 1.500-1.500 1.500-3",
    "view": "M3 19l6-10 4 6 2-3 6 7zM16 6.500a1.500 1.500 0 1 1-3 0 1.500 1.500 0 0 1 3 0",
    "leaf": "M5 19c0-8 5-13 14-14 0 9-5 14-13 14M5 19c3-4 6-6 9-8",
    "seat": "M5 11V8a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v3M4 14a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v3H4zM6 17v2M18 17v2",
    "flame": "M12 3c1 4 5 5 5 10a5 5 0 0 1-10 0c0-2 1-3 2-4 0 2 1 3 2 3 0-3-1-5 1-9z",
    "step": "M12 5.500a1.500 1.500 0 1 1-3 0 1.500 1.500 0 0 1 3 0M10.500 9v5h4l2 5M8 11a5 5 0 1 0 6 7",
    "arrow": "M5 12h14M13 6l6 6-6 6",
    "close": "M6 6l12 12M18 6L6 18",
    "chevron": "M6 9l6 6 6-6",
    "prev": "M15 5l-7 7 7 7",
    "next": "M9 5l7 7-7 7",
    "phone": "M5 4h4l2 5-2.500 1.500a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A15 15 0 0 1 3 6a2 2 0 0 1 2-2z",
    "mail": "M3 6h18v12H3zM3 7l9 6 9-6",
    "pin": "M12 21s7-6 7-11a7 7 0 1 0-14 0c0 5 7 11 7 11zM14 10a2 2 0 1 1-4 0 2 2 0 0 1 4 0",
    "clock": "M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0M12 7v5l3 2",
    "calendar": "M4 6h16v14H4zM4 10h16M8 3v4M16 3v4",
    "guests": "M12 8a3 3 0 1 1-6 0 3 3 0 0 1 6 0M3 20a6 6 0 0 1 12 0M17 8.500a2.500 2.500 0 1 1 0 5M17 14a5 5 0 0 1 4 6",
    "instagram": "M7 3h10a4 4 0 0 1 4 4v10a4 4 0 0 1-4 4H7a4 4 0 0 1-4-4V7a4 4 0 0 1 4-4zM16 12a4 4 0 1 1-8 0 4 4 0 0 1 8 0M17.500 6.500h.01",
    "pinterest": "M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0M10.500 20l1.500-7M10 13c-1.500-3 .5-6 3-6 2 0 3 1.500 3 3 0 2.500-1.500 4-3 4-1 0-1.600-.600-2-1.500",
    "mountain": "M2 19l7-11 4 6 3-4 6 9z",
    "check": "M5 12.500l4.500 4.500L19 7.500",
    "walk": "M13 4.500a1.500 1.500 0 1 1-3 0 1.500 1.500 0 0 1 3 0M9 21l2-6-2-2 1-5 3 1 2 3M13 15l2 6",
}


def icon(name: str, cls: str = "icon", size: int = 24) -> str:
    d = _ICONS[name]
    return (f'<svg class="{cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" '
            f'stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round" '
            f'aria-hidden="true" focusable="false"><path d="{d}"/></svg>')


# ------------------------------------------------------------- helpers -----
def money(n) -> str:
    return f"£{n:,}"


def fmt_date(iso: str) -> str:
    d = dt.date.fromisoformat(iso)
    return f"{d.day} {d.strftime('%B %Y')}"


def attrs_str(attrs: dict) -> str:
    out = []
    for k, v in attrs.items():
        k = k.replace("_", "-")
        if v is True:
            out.append(k)
        elif v not in (None, False):
            out.append(f'{k}="{escape(str(v), quote=True)}"')
    return (" " + " ".join(out)) if out else ""


# ------------------------------------------------------------ primitives ---
def button(label, href, variant="primary", arrow=False, cls="", **attrs) -> str:
    inner = f"<span>{label}</span>" + (icon("arrow", "btn__icon", 18) if arrow else "")
    classes = f"btn btn--{variant} {cls}".strip()
    return f'<a class="{classes}" href="{href}"{attrs_str(attrs)}>{inner}</a>'


def submit_button(label, variant="primary", cls="", **attrs) -> str:
    return f'<button class="btn btn--{variant} {cls}" type="submit"{attrs_str(attrs)}><span>{label}</span></button>'


def text_link(label, href, cls="") -> str:
    return f'<a class="link-arrow {cls}" href="{href}"><span>{label}</span>{icon("arrow", "link-arrow__icon", 18)}</a>'


def eyebrow(text, cls="") -> str:
    return f'<p class="eyebrow {cls}">{text}</p>'


def divider(cls="") -> str:
    return f'<span class="divider {cls}" aria-hidden="true"></span>'


def section_head(label, title, intro=None, tag="h2", cls="", title_cls="", title_id=None) -> str:
    intro_html = f'<p class="section-head__intro">{intro}</p>' if intro else ""
    id_attr = f' id="{title_id}"' if title_id else ""
    return (f'<header class="section-head {cls}" data-reveal>{eyebrow(label) if label else ""}'
            f'<{tag} class="section-head__title {title_cls}"{id_attr}>{title}</{tag}>{intro_html}</header>')


def media(key, ratio=(3, 2), sizes="100vw", cls="", reveal=True, **kw) -> str:
    """A framed photograph. The wrapper holds the aspect ratio so nothing shifts."""
    rw, rh = ratio
    r = " reveal-img" if reveal else ""
    return (f'<figure class="media{r} {cls}" style="--ratio:{rw}/{rh}">'
            f'{img(key, ratio=ratio, sizes=sizes, **kw)}</figure>')


def breadcrumbs(items) -> str:
    """items: [(label, path or None)] — last item is the current page."""
    lis = []
    for i, (label, path) in enumerate(items):
        if path is not None and i < len(items) - 1:
            lis.append(f'<li><a href="{url(path)}">{label}</a></li>')
        else:
            lis.append(f'<li><span aria-current="page">{label}</span></li>')
    return f'<nav class="breadcrumbs" aria-label="Breadcrumb"><ol>{"".join(lis)}</ol></nav>'


# ------------------------------------------------------------- rooms -------
def room_meta(room, price=True) -> str:
    items = [("Sleeps", str(room["sleeps"])), ("Bed", room["bed"])]
    if "size" in room:
        items.append(("Size", f'{room["size"]} m²'))
    items.append(("View", room["view"]))
    dl = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in items)
    return f'<dl class="meta">{dl}</dl>'


def price_line(room) -> str:
    return (f'<p class="price"><span class="price__from">From</span> '
            f'<span class="price__amount">{money(room["price"])}</span> '
            f'<span class="price__unit">per night</span></p>')


def room_feature(room, index, reverse=False, first=False) -> str:
    """Editorial room preview: oversized photograph, a quiet column of text."""
    href = url(f'stay/{room["slug"]}/')
    side = " feature--reverse" if reverse else ""
    ratio = (5, 4)
    return f'''<article class="feature{side}" data-reveal>
  <a class="feature__media" href="{href}" tabindex="-1" aria-hidden="true">
    {media(room["lead"], ratio, sizes="(min-width: 960px) 58vw, 100vw", cls="hover-zoom", loading="lazy")}
  </a>
  <div class="feature__body">
    <p class="feature__index" aria-hidden="true">0{index}</p>
    <h3 class="feature__title"><a href="{href}">{room["name"]}</a></h3>
    <p class="feature__text">{room["short"]}</p>
    <dl class="meta meta--compact"><div><dt>Sleeps</dt><dd>{room["sleeps"]}</dd></div><div><dt>Bed</dt><dd>{room["bed"]}</dd></div></dl>
    {price_line(room)}
    {button("View room", href, "secondary", cls="feature__cta", aria_label=f"View {room['name']}")}
  </div>
</article>'''


def room_row(room, index, reverse=False) -> str:
    """Longer listing row used on the Stay page."""
    href = url(f'stay/{room["slug"]}/')
    side = " room-row--reverse" if reverse else ""
    amen = "".join(f'<li>{icon(i, "icon", 20)}<span>{l}</span></li>' for i, l in key_amenities(room, 4))
    return f'''<article class="room-row{side}" id="{room["slug"]}" data-reveal>
  <a class="room-row__media" href="{href}" tabindex="-1" aria-hidden="true">
    {media(room["lead"], (4, 3), sizes="(min-width: 960px) 55vw, 100vw", cls="hover-zoom")}
  </a>
  <div class="room-row__body">
    <p class="eyebrow">Room 0{index}</p>
    <h2 class="room-row__title"><a href="{href}">{room["name"]}</a></h2>
    <p class="room-row__tagline">{room["tagline"]}</p>
    <p>{room["short"]}</p>
    {room_meta(room)}
    <ul class="amenity-list amenity-list--inline">{amen}</ul>
    <div class="room-row__foot">
      {price_line(room)}
      {button("View room", href, "primary", arrow=True, aria_label=f"View {room['name']}")}
    </div>
  </div>
</article>'''


def room_card(room) -> str:
    href = url(f'stay/{room["slug"]}/')
    return f'''<article class="mini-card" data-reveal>
  <a class="mini-card__link" href="{href}">
    {media(room["lead"], (4, 5), sizes="(min-width: 960px) 30vw, 90vw", cls="hover-zoom")}
    <h3 class="mini-card__title">{room["name"]}</h3>
    <p class="mini-card__meta">Sleeps {room["sleeps"]} · {room["view"]}</p>
    <p class="mini-card__price">From {money(room["price"])} per night</p>
  </a>
</article>'''


def amenity_items(room) -> str:
    return "".join(f'<li>{icon(i, "icon", 22)}<span>{l}</span></li>' for i, l in amenity_list(room))


def gallery(room) -> str:
    """Photo grid; each tile opens the lightbox (see lightbox.js)."""
    tiles = []
    for n, key in enumerate(room["gallery"]):
        big = src(key, 2400)
        thumb_ratio = (4, 3) if n else (3, 2)
        sizes = "(min-width: 960px) 40vw, 100vw" if n == 0 else "(min-width: 960px) 20vw, 50vw"
        tiles.append(
            f'<button type="button" class="gallery__tile gallery__tile--{n}" data-lightbox="{big}" '
            f'data-alt="{escape(alt_for(key), quote=True)}" data-caption="{escape(room["name"])} — photograph {n+1} of {len(room["gallery"])}" '
            f'aria-label="Open photograph {n+1} of {len(room["gallery"])}: {escape(alt_for(key), quote=True)}">'
            f'{media(key, thumb_ratio, sizes=sizes, cls="hover-zoom", loading="eager" if n == 0 else "lazy", reveal=False)}</button>')
    return f'<div class="gallery" data-gallery>{"".join(tiles)}</div>'


# ----------------------------------------------------------- journal -------
def journal_card(a, variant="default") -> str:
    href = url(f'journal/{a["slug"]}/')
    sizes = {"feature": "(min-width: 960px) 60vw, 100vw", "default": "(min-width: 960px) 30vw, 100vw",
             "compact": "(min-width: 960px) 22vw, 90vw"}[variant]
    ratio = {"feature": (3, 2), "default": (4, 5), "compact": (4, 3)}[variant]
    return f'''<article class="journal-card journal-card--{variant}" data-category="{a["category"]}" data-reveal>
  <a class="journal-card__link" href="{href}">
    {media(a["hero"], ratio, sizes=sizes, cls="hover-zoom")}
    <div class="journal-card__body">
      <p class="journal-card__meta"><span>{a["category"]}</span><time datetime="{a["date"]}">{fmt_date(a["date"])}</time></p>
      <h3 class="journal-card__title"><span>{a["title"]}</span></h3>
      {f'<p class="journal-card__excerpt">{a["excerpt"]}</p>' if variant != "compact" else ""}
    </div>
  </a>
</article>'''


# ------------------------------------------------------- testimonials ------
def testimonial(quote, who, where="Fictional guest review") -> str:
    return f'''<figure class="quote" data-reveal>
  <blockquote><p>{quote}</p></blockquote>
  <figcaption><span class="quote__who">{who}</span><span class="quote__where">{where}</span></figcaption>
</figure>'''


# ---------------------------------------------------------- accordion ------
def accordion(items, prefix="acc") -> str:
    out = []
    for i, (q, a) in enumerate(items):
        pid = f"{prefix}-{i}"
        out.append(f'''<div class="accordion__item">
  <h3 class="accordion__heading"><button type="button" class="accordion__button" aria-expanded="false" aria-controls="{pid}-panel" id="{pid}-btn"><span>{q}</span>{icon("chevron", "accordion__icon", 20)}</button></h3>
  <div class="accordion__panel" id="{pid}-panel" role="region" aria-labelledby="{pid}-btn"><div class="accordion__inner"><div class="prose">{a}</div></div></div>
</div>''')
    return f'<div class="accordion" data-accordion>{"".join(out)}</div>'


# -------------------------------------------------------------- forms ------
def field(name, label, type="text", required=False, autocomplete=None, placeholder="", extra="", cls="") -> str:
    req = " required" if required else ""
    ac = f' autocomplete="{autocomplete}"' if autocomplete else ""
    ph = f' placeholder="{placeholder}"' if placeholder else ""
    mark = ' <span class="field__req" aria-hidden="true">*</span>' if required else ""
    return (f'<div class="field {cls}"><label for="{name}">{label}{mark}</label>'
            f'<input id="{name}" name="{name}" type="{type}"{req}{ac}{ph}{extra}></div>')


def textarea(name, label, rows=5, required=False) -> str:
    req = " required" if required else ""
    mark = ' <span class="field__req" aria-hidden="true">*</span>' if required else ""
    return f'<div class="field"><label for="{name}">{label}{mark}</label><textarea id="{name}" name="{name}" rows="{rows}"{req}></textarea></div>'


def select(name, label, options, selected=None, cls="") -> str:
    opts = "".join(f'<option value="{v}"{" selected" if str(v) == str(selected) else ""}>{t}</option>' for v, t in options)
    return f'<div class="field {cls}"><label for="{name}">{label}</label><select id="{name}" name="{name}">{opts}</select></div>'


def booking_form(variant="bar", room=None, uid="b") -> str:
    """Availability search. Works as a plain GET form; datepicker.js enhances it."""
    today = dt.date(2026, 10, 12)
    hidden = f'<input type="hidden" name="room" value="{room}">' if room else ""
    guest_opts = [(i, f"{i} guest{'s' if i > 1 else ''}") for i in range(1, 4)]
    return f'''<form class="booking booking--{variant}" action="{url("book/")}" method="get" data-booking aria-label="Check availability">
  {hidden}
  <div class="booking__field">
    <label for="{uid}-in">Check-in</label>
    <input id="{uid}-in" name="checkin" type="date" min="{today.isoformat()}" required data-date="in" autocomplete="off">
  </div>
  <div class="booking__field">
    <label for="{uid}-out">Check-out</label>
    <input id="{uid}-out" name="checkout" type="date" min="{today.isoformat()}" required data-date="out" autocomplete="off">
  </div>
  <div class="booking__field">
    <label for="{uid}-guests">Guests</label>
    <select id="{uid}-guests" name="guests">{"".join(f'<option value="{v}">{t}</option>' for v, t in guest_opts)}</select>
  </div>
  <div class="booking__submit">{submit_button("Search availability", "primary")}</div>
</form>'''


def newsletter_form(uid="nl") -> str:
    return f'''<form class="newsletter" data-demo-form data-success="Thank you. This is a demonstration, so nothing has been sent and your address has not been stored." novalidate>
  <label class="visually-hidden" for="{uid}-email">Email address</label>
  <div class="newsletter__row">
    <input id="{uid}-email" name="email" type="email" placeholder="Your email address" autocomplete="email" required>
    <button class="btn btn--light" type="submit"><span>Subscribe</span></button>
  </div>
  <p class="form-status" role="status" aria-live="polite"></p>
</form>'''


def demo_banner(text=None) -> str:
    text = text or C.DEMO_NOTE
    return f'<p class="demo-note">{icon("pin", "icon", 18)}<span>{text}</span></p>'


# --------------------------------------------------------- page hero -------
def page_hero(title, label, lede, key, crumbs=None, ratio=(16, 9), mobile_ratio=(4, 5), cls="") -> str:
    """Photographic header used at the top of inner pages."""
    from .images import img as _img
    picture = _img(key, ratio=ratio, sizes="100vw", widths=(800, 1200, 1600, 2000, 2560), priority=True,
                   mobile_ratio=mobile_ratio)
    crumb_html = breadcrumbs(crumbs).replace('class="breadcrumbs"', 'class="breadcrumbs breadcrumbs--light"') if crumbs else ""
    return f'''<section class="page-hero {cls}" aria-labelledby="page-title">
  <div class="page-hero__media">{picture}</div>
  <div class="page-hero__scrim" aria-hidden="true"></div>
  <div class="page-hero__content">
    {crumb_html}
    {f'<p class="eyebrow eyebrow--light">{label}</p>' if label else ""}
    <h1 class="page-hero__title" id="page-title">{title}</h1>
    {f'<p class="page-hero__lede">{lede}</p>' if lede else ""}
  </div>
</section>'''
