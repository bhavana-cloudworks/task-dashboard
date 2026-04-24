<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

<script>
function createSparkline(canvasId, data, color) {
    const ctx = document.getElementById(canvasId).getContext('2d');

    const gradient = ctx.createLinearGradient(0, 0, 0, 40);
    gradient.addColorStop(0, color + "55");
    gradient.addColorStop(1, color + "00");

    new Chart(ctx, {
        type: 'line',
        data: {
            labels: data.map((_, i) => i),
            datasets: [{
                data: data,
                borderColor: color,
                borderWidth: 2,
                fill: true,
                backgroundColor: gradient,
                pointRadius: 0,
                tension: 0.4
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { display: false },
                tooltip: { enabled: false }
            },
            scales: {
                x: { display: false },
                y: { display: false }
            }
        }
    });
}

/* =========================
   INIT ALL SPARKLINES
========================= */
window.onload = function () {

    createSparkline("chartTotal", [4, 6, 5, 8, 7, 10], "#7c3aed");
    createSparkline("chartCompleted", [1, 2, 3, 2, 4, 5], "#14b8a6");
    createSparkline("chartOnTime", [60, 62, 65, 70, 68, 75], "#f97316");
    createSparkline("chartState", [1, 2, 1, 3, 2, 4], "#22c55e");

};
</script>