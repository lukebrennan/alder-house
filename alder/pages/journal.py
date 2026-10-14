from ..images import abs_src, EXT, TERR, ENT, BRK, BATH, BATHV, COCK, LAMB, REST, FISH, STP, WINE, AUT, EVE, WALK, JET, VIL, WTF, SUITE, CORN, FELL, GARD, HOUSE, LAKE  # noqa: F401
from ..config import url, abs_url
from ..images import src
from ..journal import ARTICLES, BY_SLUG, CATEGORIES, related
from ..layout import page
from ..ui import (breadcrumbs, button, demo_banner, eyebrow, fmt_date, icon, journal_card, media, page_hero,
                  section_head, text_link)


def listing():
    chips = '<button type="button" class="chip" aria-pressed="true" data-filter="All">All</button>' + "".join(
        f'<button type="button" class="chip" aria-pressed="false" data-filter="{c}">{c}</button>' for c in CATEGORIES)
    cards = "".join(journal_card(a, "feature" if i == 0 else "default") for i, a in enumerate(ARTICLES))
    body = f'''{page_hero("Notes from the Lakes.", "The Journal", "Walks, recipes, small discoveries and stories from the house.",
                         WTF, crumbs=[("Journal", None)])}
<section class="section section--tight-top" aria-label="Articles">
  <div class="container">
    <h2 class="visually-hidden">All articles</h2>
    <div class="filters" role="group" aria-label="Filter articles by category">{chips}</div>
    <p class="visually-hidden" role="status" aria-live="polite" data-filter-status></p>
    <div class="journal-grid" data-journal-grid>{cards}
      <aside class="journal-grid__note" data-journal-note data-reveal>
        {eyebrow("Next issue")}
        <p class="display">More notes from the Lakes arrive with the seasons.</p>
        <p>Subscribe in the footer and we will send them your way.</p>
      </aside>
    </div>
  </div>
</section>'''
    return ("journal/", page("journal/", "The Journal",
                             "Notes from the Lakes: walks, food, the house and the landscape, from The Alder House in the Lake District.",
                             body, overlay=True, og_key=WTF, crumbs=[("Journal", "journal/")]))


def render_block(b) -> str:
    kind = b[0]
    if kind == "p":
        return f"<p>{b[1]}</p>"
    if kind == "h2":
        return f'<h2 class="h3">{b[1]}</h2>'
    if kind == "quote":
        return f'<blockquote class="pullquote"><p>{b[1]}</p></blockquote>'
    if kind == "img":
        return f'<figure class="article__figure">{media(b[1], (3, 2), sizes="(min-width: 960px) 64vw, 100vw")}<figcaption>{b[2]}</figcaption></figure>'
    raise ValueError(kind)


def article_page(a):
    path = f'journal/{a["slug"]}/'
    rel = "".join(journal_card(x, "compact") for x in related(a))
    body = f'''<article class="article">
<header class="article__head">
  <div class="container narrow">
    {breadcrumbs([("Journal", "journal/"), (a["category"], None)])}
    <p class="article__meta"><span class="article__cat">{a["category"]}</span><time datetime="{a["date"]}">{fmt_date(a["date"])}</time><span>{a["read"]} minute read</span></p>
    <h1 class="display article__title">{a["title"]}</h1>
    <p class="lede">{a["excerpt"]}</p>
  </div>
</header>
<div class="container article__hero">{media(a["hero"], (16, 9), sizes="(min-width: 1360px) 1280px, 100vw", loading="eager")}</div>
<div class="container narrow article__body prose">
{"".join(render_block(b) for b in a["body"])}
<p class="article__end">{icon("mountain", "icon", 28)}</p>
</div>
<section class="section section--sand" aria-labelledby="related-title">
  <div class="container">
    {section_head("Keep reading", "More from the Journal.", title_cls="display", title_id="related-title")}
    <div class="mini-grid">{rel}</div>
    <div class="section-cta" data-reveal>{text_link("All articles", url("journal/"))}</div>
  </div>
</section>
</article>'''
    schema = [{
        "@context": "https://schema.org", "@type": "Article", "headline": a["title"],
        "description": a["excerpt"], "datePublished": a["date"], "dateModified": a["date"],
        "inLanguage": "en-GB", "mainEntityOfPage": abs_url(path),
        "image": abs_src(a["hero"]),
        "author": {"@type": "Organization", "name": "The Alder House"},
        "publisher": {"@type": "Organization", "name": "The Alder House", "url": abs_url()},
        "articleSection": a["category"],
    }]
    return (path, page(path, a["title"], a["excerpt"], body, og_type="article", schema=schema, og_key=a["hero"],
                       crumbs=[("Journal", "journal/"), (a["title"], path)]))


def build():
    return [listing()] + [article_page(a) for a in ARTICLES]
