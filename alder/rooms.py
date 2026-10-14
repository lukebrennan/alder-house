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
        tagline="Up in the eaves, with the fell in the window.",
        short="The smallest room in the house, and the one people rebook. Oak joinery, a deep window seat and the fell filling the glass.",
        long=[
            "Up under the roof at the back of the house. The ceiling slopes, the bed is low, and the window seat is deep enough to fall asleep in.",
            "Most people come for the walking and end up staying in. The kettle lives by the window, which tells you something.",
        ],
        amenities=["king", "shower", "fell", "seat"] + COMMON,
        gallery=[FELL, WALK, EVE, AUT],
        schema_bed="KingBed",
    ),
    dict(
        slug="garden-room", name="The Garden Room", price=215, sleeps=2, bed="King bed", size=26,
        view="Garden view", lead=GARD,
        tagline="Ground floor, with a door straight onto the lawn.",
        short="Step-free, with its own terrace and a door onto the garden. Good with dogs, and good for anyone who would rather avoid stairs.",
        long=[
            "On the ground floor, in what used to be the morning room. Stone-flagged floor, clay-white walls, and a bed that faces the garden.",
            "There is a table and two chairs on the terrace. Coffee out there before anyone else is up is the best argument for this room.",
        ],
        amenities=["king", "shower", "garden", "terrace", "stepfree"] + COMMON,
        gallery=[GARD, ENT, TERR, JET],
        schema_bed="KingBed",
    ),
    dict(
        slug="lake-room", name="The Lake Room", price=235, sleeps=2, bed="King bed", size=28,
        view="Lake view", lead=LAKE,
        tagline="The water, from the pillow.",
        short="First floor, facing the lake. A window seat, a good reading light and the weather doing something different every hour.",
        long=[
            "The Lake Room looks straight down the valley. On still mornings the lake holds the sky, and on wet ones it disappears altogether, which is its own sort of pleasure.",
            "Olive walls, heavy linen, and a throw guests keep photographing and then quietly asking about. We will tell you where it is from.",
        ],
        amenities=["king", "shower", "lake", "seat"] + COMMON,
        gallery=[LAKE, AUT, JET, EVE],
        schema_bed="KingBed",
    ),
    dict(
        slug="corner-room", name="The Corner Room", price=265, sleeps=2, bed="King bed", size=32,
        view="Lake and fell views", lead=CORN,
        tagline="Windows on two sides, and a bath at the foot of the bed.",
        short="Lake out of one window, fell out of the other, and a freestanding bath in between. It is never dark in here.",
        long=[
            "Two walls of windows. In the evening the lamps come on and the glass turns to mirror.",
            "The bath sits under the fell window. Run it late, leave the lights low and watch the last of the light leave the hill.",
        ],
        amenities=["king", "bath", "shower", "both"] + COMMON,
        gallery=[CORN, BATH, EVE, TERR],
        schema_bed="KingBed",
    ),
    dict(
        slug="alder-suite", name="The Alder Suite", price=310, sleeps=2, bed="King bed", size=42,
        view="Lake and garden views", lead=SUITE,
        tagline="The big room for two, with a bath by the window.",
        short="Room to spread out: a sitting area, a writing table and a bath beside the window, with the lake beyond the garden.",
        long=[
            "The Alder Suite takes the whole of the first-floor bay. A low bed faces the lake, there is an armchair and a writing table in the window, and a freestanding bath next to a walk-in rainfall shower.",
            "It is the room we would book for a birthday, an anniversary, or a Tuesday that needs doing something about.",
        ],
        amenities=["king", "bath", "shower", "lake", "sitting", "seat"] + COMMON,
        gallery=[SUITE, BATHV, TERR, AUT],
        schema_bed="KingBed",
    ),
    dict(
        slug="house-suite", name="The House Suite", price=395, sleeps=3, bed="King bed and sofa bed", size=52,
        view="Lake view", lead=HOUSE,
        tagline="The whole top floor, with an open fire.",
        short="A bedroom, a sitting room with a fire, and the best view in the house. A sofa bed makes space for a third guest.",
        long=[
            "The House Suite takes the top of the building. The bedroom is properly dark at night, the sitting room has a stone fireplace and deep armchairs, and a long window frames the lake and the fells beyond.",
            "There is a freestanding bath, a rainfall shower, and enough room for two people to share the bathroom without a negotiation.",
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
