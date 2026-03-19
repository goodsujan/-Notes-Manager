/**
 * confirm.js
 * Intercepts delete / destructive form submissions and asks the user
 * to confirm before proceeding.
 *
 * Usage: add  data-confirm="Are you sure?"  to any <button> or <a>.
 */
document.addEventListener('DOMContentLoaded', () => {
  // Buttons / links with a data-confirm attribute
  document.querySelectorAll('[data-confirm]').forEach(el => {
    el.addEventListener('click', e => {
      const message = el.dataset.confirm || 'Are you sure you want to do this?';
      if (!window.confirm(message)) {
        e.preventDefault();
        e.stopImmediatePropagation();
      }
    });
  });
});
