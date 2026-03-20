/**
 * confirm.js
 * Intercepts delete / destructive form submissions and asks the user
 * to confirm before proceeding.
 *
 * Supported patterns:
 *   1. Any element with a data-confirm="message" attribute.
 *   2. Any <button> or <input[type=submit]> with the class `confirm-delete`
 *      (uses a generic "Are you sure?" message unless data-message is set).
 */
document.addEventListener('DOMContentLoaded', () => {

  // 1. Generic data-confirm attribute (any element)
  document.querySelectorAll('[data-confirm]').forEach(el => {
    el.addEventListener('click', e => {
      const message = el.dataset.confirm || 'Are you sure you want to do this?';
      if (!window.confirm(message)) {
        e.preventDefault();
        e.stopImmediatePropagation();
      }
    });
  });

  // 2. confirm-delete class on form submit buttons
  document.querySelectorAll('button.confirm-delete, input.confirm-delete[type="submit"]').forEach(btn => {
    btn.addEventListener('click', e => {
      const message = btn.dataset.message || 'Are you sure you want to delete this? This cannot be undone.';
      if (!window.confirm(message)) {
        e.preventDefault();
        e.stopImmediatePropagation();
      }
      // Confirmed → form submits normally via POST with CSRF token intact
    });
  });

});
