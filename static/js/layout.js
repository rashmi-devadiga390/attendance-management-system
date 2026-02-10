const toggleBtn = document.getElementById("toggleBtn");
const sidebar = document.getElementById("sidebar");
const main = document.getElementById("main");

toggleBtn.addEventListener("click", () => {
    sidebar.classList.toggle("closed");
    main.classList.toggle("expand");
    toggleBtn.classList.toggle("active");
});
