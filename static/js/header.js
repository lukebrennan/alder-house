/* Header: transparent over the hero until scrolled; accessible full-screen menu. */
export function initHeader() {
  const header = document.querySelector("[data-header]");
  if (header && header.dataset.mode === "overlay") {
    let ticking = false;
    const update = () => {
      header.classList.toggle("is-solid", window.scrollY > 40);
      ticking = false;
    };
    window.addEventListener("scroll", () => { if (!ticking) { ticking = true; requestAnimationFrame(update); } }, { passive: true });
    update();
  } else if (header) {
    header.classList.add("is-solid");
  }

  const menu = document.querySelector("[data-menu]");
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
