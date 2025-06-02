document.addEventListener("DOMContentLoaded", () => {
    const whatsappBtn = document.getElementById("whatsappFloat");
    const tooltip = document.getElementById("whatsappTooltip");
    const phrases = [
        "Precisa de ajuda?",
        "Fale com a gente!",
       /* "Atendimento rápido aqui",
        "Clique e chame no Whatsapp",
        "Estamos prontos pare te atender!"*/
    ];
    let shown = false;
    let currentPhrase = 0;
    let phraseInterval = null;

    const span = document.createElement("span");
    tooltip.innerHTML = "";
    tooltip.appendChild(span);

    function rotatePhrases() {
        phraseInterval = setInterval(() => {
            span.classList.remove("show");

            setTimeout(() => {
                currentPhrase = (currentPhrase + 1) % phrases.length;
                span.textContent = phrases[currentPhrase];
                span.classList.add("show");
            }, 300);
        }, 3000);
    }

    function stopRotation() {
        clearInterval(phraseInterval);
        phraseInterval = null;
    }

    function triggerAttention() {
        if (shown) return;
        shown = true;

        // Animação pulsante
        whatsappBtn.classList.add("pulse");
        tooltip.classList.add("show");
        span.textContent = phrases[0];
        span.classList.add("show");

        rotatePhrases();

        // Remove Tooltip
        setTimeout(() => {
            tooltip.classList.remove("show");
            // stopRotation();
        }, 6000);
    }

    // Gatilho por scroll
    window.addEventListener("scroll", () => {
        if (window.scrollY > window.innerHeight * 0.4) {
            triggerAttention();
        }
    });

    // Fallback por tempo(usuário não rolou)
    setTimeout(() => {
        triggerAttention();
    }, 7000);

});