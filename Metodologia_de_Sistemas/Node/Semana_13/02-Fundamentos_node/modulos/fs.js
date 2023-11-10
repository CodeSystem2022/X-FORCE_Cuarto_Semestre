// traemos el módulo de file system
// sirve para trabajar y manipular archivos de nuestro sistema

const fs = require('fs'); //ya viene instalado en el core de Node

//Primero leemos el archivo.txt
function leer(ruta, cb){
    fs.readFile(ruta, (err, data) => {
        cb(data.toString());
    
    
    })
}

leer(`${__dirname}/archivo.txt`, console.log); //Sintaxis ES6