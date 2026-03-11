document.addEventListener('DOMContentLoaded', function () {
    setupPartnerFilters();
});


function setupPartnerFilters() {
    const filterBtns = document.querySelectorAll('.filter-btn');
    const partnerCards = document.querySelectorAll('.partner-card');

    filterBtns.forEach(btn => {
        btn.addEventListener('click', function () {
            const filter = this.dataset.filter;

            filterBtns.forEach(b => b.classList.remove('active'));
            this.classList.add('active');

            partnerCards.forEach(card => {
                const category = card.dataset.category;

                if (filter === 'all' || category === filter) {
                    card.style.display = 'block';
                } else {
                    card.style.display = 'none';
                }
            });
        });
    });
}