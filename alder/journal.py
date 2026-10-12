"""Journal articles. Body blocks: ("p", text) ("h2", text) ("quote", text) ("img", key, caption)."""

from .images import EXT, TERR, ENT, BRK, BATH, BATHV, COCK, LAMB, REST, FISH, STP, WINE, AUT, EVE, WALK, JET, VIL, WTF, SUITE, CORN, FELL, GARD, HOUSE, LAKE  # noqa: F401


ARTICLES = [
    dict(
        slug="five-walks-worth-getting-up-early-for",
        title="Five walks worth getting up early for",
        category="Explore", date="2026-10-02", read=5, hero=WALK,
        excerpt="Dawn is the best time to walk in the Lakes. These five routes reward an early start with empty paths and still water.",
        body=[
            ("p", "There is a particular quiet in the fells before nine. The paths are empty, the lakes are flat and the light arrives sideways, picking out every wall and wet leaf. We would trade a lie-in for it more often than we admit."),
            ("p", "These are the five walks we send guests on when they ask for something that rewards an early start. All are within an easy drive of the house, and none needs more than a good pair of boots and a flask."),
            ("h2", "1. Catbells, above Derwentwater"),
            ("p", "A short, steady climb with a view out of all proportion to the effort. Go at first light and you may have the summit to yourself, with the lake spread below you like poured pewter."),
            ("h2", "2. Orrest Head, above Windermere"),
            ("p", "Barely an hour up and down, and one of the best first walks in the Lakes. Take a flask and sit for a while at the top."),
            ("quote", "The paths are empty, the lakes are flat and the light arrives sideways."),
            ("h2", "3. Loughrigg Terrace, near Grasmere"),
            ("p", "A gentle shelf of a path with a wide view over Grasmere. Walk it in the early light, then walk down for breakfast in the village."),
            ("img", WALK, "Pausing above the water on the way down."),
            ("h2", "4. Tarn Hows, around the tarn"),
            ("p", "Level, easy and beautiful in the low light. The woods hold the mist longer than the open fell, and the tarn often lies perfectly still."),
            ("h2", "5. Latrigg, above Keswick"),
            ("p", "A broad, forgiving path to a summit with a huge view of Skiddaw and the lake. It is a good one for tired legs."),
            ("p", "As ever, check the forecast, carry a map and tell someone where you are going. The fells will still be there tomorrow. Breakfast, in our dining room, finishes at ten."),
        ],
    ),
    dict(
        slug="a-slow-weekend-in-the-lake-district",
        title="A slow weekend in the Lake District",
        category="Lake District", date="2026-09-18", read=4, hero=JET,
        excerpt="No itinerary, no alarm and no particular place to be. How we would spend two nights if the only aim was to slow down.",
        body=[
            ("p", "Most people arrive with a list. We would like to suggest, gently, that you leave it in the car."),
            ("h2", "Friday: arrive and do nothing"),
            ("p", "Check in from three. Take your bag to the room, open the window and listen. Walk to the water before dinner if the weather allows, or sit by the fire in the sitting room if it does not."),
            ("h2", "Saturday: one good thing"),
            ("p", "Choose a single plan for the day and let it take as long as it takes. A morning walk and a long lunch. A boat across the lake and a slow wander back. A village market and a pot of tea. Nothing more."),
            ("img", LAKE, "A window seat is a perfectly good plan for an afternoon."),
            ("quote", "Choose a single plan for the day and let it take as long as it takes."),
            ("p", "Come back to the house in the late afternoon. There is tea, and there are books, and the light will be doing something lovely over the water."),
            ("h2", "Sunday: lunch, then home"),
            ("p", "Breakfast without hurry, a last walk around the garden and Sunday lunch in the dining room. If you must go, go late. If you can stay, stay."),
            ("p", "We often hear that guests came for two nights and wished they had booked four. We take that as a compliment, and a quiet instruction."),
        ],
    ),
    dict(
        slug="where-we-source-our-ingredients",
        title="Where we source our ingredients",
        category="Food", date="2026-09-04", read=4, hero=LAMB,
        excerpt="Lamb from the next valley, trout from the river, vegetables from a walled garden. A short guide to the people behind the menu.",
        body=[
            ("p", "A menu is only as good as the people who supply it. Ours is shaped, season by season, by a small group of growers, farmers and makers within an hour of the kitchen."),
            ("h2", "Meat and fish"),
            ("p", "Our lamb is Herdwick, raised on the fells and hung properly. It has a deep, mineral flavour that needs very little help. The trout comes from a small, cold-water farm that supplies a handful of kitchens, and we take what they have that week."),
            ("img", FISH, "Fish and lamb at the pass in Alder Kitchen, both bought within an hour of the house."),
            ("h2", "Vegetables and fruit"),
            ("p", "A market garden a few miles away grows our beetroot, greens and soft herbs. In late summer we take whatever is cropping, and in winter we lean on roots, cabbages and the store cupboard."),
            ("quote", "We take what they have that week, and write the menu around it."),
            ("h2", "Bread, dairy and coffee"),
            ("p", "Sourdough from a bakery in the next village, butter and cheese from a family dairy, and coffee roasted by a small roastery nearby. All the people involved are people we know by name."),
            ("p", "None of this is a marketing exercise. Cooking this way is simply easier, tastes better and makes for a more honest kitchen. It also means the menu changes more often than we would like to print."),
        ],
    ),
    dict(
        slug="wild-swimming-for-the-nervous",
        title="Wild swimming, for the nervous",
        category="Explore", date="2026-08-21", read=5, hero=WTF,
        excerpt="Cold water is easier than it looks. A practical, unheroic guide to your first swim in a Lake District lake.",
        body=[
            ("p", "The Lakes are made for swimming, and nearly everyone who tries it wants to do it again. It is also a little frightening the first time. Here is how we would begin."),
            ("h2", "Start somewhere gentle"),
            ("p", "Choose a shallow shore with an easy way in and out, and go with a friend. Avoid anywhere with a current, deep weed or steep banks. Ask locally if you are unsure."),
            ("h2", "Go in slowly"),
            ("p", "Walk in until the water reaches your waist, then breathe out slowly and let your shoulders drop. The first minute is the hard one. After that, the cold becomes a bright, clean feeling that stays with you all day."),
            ("quote", "The first minute is the hard one. After that, the cold becomes a bright, clean feeling."),
            ("h2", "Keep it short"),
            ("p", "Five minutes is plenty. Get out before you feel cold, not after. Dry off, dress warmly and drink something hot as soon as you can."),
            ("img", JET, "Plenty of the lakes are better looked at than swum in. Know the difference."),
            ("p", "We keep a stack of large towels by the back door and a flask of hot chocolate in the kitchen. Ask, and we will point you toward a good spot. Never swim alone, and never swim somewhere you cannot see the way out."),
        ],
    ),
    dict(
        slug="restoring-the-house-in-stone-and-lime",
        title="Restoring the house, in stone and lime",
        category="Hotel", date="2026-07-30", read=6, hero=TERR,
        excerpt="How a quiet old stone house became The Alder House, and why we chose to repair rather than replace.",
        body=[
            ("p", "When we first walked through the house, it had been empty for some time. The roof was sound, the walls were thick and the light came in at angles that made us stop talking. We decided, quite quickly, that our job was to do as little as possible, and to do it well."),
            ("h2", "Repair, don't replace"),
            ("p", "Where the stone was cracked, we repaired it with lime mortar, which lets old walls breathe. Where floors were worn, we kept them. Where windows leaked, we restored the frames rather than swapping them out."),
            ("img", ENT, "A house is easier to love once you have mended it."),
            ("h2", "Local hands"),
            ("p", "A stonemason from the next valley rebuilt the garden wall. A joiner made the staircase balustrade and the window seats from oak. Local weavers and a linen supplier we trust provided the bedding and the throws."),
            ("quote", "Our job was to do as little as possible, and to do it well."),
            ("h2", "A quieter kind of design"),
            ("p", "The palette comes from the view: olive, stone, clay and the dark of wet slate. Everything is chosen to feel as though it has always been there, and to improve with wear."),
            ("p", "The Alder House is a fictional concept project, and this story is part of that fiction. But the approach, repair over replacement, local makers and a light touch, is one we would stand behind for any real house."),
        ],
    ),
    dict(
        slug="the-best-way-to-spend-a-wet-afternoon",
        title="The best way to spend a wet afternoon",
        category="Lake District", date="2026-06-12", read=3, hero=HOUSE,
        excerpt="Rain is part of the Lakes. These are the things we do when the cloud comes down.",
        body=[
            ("p", "It rains in the Lake District. It rains a great deal, in fact, and it is the reason the place is so green. We have long since stopped apologising for it."),
            ("h2", "Stay in"),
            ("p", "The first choice, and the best, is to stay put. Pick a chair by the fire, find a book from the shelf and let the afternoon go. Tea arrives at four, and so do cake and a second pot."),
                        ("h2", "Go out anyway"),
            ("p", "A waterproof, a pair of boots and a short walk to see the waterfalls at their best. The fells look different in the rain, softer and more private. Come back wet and happy and take a long bath."),
            ("img", BATHV, "A long bath is the second-best plan for a wet afternoon."),
            ("quote", "The fells look different in the rain, softer and more private."),
            ("h2", "Look around the villages"),
            ("p", "Bookshops, bakeries and small museums are all excellent places to sit out a shower. Pick a village, park and wander without a plan."),
            ("p", "By evening the cloud usually lifts. If not, dinner is at seven and the fire is still lit."),
        ],
    ),
]

BY_SLUG = {a["slug"]: a for a in ARTICLES}
CATEGORIES = ["Explore", "Food", "Hotel", "Lake District"]


def related(article, n=3):
    same = [a for a in ARTICLES if a["slug"] != article["slug"] and a["category"] == article["category"]]
    rest = [a for a in ARTICLES if a["slug"] != article["slug"] and a not in same]
    return (same + rest)[:n]
