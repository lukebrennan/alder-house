/* Demo booking flow: availability results and a mock summary.
   Everything is generated in the browser. Nothing is stored or sent anywhere. */
const base = document.documentElement.dataset.base || "";
const gbp = (n) => `£${n.toLocaleString("en-GB")}`;
const parse = (s) => { const [y, m, d] = s.split("-").map(Number); return new Date(y, m - 1, d); };
const fmt = (d, o) => d.toLocaleDateString("en-GB", o);
const day = (d) => fmt(d, { weekday: "short", day: "numeric", month: "short" });
const esc = (s) => String(s).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
const plural = (n, w) => `${n} ${w}${n === 1 ? "" : "s"}`;

const WEEKEND_UPLIFT = 20; // Friday and Saturday nights
const nightRate = (room, date) => room.price + ([5, 6].includes(date.getDay()) ? WEEKEND_UPLIFT : 0);

/** Deterministic pseudo-availability so the demo feels real but is repeatable. */
function availability(room, checkin, count) {
  let h = 0;
  for (const c of `${room.slug}${checkin}${count}`) h = (h * 31 + c.charCodeAt(0)) >>> 0;
  if (h % 9 === 0) return "sold-out";
  if (h % 4 === 0) return "last";
  return "ok";
}

function quote(room, start, count) {
  const lines = [];
  let total = 0;
  for (let i = 0; i < count; i++) {
    const d = new Date(start.getFullYear(), start.getMonth(), start.getDate() + i);
    const rate = nightRate(room, d);
    total += rate;
    lines.push(rate);
  }
  return { total, lines, avg: Math.round(total / count) };
}

function readParams() {
  const q = new URLSearchParams(location.search);
  const ci = q.get("checkin"), co = q.get("checkout");
  const guests = Math.min(Math.max(parseInt(q.get("guests") || "2", 10) || 2, 1), 3);
  if (!/^\d{4}-\d{2}-\d{2}$/.test(ci || "") || !/^\d{4}-\d{2}-\d{2}$/.test(co || "")) return { guests, room: q.get("room") };
  const start = parse(ci), end = parse(co);
  const count = Math.round((end - start) / 86400000);
  return { ci, co, start, end, count, guests, room: q.get("room") };
}

const roomsData = () => JSON.parse(document.getElementById("rooms-data")?.textContent || "[]");

function renderResults(root) {
  const p = readParams();
  const rooms = roomsData();
  if (!p.start) { root.innerHTML = ""; return; }
  const today = new Date(); today.setHours(0, 0, 0, 0);
  if (p.count < 1 || p.count > 14 || p.start < today) {
    root.innerHTML = `<div class="empty-state"><h2 class="h3">Let's check those dates</h2><p>${p.start < today ? "Check-in cannot be in the past." : p.count < 1 ? "Check-out must be after check-in." : "Stays are limited to 14 nights."} Please choose your dates again.</p></div>`;
    return;
  }
  const fits = rooms.filter((r) => r.sleeps >= p.guests);
  const hidden = rooms.length - fits.length;
  const rows = fits.map((r) => ({ r, state: availability(r, p.ci, p.count), q: quote(r, p.start, p.count) }))
    .sort((a, b) => (a.state === "sold-out") - (b.state === "sold-out") || a.q.avg - b.q.avg);
  const free = rows.filter((x) => x.state !== "sold-out").length;

  const items = rows.map(({ r, state, q }) => {
    const unavailable = state === "sold-out";
    const href = `${base}/book/summary/?room=${r.slug}&checkin=${p.ci}&checkout=${p.co}&guests=${p.guests}`;
    return `<article class="result${unavailable ? " is-unavailable" : ""}${p.room === r.slug ? " is-featured" : ""}">
      <a class="result__media media hover-zoom" style="--ratio:4/3" href="${r.href}" tabindex="-1" aria-hidden="true"><img src="${r.image}" alt="" loading="lazy" width="900" height="675"></a>
      <div>
        ${state === "last" ? '<p class="result__flag">Only one left</p>' : ""}
        <h3><a href="${r.href}">${esc(r.name)}</a></h3>
        <p>${esc(r.short)}</p>
        <p class="result__meta"><span>Sleeps ${r.sleeps}</span><span>${esc(r.bed)}</span><span>${r.size} m²</span><span>${esc(r.view)}</span></p>
      </div>
      <div class="result__side">
        ${unavailable ? '<p class="result__rate">Not available for these dates</p><p class="result__rate">Try nearby dates or another room.</p>' : `
        <p class="result__rate">${gbp(q.avg)} per night, breakfast included</p>
        <p class="result__total"><small>Total for ${plural(p.count, "night")}</small>${gbp(q.total)}</p>
        <a class="btn btn--primary" href="${href}" aria-label="Select ${esc(r.name)}"><span>Select room</span></a>`}
      </div>
    </article>`;
  }).join("");

  root.innerHTML = `<div class="results-head">
      <h2 id="results-title" tabindex="-1">${free ? `${plural(free, "room")} available` : "No rooms available"}</h2>
      <p>${day(p.start)} to ${day(p.end)} · ${plural(p.count, "night")} · ${plural(p.guests, "guest")}</p>
    </div>
    <div class="results">${items}</div>
    ${hidden ? `<p class="fine-print">${plural(hidden, "room")} not shown because ${hidden === 1 ? "it sleeps" : "they sleep"} fewer than ${p.guests} guests.</p>` : ""}
    <p class="fine-print">Rates include breakfast and taxes. Friday and Saturday nights carry a ${gbp(WEEKEND_UPLIFT)} supplement.</p>`;
}

function renderSummary(root) {
  const p = readParams();
  const room = roomsData().find((r) => r.slug === p.room);
  const today = new Date(); today.setHours(0, 0, 0, 0);
  if (!room || !p.start || p.count < 1 || p.count > 14 || p.start < today) {
    root.innerHTML = `<div class="empty-state"><h2 class="h3">We couldn't find that stay</h2><p>The room or dates are missing. Let's start again.</p><a class="btn btn--primary" href="${base}/book/"><span>Check availability</span></a></div>`;
    return;
  }
  const q = quote(room, p.start, p.count);
  const grouped = {};
  q.lines.forEach((rate) => { grouped[rate] = (grouped[rate] || 0) + 1; });
  const lines = Object.entries(grouped).map(([rate, n]) => `<div><dt>${plural(n, "night")} × ${gbp(Number(rate))}</dt><dd>${gbp(Number(rate) * n)}</dd></div>`).join("");
  const times = ["Before 3pm", "3pm to 5pm", "5pm to 7pm", "After 7pm"].map((t) => `<option>${t}</option>`).join("");

  root.innerHTML = `<div class="summary">
    <div id="summary-main">
      <h2>Your details</h2>
      <form class="form" id="guest-form" novalidate>
        <div class="form__grid">
          <div class="field"><label for="g-first">First name <span class="field__req" aria-hidden="true">*</span></label><input id="g-first" required autocomplete="given-name"></div>
          <div class="field"><label for="g-last">Last name <span class="field__req" aria-hidden="true">*</span></label><input id="g-last" required autocomplete="family-name"></div>
          <div class="field"><label for="g-email">Email <span class="field__req" aria-hidden="true">*</span></label><input id="g-email" type="email" required autocomplete="email"></div>
          <div class="field"><label for="g-arrival">Estimated arrival</label><select id="g-arrival">${times}</select></div>
        </div>
        <div class="field"><label for="g-notes">Special requests</label><textarea id="g-notes" rows="4"></textarea></div>
        <div class="demo-callout" role="note"><strong>No payment is taken.</strong> This is a demo booking, so there are no card fields and nothing is sent or stored. Please do not enter real personal details.</div>
        <button class="btn btn--primary" type="submit"><span>Confirm booking</span></button>
        <p class="form-status" role="status" aria-live="polite"></p>
      </form>
    </div>
    <aside class="summary-card" aria-labelledby="sum-title">
      <h2 id="sum-title" class="eyebrow" style="font-size:.72rem;margin:0">Stay summary</h2>
      <div class="media" style="--ratio:3/2;margin-top:1rem"><img src="${room.image}" alt="${esc(room.alt)}" width="900" height="675"></div>
      <h3 class="summary-card__room">${esc(room.name)}</h3>
      <p class="fine-print" style="margin:0">${esc(room.bed)} · ${esc(room.view)} · ${room.size} m²</p>
      <dl class="breakdown">
        <div><dt>Check-in</dt><dd>${fmt(p.start, { weekday: "short", day: "numeric", month: "long", year: "numeric" })}, from 3pm</dd></div>
        <div><dt>Check-out</dt><dd>${fmt(p.end, { weekday: "short", day: "numeric", month: "long", year: "numeric" })}, by 11am</dd></div>
        <div><dt>Guests</dt><dd>${plural(p.guests, "guest")}</dd></div>
        ${lines}
        <div><dt>Breakfast</dt><dd>Included</dd></div>
        <div><dt>Taxes</dt><dd>Included</dd></div>
        <div class="is-total"><dt>Total</dt><dd>${gbp(q.total)}</dd></div>
      </dl>
      <p class="fine-print" style="margin:1rem 0 0"><a href="${base}/book/?checkin=${p.ci}&checkout=${p.co}&guests=${p.guests}">Change dates or room</a></p>
    </aside>
  </div>`;

  const form = root.querySelector("#guest-form");
  const status = form.querySelector(".form-status");
  form.addEventListener("submit", (e) => {
    e.preventDefault();
    const bad = [...form.querySelectorAll("input, select, textarea")].filter((f) => !f.checkValidity());
    form.querySelectorAll("[aria-invalid]").forEach((f) => f.removeAttribute("aria-invalid"));
    if (bad.length) {
      bad.forEach((f) => f.setAttribute("aria-invalid", "true"));
      status.classList.add("is-error");
      status.textContent = "Please complete the highlighted fields.";
      bad[0].focus();
      return;
    }
    const ref = "AH-DEMO-" + Math.random().toString(36).slice(2, 8).toUpperCase();
    const first = esc(form.querySelector("#g-first").value.trim());
    root.querySelector("#summary-main").innerHTML = `<div class="confirmation" role="status">
      <p class="eyebrow">Booking confirmed</p>
      <h2 id="confirm-title" tabindex="-1">Thank you${first ? `, ${first}` : ""}.</h2>
      <p>Your stay in ${esc(room.name)} is confirmed for these dates.</p>
      <p class="confirmation__ref">Reference ${ref}</p>
      <p class="fine-print">This is a demo, so nothing has actually been reserved, no email has been sent and none of the details you entered have been stored.</p>
      <div class="btn-row"><a class="btn btn--primary" href="${base}/"><span>Back to the home page</span></a><a class="btn btn--secondary" href="${base}/stay/"><span>Browse the rooms</span></a></div>
    </div>`;
    root.querySelector("#confirm-title").focus();
  });
}

export function initBooking() {
  const results = document.querySelector("[data-results]");
  if (results) {
    renderResults(results);
    if (new URLSearchParams(location.search).get("checkin")) {
      results.scrollIntoView({ behavior: window.matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth", block: "start" });
    }
  }
  const summary = document.querySelector("[data-summary]");
  if (summary) renderSummary(summary);
}
