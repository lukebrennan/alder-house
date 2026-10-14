from ..config import url
from ..layout import page
from ..ui import button, eyebrow


def build():
    body = f'''<section class="page-intro page-intro--center" aria-labelledby="page-title">
  <div class="container narrow center page-intro__inner">
    {eyebrow("404")}
    <h1 class="display" id="page-title" data-split>This path doesn't lead anywhere.</h1>
    <p class="lede">The page you were looking for has wandered off. Let's get you back to somewhere comfortable.</p>
    <div class="btn-row">{button("Back to the home page", url(), "primary")}{button("View the rooms", url("stay/"), "secondary")}</div>
  </div>
</section>'''
    return [("404.html", page("404.html", "Page not found", "That page could not be found on The Alder House website.", body, noindex=True))]
