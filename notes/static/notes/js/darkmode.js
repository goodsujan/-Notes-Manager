document.addEventListener("DOMContentLoaded", function () {
  const toggleBtn = document.getElementById("themeToggle");
  const body = document.body;

  function updateBtnText() {
    if (toggleBtn) {
      if (body.classList.contains("dark-mode")) {
        toggleBtn.textContent = "☀ Light Mode";
      } else {
        toggleBtn.textContent = "🌙 Dark Mode";
      }
    }
  }

  // Load saved theme
  if (localStorage.getItem("theme") === "dark") {
    body.classList.add("dark-mode");
  }
  updateBtnText();

  // Toggle theme
  if (toggleBtn) {
    toggleBtn.addEventListener("click", () => {
      body.classList.toggle("dark-mode");

      if (body.classList.contains("dark-mode")) {
        localStorage.setItem("theme", "dark");
      } else {
        localStorage.setItem("theme", "light");
      }
      updateBtnText();
    });
  }
});
