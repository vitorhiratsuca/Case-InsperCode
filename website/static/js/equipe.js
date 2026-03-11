document.addEventListener('DOMContentLoaded', function () {
    animateStats();
});

function animateStats() {
    const numbers = document.querySelectorAll('.stat-number');

    numbers.forEach(el => {
        const text = el.textContent.trim();
        // If it's a date (contains '/'), do typing animation
        if (text.includes('/')) {
            let currentText = '';
            let index = 0;
            const typer = setInterval(() => {
                currentText += text[index];
                el.textContent = currentText;
                index++;
                if (index >= text.length) {
                    clearInterval(typer);
                }
            }, 50);
            return;
        }

        // For numbers, animate counting with '+'
        const finalValue = parseInt(text.replace('+', ''));
        if (isNaN(finalValue)) return; // Skip if not a number

        let current = 0;
        const increment = Math.ceil(finalValue / 30);

        const counter = setInterval(() => {
            current += increment;

            if (current >= finalValue) {
                el.textContent = '+' + finalValue;
                clearInterval(counter);
            } else {
                el.textContent = '+' + current;
            }
        }, 30);
    });
}