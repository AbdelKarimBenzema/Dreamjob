CREATE DATABASE IF NOT EXISTS DREAM;
USE DREAM;
CREATE TABLE usuarios(
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    apellido1 VARCHAR(255) NOT NULL,
    apellido2 VARCHAR(255) NOT NULL,
    fechanacimiento DATE NOT NULL,
);
CREATE TABLE SECTORES(
	usuario VARCHAR(100) NOT NULL PRIMARY KEY,
    clave VARCHAR(255) NOT NULL,
);

INSERT INTO `usuarios` (`nombre`, `apellido1`, `apellido2`, `fechanacimiento`) VALUES ('root', 'root', 'root', '2022-03-01');
