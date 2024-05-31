document.addEventListener('mousemove', (e) => {
    const { clientX: x, clientY: y } = e;
    const moveX = (x / window.innerWidth) * 2 - 1;
    const moveY = (y / window.innerHeight) * 2 - 1;

    document.querySelector('.movbk').style.transform = `translate(${moveX * 5}px, ${moveY * 5}px)`;
});

document.addEventListener('mousemove', function(e) {
    const cursor = document.querySelector('.custom-cursor');
    cursor.style.left = `${e.clientX}px`;
    cursor.style.top = `${e.clientY}px`;
});

// Generate flowers and light effects
const overlay = document.querySelector('.overlay');
const flowerCount = getComputedStyle(document.documentElement).getPropertyValue('--flower-count');

for (let i = 0; i < flowerCount; i++) {
    const flower = document.createElement('div');
    flower.classList.add('flower');
    flower.style.top = `${Math.random() * 100}%`;
    flower.style.left = `${Math.random() * 100}%`;
    overlay.appendChild(flower);
}

const light = document.createElement('div');
light.classList.add('light');
light.style.top = '20%'; // Adjust light position
light.style.left = '40%'; // Adjust light position
overlay.appendChild(light);
