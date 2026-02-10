document.addEventListener("DOMContentLoaded", () => {
    const circle = document.querySelector(".progress");
    const percent = document.querySelector(".circle-progress").dataset.percent;
    const radius = 75;
    const circumference = 2 * Math.PI * radius;
    const offset = circumference - (percent / 100) * circumference;

    circle.style.strokeDashoffset = offset;

});
