CREATE DATABASE IF NOT EXISTS instituto;
USE instituto;

CREATE TABLE IF NOT EXISTS alumnos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    apellido VARCHAR(100),
    dni VARCHAR(20),
    carrera VARCHAR(100),
    anio VARCHAR(10)
);

USE instituto;
SELECT * FROM alumnos;