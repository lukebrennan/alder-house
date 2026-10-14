/* Header: transparent over the hero until scrolled, tucks away on scroll-down and returns on
   scroll-up; accessible full-screen menu; mobile booking bar. */
export function initHeader() {
  const header = document.querySelector("[data-header]");
  const bar = document.querySelector("[data-book-bar]");
  const menu = document.querySelector("[data-menu]");
  const overlay = header && header.dataset.mode === "overlay";
  let lastY = window.scrollY;
  let ticking = false;

  const update = () => {
    const y = window.scrollY;
    if (header) {
      header.classList.toggle("is-solid", !overlay || y > 40);
      const dy = y - lastY;
      if (y > 240 && dy > 8) header.classList.add("is-hidden");
      else if (dy < -8 || y < 240) header.classList.remove("is-hidden");
    }
    if (bar) bar.classList.toggle("is-on", y > Math.min(window.innerHeight * 0.8, 640));
    lastY = y;
    ticking = false;
  };
  window.addEventListener("scroll", () => { if (!ticking) { ticking = true; requestAnimationFrame(update); } }, { passive: true });
  update();

  // Keep the header visible while keyboard focus is inside it.
  if (header) header.addEventListener("focusin", () => header.classList.remove("is-hidden"));

  const opener = document.querySelector("[data-menu-open]");
  if (!menu || !opener || typeof menu.showModal !== "function") return;
  const open = () => { menu.showModal(); opener.setAttribute("aria-expanded", "true"); };
  const close = () => menu.close();
  opener.addEventListener("click", open);
  menu.querySelector("[data-menu-close]").addEventListener("click", close);
  menu.addEventListener("close", () => opener.setAttribute("aria-expanded", "false"));
  menu.addEventListener("click", (e) => { if (e.target === menu) close(); });
  menu.querySelectorAll("a").forEach((a) => a.addEventListener("click", () => { if (a.hash && a.pathname === location.pathname) close(); }));
  window.matchMedia("(min-width: 1100px)").addEventListener("change", (e) => { if (e.matches && menu.open) close(); });
}
