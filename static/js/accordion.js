/* Accessible accordion: buttons toggle aria-expanded; CSS animates the panel height. */
export function initAccordions() {
  document.querySelectorAll("[data-accordion]").forEach((root) => {
    root.querySelectorAll(".accordion__button").forEach((btn) => {
      const panel = document.getElementById(btn.getAttribute("aria-controls"));
      btn.addEventListener("click", () => {
        const open = btn.getAttribute("aria-expanded") === "true";
        btn.setAttribute("aria-expanded", String(!open));
        panel.classList.toggle("is-open", !open);
      });
    });
  });
}
