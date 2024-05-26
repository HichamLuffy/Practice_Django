window.addEventListener('scroll', function() {
    let cd = document.getElementById('cd');
    let rotation = window.scrollY / 5;
    cd.style.transform = `rotate(${rotation}deg)`;

    // Optionally, change text for the next section
    let sections = document.querySelectorAll('.section');
    sections.forEach((section, index) => {
        let rect = section.getBoundingClientRect();
        if (rect.top <= window.innerHeight / 2 && rect.bottom >= window.innerHeight / 2) {
            cd.alt = section.id;  // Update the alt text or some other identifier
        }
    });
});

let isDragging = false;
let lastMouseY = 0;

const cd = document.getElementById('cd');

cd.addEventListener('mousedown', (e) => {
    isDragging = true;
    lastMouseY = e.clientY;
    document.body.style.cursor = 'grabbing';
});

document.addEventListener('mouseup', () => {
    isDragging = false;
    document.body.style.cursor = 'default';
});

document.addEventListener('mousemove', (e) => {
    if (isDragging) {
        let deltaY = e.clientY - lastMouseY;
        window.scrollBy(0, deltaY);
        lastMouseY = e.clientY;
    }
});
