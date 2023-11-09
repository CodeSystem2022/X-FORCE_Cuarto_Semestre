document.addEventListener("DOMContentLoaded", () => {


const inputList = document.querySelectorAll('input');
const deleteButtons = document.querySelectorAll(".delete");
const deleteButtonsproduct = document.querySelectorAll(".deleteproduct");

deleteButtons.forEach(button => {
    button.addEventListener("click", (e) => {
      const confirmation = confirm("¿Seguro de eliminar la cuenta?");
      if (!confirmation) {
        e.preventDefault();
      }
    });
  });
  
  deleteButtonsproduct.forEach(button => {
  button.addEventListener("click", (e) => {
    const confirmation = confirm("¿Seguro de eliminar TODO el producto?");
    if (!confirmation) {
      e.preventDefault();
    }
  });
});

})