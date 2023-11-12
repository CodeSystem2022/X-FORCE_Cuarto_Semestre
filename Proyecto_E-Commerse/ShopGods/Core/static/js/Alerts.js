document.addEventListener("DOMContentLoaded", () => {
  console.log("alertas cargadas")

const nullAlert = document.querySelector("#alert");
const inputList = document.querySelectorAll('.no-nullInput');
const deleteButtons = document.querySelectorAll(".delete");
const deleteItem = document.querySelectorAll('.delete-item');
const deleteProduct = document.querySelectorAll(".deleteproduct");
const form = document.querySelector("#formItem");

  

if (nullAlert.value==1){
  alert("fuiste redirigido/a porque se intentó vulnerar el formulario. Estas a salvo :D")
}

if (form) {
  form.addEventListener("submit", (e) => {
    var missing = false;
    inputList.forEach(input => {
      if (!input.value.trim()) {
        e.preventDefault();
        missing = true;
      }
    });
    if (missing) {
      alert("Faltan asignar valores");
    }
  });
}


deleteButtons.forEach(button => {
    button.addEventListener("click", (e) => {
      const confirmation = confirm("¿Seguro de eliminar la cuenta?");
      if (!confirmation) {
        e.preventDefault();
      }
    });
  });
  
  deleteProduct.forEach(button => {
  button.addEventListener("click", (e) => {
    const confirmation = confirm("¿Seguro de eliminar TODO el producto?");
    if (!confirmation) {
      e.preventDefault();
    }
  });
});

deleteItem.forEach(index => {
  index.addEventListener("click", (e) => {
    const confirmation = confirm("¿Seguro de eliminar el item seleccionado?");
    if (!confirmation) {
      e.preventDefault();
    }
  });
});

});


