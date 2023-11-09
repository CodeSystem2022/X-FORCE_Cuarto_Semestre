const myElement = document.querySelector(".edit-img");

// Obtén el valor de la anchura (width) del elemento
const width = myElement.offsetWidth;

// Aplica el valor de la anchura como altura
myElement.style.height = `${width}px`;