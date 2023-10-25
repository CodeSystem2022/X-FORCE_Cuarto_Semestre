-- Este archivo hace referencia a la base de datos o al script sql que vamos a utilizar
CREATE TABLE tareas (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(255) UNIQUE NOT NULL,
    descripcion TEXT,
);