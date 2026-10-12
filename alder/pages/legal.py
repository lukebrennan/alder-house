from .. import config as C
from ..config import url
from ..layout import page
from ..ui import accordion, demo_banner, eyebrow

FAQS = [
    ("What time is check-in and check-out?", "<p>Check-in is from 3pm and check-out is by 11am. Early arrivals and late departures can be arranged where possible.</p>"),
    ("Is breakfast included?", "<p>Yes. Breakfast in Alder Kitchen is included in every room rate.</p>"),
    ("Do you welcome dogs?", "<p>Well-behaved dogs are welcome in selected rooms by arrangement. Please let us know in advance and we will prepare a bed and a bowl.</p>"),
    ("Is the hotel accessible?", "<p>The Garden Room is on the ground floor with step-free access. Other rooms are up a staircase. Please get in touch and we will happily talk through your needs.</p>"),
    ("Is there parking?", "<p>There is free parking at the house for all guests.</p>"),
    ("Can I cancel or change my booking?", "<p>This is a demonstration site, so no real bookings are made and there are no real cancellation terms. If it were real, we would aim to be flexible and fair.</p>"),
    ("Is The Alder House a real hotel?", "<p>No. It is a fictional concept created as a portfolio project. The rooms, prices, reviews and contact details are all invented.</p>"),
]


def simple(path, title, desc, lead, sections):
    secs = "".join(f'<h2 class="h3">{h}</h2>{"".join(f"<p>{p}</p>" for p in ps)}' for h, ps in sections)
    body = f'''<section class="page-intro" aria-labelledby="page-title">
  <div class="container page-intro__inner">
    <nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="{url()}">Home</a></li><li><span aria-current="page">{title}</span></li></ol></nav>
    {eyebrow("The Alder House")}
    <h1 class="display" id="page-title">{title}</h1>
    <p class="lede">{lead}</p>
  </div>
</section>
<section class="section section--tight-top"><div class="container narrow prose">{secs}</div></section>
<div class="container demo-wrap">{demo_banner()}</div>'''
    return (path, page(path, title, desc, body, crumbs=[(title, path)]))


def faqs():
    body = f'''<section class="page-intro" aria-labelledby="page-title">
  <div class="container page-intro__inner">
    <nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="{url()}">Home</a></li><li><span aria-current="page">FAQs</span></li></ol></nav>
    {eyebrow("Good to know")}
    <h1 class="display" id="page-title">Frequently asked <em>questions.</em></h1>
    <p class="lede">Practical answers about your stay, and one or two about the project itself.</p>
  </div>
</section>
<section class="section section--tight-top"><div class="container narrow"><h2 class="visually-hidden">Questions</h2>{accordion(FAQS, "faq")}</div></section>
<div class="container demo-wrap">{demo_banner()}</div>'''
    return ("faqs/", page("faqs/", "FAQs", "Answers to common questions about staying at The Alder House, a fictional boutique hotel concept in the Lake District.",
                          body, crumbs=[("FAQs", "faqs/")]))


def build():
    return [
        faqs(),
        simple("accessibility/", "Accessibility", "How this website aims to meet WCAG 2.2 AA, and how to report problems. A concept project statement.",
               "We want this site to work for everyone.",
               [("Our approach", ["The site is built with semantic HTML, a logical heading structure, visible focus states, keyboard-operable menus, galleries and forms, and sufficient colour contrast. Animation is gentle and switches off if your device is set to reduce motion.",
                                  "All meaningful images have descriptive alternative text, and no essential information is held in images."]),
                ("Known limitations", ["This is a portfolio concept and has not been through a formal external audit. The photographs are placeholders from Unsplash contributors.",
                                       "The decorative map on the Explore page is an illustration; the same information is listed in text beside it."]),
                ("Feedback", [f"If you have difficulty using any part of this site, please write to {C.EMAIL} (a fictional address) and describe the problem. In a real project we would reply within two working days."])]),
        simple("privacy/", "Privacy", "Privacy information for The Alder House concept site: no personal data is collected, stored or sent.",
               "This site collects nothing.",
               [("What we collect", ["Nothing. The forms on this site (booking, reservation, contact and newsletter) are demonstrations. Anything you type stays in your browser and is never sent to a server.",
                                     "This site does not use analytics or advertising cookies."]),
                ("Third parties", ["Fonts are served by Google Fonts, and photographs by Unsplash, so those services will see a standard browser request when a page loads. Please refer to their own policies for details."]),
                ("In a real project", ["A real hotel would need a full privacy notice covering booking data, payment processors, retention and your rights under UK GDPR. This page is a placeholder for that."])]),
        simple("terms/", "Terms", "Terms of use for the fictional concept website of The Alder House.",
               "The short version: this is a design exercise.",
               [("Fictional concept", ["The Alder House is not a real business. Rooms cannot be booked, tables cannot be reserved, and no goods or services are offered. Any resemblance to a real hotel is coincidental."]),
                ("Content", ["Prices, availability, menus, reviews and contact details are invented. Photographs are from Unsplash contributors and remain the property of their creators under the Unsplash licence."]),
                ("Use of this site", ["You are welcome to browse and to look at the source code. Please do not treat anything on the site as an offer."])]),
    ]
