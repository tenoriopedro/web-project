document.addEventListener('DOMContentLoaded', () => {
    const hamburger = document.querySelector('.hamburger');
    const navMobile = document.querySelector('.nav-mobile');
    const dropdownToggles = document.querySelectorAll('.dropdown-toggle');

    // Function to check screen size
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
                // Prevents link redirection
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
            // Closes other open dropdowns
            document.querySelectorAll('.dropdown-menu.open').forEach(openMenu => {
                if (openMenu !== submenu) {
                    openMenu.classList.remove('open');
                    openMenu.previousElementSibling?.classList.remove('open');
                }
            });
            
            // Toggles the current dropdown
            submenu.classList.toggle('open');
            this.classList.toggle('open');
        }
    }

    hamburger.addEventListener('click', () => {
        if (window.innerWidth > 768) return;
        
        const isExpanded = hamburger.getAttribute('aria-expanded') === 'true';
        hamburger.setAttribute('aria-expanded', !isExpanded);
        navMobile.setAttribute('data-visible', !isExpanded);
        
        // Closes all dropdowns when the mobile menu is closed
        if (isExpanded) {
            document.querySelectorAll('.dropdown-menu.open').forEach(menu => {
                menu.classList.remove('open');
                menu.previousElementSibling?.classList.remove('open');
            });
        }
    });

    // Close dropdowns on click outside (below 1024px)
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

    // Check when loading the page
    handleResponsiveMenu();

    // Check when loading the page
    window.addEventListener('resize', handleResponsiveMenu);
});