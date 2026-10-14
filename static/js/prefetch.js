/* Warm the next page: fetch an internal page's HTML as soon as the pointer or keyboard focus signals intent. */
export function initPrefetch() {
  const seen = new Set();
  const conn = navigator.connection;
  if (conn && (conn.saveData || /2g/.test(conn.effectiveType || ""))) return;
  const warm = (e) => {
    const a = e.target.closest && e.target.closest("a[href]");
    if (!a || a.target === "_blank" || a.hasAttribute("download")) return;
    const url = new URL(a.href, location.href);
    if (url.origin !== location.origin || url.pathname === location.pathname || seen.has(url.pathname)) return;
    if (/\/book\/summary\//.test(url.pathname)) return;
    seen.add(url.pathname);
    const link = document.createElement("link");
    link.rel = "prefetch";
    link.href = url.pathname + url.search;
    link.as = "document";
    document.head.appendChild(link);
  };
  document.addEventListener("pointerover", warm, { passive: true });
  document.addEventListener("touchstart", warm, { passive: true });
  document.addEventListener("focusin", warm);
}
