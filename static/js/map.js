/* Explore map: link the places list and the illustrated pins. */
export function initMap() {
  document.querySelectorAll("[data-map]").forEach((root) => {
    const targets = (id) => root.querySelectorAll(`[data-place="${id}"]`);
    const clear = () => root.querySelectorAll(".is-active").forEach((el) => el.classList.remove("is-active"));
    const activate = (id) => { clear(); targets(id).forEach((el) => el.classList.add("is-active")); };
    root.querySelectorAll("[data-place]").forEach((el) => {
      const id = el.dataset.place;
      el.addEventListener("mouseenter", () => activate(id));
      el.addEventListener("mouseleave", clear);
      el.addEventListener("focus", () => activate(id));
      el.addEventListener("blur", clear);
      el.addEventListener("click", () => activate(id));
    });
  });
}
