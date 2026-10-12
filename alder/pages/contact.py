from ..images import EXT, TERR, ENT, BRK, BATH, BATHV, COCK, LAMB, REST, FISH, STP, WINE, AUT, EVE, WALK, JET, VIL, WTF, SUITE, CORN, FELL, GARD, HOUSE, LAKE  # noqa: F401
from .. import config as C
from ..config import url
from ..layout import page
from ..ui import (accordion, button, demo_banner, eyebrow, field, icon, section_head, select, submit_button,
                  text_link, textarea)

FAQ_TEASER = [
    ("What time is check-in and check-out?", "<p>Check-in is from 3pm and check-out is by 11am. If you arrive early, we will gladly look after your bags and put the kettle on.</p>"),
    ("Is parking available?", "<p>Yes. There is free parking at the house for all guests.</p>"),
]


def build():
    addr = "<br>".join(C.ADDRESS)
    body = f'''<section class="page-intro" aria-labelledby="page-title">
  <div class="container page-intro__inner">
    <nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="{url()}">Home</a></li><li><span aria-current="page">Contact</span></li></ol></nav>
    {eyebrow("Contact")}
    <h1 class="display" id="page-title">Get in touch, <em>or drop in.</em></h1>
    <p class="lede">Questions about a room, a special occasion or a dog? We read every message and reply within a day.</p>
  </div>
</section>
<section class="section section--tight-top" aria-label="Contact details and form">
  <div class="container contact-grid">
    <form class="form" data-demo-form data-success="Thank you. This is a demonstration form, so your message has not been sent." novalidate>
      <h2 class="h3">Send us a message</h2>
      <div class="form__grid">
        {field("c-name", "Name", required=True, autocomplete="name")}
        {field("c-email", "Email", "email", required=True, autocomplete="email")}
        {field("c-phone", "Telephone (optional)", "tel", autocomplete="tel")}
        {select("c-topic", "Topic", [("stay", "A stay"), ("dining", "Dining"), ("occasion", "A special occasion"), ("other", "Something else")])}
      </div>
      {textarea("c-message", "Your message", 6, required=True)}
      {submit_button("Send message", "primary")}
      <p class="form-status" role="status" aria-live="polite"></p>
      <p class="form__demo">{C.DEMO_NOTE}</p>
    </form>
    <aside class="contact-card" aria-label="The Alder House details">
      <h2 class="h3">The house</h2>
      <ul class="contact-list">
        <li>{icon("pin", "icon", 22)}<div><strong>Address</strong><address>{addr}</address><span class="tag">Fictional address for demonstration</span></div></li>
        <li>{icon("phone", "icon", 22)}<div><strong>Telephone</strong><a href="tel:{C.PHONE_HREF}">{C.PHONE}</a><span class="tag">Fictional number</span></div></li>
        <li>{icon("mail", "icon", 22)}<div><strong>Email</strong><a href="mailto:{C.EMAIL}">{C.EMAIL}</a><span class="tag">Fictional address</span></div></li>
        <li>{icon("clock", "icon", 22)}<div><strong>Check-in</strong>From 3pm. Check-out by 11am.<br>Reception is staffed 8am to 10pm.</div></li>
      </ul>
    </aside>
  </div>
</section>
<section class="section section--sand" aria-labelledby="dir-title">
  <div class="container directions">
    <div data-reveal>
      {eyebrow("Directions")}
      <h2 class="display" id="dir-title">Finding <em>the house.</em></h2>
      <p class="lede">The Alder House is fictional, so there is nowhere to drive to. If it were real, this is how we would tell you to arrive.</p>
    </div>
    <div class="directions__cols" data-reveal>
      <div><h3 class="h4">By car</h3><p>Follow the signs for the Lakes and take the lane signed for the village. The house is the last on the left, with a slate sign and a green gate. Parking is free.</p></div>
      <div><h3 class="h4">By train</h3><p>Take a train to the nearest station and a short taxi ride up the valley. We are happy to arrange a car for you.</p></div>
      <div><h3 class="h4">On foot</h3><p>Several footpaths cross the fell and arrive at our back gate. Boots by the door, please.</p></div>
    </div>
  </div>
</section>
<section class="section" aria-labelledby="faq-title">
  <div class="container narrow">
    {section_head("Good to know", "Quick <em>questions.</em>", title_cls="display", title_id="faq-title")}
    {accordion(FAQ_TEASER, "cfaq")}
    <p class="center" data-reveal>{text_link("Read all the FAQs", url("faqs/"))}</p>
  </div>
</section>
<div class="container demo-wrap">{demo_banner("Every contact detail on this page is invented. Please do not try to call or write.")}</div>'''
    return [("contact/", page("contact/", "Contact",
                              "Contact The Alder House, a fictional boutique hotel concept in the Lake District. Demo contact form, directions, check-in information and FAQs.",
                              body, og_key=EVE, crumbs=[("Contact", "contact/")]))]
