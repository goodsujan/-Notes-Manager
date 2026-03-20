/**
 * color_preview.js
 * Updates the card preview box whenever the color picker value changes.
 */
(function () {
  'use strict';

  function initColorPreview() {
    const picker  = document.getElementById('color-picker');
    const preview = document.getElementById('color-preview');
    if (!picker || !preview) return;

    function applyColor(hex) {
      preview.style.background    = hex;
      preview.style.borderColor   = hex;
      preview.querySelector('.preview-label').textContent = hex.toUpperCase();
    }

    // Set initial state
    applyColor(picker.value || '#f9f9f9');

    // Live update
    picker.addEventListener('input', function () {
      applyColor(this.value);
    });
  }

  document.addEventListener('DOMContentLoaded', initColorPreview);
})();
