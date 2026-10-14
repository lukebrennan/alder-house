import { initCurtain } from "./curtain.js";
import { initSplit } from "./split.js";
import { initHeader } from "./header.js";
import { initReveal } from "./reveal.js";
import { initAccordions } from "./accordion.js";
import { initLightbox } from "./lightbox.js";
import { initDatePickers } from "./datepicker.js";
import { initForms } from "./forms.js";
import { initMap } from "./map.js";
import { initJournalFilter } from "./filter.js";
import { initBooking } from "./booking.js";

const domReady = (fn) => (document.readyState === "loading" ? document.addEventListener("DOMContentLoaded", fn) : fn());

domReady(() => {
  const ready = initCurtain();
  initSplit();
  initHeader();
  initAccordions();
  initLightbox();
  initDatePickers();
  initForms();
  initMap();
  initJournalFilter();
  initBooking();
  // Scroll reveals wait for the curtain so nothing animates unseen behind it.
  ready.then(initReveal);
});
