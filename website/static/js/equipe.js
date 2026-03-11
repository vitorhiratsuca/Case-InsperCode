window.addEventListener("load", function () {
    positionLogos();
    window.addEventListener("resize", positionLogos);
});

function positionLogos() {
    const cloud = document.getElementById("logoCloud");
    if (!cloud) return;

    const items = Array.from(cloud.querySelectorAll(".logo-cloud-item"));
    const total = items.length;
    if (total === 0) return;

    const width = cloud.clientWidth;
    const height = cloud.clientHeight;

    const centerX = width / 2;
    const startY = height * 0.25;

    // Define quantas "linhas" terá
    const rows = Math.ceil(Math.sqrt(total));
    let index = 0;

    for (let r = 0; r < rows; r++) {

        const itemsInRow = r + 1; // 1 em cima, 2 depois, 3 depois...
        const rowWidth = itemsInRow * 120;
        const rowStartX = centerX - rowWidth / 2;

        for (let c = 0; c < itemsInRow && index < total; c++) {

            const item = items[index];

            const randomOffsetX = (Math.random() - 0.5) * 30;
            const randomOffsetY = (Math.random() - 0.5) * 20;

            const x = rowStartX + c * 120 + randomOffsetX;
            const y = startY + r * 90 + randomOffsetY;

            const scale = 0.8 + Math.random() * 0.4; // variação de tamanho

            item.style.position = "absolute";
            item.style.left = x + "px";
            item.style.top = y + "px";
            item.style.transform = `translate(-50%, -50%) scale(${scale})`;

            index++;
        }
    }
}