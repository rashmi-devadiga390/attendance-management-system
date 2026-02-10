document.addEventListener("DOMContentLoaded", () => {
    const circles = document.querySelectorAll(".progress-circle, .mini-circle, .big-circle");

    circles.forEach(circle => {
        const percent = parseInt(circle.dataset.percent) || 0;
        const degree = percent * 3.6;

        circle.style.background =
            `conic-gradient(#7a72ff ${degree}deg, #e6e6e6 ${degree}deg)`;

        const text = circle.querySelector(".percent-text");
        if (text) text.innerText = percent + "%";
    });

const progressBars = document.querySelectorAll(".today-progress");

progressBars.forEach(el => {
    const percent = parseInt(el.dataset.percent) || 0;

    const circle = el.querySelector(".progress");
    const radius = 45;   
    const circumference = 2 * Math.PI * radius;

    circle.style.strokeDasharray = circumference;
    circle.style.strokeDashoffset =
        circumference - (percent / 100) * circumference;

    if (percent >= 75) {
        circle.style.stroke = "#28a745";   
    } else if (percent >= 40) {
        circle.style.stroke = "#ffc107";   
    } else {
        circle.style.stroke = "#dc3545";   
    }
});

});
