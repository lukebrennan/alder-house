"""Room data. Prices are nightly, in GBP, breakfast included."""

from .images import EXT, TERR, ENT, BRK, BATH, BATHV, COCK, LAMB, REST, FISH, STP, WINE, AUT, EVE, WALK, JET, VIL, WTF, SUITE, CORN, FELL, GARD, HOUSE, LAKE  # noqa: F401


# (icon, label)
A = {
    "king": ("bed", "King bed"),
    "shower": ("shower", "Walk-in rainfall shower"),
    "bath": ("bath", "Freestanding bath"),
    "radio": ("radio", "Roberts radio"),
    "wifi": ("wifi", "Complimentary Wi-Fi"),
    "tv": ("tv", "Smart TV"),
    "coffee": ("cup", "Tea and locally roasted coffee"),
    "robes": ("robe", "Bathrobes"),
    "toiletries": ("drop", "Luxury toiletries"),
    "breakfast": ("breakfast", "Breakfast included"),
    "fell": ("view", "Fell views"),
    "lake": ("view", "Lake views"),
    "garden": ("leaf", "Garden views"),
    "both": ("view", "Lake and fell views"),
    "terrace": ("leaf", "Private terrace"),
    "seat": ("seat", "Window seat"),
    "sitting": ("seat", "Separate sitting area"),
    "fire": ("flame", "Open fire in the sitting room"),
    "stepfree": ("step", "Step-free access"),
    "sofabed": ("bed", "Sofa bed for a third guest"),
}

COMMON = ["radio", "wifi", "tv", "coffee", "robes", "toiletries", "breakfast"]

ROOMS = [
    dict(
        slug="fell-room", name="The Fell Room", price=195, sleeps=2, bed="King bed", size=24,
        view="Fell view", lead=FELL,
        tagline="Warm timber, soft linen and the fells filling the window.",
        short="A calm room under the eaves, with oak joinery, a deep window seat and the fells filling the glass.",
        long=[
            "The Fell Room is the quietest corner of the house. A low ceiling, a bed dressed in washed linen and a window deep enough to sit in with a book.",
            "Mornings begin with the light moving across the fell. There is no hurry to leave, which is rather the point.",
        ],
        amenities=["king", "shower", "fell", "seat"] + COMMON,
        gallery=[FELL, WALK, EVE, AUT],
        schema_bed="KingBed",
    ),
    dict(
        slug="garden-room", name="The Garden Room", price=215, sleeps=2, bed="King bed", size=26,
        view="Garden view", lead=GARD,
        tagline="On the ground floor, with its own terrace and a door to the lawn.",
        short="Step-free and light-filled, with a private terrace for early coffee and a door straight onto the lawn.",
        long=[
            "Set on the ground floor and opening onto the garden, this is the easiest room in the house to settle into. The floor is flagged in local stone, the walls are a soft clay white and the bed faces the light.",
            "A small terrace holds two chairs and a table, ideal for a first cup of coffee while the lawn is still wet.",
        ],
        amenities=["king", "shower", "garden", "terrace", "stepfree"] + COMMON,
        gallery=[GARD, ENT, TERR, JET],
        schema_bed="KingBed",
    ),
    dict(
        slug="lake-room", name="The Lake Room", price=235, sleeps=2, bed="King bed", size=28,
        view="Lake view", lead=LAKE,
        tagline="A first-floor room with the water in view from the pillow.",
        short="A generous first-floor room facing the water, with a window seat made for watching the weather change.",
        long=[
            "The Lake Room looks straight down the valley. On still mornings the water holds the sky, and on wetter ones it disappears altogether, which is its own kind of pleasure.",
            "The bed is dressed in heavy linen, the walls in a muted olive, and the window seat is the best place in the house for an afternoon doing very little.",
        ],
        amenities=["king", "shower", "lake", "seat"] + COMMON,
        gallery=[LAKE, AUT, JET, EVE],
        schema_bed="KingBed",
    ),
    dict(
        slug="corner-room", name="The Corner Room", price=265, sleeps=2, bed="King bed", size=32,
        view="Lake and fell views", lead=CORN,
        tagline="Windows on two sides, and a freestanding bath at the foot of the bed.",
        short="Dual-aspect and unhurried, with lake views one way, fell views the other and a freestanding bath between.",
        long=[
            "Two walls of windows make the Corner Room feel closer to the landscape than any other. In the evening the lamps come on and the glass turns to mirror.",
            "The freestanding bath sits beneath the fell-facing window. Run it late, leave the lights low and watch the last of the light leave the hillside.",
        ],
        amenities=["king", "bath", "shower", "both"] + COMMON,
        gallery=[CORN, BATH, EVE, TERR],
        schema_bed="KingBed",
    ),
    dict(
        slug="alder-suite", name="The Alder Suite", price=310, sleeps=2, bed="King bed", size=42,
        view="Lake and garden views", lead=SUITE,
        tagline="Our most generous room for two, with a sitting area and a bath by the window.",
        short="Space to spread out: a sitting area, a bath beside the window and the lake beyond the garden.",
        long=[
            "The Alder Suite takes up the whole of the first-floor bay. A low bed faces the lake, an armchair and writing table sit in the window, and the bathroom has a deep freestanding bath and a walk-in rainfall shower.",
            "It is the room we would book for a birthday, an anniversary or a Tuesday that needs something done about it.",
        ],
        amenities=["king", "bath", "shower", "lake", "sitting", "seat"] + COMMON,
        gallery=[SUITE, BATHV, TERR, AUT],
        schema_bed="KingBed",
    ),
    dict(
        slug="house-suite", name="The House Suite", price=395, sleeps=3, bed="King bed and sofa bed", size=52,
        view="Lake view", lead=HOUSE,
        tagline="The whole top floor: a bedroom, a sitting room with an open fire and the best view in the house.",
        short="Our largest suite, with a separate sitting room, an open fire and a bath in its own bay window.",
        long=[
            "The House Suite occupies the top of the building. The bedroom is quiet and dark at night, the sitting room has a stone fireplace and deep armchairs, and a long window frames the lake and the fells beyond it.",
            "A sofa bed makes room for a third guest, and the bathroom has a freestanding bath, a rainfall shower and plenty of space for both.",
        ],
        amenities=["king", "sofabed", "bath", "shower", "fire", "sitting", "lake"] + COMMON,
        gallery=[HOUSE, BATH, BATHV, EVE, TERR],
        schema_bed="KingBed",
    ),
]

BY_SLUG = {r["slug"]: r for r in ROOMS}
FEATURED = ["fell-room", "lake-room", "alder-suite"]


def amenity_list(room):
    return [A[k] for k in room["amenities"]]


def key_amenities(room, n=4):
    """The few amenities worth surfacing on listing pages."""
    skip = {"radio", "wifi", "tv", "coffee", "robes", "toiletries", "breakfast"}
    return [A[k] for k in room["amenities"] if k not in skip][:n]
