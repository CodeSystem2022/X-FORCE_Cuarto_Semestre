const btn = document.querySelector('.btn-neon-black');
const img1 = document.querySelector('.fa-solid');
const img2 = document.querySelector('.fa-solid');
let isClicked = false;

btn.addEventListener('click', () => {
    if (!isClicked) {
        img1.classList.add('fa-sun');
        img1.classList.add('fa-moon');
        img2.classList.remove('fa-moon');
        img2.classList.add('fa-sun');
        img2.style.color = '#e5a315';
        document.documentElement.style.setProperty('--Sombras', '#cc3333');
        document.documentElement.style.setProperty('--SombraNeon', '#eed48c');
        document.documentElement.style.setProperty('--ColorPrimario', '#ececec');
        document.documentElement.style.setProperty('--ColorTerciario', 'rgb(145, 3, 3)');
        document.documentElement.style.setProperty('--Fondo', ' #1c1c1c');
        document.documentElement.style.setProperty('--FondoBody', '#0f0f0f');
    } else {
        img1.classList.remove('fa-moon');
        img1.classList.add('fa-sun');
        img2.classList.remove('fa-sun');
        img2.classList.add('fa-moon');
        // Restaura el color original
        document.documentElement.style.setProperty('--Sombras', '#0f0f0f');
        document.documentElement.style.setProperty('--SombraNeon', '#0e0024');
        document.documentElement.style.setProperty('--ColorPrimario', 'rgb(20, 20, 20)')
        document.documentElement.style.setProperty('--ColorTerciario', 'rgb(0, 217, 255)')
        document.documentElement.style.setProperty('--Fondo', ' #e1e1e1');
        document.documentElement.style.setProperty('--FondoBody', '#ffffff');
        img2.style.color = '#dbadf0';
    }
    isClicked = !isClicked;
});


--FondoBody