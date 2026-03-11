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

    // 🔥 Número de camadas baseado na raiz
    const layers = Math.ceil(Math.sqrt(total));

    // 🔥 Altura dinâmica baseada nas camadas
    const rowSpacing = 120;
    const paddingTop = 60;
    const paddingBottom = 20;

    const dynamicHeight =
        paddingTop +
        layers * rowSpacing +
        paddingBottom;

    cloud.style.height = dynamicHeight + "px";

    const centerX = width / 2;
    const topOffset = paddingTop;

    // 🔥 Distribuição progressiva (1,2,3,...)
    let distribution = [];
    for (let i = 1; i <= layers; i++) {
        distribution.push(i);
    }

    // 🔥 Ajusta proporcionalmente ao total
    const sumWeights = distribution.reduce((a, b) => a + b, 0);

    distribution = distribution.map(w =>
        Math.max(1, Math.round((w / sumWeights) * total))
    );

    // 🔥 Corrige diferença para bater exatamente com total
    let currentSum = distribution.reduce((a, b) => a + b, 0);

    while (currentSum > total) {
        for (let i = 0; i < distribution.length && currentSum > total; i++) {
            if (distribution[i] > 1) {
                distribution[i]--;
                currentSum--;
            }
        }
    }

    while (currentSum < total) {
        distribution[distribution.length - 1]++;
        currentSum++;
    }

    // 🔥 Garante que base sempre tenha mais que a camada acima
    for (let i = 0; i < distribution.length - 1; i++) {
        if (distribution[i] >= distribution[i + 1]) {
            distribution[i + 1] = distribution[i] + 1;
        }
    }

    const minCount = Math.min(...distribution);
    const maxCount = Math.max(...distribution);

    let index = 0;

    distribution.forEach((count, layerIndex) => {

        const y = topOffset + layerIndex * rowSpacing;

        const layerWidth = width * (0.25 + layerIndex * 0.08);
        const startX = centerX - layerWidth / 2;

        for (let i = 0; i < count && index < total; i++) {

            let x;

            if (count === 1) {
                x = centerX;
            } else {
                x = startX + (i / (count - 1)) * layerWidth;
            }

            // 🔥 Camada com menos itens = maior logo
            const normalized =
                (1 - ((count - minCount) / (maxCount - minCount || 1)));

            const scale =
                1.4 + normalized * 0.5;

            const randomX = (Math.random() - 0.5) * 20;
            const randomY = (Math.random() - 0.5) * 10;

            const item = items[index];

            item.style.position = "absolute";
            item.style.left = (x + randomX) + "px";
            item.style.top = (y + randomY) + "px";
            item.style.transform = `translate(-50%, -50%) scale(${scale})`;
            item.style.zIndex = 100 - count;

            index++;
        }
    });
}