"""Photography manifest and <img> helper.

Photographs are the supplied WebP files in static/img/photos/. Keys are the file
names (without extension), so every image has a descriptive filename. Swap a
photo by replacing the file; edit alt text and focal point here.
"""
from __future__ import annotations

from html import escape

from .config import abs_url, url

EXT = "alder-house-lake-district-hotel-exterior-sunset"
TERR = "alder-house-lakeside-terrace-golden-hour"
ENT = "alder-house-boutique-hotel-entrance"
BRK = "alder-house-breakfast-full-english"
BATH = "alder-house-freestanding-bath-room-detail"
BATHV = "alder-house-lake-view-bathroom"
COCK = "alder-house-signature-cocktail"
LAMB = "alder-kitchen-herdwick-lamb-main-course"
REST = "alder-kitchen-restaurant-interior"
FISH = "alder-kitchen-seasonal-fish-main-course"
STP = "alder-kitchen-sticky-toffee-pudding"
WINE = "alder-kitchen-wine-dinner-setting"
AUT = "lake-district-autumn-lake-mountains"
EVE = "lake-district-evening-fell-landscape"
WALK = "lake-district-fell-walking-sunrise"
JET = "lake-district-lakeside-jetty-rowing-boat"
VIL = "lake-district-stone-village-street"
WTF = "lake-district-woodland-waterfall"
SUITE = "the-alder-suite-lake-view-bedroom"
CORN = "the-corner-room-boutique-hotel"
FELL = "the-fell-room-lake-district-boutique-hotel"
GARD = "the-garden-room-boutique-hotel"
HOUSE = "the-house-suite-private-lounge"
LAKE = "the-lake-room-boutique-hotel"

# key: (width, height, alt, focal x, focal y)
_RAW = {
    EXT: (2000, 1200, "Golden light over a Lake District lake and fells, with a hotel terrace among the trees on the right", .42, .5),
    TERR: (1800, 1200, "A lakeside terrace with parasols and tables, and a view across the water to the fells at golden hour", .5, .5),
    ENT: (1600, 1200, "A black front door with a brass knocker, flanked by olive trees in stone planters", .35, .5),
    BRK: (1600, 1200, "A cooked breakfast of eggs, bacon, sausage, tomato and mushrooms, with coffee and juice", .5, .5),
    BATH: (1600, 1200, "A freestanding bath beside a window in a calm bathroom with a lamp and an armchair", .5, .5),
    BATHV: (1600, 1200, "A freestanding bath and a basin in a bright bathroom with a view of the fells", .4, .5),
    COCK: (1600, 1200, "A creamy cocktail in a coupe glass, garnished with a dried orange slice", .5, .5),
    LAMB: (1600, 1200, "Herdwick lamb with potatoes and greens on a white plate", .5, .5),
    REST: (1800, 1200, "The Alder Kitchen dining room, with wooden tables and chairs, plants and a lit shelf of bottles", .5, .5),
    FISH: (1600, 1200, "A seared fish fillet on a bed of greens in a pale sauce", .5, .5),
    STP: (1600, 1200, "Sticky toffee pudding with cream and caramel sauce on a white plate", .5, .5),
    WINE: (1600, 1200, "A glass of white wine beside a candle and sprigs of herbs on a dinner table", .6, .5),
    AUT: (1800, 1200, "An autumn lake with a wooded island and mountains beyond", .5, .5),
    EVE: (1800, 1200, "A footpath beside a dry stone wall leading to a lake and fells in evening light", .5, .5),
    WALK: (1800, 1200, "A walker looking out over a lake and fells at sunrise", .5, .5),
    JET: (1800, 1200, "A wooden rowing boat beside a jetty on a lake, with fells beyond", .5, .5),
    VIL: (1800, 1200, "A Lakeland village street lined with stone cottages and flowers", .4, .5),
    WTF: (1600, 1200, "A waterfall tumbling over mossy rocks in woodland", .5, .5),
    SUITE: (1600, 1200, "The Alder Suite bedroom, with olive and cream linen, lamps and a lake view", .3, .6),
    CORN: (1600, 1200, "The Corner Room, with an olive throw on a cream bed and windows looking out to the fells", .5, .5),
    FELL: (1600, 1200, "The Fell Room, with an upholstered headboard, an olive throw, bedside lamps and a view of the fells", .5, .5),
    GARD: (1600, 1200, "The Garden Room, with an olive throw on a white bed, lamps and tall doors to the garden", .5, .5),
    HOUSE: (1600, 1200, "The House Suite sitting room, with green armchairs beside a lit fire", .5, .5),
    LAKE: (1600, 1200, "The Lake Room, with olive and white linen on the bed and a lake view through the window", .5, .5),
}

IMAGES = {k: dict(w=v[0], h=v[1], alt=v[2], fx=v[3], fy=v[4]) for k, v in _RAW.items()}


def src(key: str, *_ignored, **__) -> str:
    """Root-relative URL of a photograph (extra size arguments are accepted and ignored)."""
    return url(f"assets/img/photos/{key}.webp")


def abs_src(key: str) -> str:
    return abs_url(f"assets/img/photos/{key}.webp")


def alt_for(key: str) -> str:
    return IMAGES[key]["alt"]


def img(key, ratio=None, sizes="100vw", widths=None, alt=None, loading="lazy", cls="", priority=False,
        mobile_ratio=None) -> str:
    """<img> with intrinsic dimensions (no layout shift) and a focal-point crop."""
    d = IMAGES[key]
    a = escape(alt if alt is not None else d["alt"], quote=True)
    load = 'fetchpriority="high" loading="eager"' if priority else f'loading="{loading}"'
    # The Alder Suite photo has a decorative script sign on the wall; crop it out on the page.
    cls = f"{cls} crop-clear-sign".strip() if key == SUITE else cls
    c = f' class="{cls}"' if cls else ""
    pos = f'style="object-position:{round(d["fx"] * 100)}% {round(d["fy"] * 100)}%" '
    return (f'<img src="{src(key)}" width="{d["w"]}" height="{d["h"]}" alt="{a}" sizes="{sizes}" '
            f'{pos}decoding="async" {load}{c}>')


def og_image(key: str) -> str:
    return abs_src(key)
