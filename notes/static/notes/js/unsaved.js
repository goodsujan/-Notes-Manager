/**
 * unsaved.js
 * Warns the user if they try to leave a page that has unsaved form changes.
 *
 * Works automatically on any <form> that contains text inputs or textareas.
 */
document.addEventListener('DOMContentLoaded', () => {
  let formDirty = false;

  // Mark form as dirty whenever any input changes
  document.querySelectorAll('form input, form textarea, form select').forEach(el => {
    el.addEventListener('input', () => { formDirty = true; });
    el.addEventListener('change', () => { formDirty = true; });
  });

  // Clear the dirty flag when the form is intentionally submitted
  document.querySelectorAll('form').forEach(form => {
    form.addEventListener('submit', () => { formDirty = false; });
  });

  // Intercept page unload
  window.addEventListener('beforeunload', e => {
    if (formDirty) {
      const msg = 'You have unsaved changes. Are you sure you want to leave?';
      e.returnValue = msg;
      return msg;
    }
  });
});
