CREATE DATABASE h2o;

CREATE TABLE Participante (
    id int NOT NULL AUTO_INCREMENT,
    localizacion varchar(30) NOT NULL,
    correo varchar(50) NOT NULL,
    PRIMARY KEY (id) 
);