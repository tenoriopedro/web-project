document.addEventListener('DOMContentLoaded', () => {
    const hamburger = document.querySelector('.hamburger');
    const navMobile = document.querySelector('.nav-mobile');
    const dropdownToggles = document.querySelectorAll('.nav-mobile .dropdown-toggle');

    // Função para verificar o tamanho da tela
    function handleResponsiveMenu() {
        const isMobile = window.innerWidth <= 768;
        
        if (!isMobile) {
            // Fecha o menu se a tela for maior que 768px
            hamburger.setAttribute('aria-expanded', 'false');
            navMobile.setAttribute('data-visible', 'false');
            document.body.style.overflow = 'auto';
        }
    }

    // Controle do menu hambúrguer
    hamburger.addEventListener('click', () => {
        const isExpanded = hamburger.getAttribute('aria-expanded') === 'true';
        hamburger.setAttribute('aria-expanded', !isExpanded);
        navMobile.setAttribute('data-visible', !isExpanded);
        document.body.style.overflow = isExpanded ? 'hidden' : 'auto';
    });

    // Verifica ao carregar a página
    handleResponsiveMenu();

    // Verifica quando a janela é redimensionada
    window.addEventListener('resize', handleResponsiveMenu);
});