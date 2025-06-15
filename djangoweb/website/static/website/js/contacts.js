document.addEventListener('DOMContentLoaded', function () {
    const copyButton = document.querySelector('.copy-email-button');
    const emailText = document.querySelector('.email-text');
    const feedback = document.querySelector('.copy-feedback');

    if (copyButton && emailText && feedback) {
        copyButton.addEventListener('click', function () {
            const text = emailText.textContent.trim();

            navigator.clipboard.writeText(text).then(function () {

                feedback.classList.add('visible');

                setTimeout(() => {
                    feedback.classList.remove('visible');
                }, 2000);
            }).catch(function (err) {
            console.error('Erro ao copiar email: ', err);
            });
        });
    }
});