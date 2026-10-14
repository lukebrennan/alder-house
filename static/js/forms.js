/* Demo forms: validate accessibly, show a confirmation, send nothing anywhere. */
export function initForms() {
  document.querySelectorAll("[data-demo-form]").forEach((form) => {
    const status = form.querySelector(".form-status");

    const clearError = (field) => {
      field.removeAttribute("aria-invalid");
      const err = field.parentElement.querySelector(".field__error");
      if (err) { err.remove(); field.removeAttribute("aria-describedby"); }
    };
    form.addEventListener("input", (e) => { if (e.target.matches("input, select, textarea")) clearError(e.target); });

    form.addEventListener("submit", (e) => {
      e.preventDefault();
      let firstBad = null;
      form.querySelectorAll("input, select, textarea").forEach((field) => {
        clearError(field);
        if (field.checkValidity()) return;
        firstBad = firstBad || field;
        field.setAttribute("aria-invalid", "true");
        const err = document.createElement("p");
        err.className = "field__error";
        err.id = `${field.id || field.name}-error`;
        err.textContent = field.validity.typeMismatch ? "Please enter a valid email address." : "Please complete this field.";
        field.setAttribute("aria-describedby", err.id);
        field.insertAdjacentElement("afterend", err);
      });
      if (firstBad) {
        if (status) { status.classList.add("is-error"); status.textContent = "Please check the highlighted fields."; }
        firstBad.focus();
        return;
      }
      form.reset();
      if (status) { status.classList.remove("is-error"); status.textContent = form.dataset.success || "Thank you. This is a demo, so nothing has been sent."; }
    });
  });
}
