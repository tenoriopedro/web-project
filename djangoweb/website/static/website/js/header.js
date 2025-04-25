document.addEventListener('DOMContentLoaded', () => {
    const hamburger = document.querySelector('.hamburger');
    const navMobile = document.querySelector('.nav-mobile');
    const dropdownToggles = document.querySelectorAll('.nav-mobile .dropdown-toggle');

    // Controle do menu hambúrguer
    hamburger.addEventListener('click', () => {
        const isExpanded = hamburger.getAttribute('aria-expanded') === 'true';
        hamburger.setAttribute('aria-expanded', !isExpanded);
        navMobile.setAttribute('data-visible', !isExpanded);
        document.body.style.overflow = isExpanded ? 'auto' : 'hidden';
    });

    // Dropdown mobile (por clique)
    dropdownToggles.forEach(toggle => {
        toggle.addEventListener('click', (e) => {
            e.preventDefault();
            const parent = toggle.parentElement;
            parent.classList.toggle('active');
        });
    });
});