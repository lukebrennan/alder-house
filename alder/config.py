"""Site-wide constants and URL helpers.

SITE_ORIGIN and BASE_PATH come from the environment so the same source builds
for localhost, a GitHub Pages project site (/repo-name) or a custom domain.
"""
import os

NAME = "The Alder House"
DESCRIPTOR = "Boutique Hotel"
LOCATION = "Lake District, England"
TAGLINE = "Stay a little longer."
SUPPORT = "Boutique comfort. Extraordinary surroundings."

ORIGIN = os.environ.get("SITE_ORIGIN", "http://localhost:8000").rstrip("/")
_base = os.environ.get("BASE_PATH", "").strip("/")
BASE = f"/{_base}" if _base else ""

# Placeholder contact details. .example is a reserved TLD; 01632 960xxx is an
# Ofcom-reserved range for drama use, so neither can reach a real person.
PHONE = "01632 960 417"
PHONE_HREF = "+441632960417"
EMAIL = "hello@alderhouse.example"
ADDRESS = ["The Alder House", "Fellside Lane", "Example Village", "Cumbria", "LA00 0XX"]

DEMO_NOTE = "Demo form: nothing you enter here is sent or stored."
BOOKING_NOTE = "Demo booking: no payment is taken and no reservation is made."


def url(path: str = "") -> str:
    """Root-relative URL that respects BASE_PATH."""
    path = path.lstrip("/")
    return f"{BASE}/{path}"


def abs_url(path: str = "") -> str:
    return f"{ORIGIN}{url(path)}"


# Fingerprinted asset paths. build.py overwrites these with hashed names so every deploy
# gets fresh CSS and JS instead of a copy cached by the browser or the CDN.
CSS_PATH = "assets/css/main.css"
JS_PATH = "assets/js/main.js"
