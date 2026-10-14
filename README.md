# The Alder House

A website for The Alder House, a boutique hotel in the English Lake District: a complete, responsive, accessible
static site with a front-end booking demo. Rooms, rates, menus, reviews and contact details are placeholder content.

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
  config.py         Names, placeholder contact details, URL helpers (BASE_PATH / SITE_ORIGIN aware)
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
  img/photos/       Photography, three WebP sizes each (see SOURCES.md)
  favicons/         Favicon set from the supplied brand assets
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
  real telephone number in the schema, because the contact details are placeholders. `/book/summary/` is `noindex`.
- **Booking demo.** Availability and prices are generated deterministically in the browser. There are no payment
  fields and nothing is stored or sent.

## Photography

All 24 photographs are from [Unsplash](https://unsplash.com/) contributors, used under the Unsplash licence. Each
lives in `static/img/photos/` as **AVIF** (served first) and **WebP** (fallback) at three widths (640, 1280 and
2000px), so phones download small files and retina desktops get sharp ones. The hero is preloaded with its AVIF
`srcset`. A typical page pulls a few hundred KB of imagery.

To swap a photograph, replace its six files (keeping the names) or add new ones and update the manifest in
`alder/images.py`, which also holds the alt text and focal point for each image. The original Unsplash IDs are listed
in `static/img/photos/SOURCES.md`.
