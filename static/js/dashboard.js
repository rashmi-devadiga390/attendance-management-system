document.addEventListener("DOMContentLoaded", () => {
    const circles = document.querySelectorAll(".mini-circle");

    circles.forEach(circle => {
        const percent = parseInt(circle.dataset.percent) || 0;
        const degree = percent * 3.6;

        let color = "#dc3545";   

        if (percent >= 75) color = "#28a745";       
        else if (percent >= 50) color = "#ff9800";  
        else color = "#dc3545";                    

        circle.style.background =
            `conic-gradient(${color} ${degree}deg, #e6e6e6 ${degree}deg)`;
        circle.innerHTML = `<span>${percent}%</span>`;
    });

    const numbers = document.querySelectorAll(".sum-card p");

    numbers.forEach(el => {
        const finalValue = parseFloat(el.innerText);

        if (isNaN(finalValue)) return;

        let current = 0;
        const duration = 800;
        const step = finalValue / (duration / 16);

        const counter = setInterval(() => {
            current += step;
            if (current >= finalValue) {
                el.innerText = finalValue;
                clearInterval(counter);
            } else {
                el.innerText = Math.floor(current);
            }

        }, 16);
    });
});
