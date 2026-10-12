from ..images import EXT, TERR, ENT, BRK, BATH, BATHV, COCK, LAMB, REST, FISH, STP, WINE, AUT, EVE, WALK, JET, VIL, WTF, SUITE, CORN, FELL, GARD, HOUSE, LAKE  # noqa: F401
from ..config import url
from ..layout import page
from ..ui import button, demo_banner, eyebrow, icon, media, page_hero, section_head

HOTEL = (330, 270)
# name, slug, minutes, (x, y), label offset (dx, dy), text-anchor
PLACES = [
    ("Grasmere", "grasmere", 18, (275, 205), (-12, -4), "end"),
    ("Ambleside", "ambleside", 22, (313, 368), (-12, 4), "end"),
    ("Windermere", "windermere", 28, (376, 397), (14, 5), "start"),
    ("Hawkshead", "hawkshead", 30, (434, 330), (12, 4), "start"),
    ("Keswick", "keswick", 35, (267, 96), (-12, -4), "end"),
    ("Ullswater", "ullswater", 45, (459, 117), (12, -4), "start"),
]

TOPICS = [
    dict(id="walking", title="Walking", img=WALK,
         text="Start with a short, rewarding climb and build from there. There is a path for every pair of legs, and a hot bath waiting at the end of it.",
         items=[("Catbells", "A short ridge walk above Derwentwater with a view out of all proportion to the effort."),
                ("Orrest Head", "An easy hour up and down, and one of the best first walks in the Lakes."),
                ("Loughrigg Terrace", "A level shelf of path with a wide view over Grasmere."),
                ("Tarn Hows", "A gentle circuit around a still tarn, lovely in low light.")]),
    dict(id="lakes", title="Lakes", img=JET,
         text="The water is the heart of the place. Take a boat, hire a rowing boat for an hour, or find a quiet shore and swim.",
         items=[("Windermere", "The largest lake in England, with steamers, rowing boats and long shoreline walks."),
                ("Derwentwater", "Wooded islands, a gentle shore path and the fells reflected on still mornings."),
                ("Ullswater", "A long, quiet lake with a classic steamer route and good walking along the shore."),
                ("Wild swimming", "Choose a shallow, easy shore, go with a friend and keep it short.")]),
    dict(id="food-drink", title="Food & Drink", img=BRK,
         text="Small bakeries, farm shops and old ale houses. Eat well, and take a little home with you.",
         items=[("Village bakeries", "Warm bread, pies and gingerbread for the rucksack."),
                ("Farm shops", "Cheese, chutney and cured meats from within a few miles."),
                ("Ale houses", "Stone floors, low beams and a fire. Order the local."),
                ("Picnics", "Ask us, and the kitchen will pack one for the fell.")]),
    dict(id="villages", title="Villages", img=VIL,
         text="Slate roofs, whitewashed walls and lanes that were never meant for cars. Each village has its own pace.",
         items=[("Grasmere", "Quiet, stone-built and set beside its own small lake."),
                ("Ambleside", "Independent shops, outdoor kit and an honest bakery."),
                ("Hawkshead", "A web of lanes, small galleries and tea rooms."),
                ("Keswick", "A proper market town on the edge of Derwentwater.")]),
    dict(id="culture", title="Culture", img=ENT,
         text="Poets, painters and storytellers have always been drawn to this corner of England. You can follow their footsteps, or simply sit where they sat.",
         items=[("Poets' houses", "Grasmere and Rydal have long literary associations."),
                ("Story and setting", "Several small museums celebrate the people who loved the Lakes."),
                ("Theatre and cinema", "Small venues in the larger towns, including a lakeside theatre."),
                ("Galleries", "Local painters and potters show work in many of the villages.")]),
    dict(id="rainy-days", title="Rainy Days", img=HOUSE,
         text="It rains. It is part of the charm, and the reason everything is so green. These are the things we do when the cloud comes down.",
         items=[("Stay in", "A fire, a book and a pot of tea. The best plan, honestly."),
                ("Waterfalls", "Wear a waterproof and visit them at their best."),
                ("Bookshops", "The Lakes are well stocked with good, crowded second-hand shops."),
                ("A long lunch", "A table by the window, and nowhere to be.")]),
]


def map_svg() -> str:
    hx, hy = HOTEL
    lines, pins = [], []
    for name, slug, mins, (x, y), (dx, dy), anchor in PLACES:
        lines.append(f'<line class="map__route" data-place="{slug}" x1="{hx}" y1="{hy}" x2="{x}" y2="{y}"/>')
        pins.append(
            f'<g class="map__pin" data-place="{slug}" transform="translate({x} {y})">'
            f'<circle r="14" class="map__halo"/><circle r="6" class="map__dot"/>'
            f'<text x="{dx}" y="{dy}" text-anchor="{anchor}" class="map__label">{name}'
            f'<tspan x="{dx}" dy="14" class="map__mins">{mins} min</tspan></text></g>')
    return f'''<svg class="map__svg" viewBox="0 0 600 520" role="img" aria-labelledby="map-title map-desc" focusable="false">
  <title id="map-title">Illustrative map of nearby villages and lakes</title>
  <desc id="map-desc">A stylised map showing The Alder House at the centre, with Grasmere, Ambleside, Windermere, Hawkshead, Keswick and Ullswater marked at approximate drive times. The map is not to scale and The Alder House is fictional.</desc>
  <g class="map__contours" fill="none">
    <path d="M60 80C120 40 220 50 250 110C280 170 200 210 140 190C80 170 20 130 60 80Z"/>
    <path d="M100 95C140 70 200 80 215 115C230 150 180 170 145 160C110 150 80 125 100 95Z"/>
    <path d="M430 40C500 20 570 70 560 140C550 200 480 220 430 190C390 160 380 70 430 40Z"/>
    <path d="M455 70C500 55 535 85 528 130C520 165 480 175 455 155C430 135 425 90 455 70Z"/>
    <path d="M60 380C100 330 190 340 200 410C210 470 120 500 70 470C30 440 30 410 60 380Z"/>
    <path d="M92 395C120 365 170 372 176 415C181 450 128 470 98 452C70 436 70 420 92 395Z"/>
    <path d="M470 420C520 390 585 420 580 475C575 515 500 520 465 495C430 470 440 440 470 420Z"/>
  </g>
  <g class="map__water">
    <path d="M362 300C372 330 366 360 376 395C386 430 380 470 372 505C362 500 356 470 360 440C364 410 352 380 354 350C356 325 352 310 362 300Z"/>
    <path d="M240 118C262 112 280 125 278 148C276 172 255 180 238 170C222 160 222 128 240 118Z"/>
    <path d="M255 222C265 214 280 218 282 230C280 242 262 244 254 236Z"/>
    <path d="M440 138C455 128 478 120 500 100C508 110 494 128 478 142C462 156 446 160 440 138Z"/>
  </g>
  <g>{"".join(lines)}</g>
  <g class="map__hotel" transform="translate({hx} {hy})">
    <circle r="20" class="map__hotel-ring"/><path d="M-9 6 L-3 -5 L1 1 L4 -3 L9 6 Z" class="map__hotel-mark"/>
    <text y="34" text-anchor="middle" class="map__hotel-label">The Alder House</text>
  </g>
  {"".join(pins)}
  <g class="map__compass" transform="translate(556 44)"><path d="M0 14V-14M0 -14l-5 8M0 -14l5 8"/><text y="30" text-anchor="middle">N</text></g>
</svg>'''


def map_section() -> str:
    items = "".join(
        f'<li><button type="button" class="places__item" data-place="{slug}"><span class="places__name">{name}</span>'
        f'<span class="places__time">{mins} minutes</span></button></li>'
        for name, slug, mins, *_ in PLACES)
    return f'''<section class="section section--tight-top" aria-labelledby="near-title">
  <div class="container">
    {section_head("Getting around", "Close at <em>hand.</em>", "Approximate drive times from the house. The Alder House is fictional, so these are illustrative rather than exact.", title_cls="display", title_id="near-title")}
    <div class="map" data-map data-reveal>
      <ul class="places" aria-label="Places and drive times">{items}</ul>
      <div class="map__figure">{map_svg()}<p class="map__caption">Illustrative map. Not to scale.</p></div>
    </div>
  </div>
</section>'''


def topic(t, i) -> str:
    rev = " topic--flip" if i % 2 else ""
    lis = "".join(f'<li><h3>{a}</h3><p>{b}</p></li>' for a, b in t["items"])
    return f'''<section class="topic{rev}" id="{t["id"]}" aria-labelledby="{t["id"]}-title">
  <div class="topic__media">{media(t["img"], (4, 5), sizes="(min-width: 960px) 38vw, 100vw")}</div>
  <div class="topic__text" data-reveal>
    {eyebrow(f"0{i + 1}")}
    <h2 class="display" id="{t["id"]}-title">{t["title"]}</h2>
    <p class="lede">{t["text"]}</p>
    <ul class="topic__list">{lis}</ul>
  </div>
</section>'''


def build():
    jump = "".join(f'<li><a href="#{t["id"]}">{t["title"]}</a></li>' for t in TOPICS)
    body = f'''{page_hero("The Lakes are <em>outside your door.</em>", "Explore", "Fells, lakes, villages and the occasional wet afternoon. This is how we would spend the days.",
                         AUT, crumbs=[("Explore", None)])}
<div class="container"><nav class="anchor-nav anchor-nav--wide" aria-label="Guide sections"><ul>{jump}</ul></nav></div>
{map_section()}
{"".join(topic(t, i) for i, t in enumerate(TOPICS))}
<section class="section section--dark" aria-labelledby="explore-cta">
  <div class="container narrow center" data-reveal>
    {eyebrow("Plan a stay", "eyebrow--gold")}
    <h2 class="display" id="explore-cta">Come for the landscape. <em>Stay for everything else.</em></h2>
    <div class="btn-row">{button("Check availability", url("book/"), "primary", cls="btn--on-image")}{button("Ask for ideas", url("contact/"), "light")}</div>
  </div>
</section>
<div class="container demo-wrap">{demo_banner("The places mentioned are real parts of the Lake District; The Alder House is fictional. Check opening times and conditions before you set out.")}</div>'''
    return [("explore/", page("explore/", "Explore the Lake District",
                              "A guide to walking, lakes, villages, food and rainy-day ideas around The Alder House, a fictional boutique hotel in the Lake District. Illustrative drive times.",
                              body, overlay=True, og_key=AUT, crumbs=[("Explore", "explore/")]))]
