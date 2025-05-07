    let lastScrollY = 0;
    const bottomHeader = document.querySelector('.bottom-header');

    window.addEventListener('scroll', () => {
        const currentScrollY = window.scrollY;

        if (currentScrollY > lastScrollY) {
            bottomHeader.classList.add('visible');
        } else {
            bottomHeader.classList.remove('visible');
        }

        lastScrollY = currentScrollY;
    });