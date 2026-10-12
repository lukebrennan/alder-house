from ..images import abs_src, EXT, TERR, ENT, BRK, BATH, BATHV, COCK, LAMB, REST, FISH, STP, WINE, AUT, EVE, WALK, JET, VIL, WTF, SUITE, CORN, FELL, GARD, HOUSE, LAKE  # noqa: F401
from ..config import url, abs_url
from ..images import src
from ..layout import page
from ..rooms import ROOMS, amenity_list
from ..ui import (amenity_items, booking_form, breadcrumbs, button, demo_banner, eyebrow, gallery, icon,
                  money, page_hero, price_line, room_card, room_meta, room_row, section_head, text_link)


def listing():
    rows = "".join(room_row(r, i + 1, reverse=bool(i % 2)) for i, r in enumerate(ROOMS))
    body = f'''{page_hero("Stay", "The Alder House", "Individually designed rooms, quiet mornings and views that make it tempting to stay in bed a little longer.",
                         TERR, crumbs=[("Stay", None)])}
<section class="section section--tight-top" aria-label="Rooms">
  <div class="container">
    <div class="stay-intro" data-reveal>
      <p class="lede">Six rooms and suites, each different in shape, outlook and mood. Every one has a bed dressed in heavy linen, a bathroom with proper water pressure and breakfast in the morning.</p>
      <ul class="stay-intro__facts">
        <li>{icon("breakfast", "icon", 22)}<span>Breakfast included</span></li>
        <li>{icon("wifi", "icon", 22)}<span>Complimentary Wi-Fi</span></li>
        <li>{icon("leaf", "icon", 22)}<span>Dogs by arrangement</span></li>
      </ul>
    </div>
    <div class="room-list">{rows}</div>
  </div>
</section>
<section class="section section--sand" aria-labelledby="stay-cta-title">
  <div class="container narrow center" data-reveal>
    {eyebrow("Plan your stay")}
    <h2 class="display" id="stay-cta-title">Not sure which room? <em>Ask us.</em></h2>
    <p class="lede">Tell us what you are celebrating, or simply what you need, and we will suggest the right room and the best time to come.</p>
    <div class="btn-row">{button("Check availability", url("book/"), "primary")}{button("Contact the house", url("contact/"), "secondary")}</div>
  </div>
</section>
<div class="container demo-wrap">{demo_banner("Room names, sizes and prices are invented for this concept project. Prices shown are per room, per night, including breakfast.")}</div>'''
    return ("stay/", page("stay/", "Stay", "Six individually designed rooms and suites at The Alder House, a fictional boutique hotel in the Lake District. Breakfast included.",
                          body, overlay=True, crumbs=[("Stay", "stay/")], og_key=TERR,
                          preload=None))


def room_page(r):
    path = f'stay/{r["slug"]}/'
    others = [x for x in ROOMS if x["slug"] != r["slug"]]
    # Two closest in price plus one other, so "related" is meaningful.
    others.sort(key=lambda x: abs(x["price"] - r["price"]))
    related = "".join(room_card(x) for x in others[:3])
    body = f'''<article class="room-page">
<div class="container room-page__head">
  {breadcrumbs([("Stay", "stay/"), (r["name"], None)])}
  <div class="room-page__title" data-reveal>
    {eyebrow("Stay · " + r["view"])}
    <h1 class="display">{r["name"]}</h1>
    <p class="lede">{r["tagline"]}</p>
  </div>
</div>
<div class="container">{gallery(r)}
  <p class="gallery__hint" data-reveal>{icon("view", "icon", 18)}<span>Select a photograph to view it larger.</span></p>
</div>
<div class="container room-page__grid">
  <div class="room-page__main">
    <div data-reveal>
      {room_meta(r)}
      <div class="prose prose--lede">{"".join(f"<p>{p}</p>" for p in [r["short"]] + r["long"])}</div>
    </div>
    <section aria-labelledby="amen-title" data-reveal>
      <h2 class="h3" id="amen-title">In the room</h2>
      <ul class="amenity-list">{amenity_items(r)}</ul>
    </section>
    <section aria-labelledby="know-title" data-reveal>
      <h2 class="h3" id="know-title">Good to know</h2>
      <ul class="know-list">
        <li>Check-in from 3pm, check-out by 11am.</li>
        <li>Breakfast in Alder Kitchen is included in the room rate.</li>
        <li>Well-behaved dogs are welcome in selected rooms by arrangement.</li>
      </ul>
    </section>
  </div>
  <aside class="booking-panel" aria-labelledby="book-title" data-reveal>
    <h2 class="booking-panel__title" id="book-title">Reserve {r["name"]}</h2>
    {price_line(r)}
    <p class="booking-panel__note">Breakfast included. Taxes included.</p>
    {booking_form("stacked", room=r["slug"], uid="room")}
    <p class="booking-panel__demo">Demonstration only. No payment is taken.</p>
  </aside>
</div>
<section class="section section--sand" aria-labelledby="related-title">
  <div class="container">
    {section_head("Other rooms", "You might also <em>like.</em>", title_cls="display", title_id="related-title")}
    <div class="mini-grid">{related}</div>
    <div class="section-cta" data-reveal>{text_link("View all rooms", url("stay/"))}</div>
  </div>
</section>
</article>'''
    schema = [{
        "@context": "https://schema.org", "@type": "HotelRoom", "name": r["name"],
        "description": r["short"], "url": abs_url(path),
        "image": abs_src(r["lead"]),
        "occupancy": {"@type": "QuantitativeValue", "maxValue": r["sleeps"]},
        "bed": {"@type": "BedDetails", "typeOfBed": r["schema_bed"], "numberOfBeds": 1},
        "floorSize": {"@type": "QuantitativeValue", "value": r["size"], "unitCode": "MTK"},
        "isPartOf": {"@type": "Hotel", "name": "The Alder House", "url": abs_url()},
        "amenityFeature": [{"@type": "LocationFeatureSpecification", "name": l, "value": True} for _, l in amenity_list(r)],
    }]
    return (path, page(path, r["name"], f'{r["name"]} at The Alder House, a fictional boutique hotel in the Lake District: {r["short"]}',
                       body, lightbox=True, schema=schema, og_key=r["lead"],
                       crumbs=[("Stay", "stay/"), (r["name"], path)]))


def build():
    return [listing()] + [room_page(r) for r in ROOMS]
