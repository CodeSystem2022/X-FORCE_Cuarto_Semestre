document.addEventListener("DOMContentLoaded", () => {

    var price = document.querySelector(".price");
    price = parseFloat(price.textContent);
    var amount = document.querySelector(".product-stock");
    amount = parseFloat(amount.textContent);
    const priceTotal = document.querySelector(".priceTotal");
    var numAmountInput = document.querySelector('input[name="numAmount"]');

    console.log(price)
    console.log(amount)
    console.log(priceTotal)
    console.log(numAmountInput)

    numAmountInput.addEventListener("input", () => {
        console.log("lala")
        const inputValue = parseFloat(numAmountInput.value);

        if (!isNaN(inputValue)) {
            const totalValue = inputValue * price;
            
            priceTotal.textContent = totalValue.toFixed(2); 
        } else {
            console.error("Ingrese un valor numérico válido");
        }
    });



    function validateInput() {
        const numAmountInput = document.querySelector('input[name="numAmount"]');
        const maxStock = parseInt(numAmountInput.getAttribute('max'), 10);
        const inputValue = parseInt(numAmountInput.value, 10);
    
        if (inputValue > maxStock) {
            numAmountInput.setCustomValidity('lala');
        } else {
            numAmountInput.setCustomValidity('');
        }
    
        numAmountInput.reportValidity();
    }

    function validateForm() {
        validateInput(); // Llamamos a la función de validación antes de enviar el formulario

        // Resto de la lógica de validación del formulario si es necesario

        return document.querySelector('input[name="numAmount"]').checkValidity();
    }
});