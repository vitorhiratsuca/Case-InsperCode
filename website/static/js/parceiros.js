document.addEventListener('DOMContentLoaded', function () {
    setupPartnerFilters();
    setupLogoCloud();
});

function setupLogoCloud() {
    const cloud = document.getElementById('logoCloud');
    if (!cloud) return;

    const items = cloud.querySelectorAll('.logo-cloud-item');

    items.forEach(item => {
        item.addEventListener('mouseenter', function () {
            cloud.classList.add('dimmed');

            items.forEach(i => i.classList.remove('active-focus'));
            this.classList.add('active-focus');
        });

        item.addEventListener('mouseleave', function () {
            cloud.classList.remove('dimmed');
            items.forEach(i => i.classList.remove('active-focus'));
        });
    });
}

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