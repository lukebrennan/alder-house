"""Photography manifest and responsive <img> helper.

Photographs live in static/img/photos/ in three sizes per image
(<name>-800.webp, <name>-1600.webp, <name>-2400.webp). Keys are the file names
without the size suffix, so every image has a descriptive filename. To swap a
photo, replace its three files (keep the names) or edit the manifest below.
"""
from __future__ import annotations

from html import escape

from .config import abs_url, url

EXT = "windermere-sunset-jetty-silhouette"
TERR = "derwentwater-dusk-pink-cloud"
ENT = "stone-manor-house-reflected-in-water"
BRK = "breakfast-table-by-window"
BATH = "freestanding-bath-wide-window"
BATHV = "white-freestanding-bath-with-fern"
COCK = "cocktail-glass-dark-bar"
LAMB = "sunday-roast-plate-greens"
REST = "timber-dining-room-tall-windows"
FISH = "roast-fish-tomatoes-golden-sauce"
STP = "sticky-toffee-pudding-blue-plate"
WINE = "dinner-table-wine-glasses"
AUT = "lakes-between-green-hills"
EVE = "rowing-boats-moored-at-dusk"
WALK = "walker-above-lake-district-lake"
JET = "boats-on-windermere-golden-haze"
VIL = "lakeland-cottage-red-door"
WTF = "wild-swimmer-lake-fells"
SUITE = "green-bedroom-white-bedding"
CORN = "bedroom-sculptural-timber-headboard"
FELL = "bedroom-green-panelling-throw"
GARD = "bed-beside-bright-window"
HOUSE = "sitting-room-wood-burner"
LAKE = "bedroom-olive-wall-gingham-pillows"

# key: (width of largest file, height, alt text, focal point x, focal point y)
_RAW = {
    EXT: (2400, 1600, "Sunset over Windermere, with the posts of an old jetty silhouetted against the water", 0.5, 0.55),
    TERR: (2400, 1600, "Derwentwater at dusk, with pink cloud above the fells and still water below", 0.5, 0.5),
    ENT: (2400, 1606, "A timber-framed manor house with tall brick chimneys, reflected in still water beneath a blue sky", 0.5, 0.45),
    BRK: (2400, 1585, "A breakfast table by a window, laid with coffee, bread and a potted plant", 0.5, 0.5),
    BATH: (2400, 1350, "A freestanding stone bath beside a wide window looking out to open landscape", 0.5, 0.5),
    BATHV: (2400, 1600, "A white freestanding bath in a bright bathroom with a fern beside it", 0.5, 0.5),
    COCK: (2400, 1600, "A cocktail in a glass on a dark bar table", 0.5, 0.5),
    LAMB: (2400, 1800, "A plate of roast meat with greens and carrots", 0.5, 0.5),
    REST: (2400, 1600, "A timber-lined dining room with lamps, set tables and windows looking out to trees", 0.5, 0.5),
    FISH: (2400, 3600, "A fillet of white fish with roasted tomatoes and a golden sauce", 0.5, 0.3),
    STP: (2400, 1921, "Sticky toffee pudding topped with ice cream, on a blue patterned plate", 0.5, 0.5),
    WINE: (2400, 1602, "A dinner table laid with wine glasses and a candlelit lamp", 0.5, 0.5),
    AUT: (2400, 1600, "A lake lying between rolling green hills under a broad sky", 0.5, 0.5),
    EVE: (2400, 1600, "Rowing boats moored on a lake at dusk, with dark fells behind", 0.5, 0.5),
    WALK: (2400, 1600, "A walker sitting on a hillside high above a Lake District lake", 0.5, 0.5),
    JET: (2400, 1800, "Boats on the water at Windermere in golden haze", 0.5, 0.5),
    VIL: (2400, 1639, "A whitewashed Lakeland cottage with a red door beside a country lane", 0.5, 0.5),
    WTF: (2400, 1351, "A wild swimmer in a Lake District lake, with fells rising behind", 0.5, 0.5),
    SUITE: (2400, 1600, "The Alder Suite bedroom, with deep green walls, white bedding and windows onto the trees", 0.5, 0.5),
    CORN: (2400, 1600, "The Corner Room, with a sculptural timber headboard, white linen and a striped rug", 0.5, 0.5),
    FELL: (2400, 1636, "The Fell Room, with sage green panelling, white linen and a heather-coloured throw", 0.5, 0.5),
    GARD: (2400, 1600, "The Garden Room, with a white-linen bed beside a bright window", 0.5, 0.5),
    HOUSE: (2400, 1600, "The House Suite sitting room, with a lit wood burner, armchairs and warm lamplight", 0.5, 0.5),
    LAKE: (2400, 1536, "The Lake Room, with olive walls, gingham cushions and a brown wool blanket", 0.5, 0.5),
}

IMAGES = {k: dict(w=v[0], h=v[1], alt=v[2], fx=v[3], fy=v[4]) for k, v in _RAW.items()}
SIZES = (800, 1600, 2400)


def src(key: str, width: int = 1600, **_ignored) -> str:
    """Root-relative URL of the smallest rendition that is at least `width` wide."""
    size = next((s for s in SIZES if s >= width), SIZES[-1])
    return url(f"assets/img/photos/{key}-{size}.webp")


def abs_src(key: str, width: int = 1600) -> str:
    size = next((s for s in SIZES if s >= width), SIZES[-1])
    return abs_url(f"assets/img/photos/{key}-{size}.webp")


def alt_for(key: str) -> str:
    return IMAGES[key]["alt"]


def img(key, ratio=None, sizes="100vw", widths=None, alt=None, loading="lazy", cls="", priority=False,
        mobile_ratio=None) -> str:
    """<img> with a srcset, intrinsic dimensions (no layout shift) and a focal-point crop."""
    d = IMAGES[key]
    a = escape(alt if alt is not None else d["alt"], quote=True)
    load = 'fetchpriority="high" loading="eager"' if priority else f'loading="{loading}"'
    c = f' class="{cls}"' if cls else ""
    pos = f'style="object-position:{round(d["fx"] * 100)}% {round(d["fy"] * 100)}%" '
    srcset = ", ".join(f"{src(key, s)} {s}w" for s in SIZES)
    return (f'<img src="{src(key, 1600)}" srcset="{srcset}" sizes="{sizes}" width="{d["w"]}" height="{d["h"]}" '
            f'alt="{a}" {pos}decoding="async" {load}{c}>')


def og_image(key: str) -> str:
    return abs_src(key, 1600)
