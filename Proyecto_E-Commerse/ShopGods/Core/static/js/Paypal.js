//-----------------NO TOCAR-----------------------//
//-----------------NO TOCAR-----------------------//
//-----------------NO TOCAR-----------------------//
//-----------------NO TOCAR-----------------------//


document.addEventListener("DOMContentLoaded", () => {
    
    
    const elementosConIdClient = document.querySelectorAll('[id-client]');
    const payButton = document.querySelectorAll('.pay-button');

    var mid = ""


    var idClient = ""

    payButton.forEach(button => {       //muestra u oculta los botones, tambien pasa el ID
        
        button.addEventListener('click', function(e) {

            payButton.forEach(button => {
            button.firstChild.nodeValue = "Comprar producto";
            })

            elementosConIdClient.forEach(button => {
                button.style.display="none"
            })


            const idClientElement = button.querySelector('[id-client]');
            if (idClientElement) {
            const idClientValue = idClientElement.getAttribute('id-client');
            console.log(idClientValue);

            // Cambiar el src del script de PayPal
            changePayPalScriptSrc(mid);
            const currentDisplayStyle = idClientElement.style.display;

            mid = idClientValue;



            // Cambiar el estilo del elemento dentro del botón
            idClientElement.style.display = currentDisplayStyle === 'none' ? 'block' : 'none';
            button.firstChild.nodeValue = "";
        }
          
    });
              
});

    function changePayPalScriptSrc(idClient) {
        const existingScript = document.querySelector('.una-variable-mas');
        const newScript = document.createElement('script');
        
        newScript.classList.add('una-variable-mas');
        newScript.src = `https://www.paypal.com/sdk/js?client-id=${idClient}&currency=USD`;

        console.log("entro a la funcion una-variable-mas")
        console.log(newScript.src)
    
        existingScript.parentNode.replaceChild(newScript, existingScript);
    }

});