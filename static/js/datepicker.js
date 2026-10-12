/* Accessible check-in / check-out range picker. Progressive enhancement of two <input type="date"> fields:
   without JavaScript the native date inputs still work. */
const pad = (n) => String(n).padStart(2, "0");
const iso = (d) => `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}`;
const parse = (s) => { const [y, m, d] = s.split("-").map(Number); return new Date(y, m - 1, d); };
const addDays = (d, n) => new Date(d.getFullYear(), d.getMonth(), d.getDate() + n);
const addMonths = (d, n) => new Date(d.getFullYear(), d.getMonth() + n, 1);
const sameDay = (a, b) => a && b && iso(a) === iso(b);
const short = (d) => d.toLocaleDateString("en-GB", { weekday: "short", day: "numeric", month: "short" });
const long = (d) => d.toLocaleDateString("en-GB", { weekday: "long", day: "numeric", month: "long", year: "numeric" });
const nights = (a, b) => Math.round((b - a) / 86400000);

export function initDatePickers() {
  document.querySelectorAll("[data-booking]").forEach(enhance);
}

function enhance(form) {
  const nativeIn = form.querySelector('[data-date="in"]');
  const nativeOut = form.querySelector('[data-date="out"]');
  if (!nativeIn || !nativeOut) return;

  const now = new Date();
  const today = new Date(now.getFullYear(), now.getMonth(), now.getDate());
  let start = null, end = null, hover = null, active = "in";
  let view = new Date(today.getFullYear(), today.getMonth(), 1);
  let focusDate = today;

  // Swap each native input for a read-only display field plus a hidden ISO value.
  const make = (native, placeholder) => {
    const display = document.createElement("input");
    display.type = "text";
    display.readOnly = true;
    display.required = true;
    display.id = native.id;
    display.placeholder = placeholder;
    display.autocomplete = "off";
    display.setAttribute("aria-haspopup", "dialog");
    display.setAttribute("aria-expanded", "false");
    display.setAttribute("data-datefield", native.dataset.date);
    native.id = `${native.id}-value`;
    native.type = "hidden";
    native.removeAttribute("required");
    native.removeAttribute("min");
    native.removeAttribute("data-date");
    native.parentElement.insertBefore(display, native);
    return display;
  };
  const dIn = make(nativeIn, "Add date");
  const dOut = make(nativeOut, "Add date");

  const sync = () => {
    nativeIn.value = start ? iso(start) : "";
    nativeOut.value = end ? iso(end) : "";
    dIn.value = start ? short(start) : "";
    dOut.value = end ? short(end) : "";
  };

  // Prefill from the query string on the booking page.
  if (form.classList.contains("booking--page")) {
    const q = new URLSearchParams(location.search);
    const a = q.get("checkin"), b = q.get("checkout");
    if (a && /^\d{4}-\d{2}-\d{2}$/.test(a)) start = parse(a);
    if (b && /^\d{4}-\d{2}-\d{2}$/.test(b)) end = parse(b);
    const g = form.querySelector('[name="guests"]');
    if (g && q.get("guests")) g.value = q.get("guests");
    if (start) { view = new Date(start.getFullYear(), start.getMonth(), 1); focusDate = start; }
    sync();
  }

  const cal = document.createElement("div");
  cal.className = "cal";
  cal.hidden = true;
  cal.setAttribute("role", "dialog");
  cal.setAttribute("aria-label", "Choose your dates");
  const backdrop = document.createElement("div");
  backdrop.className = "cal-backdrop";
  backdrop.hidden = true;
  const err = document.createElement("p");
  err.className = "field-error";
  err.setAttribute("role", "alert");
  err.hidden = true;
  form.append(err, backdrop, cal);

  const monthCount = () => (window.matchMedia("(min-width: 700px)").matches ? 2 : 1);

  function monthGrid(first) {
    const label = first.toLocaleDateString("en-GB", { month: "long", year: "numeric" });
    const lead = (first.getDay() + 6) % 7; // Monday first
    const days = new Date(first.getFullYear(), first.getMonth() + 1, 0).getDate();
    let rows = "";
    let day = 1 - lead;
    for (let w = 0; w < 6 && day <= days; w++) {
      let tds = "";
      for (let i = 0; i < 7; i++, day++) {
        if (day < 1 || day > days) { tds += "<td></td>"; continue; }
        const d = new Date(first.getFullYear(), first.getMonth(), day);
        const disabled = d < today;
        const edge = sameDay(d, start) || sameDay(d, end);
        const upper = end || (start && hover && hover > start ? hover : null);
        const inRange = start && upper && d > start && d < upper;
        const cls = ["cal__day", edge && "is-edge", inRange && "is-in-range", sameDay(d, today) && "is-today"].filter(Boolean).join(" ");
        tds += `<td><button type="button" class="${cls}" data-date="${iso(d)}" tabindex="${sameDay(d, focusDate) ? 0 : -1}" aria-label="${long(d)}${edge ? (sameDay(d, start) ? ", check-in" : ", check-out") : ""}"${disabled ? " disabled" : ""}>${day}</button></td>`;
      }
      rows += `<tr>${tds}</tr>`;
    }
    const heads = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"].map((d) => `<th scope="col" abbr="${d}">${d.slice(0, 2)}</th>`).join("");
    return `<div class="cal__month"><h3 class="cal__month-name" aria-live="polite">${label}</h3><table role="grid" aria-label="${label}"><thead><tr>${heads}</tr></thead><tbody>${rows}</tbody></table></div>`;
  }

  const chev = (d) => `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="${d}"/></svg>`;

  function render(refocus) {
    const count = monthCount();
    const atMin = view <= new Date(today.getFullYear(), today.getMonth(), 1);
    let summary = "Select your check-in date";
    if (start && !end) summary = `Check-in ${short(start)}. Now choose check-out`;
    if (start && end) summary = `${short(start)} to ${short(end)}: ${nights(start, end)} night${nights(start, end) === 1 ? "" : "s"}`;
    cal.innerHTML = `
      <div class="cal__head">
        <button type="button" class="cal__nav" data-nav="-1" aria-label="Previous month"${atMin ? " disabled" : ""}>${chev("M15 5l-7 7 7 7")}</button>
        <span class="cal__title">${view.toLocaleDateString("en-GB", { month: "long", year: "numeric" })}</span>
        <button type="button" class="cal__nav" data-nav="1" aria-label="Next month">${chev("M9 5l7 7-7 7")}</button>
      </div>
      <div class="cal__months">${Array.from({ length: count }, (_, i) => monthGrid(addMonths(view, i))).join("")}</div>
      <div class="cal__foot">
        <p class="cal__summary" role="status">${summary}</p>
        <div class="cal__actions">
          <button type="button" class="btn btn--secondary btn--small" data-clear>Clear</button>
          <button type="button" class="btn btn--primary btn--small" data-done>Done</button>
        </div>
      </div>`;
    if (refocus) (cal.querySelector(`[data-date="${iso(focusDate)}"]`) || cal.querySelector(".cal__day:not([disabled])"))?.focus();
  }

  function open(which) {
    active = which;
    err.hidden = true;
    if (start && which === "in") { view = new Date(start.getFullYear(), start.getMonth(), 1); focusDate = start; }
    if (end && which === "out") { view = new Date(end.getFullYear(), end.getMonth(), 1); focusDate = end; }
    if (!start && focusDate < today) focusDate = today;
    cal.hidden = false;
    backdrop.hidden = false;
    [dIn, dOut].forEach((i) => i.setAttribute("aria-expanded", "true"));
    render(true);
  }
  function close(returnFocus) {
    if (cal.hidden) return;
    cal.hidden = true;
    backdrop.hidden = true;
    hover = null;
    [dIn, dOut].forEach((i) => i.setAttribute("aria-expanded", "false"));
    if (returnFocus) (active === "out" && end ? dOut : dIn).focus();
  }

  function pick(d) {
    if (d < today) return;
    if (!start || (start && end) || d <= start) { start = d; end = null; active = "out"; }
    else { end = d; }
    sync();
    if (end) {
      close(false);
      form.querySelector('[name="guests"]')?.focus();
    } else {
      view = new Date(d.getFullYear(), d.getMonth(), 1);
      focusDate = d;
      render(true);
    }
  }

  [dIn, dOut].forEach((input, i) => {
    const which = i === 0 ? "in" : "out";
    input.addEventListener("click", () => open(which));
    input.addEventListener("keydown", (e) => { if (["Enter", " ", "ArrowDown"].includes(e.key)) { e.preventDefault(); open(which); } });
  });

  cal.addEventListener("click", (e) => {
    const day = e.target.closest(".cal__day");
    if (day) return pick(parse(day.dataset.date));
    const nav = e.target.closest("[data-nav]");
    if (nav) { view = addMonths(view, Number(nav.dataset.nav)); focusDate = view < today ? today : view; return render(false); }
    if (e.target.closest("[data-clear]")) { start = end = null; sync(); active = "in"; return render(false); }
    if (e.target.closest("[data-done]")) close(true);
  });
  cal.addEventListener("mouseover", (e) => {
    const day = e.target.closest(".cal__day");
    if (!day || !start || end) return;
    const h = parse(day.dataset.date);
    if (sameDay(h, hover)) return;
    hover = h;
    cal.querySelectorAll(".cal__day").forEach((b) => {
      const d = parse(b.dataset.date);
      b.classList.toggle("is-in-range", d > start && d < hover);
    });
  });
  cal.addEventListener("keydown", (e) => {
    if (e.key === "Escape") { e.preventDefault(); e.stopPropagation(); return close(true); }
    const day = e.target.closest(".cal__day");
    if (!day) return;
    const cur = parse(day.dataset.date);
    const moves = { ArrowLeft: addDays(cur, -1), ArrowRight: addDays(cur, 1), ArrowUp: addDays(cur, -7), ArrowDown: addDays(cur, 7),
      Home: addDays(cur, -((cur.getDay() + 6) % 7)), End: addDays(cur, 6 - ((cur.getDay() + 6) % 7)),
      PageUp: new Date(cur.getFullYear(), cur.getMonth() - 1, cur.getDate()), PageDown: new Date(cur.getFullYear(), cur.getMonth() + 1, cur.getDate()) };
    if (!moves[e.key]) return;
    e.preventDefault();
    let next = moves[e.key];
    if (next < today) next = today;
    focusDate = next;
    const last = addMonths(view, monthCount() - 1);
    if (next < view || next >= addMonths(last, 1)) view = new Date(next.getFullYear(), next.getMonth(), 1);
    render(true);
  });
  backdrop.addEventListener("click", () => close(true));
  document.addEventListener("click", (e) => {
    if (cal.hidden || cal.contains(e.target) || e.target === dIn || e.target === dOut) return;
    close(false);
  });

  form.addEventListener("submit", (e) => {
    if (start && end) return;
    e.preventDefault();
    err.textContent = !start ? "Please choose a check-in date." : "Please choose a check-out date.";
    err.hidden = false;
    open(!start ? "in" : "out");
  });
}
