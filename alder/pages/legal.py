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
    ("Can I cancel or change my booking?", "<p>You can cancel free of charge up to 48 hours before arrival. After that we charge the first night. If your plans change, tell us as early as you can and we will do our best to help.</p>"),
    ("Do you host weddings or events?", "<p>We host small gatherings and intimate celebrations for up to 24 guests. Get in touch and we will talk through your plans.</p>"),
]


def simple(path, title, desc, lead, sections):
    secs = "".join(f'<h2 class="h3">{h}</h2>{"".join(f"<p>{p}</p>" for p in ps)}' for h, ps in sections)
    body = f'''<section class="page-intro" aria-labelledby="page-title">
  <div class="container page-intro__inner">
    <nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="{url()}">Home</a></li><li><span aria-current="page">{title}</span></li></ol></nav>
    {eyebrow("The Alder House")}
    <h1 class="display" id="page-title" data-split>{title}</h1>
    <p class="lede">{lead}</p>
  </div>
</section>
<section class="section section--tight-top"><div class="container narrow prose">{secs}</div></section>'''
    return (path, page(path, title, desc, body, crumbs=[(title, path)]))


def faqs():
    body = f'''<section class="page-intro" aria-labelledby="page-title">
  <div class="container page-intro__inner">
    <nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="{url()}">Home</a></li><li><span aria-current="page">FAQs</span></li></ol></nav>
    {eyebrow("Good to know")}
    <h1 class="display" id="page-title" data-split>Frequently asked questions.</h1>
    <p class="lede">Practical answers about your stay, and one or two about the project itself.</p>
  </div>
</section>
<section class="section section--tight-top"><div class="container narrow"><h2 class="visually-hidden">Questions</h2>{accordion(FAQS, "faq")}</div></section>'''
    return ("faqs/", page("faqs/", "FAQs", "Answers to common questions about staying at The Alder House in the Lake District.",
                          body, crumbs=[("FAQs", "faqs/")]))


def build():
    return [
        faqs(),
        simple("accessibility/", "Accessibility", "How this website aims to meet WCAG 2.2 AA, and how to report problems.",
               "We want this site to work for everyone.",
               [("Our approach", ["The site is built with semantic HTML, a logical heading structure, visible focus states, keyboard-operable menus, galleries and forms, and sufficient colour contrast. Animation is gentle and switches off if your device is set to reduce motion.",
                                  "All meaningful images have descriptive alternative text, and no essential information is held in images."]),
                ("Known limitations", ["This website has not yet been through a formal external audit. The photography is supplied by Unsplash contributors.",
                                       "The decorative map on the Explore page is an illustration; the same information is listed in text beside it."]),
                ("Feedback", [f"If you have difficulty using any part of this site, please write to {C.EMAIL} and describe the problem. We aim to reply within two working days."])]),
        simple("privacy/", "Privacy", "Privacy information for The Alder House website: no personal data is collected, stored or sent.",
               "This site collects nothing.",
               [("What we collect", ["Nothing. The forms on this site (booking, reservation, contact and newsletter) are demos. Anything you type stays in your browser and is never sent to a server.",
                                     "This site does not use analytics or advertising cookies."]),
                ("Third parties", ["Fonts are served by Google Fonts, and photographs by Unsplash, so those services will see a standard browser request when a page loads. Please refer to their own policies for details."]),
                ("Third-party services", ["A full privacy notice covering booking data, payment providers and retention will accompany the live booking service."])]),
        simple("terms/", "Terms", "Terms of use for The Alder House website.",
               "The short version: this is a design exercise.",
               [("About this website", ["Information on this site, including rates, availability and menus, is for guidance. A booking request made here is not a confirmed reservation until we have confirmed it with you."]),
                ("Content", ["Rates, menus and opening times may change. Photographs are from Unsplash contributors and remain the property of their creators under the Unsplash licence."]),
                ("Using this site", ["You are welcome to browse and share the site. Please do not copy the content without asking."])]),
    ]
