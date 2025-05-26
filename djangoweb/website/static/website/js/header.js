document.addEventListener('DOMContentLoaded', () => {
    const hamburger = document.querySelector('.hamburger');
    const navMobile = document.querySelector('.nav-mobile');
    const dropdownToggles = document.querySelectorAll('.dropdown-toggle');

    // Função para verificar o tamanho da tela
    function handleResponsiveMenu() {
        const isMobileMenu = window.innerWidth <= 768;
        const isTablet = window.innerWidth <= 1024;
        
        if (!isMobileMenu) {
            hamburger.setAttribute('aria-expanded', 'false');
            navMobile.setAttribute('data-visible', 'false');
            document.body.style.overflow = 'auto';
        }

        dropdownToggles.forEach(toggle => {
            toggle.removeEventListener('click', handleDropdownToggle);
            
            if (isTablet) {
                toggle.addEventListener('click', handleDropdownToggle);
                // Previne o redirecionamento do link
                toggle.addEventListener('click', (e) => {
                    if (toggle.nextElementSibling) {
                        e.preventDefault();
                    }
                });
            }
        });
    }

    function handleDropdownToggle(e) {
        
        if (window.innerWidth > 1024) return;
        
        const submenu = this.nextElementSibling;
        
        if (submenu) {
            // Fecha outros dropdowns abertos
            document.querySelectorAll('.dropdown-menu.open').forEach(openMenu => {
                if (openMenu !== submenu) {
                    openMenu.classList.remove('open');
                    openMenu.previousElementSibling?.classList.remove('open');
                }
            });
            
            // Alterna o dropdown atual
            submenu.classList.toggle('open');
            this.classList.toggle('open');
        }
    }

    hamburger.addEventListener('click', () => {
        if (window.innerWidth > 768) return;
        
        const isExpanded = hamburger.getAttribute('aria-expanded') === 'true';
        hamburger.setAttribute('aria-expanded', !isExpanded);
        navMobile.setAttribute('data-visible', !isExpanded);
        
        // Fecha todos os dropdowns quando o menu mobile é fechado
        if (isExpanded) {
            document.querySelectorAll('.dropdown-menu.open').forEach(menu => {
                menu.classList.remove('open');
                menu.previousElementSibling?.classList.remove('open');
            });
        }
    });

    // Fecha dropdowns ao clicar fora (abaixo de 1024px)
    document.addEventListener('click', (e) => {
        if (window.innerWidth > 1024) return;
        
        const isDropdownToggle = e.target.matches('.dropdown-toggle') || 
                               e.target.closest('.dropdown-toggle');
        const isInDropdown = e.target.closest('.dropdown-menu');
        
        if (!isDropdownToggle && !isInDropdown) {
            document.querySelectorAll('.dropdown-menu.open').forEach(menu => {
                menu.classList.remove('open');
                menu.previousElementSibling?.classList.remove('open');
            });
        }
    });

    // Verifica ao carregar a página
    handleResponsiveMenu();

    // Verifica quando a janela é redimensionada
    window.addEventListener('resize', handleResponsiveMenu);
});