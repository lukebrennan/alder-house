import { initHeader } from "./header.js";
import { initReveal } from "./reveal.js";
import { initAccordions } from "./accordion.js";
import { initLightbox } from "./lightbox.js";
import { initDatePickers } from "./datepicker.js";
import { initForms } from "./forms.js";
import { initMap } from "./map.js";
import { initJournalFilter } from "./filter.js";
import { initBooking } from "./booking.js";

const ready = (fn) => (document.readyState === "loading" ? document.addEventListener("DOMContentLoaded", fn) : fn());

ready(() => {
  initHeader();
  initReveal();
  initAccordions();
  initLightbox();
  initDatePickers();
  initForms();
  initMap();
  initJournalFilter();
  initBooking();
});
