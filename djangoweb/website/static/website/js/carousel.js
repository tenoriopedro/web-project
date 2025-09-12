document.addEventListener("DOMContentLoaded", () => {
    const track = document.getElementById("track");
    const slides = Array.from(track.children);
    const prevBtn = document.getElementById("prevBtn");
    const nextBtn = document.getElementById("nextBtn");
    const dotsContainer = document.getElementById("dots");
    let index = 0;

    function getSlideWidth() {
        const screenWidth = window.innerWidth;
        
        if (screenWidth <= 768) {
            return 100; 
        } else if (screenWidth <= 1024) {
            return 50;
        } else {
            return 35; 
        }
    }

    function updateSlideStyles() {
        const slideWidth = getSlideWidth();
        
        slides.forEach(slide => {
            slide.style.flex = `0 0 ${slideWidth}%`;
            slide.style.maxWidth = `${slideWidth}%`;
        });
        
        return slideWidth;
    }

    function createDots() {
        dotsContainer.innerHTML = '';
        
        const slideWidthValue = updateSlideStyles();
        const trackWidth = track.offsetWidth;
        const visibleSlides = Math.floor(
            trackWidth / (trackWidth * slideWidthValue / 100));
        const maxIndex = Math.max(0, slides.length - visibleSlides);
        
        for (let i = 0; i <= maxIndex; i++) {
            const dot = document.createElement("span");
            dot.classList.add("dot");
            if (i === 0) dot.classList.add("active");
            dot.addEventListener("click", () => goToSlide(i));
            dotsContainer.appendChild(dot);
        }

        return maxIndex
    }

    function goToSlide(i){

        index = i;
        updateCarousel();
    }

    function updateCarousel() {
        const slideWidtValueh = updateSlideStyles();
        const trackWidth = track.offsetWidth;
        const slideWidth = trackWidth * slideWidtValueh / 100;
        const visibleSlides = Math.floor(trackWidth / slideWidth);

        const maxIndex = Math.max(0, slides.length - visibleSlides);

        if (index < 0) {
            index = maxIndex;
        } else if (index > maxIndex) {
            index = 0; 
        }

        track.style.transform = `translateX(-${index * slideWidth}px)`;

        const dots = Array.from(dotsContainer.children);
        dots.forEach((dot, i) => {
            dot.classList.toggle("active", i === index);
        });
    }

    prevBtn.addEventListener("click", () => goToSlide(index - 1));
    nextBtn.addEventListener("click", () => goToSlide(index + 1));

    let resizeTimeout;
    window.addEventListener("resize", () => {
        clearTimeout(resizeTimeout);
        resizeTimeout = setTimeout(() => {
            createDots();
            updateCarousel();
        }, 250);
    });

    createDots();
    updateCarousel();

    // setInterval(() => updateSlide(index + 1), 5000);
});