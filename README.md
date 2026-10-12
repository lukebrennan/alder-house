# The Alder House

A fictional boutique hotel in the English Lake District, built as a portfolio project: a complete, responsive,
accessible static website with a front-end booking demonstration.

**The Alder House is not a real business.** Rooms, prices, reviews, menus, the address, phone number and email
are all invented, and nothing on the site collects, stores or sends personal or payment data.

## What's inside

| Area | Pages |
| --- | --- |
| Home | `/` with hero, availability bar, rooms, dining, explore, testimonials, journal |
| Stay | `/stay/` and six room pages `/stay/<room>/` with gallery lightbox |
| Dining | `/dining/` with sample menus and a demo reservation form |
| Explore | `/explore/` with an illustrated map and a destination guide |
| Our Story, Journal | `/our-story/`, `/journal/`, six articles |
| Booking demo | `/book/` (search and results), `/book/summary/` (mock summary and confirmation) |
| Other | `/contact/`, `/faqs/`, `/accessibility/`, `/privacy/`, `/terms/`, `404.html` |

## Run it locally

No dependencies beyond Python 3.9+. There is no Node, npm or bundler.

```bash
python3 build.py --serve   # builds into dist/ and serves http://localhost:8000
python3 build.py           # build only
```

## Project structure

```
build.py            Builds every page into dist/, concatenates + minifies CSS, writes sitemap/robots/manifest
alder/
  config.py         Names, fictional contact details, URL helpers (BASE_PATH / SITE_ORIGIN aware)
  images.py         Photography manifest: file names, alt text, focal points
  rooms.py          Room data (prices, amenities, galleries)
  journal.py        Journal articles
  ui.py             Reusable components: buttons, section heads, media, room/journal cards,
                    accordion, gallery, booking form, forms, newsletter, page hero
  layout.py         <head>, SEO tags, header, full-screen menu, footer, lightbox shell
  pages/            One module per page or section
static/
  css/              tokens → base → layout → components → sections → pages → motion
  js/               Small ES modules: header, reveal, accordion, lightbox, datepicker, forms, map, filter, booking
  img/photos/       Supplied photography (WebP)
  img/brand/        Supplied logos and brand elements
  favicons/         Supplied favicon set
.github/workflows/  GitHub Pages deployment
```

Design tokens (colour, type, spacing) live in `static/css/00-tokens.css`.

## Deploying to GitHub Pages

1. Push to a GitHub repository on the `main` branch.
2. In **Settings → Pages**, set **Source** to **GitHub Actions**.
3. The workflow in `.github/workflows/pages.yml` builds the site and publishes it. It works out the right
   `SITE_ORIGIN` and `BASE_PATH` from the repository name (`/<repo>` for project sites, blank for
   `<user>.github.io`), so canonical URLs, Open Graph tags, the sitemap and all links are correct.

For a custom domain, set `SITE_ORIGIN` to the domain and `BASE_PATH` to empty in the workflow's build step.

## Notes on specific decisions

- **Colour and contrast.** The brand palette is used as specified. Stone `#A79D8F` is used for borders and on
  dark backgrounds; text on cream uses a darkened derivative (`--stone-ink: #6B6358`, 5.3:1) so secondary text passes
  WCAG AA. Gold appears only in rules, small labels on dark and decorative details.
- **Accessibility.** Semantic landmarks, one `h1` per page, skip link, visible focus, a `<dialog>`-based menu and
  lightbox (focus trap, Esc, focus restore), keyboard-operable date picker and accordion, labelled forms with
  inline errors, and `prefers-reduced-motion` support.
- **Performance.** No frameworks or runtime dependencies. Native ES modules, WebP photography with intrinsic
  dimensions (no layout shift), lazy loading below the fold, hero preloaded, fonts via `display=swap`, CSS
  scroll-driven parallax with no JavaScript, and cross-document view transitions where supported.
- **SEO.** Unique titles, descriptions, canonicals and Open Graph tags; `Hotel`, `HotelRoom`, `Restaurant`,
  `Article` and `BreadcrumbList` structured data. There is deliberately no review markup, no street address and no
  real telephone number in the schema, because the hotel is fictional. `/book/summary/` is `noindex`.
- **Booking demo.** Availability and prices are generated deterministically in the browser. There are no payment
  fields and nothing is stored or sent.

## Photography

Photographs come from the supplied asset pack (`the-alder-house-website-assets`). Swap any image by replacing its
file in `static/img/photos/` (keep the file name or update `alder/images.py`). One image,
`the-alder-suite-lake-view-bedroom.webp`, contains a script sign on the wall; the site crops it out on the page via
the `crop-clear-sign` class, but the lightbox shows the full frame.
