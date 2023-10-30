# Clase 09 - Python - Python en Entorno Profesional -> Parte 2
## Scrum Master Jeronimo Alvarez

---

### *Abrió:* Lunes, 20 de Octubre de 2023, 18:00
### *Cierra:* Viernes, 27 de Octubre de 2023, 23:59

---

## 📚 Temas:

- 9.1 Terminal Linux -> Comandos para iniciar Python Profesional
- Les sugiero: La carpeta a crear deben ponerle el nombre de -> py-project
- El archivo dentro de esta carpeta debe llamarse -> hello.py

- 📽 [VIDEO 1](https://drive.google.com/file/d/12fREHFPzdO7YAP5DOEJQi8ADwnR7F3s4/view)

<br>

- 9.2 Comandos para utilizar e instalar dependencias

- 📽 [VIDEO 2](https://drive.google.com/file/d/1R6h4nQ-xdu_oEBeRzcGq24Avw5yGD_MS/view)

<br>

- 9.3 Más instalaciones por hacer y extensiones para VSC

- 📽 [VIDEO 3](https://drive.google.com/file/d/1trlRI08diH1moH95TREwI9poHte5gesy/view)

<br>

- 9.4 Configuraciones, instalaciones para solucionar posibles errores

- 📽 [VIDEO 4](https://drive.google.com/file/d/1B0qJk9mXs4gAFQxpFTb7JobsUIy0Ki-n/view)

<br>

- 9.5 Como se ejecutan desde la terminal los archivos.py

- 📽 [VIDEO 5](https://drive.google.com/file/d/1AgNjUx1Y6CP5OQWD7SbRcoa4W-NuK-XX/view)

<br>

- 9.6 Creamos el repositorio en GitHub desde la terminal
- Recuerden que para crear el repositorio deben utilizar el comando -> git init
- Yo no lo utilizo porque ya lo había hecho y no lo grabe

- 📽 [VIDEO 6](https://drive.google.com/file/d/1i7RcKgK1waH3yuKab0hmAHMel8j4PxNf/view)

<br>

- 9.7 Solucionamos fallas en GitHub -> Guía y enlace desde YouTube

- 📽 [VIDEO 7](https://drive.google.com/file/d/1ACingFHHPHrjZzTLcsM25dLWthZ7Gwmi/view)

[ENLACE](https://youtu.be/YnSMYgIybFU)

<br>

En el enlace da los pasos para lograr la conexión sin problemas

comandos a agregar en la terminal mostrados en el video de YouTube:

Paso 1 -> ls -al ~/.ssh

Paso 2 -> ssh-keygen -t ed25519 -C "tu_correo@mail.com"

Paso 3 -> Enter file in which to save the key (/root/.ssh/id_ed25519):NO COLOCAR NADA SOLO ENTER

Paso 4 -> Enter passphrase (empty for no passphrase): password

Paso 5 -> Enter same passphrase again: password   => ingresamos de nuevo la contraseña

Paso 6 -> The key fingerprint is: nos genera un código personal con nuestro correo

Paso 7 -> eval `ssh-agent -s`  ingresamos este comando press enter

Paso 8 -> ssh-add ~/.ssh/id_ed25519  ingresamos este comando press enter

Paso 9 -> nos pide el password de nuevo => debemos ingresarlo luego enter

Paso 10 -> cat ~/.ssh/id_ed25519.pub   ingresar ahora este comando press enter

Paso 11 -> copy and paste en github.perfil Settings => SSH and GPG Keys 

Paso 12 -> New SSH key

Paso 13 -> Colocar un título

Paso 14 -> Pegar el código que obtuvimos desde la terminal en ubuntu => create

Paso 15 -> ahora hacemos un git push origin master o main => elegir una de las dos

Si elegiste master y era main va a crear la rama master o viceversa.


