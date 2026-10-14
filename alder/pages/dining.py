from ..images import abs_src, EXT, TERR, ENT, BRK, BATH, BATHV, COCK, LAMB, REST, FISH, STP, WINE, AUT, EVE, WALK, JET, VIL, WTF, SUITE, CORN, FELL, GARD, HOUSE, LAKE  # noqa: F401
from .. import config as C
from ..config import url, abs_url
from ..images import src
from ..layout import page
from ..ui import (button, demo_banner, eyebrow, field, icon, media, page_hero, section_head, select,
                  submit_button, textarea)

DINNER = [
    ("Starter", "Roasted beetroot, whipped goat's cheese, walnut"),
    ("Starter", "Cumbrian trout, cucumber, dill"),
    ("Main", "Herdwick lamb, spring greens, rosemary jus"),
    ("Main", "Wild mushroom barley risotto"),
    ("Dessert", "Sticky toffee pudding, clotted cream"),
    ("Dessert", "Yorkshire rhubarb, vanilla custard"),
]
BREAKFAST = [
    ("Cooked", "The Alder breakfast: free-range eggs, dry-cured bacon, Cumbrian sausage, tomato, mushrooms, sourdough"),
    ("Lighter", "Porridge with local honey and poached rhubarb"),
    ("Lighter", "Smoked haddock, soft egg, wilted spinach"),
    ("Baked", "Pastries and sourdough, baked in the next village each morning"),
    ("Drinks", "Locally roasted coffee, loose-leaf tea, fresh juice"),
]
SUNDAY = [
    ("To start", "Soup of the day, warm soda bread, salted butter"),
    ("Roast", "Cumbrian beef sirloin, Yorkshire pudding, roast potatoes, greens, proper gravy"),
    ("Roast", "Slow-cooked Herdwick shoulder, mint, red cabbage"),
    ("Roast", "Chestnut and mushroom wellington, roast roots, gravy"),
    ("To finish", "Bramley apple crumble with custard"),
]
DRINKS = [
    ("On tap", "Lakeland ales, poured properly"),
    ("By the glass", "English sparkling, a short list of small-producer wines"),
    ("To mix", "The Alder spritz: elderflower, English sparkling, a twist of lemon"),
    ("Low and no", "Cold-pressed apple, ginger beer, zero-alcohol spirits"),
    ("To finish", "Fireside whiskies and a pot of strong coffee"),
]
HOURS = [("Breakfast", "Daily, 7.30–10.00am"), ("Dinner", "Wednesday to Sunday, 6.30–9.00pm"),
         ("Sunday lunch", "Sundays, 12.00–4.00pm"), ("The bar", "Daily, 11.00am–11.00pm")]


def menu(title, sub, items, key, anchor, flip=False, price=None):
    rows = "".join(f'<li><span class="menu-list__course">{c}</span><span class="menu-list__dish">{d}</span></li>' for c, d in items)
    price_html = f'<p class="menu__price">{price}</p>' if price else ""
    cls = " menu-block--flip" if flip else ""
    return f'''<section class="menu-block{cls}" id="{anchor}" aria-labelledby="{anchor}-title">
  <div class="menu-block__media">{media(key, (4, 5), sizes="(min-width: 960px) 36vw, 100vw")}</div>
  <div class="menu-block__text" data-reveal>
    {eyebrow(sub)}
    <h2 class="display" id="{anchor}-title">{title}</h2>
    <ul class="menu-list">{rows}</ul>
    {price_html}
    <p class="menu-block__note">Sample menu. Dishes change with the seasons.</p>
  </div>
</section>'''


def reservation():
    times = [("18:30", "6.30pm"), ("19:00", "7.00pm"), ("19:30", "7.30pm"), ("20:00", "8.00pm"), ("20:30", "8.30pm")]
    return f'''<section class="section section--sand reserve" id="reserve" aria-labelledby="reserve-title">
  <div class="container reserve__grid">
    <div class="reserve__text" data-reveal>
      {eyebrow("Reserve a table")}
      <h2 class="display" id="reserve-title">Join us for dinner.</h2>
      <p class="lede">Tell us when you would like to come and we will do the rest. Residents and visitors are equally welcome.</p>
      <dl class="hours">{"".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in HOURS)}</dl>
    </div>
    <form class="form form--card" data-demo-form data-success="Thank you. This is a demo form, so no table has been reserved and nothing has been sent." novalidate>
      <div class="form__grid">
        {field("res-name", "Name", required=True, autocomplete="name")}
        {field("res-email", "Email", "email", required=True, autocomplete="email")}
        {field("res-date", "Date", "date", required=True)}
        {select("res-time", "Time", times, "19:00")}
        {select("res-guests", "Guests", [(i, f"{i} guest{'s' if i > 1 else ''}") for i in range(1, 9)], 2)}
        {select("res-occasion", "Occasion", [("", "No special occasion"), ("birthday", "Birthday"), ("anniversary", "Anniversary"), ("other", "Something else")])}
      </div>
      {textarea("res-notes", "Dietary requirements or notes", 4)}
      {submit_button("Request a table", "primary")}
      <p class="form-status" role="status" aria-live="polite"></p>
      <p class="form__demo">{C.DEMO_NOTE}</p>
    </form>
  </div>
</section>'''


def build():
    anchors = "".join(f'<li><a href="#{a}">{t}</a></li>' for t, a in
                      [("Breakfast", "breakfast"), ("Dinner", "dinner"), ("Sunday lunch", "sunday-lunch"), ("Drinks", "drinks")])
    body = f'''{page_hero("Seasonal cooking. No unnecessary fuss.", "Alder Kitchen",
                         "The kitchen at The Alder House cooks with British produce and the people who grow it.",
                         REST, crumbs=[("Dining", None)])}
<section class="section" aria-labelledby="kitchen-title">
  <div class="container narrow center" data-reveal>
    {eyebrow("Eat & drink")}
    <h2 class="display" id="kitchen-title">Food rooted in the landscape.</h2>
    <p class="lede">Alder Kitchen is a relaxed room with a short menu. We buy from farmers, growers and makers within an hour of the house, cook over wood and flame where it makes sense and let the ingredients do most of the talking.</p>
    <p>Lamb from the fell, trout from the river, vegetables from a walled garden. It is simple food, done with care, and it changes with the weather.</p>
    <nav class="anchor-nav" aria-label="Menus"><ul>{anchors}</ul></nav>
  </div>
</section>
{menu("Breakfast", "Served daily", BREAKFAST, BRK, "breakfast")}
{menu("Dinner", "Wednesday to Sunday", DINNER, FISH, "dinner", flip=True, price="Two courses £38 · Three courses £46")}
{menu("Sunday lunch", "Sundays, 12 until 4", SUNDAY, LAMB, "sunday-lunch", price="Two courses £34 · Three courses £41")}
{menu("Drinks", "The bar", DRINKS, COCK, "drinks", flip=True)}
{reservation()}'''
    schema = [{
        "@context": "https://schema.org", "@type": "Restaurant", "name": "Alder Kitchen",
        "description": "The restaurant of The Alder House: seasonal British cooking, local suppliers and a relaxed table.",
        "servesCuisine": "British", "url": abs_url("dining/"),
        "image": abs_src(REST),
        "address": {"@type": "PostalAddress", "addressRegion": "Cumbria", "addressCountry": "GB"},
        "parentOrganization": {"@type": "Hotel", "name": "The Alder House", "url": abs_url()},
    }]
    return [("dining/", page("dining/", "Alder Kitchen: Seasonal Cooking",
                              "Alder Kitchen at The Alder House in the Lake District: seasonal British cooking, local suppliers and a relaxed table. Sample menus and table reservations.",
                              body, overlay=True, schema=schema, og_key=REST,
                              crumbs=[("Dining", "dining/")],
                              full_title="Alder Kitchen | Seasonal Dining at The Alder House"))]
