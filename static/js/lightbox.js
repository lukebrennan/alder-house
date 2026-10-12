/* Photo lightbox built on <dialog>: focus trap, Esc, arrows, swipe, focus restore. */
export function initLightbox() {
  const dialog = document.querySelector("[data-lightbox-dialog]");
  const galleries = document.querySelectorAll("[data-gallery]");
  if (!dialog || !galleries.length || typeof dialog.showModal !== "function") return;

  const img = dialog.querySelector("[data-lb-img]");
  const caption = dialog.querySelector("[data-lb-caption]");
  let tiles = [];
  let index = 0;

  const show = (i) => {
    index = (i + tiles.length) % tiles.length;
    const t = tiles[index];
    img.src = t.dataset.lightbox;
    img.alt = t.dataset.alt || "";
    caption.textContent = t.dataset.caption || "";
    const next = tiles[(index + 1) % tiles.length];
    if (next) new Image().src = next.dataset.lightbox;
  };

  galleries.forEach((g) => {
    const list = [...g.querySelectorAll("[data-lightbox]")];
    list.forEach((tile) => tile.addEventListener("click", () => {
      tiles = list;
      show(list.indexOf(tile));
      dialog.showModal();
    }));
  });

  dialog.querySelector("[data-lb-close]").addEventListener("click", () => dialog.close());
  dialog.querySelector("[data-lb-prev]").addEventListener("click", () => show(index - 1));
  dialog.querySelector("[data-lb-next]").addEventListener("click", () => show(index + 1));
  dialog.addEventListener("keydown", (e) => {
    if (e.key === "ArrowLeft") { e.preventDefault(); show(index - 1); }
    if (e.key === "ArrowRight") { e.preventDefault(); show(index + 1); }
  });
  dialog.addEventListener("click", (e) => { if (e.target === dialog) dialog.close(); });

  let startX = null;
  dialog.addEventListener("pointerdown", (e) => { startX = e.clientX; });
  dialog.addEventListener("pointerup", (e) => {
    if (startX === null) return;
    const dx = e.clientX - startX;
    startX = null;
    if (Math.abs(dx) > 60) show(index + (dx < 0 ? 1 : -1));
  });
}
