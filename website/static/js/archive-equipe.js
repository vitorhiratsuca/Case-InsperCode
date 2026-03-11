const cards = document.querySelectorAll('.member-card');
const noResults = document.getElementById('no-results');
const visibleCount = document.getElementById('visible-count');

let activeFilters = {
    position: 'all',
    year: 'all',
    status: 'all'
};

function applyFilters() {
    let count = 0;

    cards.forEach(card => {
        const pos = card.dataset.position;
        const year = card.dataset.year;
        const status = card.dataset.status;

        const matchPos = activeFilters.position === 'all' || pos === activeFilters.position;
        const matchYear = activeFilters.year === 'all' || year === activeFilters.year;
        const matchStatus = activeFilters.status === 'all' || status === activeFilters.status;

        if (matchPos && matchYear && matchStatus) {
            card.style.display = '';
            card.classList.remove('hidden');
            count++;
        } else {
            card.style.display = 'none';
            card.classList.add('hidden');
        }
    });

    visibleCount.textContent = count;
    noResults.style.display = count === 0 ? 'flex' : 'none';
}

document.querySelectorAll('#filter-position .pill').forEach(btn => {
    btn.addEventListener('click', () => {
        document.querySelectorAll('#filter-position .pill').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        activeFilters.position = btn.dataset.position;
        applyFilters();
    });
});

document.querySelectorAll('#filter-year .pill').forEach(btn => {
    btn.addEventListener('click', () => {
        document.querySelectorAll('#filter-year .pill').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        activeFilters.year = btn.dataset.year;
        applyFilters();
    });
});

document.querySelectorAll('#filter-status .pill').forEach(btn => {
    btn.addEventListener('click', () => {
        document.querySelectorAll('#filter-status .pill').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        activeFilters.status = btn.dataset.status;
        applyFilters();
    });
});

document.getElementById('reset-filters')?.addEventListener('click', () => {
    document.querySelectorAll('.pill').forEach(b => b.classList.remove('active'));
    document.querySelectorAll('.pill[data-position="all"], .pill[data-year="all"], .pill[data-status="all"]')
        .forEach(b => b.classList.add('active'));
    activeFilters = { position: 'all', year: 'all', status: 'all' };
    applyFilters();
});