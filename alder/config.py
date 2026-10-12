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

# Fictional contact details. .example is a reserved TLD; 01632 960xxx is an
# Ofcom-reserved range for drama use.
PHONE = "01632 960 417"
PHONE_HREF = "+441632960417"
EMAIL = "hello@alderhouse.example"
ADDRESS = ["The Alder House", "Fellside Lane", "Example Village", "Cumbria", "LA00 0XX"]

DEMO_NOTE = (
    "The Alder House is a fictional concept project. Nothing on this site can be booked, "
    "and no payment or personal information is collected."
)


def url(path: str = "") -> str:
    """Root-relative URL that respects BASE_PATH."""
    path = path.lstrip("/")
    return f"{BASE}/{path}"


def abs_url(path: str = "") -> str:
    return f"{ORIGIN}{url(path)}"
