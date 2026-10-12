/* Fade-and-rise reveals using IntersectionObserver. Respects reduced motion via CSS. */
export function initReveal() {
  const items = document.querySelectorAll("[data-reveal], .reveal-img");
  if (!items.length) return;
  const showAll = () => items.forEach((el) => el.classList.add("is-visible"));
  if (!("IntersectionObserver" in window) || window.matchMedia("(prefers-reduced-motion: reduce)").matches) return showAll();
  const io = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) { entry.target.classList.add("is-visible"); io.unobserve(entry.target); }
    });
  }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
  items.forEach((el) => io.observe(el));
}
