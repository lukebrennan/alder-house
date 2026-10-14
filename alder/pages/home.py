from ..config import url, abs_url
from ..images import (AUT, BRK, COCK, CORN, ENT, EVE, EXT, FELL, FISH, GARD, HOUSE, JET, LAKE, LAMB, REST, STP,
                      SUITE, TERR, VIL, WALK, WTF, abs_src, img)
from ..journal import BY_SLUG as ARTICLES
from ..layout import page
from ..rooms import BY_SLUG as ROOMS, FEATURED
from ..ui import (booking_form, button, eyebrow, journal_card, media, room_tile, testimonial, text_link)


def hero() -> str:
    picture = img(EXT, sizes="100vw", priority=True)
    return f'''<section class="hero" aria-labelledby="hero-title">
  <div class="hero__media">{picture}</div>
  <div class="hero__scrim" aria-hidden="true"></div>
  <div class="hero__content">
    <p class="hero__label">Boutique hotel · Lake District</p>
    <h1 class="hero__title" id="hero-title">A more thoughtful kind of escape.</h1>
    <div class="hero__row">
      <p class="hero__lede">A quiet retreat in the heart of the Lake District, shaped by beautiful surroundings, thoughtful hospitality and the simple pleasure of slowing down.</p>
      <div class="hero__actions">
        {button("Book your stay", url("book/"), "primary", cls="btn--on-image")}
        {text_link("Discover the house", "#welcome", "link-arrow--light")}
      </div>
    </div>
    <div class="hero__dock">{booking_form("bar", uid="home")}</div>
  </div>
</section>'''


def intro() -> str:
    return f'''<section class="section intro" id="welcome" aria-labelledby="intro-title">
  <div class="container intro__grid">
    <div class="intro__text" data-reveal>
      {eyebrow("Welcome to The Alder House")}
      <h2 class="display" id="intro-title">Some places make it easier to slow down.</h2>
      <p class="lede">Set amongst the fells and waters of the Lake District, The Alder House is a small boutique hotel created for unhurried stays. Beautiful rooms, thoughtful food and the landscape right outside your door.</p>
      {text_link("Discover our story", url("our-story/"))}
    </div>
    <div class="intro__images">{media(ENT, (4, 5), sizes="(min-width: 960px) 46vw, 100vw")}</div>
  </div>
</section>'''


def rooms() -> str:
    tiles = "".join(room_tile(ROOMS[s]) for s in FEATURED)
    return f'''<section class="section section--tight-top" aria-labelledby="rooms-title">
  <div class="container">
    <div class="head-row" data-reveal>
      <div>{eyebrow("Stay")}<h2 class="display" id="rooms-title">Rooms made for switching off.</h2></div>
      {text_link("View all rooms", url("stay/"))}
    </div>
    <div class="tiles">{tiles}</div>
  </div>
</section>'''


def statement() -> str:
    return f'''<section class="statement" aria-labelledby="statement-title">
  <div class="statement__media" data-parallax>{img(EVE, sizes="100vw")}</div>
  <div class="statement__scrim" aria-hidden="true"></div>
  <div class="statement__content" data-reveal>
    <h2 class="statement__title" id="statement-title">Stay a little longer.</h2>
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
      {media(LAMB, (4, 5), sizes="(min-width: 960px) 22vw, 45vw", cls="dining__a")}
      {media(STP, (4, 5), sizes="(min-width: 960px) 22vw, 45vw", cls="dining__b")}
    </div>
    <div class="dining__text" data-reveal>
      {eyebrow("Eat and drink", "eyebrow--gold")}
      <h2 class="display" id="dining-title">Food rooted in the landscape.</h2>
      <p class="lede">Alder Kitchen cooks with the seasons. Seasonal British produce, local suppliers and a relaxed room in which to enjoy them, with nothing fussy and nothing forced.</p>
      <ul class="dining__list">{lis}</ul>
      {button("Discover Alder Kitchen", url("dining/"), "light", arrow=True)}
    </div>
  </div>
</section>'''


def explore() -> str:
    items = [
        ("Fell walking", WALK, "explore/#walking", "Paths that begin at the gate."),
        ("Wild swimming", WTF, "explore/#lakes", "Cold, clear and quietly addictive."),
        ("Lake cruises", JET, "explore/#lakes", "See the shoreline from the water."),
        ("Villages and markets", VIL, "explore/#villages", "Bakeries, bookshops and stone lanes."),
    ]
    cards = "".join(f'''<li class="experience" data-reveal>
  <a href="{url(p)}">{media(k, (3, 4), sizes="(min-width: 1000px) 24vw, (min-width: 640px) 48vw, 74vw", cls="hover-zoom")}
  <span class="experience__label"><span class="experience__title">{t}</span><span class="experience__line">{line}</span></span></a></li>''' for t, k, p, line in items)
    return f'''<section class="section explore" aria-labelledby="explore-title">
  <div class="container">
    <div class="head-row" data-reveal>
      <div>{eyebrow("Explore")}<h2 class="display" id="explore-title">Step outside.</h2></div>
      {text_link("Explore the Lake District", url("explore/"))}
    </div>
    <ul class="experience-grid">{cards}</ul>
  </div>
</section>'''


def split() -> str:
    pts = [("Thoughtful spaces", "Every room is individually designed with natural materials, soft textures and views worth waking up for."),
           ("Good food", "Seasonal cooking, local ingredients and an atmosphere that never feels overly formal."),
           ("Room to breathe", "Walk from the hotel into some of Britain's most remarkable countryside.")]
    lis = "".join(f'<li><h3>{t}</h3><p>{d}</p></li>' for t, d in pts)
    return f'''<section class="split" aria-labelledby="split-title">
  <div class="split__panel" data-reveal>
    {eyebrow("The house", "eyebrow--gold")}
    <h2 class="display" id="split-title">Designed around the way you want to stay.</h2>
    <ul class="points">{lis}</ul>
  </div>
  <div class="split__media">{media(HOUSE, (4, 3), sizes="(min-width: 960px) 50vw, 100vw", reveal=False)}</div>
</section>'''


def testimonials() -> str:
    return f'''<section class="section section--sand testimonials" aria-labelledby="quotes-title">
  <div class="container">
    <div class="head-row" data-reveal><div>{eyebrow("Guest notes")}<h2 class="display" id="quotes-title">What guests say.</h2></div></div>
    <div class="quotes">
      {testimonial("One of those rare hotels where everything feels considered, but nothing feels forced.", "A weekend guest")}
      {testimonial("The view from our room was extraordinary. We came for two nights and immediately wished we'd booked four.", "A couple, in the Lake Room")}
      {testimonial("The perfect balance of beautiful design, wonderful food and genuine warmth.", "A midweek guest")}
    </div>
  </div>
</section>'''


def journal() -> str:
    a, b, c = (ARTICLES[s] for s in ("five-walks-worth-getting-up-early-for", "a-slow-weekend-in-the-lake-district", "where-we-source-our-ingredients"))
    return f'''<section class="section journal-preview" aria-labelledby="journal-title">
  <div class="container">
    <div class="head-row" data-reveal>
      <div>{eyebrow("From the journal")}<h2 class="display" id="journal-title">Notes from the Lakes.</h2></div>
      {text_link("Read the Journal", url("journal/"))}
    </div>
    <div class="magazine">
      <div class="magazine__lead">{journal_card(a, "feature")}</div>
      <div class="magazine__side">{journal_card(b, "compact")}{journal_card(c, "compact")}</div>
    </div>
  </div>
</section>'''


def final_cta() -> str:
    return f'''<section class="final-cta" aria-labelledby="cta-title">
  <div class="final-cta__media">{img(TERR, sizes="100vw")}</div>
  <div class="final-cta__scrim" aria-hidden="true"></div>
  <div class="final-cta__content" data-reveal>
    <h2 class="final-cta__title" id="cta-title">Your room is waiting.</h2>
    <p class="final-cta__text">Come for the landscape. Stay for everything else.</p>
    {button("Check availability", url("book/"), "primary", cls="btn--on-image")}
  </div>
</section>'''


def hotel_schema():
    return {
        "@context": "https://schema.org", "@type": "Hotel",
        "name": "The Alder House", "url": abs_url(),
        "description": "A small boutique hotel in the English Lake District with individually designed rooms, seasonal cooking and easy access to the fells and lakes.",
        "image": abs_src(EXT),
        "address": {"@type": "PostalAddress", "addressRegion": "Cumbria", "addressCountry": "GB"},
        "amenityFeature": [{"@type": "LocationFeatureSpecification", "name": n, "value": True}
                           for n in ("Restaurant", "Free Wi-Fi", "Breakfast included", "Bar")],
    }


def build():
    body = "\n".join([hero(), intro(), rooms(), statement(), dining(), explore(), split(),
                      testimonials(), journal(), final_cta()])
    html = page("", "The Alder House",
                "A small boutique hotel in the Lake District: individually designed rooms, seasonal cooking and a quiet corner of the fells. Stay a little longer.",
                body, overlay=True, schema=[hotel_schema()], body_class="page-home",
                full_title="The Alder House | Boutique Hotel in the Lake District", preload=EXT)
    return [("", html)]
