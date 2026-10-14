/* Fade-and-rise reveals. IntersectionObserver does the work; a scroll check backs it up so nothing
   on screen can ever stay hidden. Reduced motion is handled in CSS. */
export function initReveal() {
  const items = [...document.querySelectorAll("[data-reveal], .reveal-img")];
  if (!items.length) return;
  const show = (el) => el.classList.add("is-visible");
  if (!("IntersectionObserver" in window) || window.matchMedia("(prefers-reduced-motion: reduce)").matches) return items.forEach(show);

  const io = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) { show(entry.target); io.unobserve(entry.target); }
    });
  }, { rootMargin: "0px 0px -6% 0px", threshold: 0.05 });
  items.forEach((el) => io.observe(el));

  // Backup: reveal anything whose box is in the viewport, whatever the observer did.
  let pending = items.filter((el) => !el.classList.contains("is-visible"));
  const sweep = () => {
    const vh = window.innerHeight;
    pending = pending.filter((el) => {
      const r = el.getBoundingClientRect();
      if (r.top < vh * 0.96 && r.bottom > 0) { show(el); io.unobserve(el); return false; }
      return true;
    });
  };
  let ticking = false;
  const onScroll = () => { if (!ticking) { ticking = true; requestAnimationFrame(() => { sweep(); ticking = false; }); } };
  window.addEventListener("scroll", onScroll, { passive: true });
  window.addEventListener("resize", onScroll, { passive: true });
  window.addEventListener("load", () => setTimeout(sweep, 400));
  setTimeout(sweep, 1200);
}
