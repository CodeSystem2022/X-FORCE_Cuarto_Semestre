document.addEventListener("DOMContentLoaded", () => {

const nullAlert = document.querySelector(".null-alert");
const inputList = document.querySelectorAll('input');
const deleteButtons = document.querySelectorAll(".delete");
const deleteItem = document.querySelectorAll('.delete-item');
const deleteProduct = document.querySelectorAll(".deleteproduct");


if (nullAlert.value==1){
  alert("fuiste redirigido/a porque se intentó vulnerar el formulario. Estas a salvo :D")
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

deleteItem.forEach(anchor => {
  anchor.addEventListener("click", (e) => {
    const confirmation = confirm("¿Seguro de eliminar el item seleccionado?");
    if (!confirmation) {
      e.preventDefault();
    }
  });
});

})