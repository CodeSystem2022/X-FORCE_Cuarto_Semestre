document.addEventListener("DOMContentLoaded", () => {
    const buttons = document.querySelectorAll(".no-nullButton");
    const inputs = document.querySelectorAll(".no-nullInput");
    var partName = document.target.getAttribute('numAmount');

    buttons.forEach(button => {
        button.addEventListener("click", (e) => {
            for (const index of inputs) {
                if (index.value == null || index.value.trim() === "") {
                    e.preventDefault();
                    return;
                }
            }
        });
    });






});