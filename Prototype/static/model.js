// dark theme toggle implementation
const themeIcon = document.querySelector("#dark-theme i");
const currentTheme = localStorage.getItem("theme") || "light";

if (currentTheme === "dark") {
  document.body.classList.add("dark");
  themeIcon.classList.add("ri-moon-line");
} else {
  themeIcon.classList.add("ri-sun-line");
}

themeIcon.parentElement.addEventListener("click", () => {
  document.body.classList.toggle("dark");

  // Toggle icons based on the current theme
  if (document.body.classList.contains("dark")) {
    themeIcon.classList.remove("ri-sun-line");
    themeIcon.classList.add("ri-moon-line");
    document.querySelector(".logo-image").src =
      "./assets/images/icons/icon-white.svg";
    localStorage.setItem("theme", "dark");
  } else {
    themeIcon.classList.remove("ri-moon-line");
    themeIcon.classList.add("ri-sun-line");
    document.querySelector(".logo-image").src =
      "./assets/images/icons/icon-black.svg";
    localStorage.setItem("theme", "light");
  }
});
