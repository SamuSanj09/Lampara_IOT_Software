document.addEventListener('scroll', function() {
    const elementos = document.querySelectorAll('.grafico');
    elementos.forEach(el => {
        if (el.getBoundingClientRect().top < window.innerHeight) {
            el.classList.add('visible');
        }
    });
});
