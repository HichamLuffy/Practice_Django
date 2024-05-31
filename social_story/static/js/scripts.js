document.addEventListener('DOMContentLoaded', () => {
    const sections = document.querySelectorAll('.section');
    const sectionArray = Array.from(sections);
    let isScrolling = false;

    // IntersectionObserver to add 'visible' class
    const options = {
        root: null,
        threshold: 0.5
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            } else {
                entry.target.classList.remove('visible');
            }
        });
    }, options);

    sections.forEach(section => {
        observer.observe(section);
    });

    const scrollToSection = (index) => {
        if (index >= 0 && index < sectionArray.length) {
            isScrolling = true;
            sectionArray[index].scrollIntoView({
                behavior: 'smooth'
            });
            setTimeout(() => isScrolling = false, 1000); // Adjust timeout as needed
        }
    };

    let currentSectionIndex = 0;

    // Event listeners for arrow clicks
    document.querySelector('.left-arrow').addEventListener('click', () => {
        if (isScrolling) return;
        currentSectionIndex = Math.max(currentSectionIndex - 1, 0);
        scrollToSection(currentSectionIndex);
    });

    document.querySelector('.right-arrow').addEventListener('click', () => {
        if (isScrolling) return;
        currentSectionIndex = Math.min(currentSectionIndex + 1, sectionArray.length - 1);
        scrollToSection(currentSectionIndex);
    });

    // Keyboard support for arrow keys
    window.addEventListener('keydown', (event) => {
        if (isScrolling) return;

        if (event.key === 'ArrowRight') {
            currentSectionIndex = Math.min(currentSectionIndex + 1, sectionArray.length - 1);
            scrollToSection(currentSectionIndex);
        } else if (event.key === 'ArrowLeft') {
            currentSectionIndex = Math.max(currentSectionIndex - 1, 0);
            scrollToSection(currentSectionIndex);
        }
    });
});
