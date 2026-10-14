/* Loading screen and page transitions.
   First visit in a session: a short branded loader, then the curtain lifts.
   After that: clicking an internal link drops the curtain with the destination name, the next page
   loads behind it, and the curtain lifts once it is ready. Skipped entirely for reduced motion. */
const root = document.documentElement;
const wait = (ms) => new Promise((r) => setTimeout(r, ms));
const COVER_MS = 480;

function pageReady(minMs) {
  const loaded = document.readyState === "complete" ? Promise.resolve() : new Promise((r) => window.addEventListener("load", r, { once: true }));
  const fonts = document.fonts && document.fonts.ready ? document.fonts.ready : Promise.resolve();
  return Promise.race([Promise.all([loaded, fonts, wait(minMs)]), wait(4200)]);
}

/** Resolves once the opening curtain has lifted (immediately if there is none). */
export function initCurtain() {
  const holding = root.classList.contains("loader") || root.classList.contains("curtain-hold");
  const started = performance.now();

  const lift = () => {
    root.classList.remove("loader", "curtain-hold", "curtain-cover");
    root.classList.add("is-ready");
    document.dispatchEvent(new Event("ah:ready"));
  };

  const ready = holding
    ? pageReady(Math.max(0, (root.classList.contains("loader") ? 1000 : 200) - (performance.now() - started))).then(lift)
    : Promise.resolve(root.classList.add("is-ready"));

  if (!window.matchMedia("(prefers-reduced-motion: reduce)").matches) bindLinks();

  // Coming back via the browser's back/forward cache: never show a stuck curtain.
  window.addEventListener("pageshow", (e) => { if (e.persisted) lift(); });
  return ready;
}

function bindLinks() {
  document.addEventListener("click", (e) => {
    if (e.defaultPrevented || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
    const a = e.target.closest("a[href]");
    if (!a || a.target === "_blank" || a.hasAttribute("download") || a.dataset.noTransition !== undefined) return;
    const url = new URL(a.href, location.href);
    if (url.origin !== location.origin || /^(mailto|tel):/.test(a.getAttribute("href"))) return;
    if (url.pathname === location.pathname && url.search === location.search) return; // same page / in-page anchor
    e.preventDefault();

    const label = (a.dataset.transitionLabel || (a.classList.contains("logo") ? "Home" : a.textContent.replace(/\s+/g, " ").trim()))
      .replace(/\s*[→>]\s*$/, "").slice(0, 28);
    const text = document.querySelector("[data-curtain-text]");
    if (text) text.textContent = label;
    try { sessionStorage.setItem("ah-label", label); } catch (err) { /* private mode: still navigate */ }
    const menu = document.querySelector("[data-menu]");
    if (menu && menu.open) menu.close();
    root.classList.add("curtain-cover");
    setTimeout(() => { location.href = a.href; }, COVER_MS);
  });
}
