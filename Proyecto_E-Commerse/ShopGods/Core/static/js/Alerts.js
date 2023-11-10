document.addEventListener("DOMContentLoaded", () => {


const inputList = document.querySelectorAll('input');
const deleteButtons = document.querySelectorAll(".delete");
const deleteItem = document.querySelectorAll('.delete-item');
const deleteProduct = document.querySelectorAll(".deleteproduct");

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