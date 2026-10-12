from ..images import abs_src, EXT, TERR, ENT, BRK, BATH, BATHV, COCK, LAMB, REST, FISH, STP, WINE, AUT, EVE, WALK, JET, VIL, WTF, SUITE, CORN, FELL, GARD, HOUSE, LAKE  # noqa: F401
from .. import config as C
from ..config import url, abs_url
from ..images import img, src
from ..journal import BY_SLUG as ARTICLES
from ..layout import page
from ..rooms import BY_SLUG as ROOMS, FEATURED
from ..ui import (booking_form, button, demo_banner, eyebrow, icon, journal_card, media,
                  room_feature, section_head, testimonial, text_link)


def hero() -> str:
    picture = img(EXT, ratio=(16, 9), sizes="100vw", widths=(800, 1200, 1600, 2000, 2560),
                  priority=True, mobile_ratio=(3, 4))
    return f'''<section class="hero" aria-labelledby="hero-title">
  <div class="hero__media">{picture}</div>
  <div class="hero__scrim" aria-hidden="true"></div>
  <div class="hero__content">
    <p class="hero__wordmark">The Alder House</p>
    <p class="hero__label"><span class="hero__rule" aria-hidden="true"></span>Boutique Hotel · Lake District</p>
    <h1 class="hero__title" id="hero-title">A more thoughtful kind of <em>escape.</em></h1>
    <p class="hero__lede">A quiet retreat in the heart of the Lake District, shaped by beautiful surroundings, thoughtful hospitality and the simple pleasure of slowing down.</p>
    <div class="hero__actions">
      {button("Book Your Stay", url("book/"), "primary", cls="btn--on-image")}
      {button("Discover The House", "#welcome", "light")}
    </div>
  </div>
  <a class="hero__scroll" href="#welcome" aria-label="Scroll to content"><span>Scroll</span><i aria-hidden="true"></i></a>
</section>'''


def booking_strip() -> str:
    return f'''<section class="booking-strip" aria-label="Check availability">
  <div class="container">
    <div class="booking-strip__card">
      <p class="booking-strip__title">Check availability</p>
      {booking_form("bar", uid="home")}
    </div>
  </div>
</section>'''


def intro() -> str:
    return f'''<section class="section intro" id="welcome" aria-labelledby="intro-title">
  <div class="container intro__grid">
    <div class="intro__text" data-reveal>
      {eyebrow("Welcome to The Alder House")}
      <h2 class="display" id="intro-title">Some places make it easier to <em>slow down.</em></h2>
      <p class="lede">Set amongst the fells and waters of the Lake District, The Alder House is a small boutique hotel created for unhurried stays. Beautiful rooms, thoughtful food and the landscape right outside your door.</p>
      {text_link("Discover our story", url("our-story/"))}
    </div>
    <div class="intro__images">
      {media(CORN, (4, 5), sizes="(min-width: 960px) 34vw, 70vw", cls="intro__main")}
      {media(ENT, (1, 1), sizes="(min-width: 960px) 20vw, 45vw", cls="intro__inset")}
    </div>
  </div>
</section>'''


def rooms() -> str:
    feats = "".join(room_feature(ROOMS[s], i + 1, reverse=bool(i % 2)) for i, s in enumerate(FEATURED))
    return f'''<section class="section section--tight-top rooms-preview" aria-labelledby="rooms-title">
  <div class="container">
    {section_head("Stay", "Rooms made for <em>switching off.</em>", title_cls="display", title_id="rooms-title")}
    <div class="feature-list">{feats}</div>
    <div class="section-cta" data-reveal>{button("View all rooms", url("stay/"), "secondary", arrow=True)}</div>
  </div>
</section>'''


def statement() -> str:
    return f'''<section class="statement" aria-labelledby="statement-title">
  <div class="statement__media" data-parallax>{img(EVE, ratio=(16, 9), sizes="100vw", widths=(800, 1200, 1600, 2000, 2560), mobile_ratio=(4, 5))}</div>
  <div class="statement__scrim" aria-hidden="true"></div>
  <div class="statement__content" data-reveal>
    <h2 class="statement__title" id="statement-title">Stay a little <em>longer.</em></h2>
    <p class="statement__text">There is nowhere you need to be.</p>
  </div>
</section>'''


def dining() -> str:
    items = [("Breakfast", "Eggs from up the road, warm bread and proper coffee."),
             ("Dinner", "A short, seasonal menu cooked over wood and flame."),
             ("Sunday lunch", "Roasts, big plates and a table that stays put until four."),
             ("Drinks", "Lakeland ales, English wine and a bar for lingering.")]
    lis = "".join(f'<li><h3>{t}</h3><p>{d}</p></li>' for t, d in items)
    return f'''<section class="section section--dark dining" aria-labelledby="dining-title">
  <div class="container dining__grid">
    <div class="dining__images" data-reveal>
      {media(LAMB, (4, 5), sizes="(min-width: 960px) 28vw, 60vw", cls="dining__a")}
      {media(STP, (1, 1), sizes="(min-width: 960px) 20vw, 45vw", cls="dining__b")}
    </div>
    <div class="dining__text" data-reveal>
      {eyebrow("Eat & drink", "eyebrow--gold")}
      <h2 class="display" id="dining-title">Food rooted in the <em>landscape.</em></h2>
      <p class="lede">Alder Kitchen cooks with the seasons. Seasonal British produce, local suppliers and a relaxed room in which to enjoy them, with nothing fussy and nothing forced.</p>
      <ul class="dining__list">{lis}</ul>
      {button("Discover Alder Kitchen", url("dining/"), "light", arrow=True)}
    </div>
  </div>
</section>'''


def explore() -> str:
    items = [
        ("Fell Walking", WALK, "explore/#walking", "Paths that begin at the gate."),
        ("Wild Swimming", WTF, "explore/#lakes", "Cold, clear and quietly addictive."),
        ("Lake Cruises", JET, "explore/#lakes", "See the shoreline from the water."),
        ("Villages & Markets", VIL, "explore/#villages", "Bakeries, bookshops and stone lanes."),
    ]
    cards = "".join(f'''<li class="experience" data-reveal>
  <a href="{url(p)}">{media(k, (3, 4), sizes="(min-width: 960px) 24vw, 70vw", cls="hover-zoom")}
  <span class="experience__label"><span class="experience__title">{t}</span><span class="experience__line">{line}</span></span></a></li>''' for t, k, p, line in items)
    return f'''<section class="section explore" aria-labelledby="explore-title">
  <div class="container">
    {section_head("Explore", "Step <em>outside.</em>", "The Lakes begin at the front door. Walk, swim, sail or simply wander, and come back to a warm room and a good table.", title_cls="display", title_id="explore-title")}
    <ul class="experience-grid">{cards}</ul>
    <div class="section-cta" data-reveal>{button("Explore the Lake District", url("explore/"), "secondary", arrow=True)}</div>
  </div>
</section>'''


def split() -> str:
    pts = [("Thoughtful spaces", "Every room is individually designed with natural materials, soft textures and views worth waking up for."),
           ("Good food", "Seasonal cooking, local ingredients and an atmosphere that never feels overly formal."),
           ("Room to breathe", "Walk from the hotel into some of Britain's most remarkable countryside.")]
    lis = "".join(f'<li><span class="points__n" aria-hidden="true">0{i+1}</span><div><h3>{t}</h3><p>{d}</p></div></li>' for i, (t, d) in enumerate(pts))
    return f'''<section class="split" aria-labelledby="split-title">
  <div class="split__media">{media(HOUSE, (4, 3), sizes="(min-width: 960px) 62vw, 100vw", cls="split__img")}</div>
  <div class="split__panel" data-reveal>
    {eyebrow("The house", "eyebrow--gold")}
    <h2 class="display" id="split-title">Designed around the way you want to <em>stay.</em></h2>
    <ul class="points">{lis}</ul>
  </div>
</section>'''


def testimonials() -> str:
    return f'''<section class="section section--sand testimonials" aria-labelledby="quotes-title">
  <div class="container">
    {section_head("Guest notes", "Kind words from <em>fictional guests.</em>", title_cls="display", title_id="quotes-title")}
    <div class="quotes">
      <div class="quotes__lead">{testimonial("One of those rare hotels where everything feels considered, but nothing feels forced.", "A weekend guest")}</div>
      <div class="quotes__pair">
        {testimonial("The view from our room was extraordinary. We came for two nights and immediately wished we'd booked four.", "A couple, in the Lake Room")}
        {testimonial("The perfect balance of beautiful design, wonderful food and genuine warmth.", "A midweek guest")}
      </div>
    </div>
    <p class="fine-print" data-reveal>These comments were written for this concept project. They are not real reviews.</p>
  </div>
</section>'''


def journal() -> str:
    a, b, c = (ARTICLES[s] for s in ("five-walks-worth-getting-up-early-for", "a-slow-weekend-in-the-lake-district", "where-we-source-our-ingredients"))
    return f'''<section class="section journal-preview" aria-labelledby="journal-title">
  <div class="container">
    {section_head("From the journal", "Notes from the <em>Lakes.</em>", title_cls="display", title_id="journal-title")}
    <div class="magazine">
      <div class="magazine__lead">{journal_card(a, "feature")}</div>
      <div class="magazine__side">{journal_card(b, "compact")}{journal_card(c, "compact")}</div>
    </div>
    <div class="section-cta" data-reveal>{button("Read the Journal", url("journal/"), "secondary", arrow=True)}</div>
  </div>
</section>'''


def final_cta() -> str:
    return f'''<section class="final-cta" aria-labelledby="cta-title">
  <div class="final-cta__media">{img(TERR, ratio=(16, 9), sizes="100vw", widths=(800, 1200, 1600, 2000, 2560), mobile_ratio=(4, 5))}</div>
  <div class="final-cta__scrim" aria-hidden="true"></div>
  <div class="final-cta__content" data-reveal>
    <h2 class="final-cta__title" id="cta-title">Your room is <em>waiting.</em></h2>
    <p class="final-cta__text">Come for the landscape. Stay for everything else.</p>
    {button("Check Availability", url("book/"), "primary", cls="btn--on-image")}
  </div>
</section>
<div class="container demo-wrap">{demo_banner()}</div>'''


def hotel_schema():
    return {
        "@context": "https://schema.org", "@type": "Hotel",
        "name": "The Alder House", "url": abs_url(),
        "description": "A fictional boutique hotel concept in the English Lake District. Portfolio project; not a real business.",
        "disambiguatingDescription": "Fictional concept project. Not a real, bookable hotel.",
        "image": abs_src(EXT),
        "address": {"@type": "PostalAddress", "addressRegion": "Cumbria", "addressCountry": "GB"},
        "amenityFeature": [{"@type": "LocationFeatureSpecification", "name": n, "value": True}
                           for n in ("Restaurant", "Free Wi-Fi", "Breakfast included", "Bar")],
    }


def build():
    body = "\n".join([hero(), booking_strip(), intro(), rooms(), statement(), dining(), explore(), split(),
                      testimonials(), journal(), final_cta()])
    html = page("", "The Alder House",
                "A fictional boutique hotel concept in the Lake District: individually designed rooms, seasonal cooking and a quiet corner of the fells. Stay a little longer.",
                body, overlay=True, schema=[hotel_schema()], body_class="page-home",
                full_title="The Alder House | Boutique Hotel in the Lake District (Concept Project)",
                preload=src(EXT))
    return [("", html)]
