/* Journal category filter. All articles are visible without JavaScript. */
export function initJournalFilter() {
  const grid = document.querySelector("[data-journal-grid]");
  if (!grid) return;
  const chips = document.querySelectorAll("[data-filter]");
  const cards = grid.querySelectorAll("[data-category]");
  const note = grid.querySelector("[data-journal-note]");
  const status = document.querySelector("[data-filter-status]");
  chips.forEach((chip) => chip.addEventListener("click", () => {
    const f = chip.dataset.filter;
    chips.forEach((c) => c.setAttribute("aria-pressed", String(c === chip)));
    let shown = 0;
    cards.forEach((card) => {
      const match = f === "All" || card.dataset.category === f;
      card.hidden = !match;
      if (match) { shown += 1; card.querySelector("[data-reveal]") || card.classList.add("is-visible"); }
    });
    grid.toggleAttribute("data-filtered", f !== "All");
    if (note) note.hidden = f !== "All";
    if (status) status.textContent = f === "All" ? `Showing all ${shown} articles` : `Showing ${shown} article${shown === 1 ? "" : "s"} in ${f}`;
  }));
}
