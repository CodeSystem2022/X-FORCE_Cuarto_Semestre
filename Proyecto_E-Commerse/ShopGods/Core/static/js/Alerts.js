
const inputList = document.querySelectorAll('input');
const deleteButtons = document.querySelectorAll(".delete");

deleteButtons.forEach(button => {
    button.addEventListener("click", (e) => {
      const confirmation = confirm("¿Seguro de eliminar la cuenta?");
      if (!confirmation) {
        e.preventDefault();
      }
    });
  });