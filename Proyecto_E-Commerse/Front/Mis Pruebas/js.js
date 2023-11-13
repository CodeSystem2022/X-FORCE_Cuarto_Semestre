const btn = document.querySelector('.btn-neon-black');
const img1 = document.querySelector('.fa-solid');
const img2 = document.querySelector('.fa-solid');
const forms= document.querySelector(".forms"),
    pwShowhide= document.querySelectorAll(".eye-icon"),
    links= document.querySelectorAll(".link");
pwShowhide.forEach(eyeIcon =>{
    eyeIcon.addEventListener("click", ()=> {
        let pwFields = eyeIcon.parentElement.querySelectorAll(".password")
        
        pwFields.forEach(password =>{
            if(password.type === "password"){
                password.type = "text";
                eyeIcon.classList.replace("bx-hide", "bx-show");
                return;
        }
        password.type = "password";
                eyeIcon.classList.replace("bx-show", "bx-hide");
           
    })
})
links.forEach(link =>{
    link.addEventListener("click", e =>{
        e.preventDefault();
        forms.classList.toggle("show-signup");
    })
})

let isClicked = false;

btn.addEventListener('click', () => {
    
    if (!isClicked) {
        img1.classList.add('fa-sun');
        img1.classList.add('fa-moon');
        img2.classList.remove('fa-moon');
        img2.classList.add('fa-sun');
        img2.style.color = '#e5a315';
        document.documentElement.style.setProperty('--Sombras', '#d4af37');
        document.documentElement.style.setProperty('--SombraNeon', '#eed48c');
        document.documentElement.style.setProperty('--ColorPrimario', '#ececec');
        document.documentElement.style.setProperty('--ColorTerciario', 'rgb(145, 3, 3)');
        document.documentElement.style.setProperty('--Fondo', ' #1c1c1c');
        document.documentElement.style.setProperty('--FondoBody', '#0f0f0f');
        document.documentElement.style.setProperty('--FondoPerfil', ' #1c1c1c');
        document.documentElement.style.setProperty('--FondoAvatar', ' #1c1c1c');
        document.documentElement.style.setProperty('--FondoBorde', ' #0f0f0f');
        document.documentElement.style.setProperty('--SombraPerfil', 'rgb(37, 34, 25)');
        document.documentElement.style.setProperty('--ColorPortada1', '#2A132C');
        document.documentElement.style.setProperty('--ColorPortada2', '#0D1828');
        document.documentElement.style.setProperty('--ColorPortada3', '#1B0303');
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
        document.documentElement.style.setProperty('--FondoPerfil', '#ffffff');
        document.documentElement.style.setProperty('--FondoAvatar', ' #edf0f5');
        document.documentElement.style.setProperty('--FondoBorde', ' #ffffff');
        document.documentElement.style.setProperty('--SombraPerfil', 'rgb(255, 229, 209)');
        document.documentElement.style.setProperty('--ColorPortada1', 'rgb(252, 185, 185)');
        document.documentElement.style.setProperty('--ColorPortada2', 'rgb(203, 253, 174)');
        document.documentElement.style.setProperty('--ColorPortada3', 'rgb(255, 220, 130)');
        img2.style.color = '#7d1fa8';
    }
    isClicked = !isClicked;
});



})