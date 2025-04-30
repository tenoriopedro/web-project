document.addEventListener(
    'DOMContentLoaded', function () {
        const glide = new Glide('.glide', {
            type: 'carousel',
            autoplay: 4000,
            hoverpause: true,
            animationDuration: 800,
            perView: 1
        });
        
        glide.mount();
});