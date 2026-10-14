from ..images import EXT, TERR, ENT, BRK, BATH, BATHV, COCK, LAMB, REST, FISH, STP, WINE, AUT, EVE, WALK, JET, VIL, WTF, SUITE, CORN, FELL, GARD, HOUSE, LAKE  # noqa: F401
from ..config import url
from ..images import img
from ..layout import page
from ..ui import button, demo_banner, eyebrow, icon, media, page_hero, text_link

CHAPTERS = [
    ("Respect for the building", TERR,
     ["Old walls are patient. We repaired the stonework with lime, kept the slate roof and restored the windows rather than replacing them.",
      "Where something was worn, we left it worn. A step that has been walked on for a century has earned its dip."]),
    ("Natural materials", CORN,
     ["Oak, wool, linen, slate and clay. Materials that age well and feel good under the hand.",
      "Nothing is plastic where it could be wood, and nothing is shiny where it could be matt. The rooms are quieter for it."]),
    ("Local craftspeople", FELL,
     ["A stonemason from the next valley rebuilt the garden wall. A joiner made the window seats and the staircase. Weavers and a small linen company made the throws and bedding.",
      "Their work is in every room, and we would rather you knew who made it."]),
    ("Independent suppliers", LAMB,
     ["We buy from people we can name: the farmer who raises our lamb, the grower who brings the leaves, the roaster who supplies the coffee.",
      "It makes the kitchen more honest, and the menu shorter and better."]),
    ("Relaxed hospitality", HOUSE,
     ["We want you to feel looked after, not watched. Someone will always know your name, and nobody will insist on a tour.",
      "Wet boots are expected, dogs are welcome by arrangement and the fire is lit from lunchtime on grey days."]),
    ("A connection to the landscape", EVE,
     ["The house sits at the edge of the fells and everything about it faces outwards. The windows are big, the doors are used and the best seats are by the glass.",
      "We hope you leave a little more aware of the place than when you arrived."]),
]


def chapter(i, c) -> str:
    title, key, paras = c
    rev = " topic--flip" if i % 2 else ""
    ps = "".join(f"<p>{p}</p>" for p in paras)
    return f'''<section class="topic{rev}" aria-labelledby="ch-{i}">
  <div class="topic__media">{media(key, (4, 5), sizes="(min-width: 960px) 38vw, 100vw")}</div>
  <div class="topic__text" data-reveal>
    {eyebrow(f"Chapter 0{i + 1}")}
    <h2 class="display" id="ch-{i}">{title}</h2>
    <div class="prose prose--lede">{ps}</div>
  </div>
</section>'''


def build():
    body = f'''{page_hero("A house shaped by its <em>surroundings.</em>", "Our story", "How an old house in the fells became a small, quiet hotel.",
                         ENT, crumbs=[("Our Story", None)])}
<section class="section" aria-labelledby="begin-title">
  <div class="container narrow" data-reveal>
    {eyebrow("The beginning")}
    <h2 class="display" id="begin-title">It did not need to be reinvented. It needed to be <em>looked after.</em></h2>
    <div class="prose prose--lede">
      <p>The Alder House began with an old house, a slope of fell behind it and a lake in front. It was quiet and a little tired, and it was clear what it wanted.</p>
      <p>We spent the first year doing very little. We walked the rooms in different weather, learned where the light fell at four o'clock and listened to the people who knew the building better than we did.</p>
      <p>The plan, once we had one, was simple: keep what was good, mend what was broken and add only what we would use ourselves.</p>
    </div>
  </div>
</section>
{"".join(chapter(i, c) for i, c in enumerate(CHAPTERS))}
<section class="statement statement--short" aria-label="A closing thought">
  <div class="statement__media" data-parallax>{img(WTF, ratio=(16, 9), sizes="100vw", widths=(800, 1200, 1600, 2000, 2560), mobile_ratio=(4, 5))}</div>
  <div class="statement__scrim" aria-hidden="true"></div>
  <div class="statement__content" data-reveal>
    <blockquote class="statement__quote"><p>Our job was to do as little as possible, and to do it <em>well.</em></p></blockquote>
  </div>
</section>
<section class="section section--sand" aria-labelledby="story-cta">
  <div class="container narrow center" data-reveal>
    {eyebrow("Come and see")}
    <h2 class="display" id="story-cta">The best way to understand a house is to <em>stay in it.</em></h2>
    <div class="btn-row">{button("View the rooms", url("stay/"), "primary")}{text_link("Read the Journal", url("journal/"))}</div>
  </div>
</section>
<div class="container demo-wrap">{demo_banner("This story is fiction, written for the concept. The Alder House is not a real property, and no real building, history or craftsperson is described.")}</div>'''
    return [("our-story/", page("our-story/", "Our Story",
                                "The fictional story of The Alder House: an old house in the Lake District, repaired with care, local craftspeople and a light touch.",
                                body, overlay=True, og_key=ENT, crumbs=[("Our Story", "our-story/")]))]
