/* Wrap the words of [data-split] headings so they can rise into view one by one.
   The heading keeps its full text as an accessible name. */
export function initSplit() {
  document.querySelectorAll("[data-split]").forEach((el) => {
    if (el.dataset.splitDone) return;
    const text = el.textContent.replace(/\s+/g, " ").trim();
    if (!text) return;
    el.setAttribute("aria-label", text);
    const wrap = document.createElement("span");
    wrap.setAttribute("aria-hidden", "true");
    text.split(" ").forEach((word, i, all) => {
      const outer = document.createElement("span");
      outer.className = "w";
      const inner = document.createElement("span");
      inner.className = "wi";
      inner.style.setProperty("--i", i);
      inner.textContent = word;
      outer.appendChild(inner);
      wrap.appendChild(outer);
      if (i < all.length - 1) wrap.appendChild(document.createTextNode(" "));
    });
    el.textContent = "";
    el.appendChild(wrap);
    el.dataset.splitDone = "1";
  });
}
