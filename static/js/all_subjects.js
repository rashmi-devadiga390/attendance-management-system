document.querySelectorAll(".mini-circle").forEach(circle => {
    const percent = parseInt(circle.dataset.percent);
    const degree = percent * 3.6;

    let color = "#7a72ff";

    if (percent < 50) color = "#dc3545";       
    else if (percent < 75) color = "#ff9800";  
    else color = "#28a745";                   

    circle.style.background =
        `conic-gradient(${color} ${degree}deg, #eee ${degree}deg)`;
});
