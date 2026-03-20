/**
 * confirm.js
 * Intercepts any button with class `confirm-delete` and asks the user
 * to confirm before the parent <form> is submitted.
 * Works with Django's POST + CSRF pattern — the form is never bypassed.
 */
(function () {
  'use strict';

  document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.confirm-delete').forEach(function (btn) {
      btn.addEventListener('click', function (e) {
        var message = btn.dataset.message || 'Are you sure you want to delete this note? This cannot be undone.';
        if (!window.confirm(message)) {
          // User clicked Cancel — stop the form from submitting
          e.preventDefault();
          e.stopPropagation();
        }
        // User clicked OK — let the event bubble and the form submit normally (POST + CSRF intact)
      });
    });
  });

})();
