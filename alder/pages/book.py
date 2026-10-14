from ..images import EXT, TERR, ENT, BRK, BATH, BATHV, COCK, LAMB, REST, FISH, STP, WINE, AUT, EVE, WALK, JET, VIL, WTF, SUITE, CORN, FELL, GARD, HOUSE, LAKE  # noqa: F401
import json

from .. import config as C
from ..config import url
from ..images import alt_for, src
from ..layout import page
from ..rooms import ROOMS
from ..ui import booking_form, demo_banner, eyebrow, icon


def rooms_json() -> str:
    data = [dict(slug=r["slug"], name=r["name"], price=r["price"], sleeps=r["sleeps"], bed=r["bed"], view=r["view"],
                 size=r["size"], short=r["short"], image=src(r["lead"], 800), alt=alt_for(r["lead"]),
                 href=url(f'stay/{r["slug"]}/')) for r in ROOMS]
    payload = json.dumps(data).replace("</", "<\\/")
    return f'<script type="application/json" id="rooms-data">{payload}</script>'


STEPS = ["Dates", "Room", "Details"]


def steps(current: int) -> str:
    items = []
    for i, s in enumerate(STEPS):
        aria = ' aria-current="step"' if i == current else ""
        done = "is-done" if i < current else ""
        items.append(f'<li{aria} class="{done}"><span class="steps__n">{i + 1}</span><span>{s}</span></li>')
    return f'<ol class="steps" aria-label="Booking progress">{"".join(items)}</ol>'


def book():
    body = f'''<section class="page-intro" aria-labelledby="page-title">
  <div class="container page-intro__inner">
    <nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="{url()}">Home</a></li><li><span aria-current="page">Book</span></li></ol></nav>
    {eyebrow("Book your stay")}
    <h1 class="display" id="page-title" data-split>Check availability.</h1>
    <p class="lede">Choose your dates and we will show you what is free. Breakfast is included in every room.</p>
  </div>
</section>
<section class="section section--tight-top book" aria-label="Availability search">
  <div class="container">
    <div class="demo-callout" role="note"><strong>Demo booking.</strong> No payment is taken and no reservation is made. The availability and rates shown are for demonstration.</div>
    {steps(0)}
    <div class="book__search">{booking_form("page", uid="book")}</div>
    <div class="book__results" data-results aria-live="polite" aria-busy="false">
      <noscript><p class="notice">Availability results need JavaScript. Please enable it to continue.</p></noscript>
    </div>
  </div>
</section>
{rooms_json()}'''
    return ("book/", page("book/", "Book Your Stay", "Check availability at The Alder House in the Lake District. Choose your dates, pick a room and review your stay.",
                          body, og_key=TERR, crumbs=[("Book", "book/")]))


def summary():
    body = f'''<section class="page-intro" aria-labelledby="page-title">
  <div class="container page-intro__inner">
    <nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="{url()}">Home</a></li><li><a href="{url("book/")}">Book</a></li><li><span aria-current="page">Summary</span></li></ol></nav>
    {eyebrow("Almost there")}
    <h1 class="display" id="page-title" data-split>Your stay.</h1>
  </div>
</section>
<section class="section section--tight-top book" aria-label="Booking summary">
  <div class="container">
    <div class="demo-callout" role="note"><strong>Demo booking.</strong> No payment is requested, no card details are collected and no reservation is made.</div>
    {steps(2)}
    <div data-summary aria-live="polite"><noscript><p class="notice">The booking summary needs JavaScript.</p></noscript></div>
  </div>
</section>
{rooms_json()}'''
    return ("book/summary/", page("book/summary/", "Booking Summary", "Review your stay at The Alder House before you confirm.",
                                  body, noindex=True, crumbs=[("Book", "book/"), ("Summary", "book/summary/")]))


def build():
    return [book(), summary()]
