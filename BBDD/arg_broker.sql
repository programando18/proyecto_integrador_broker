CREATE DATABASE arg_broker; 
USE arg_broker; 

CREATE TABLE inversores (
    id_inversor INT PRIMARY KEY AUTO_INCREMENT,
    cuit VARCHAR(11) NOT NULL,  
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    contraseña VARCHAR(100) NOT NULL,
    saldo FLOAT DEFAULT 0,  
    fecha_alta DATE,
    pregunta_secreta VARCHAR(100), 
    respuesta_secreta VARCHAR(100)
);

CREATE TABLE acciones (
    id_accion INT PRIMARY KEY AUTO_INCREMENT,
    simbolo VARCHAR(10) NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    precio_compra_actual FLOAT NOT NULL,
    precio_venta_actual FLOAT NOT NULL,
    cantidad INT NOT NULL
);

CREATE TABLE historico_cotizaciones (
    id_historico INT PRIMARY KEY AUTO_INCREMENT,
    fecha_cotizacion DATE NOT NULL,
    precio_compra FLOAT NOT NULL,
    precio_venta FLOAT NOT NULL,
    cantidad_venta INT NOT NULL,
    cantidad_compra INT NOT NULL,
    id_accion INT NOT NULL,
    FOREIGN KEY (id_accion) REFERENCES acciones(id_accion)
);

CREATE TABLE registro_transacciones (
    id_transaccion INT PRIMARY KEY AUTO_INCREMENT,
    id_inversor INT,
    nombre_inversor VARCHAR(100) NOT NULL,
    tipo_operacion VARCHAR(6) NOT NULL, 
    simbolo VARCHAR(10) NOT NULL,
    cantidad INT NOT NULL,
    precio_unidad FLOAT NOT NULL,
    precio_total FLOAT NOT NULL,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_inversor) REFERENCES inversores(id_inversor)
);

CREATE TABLE portafolios (
    id_portafolio INT PRIMARY KEY AUTO_INCREMENT,
    id_inversor INT,
    total_invertido FLOAT,
    saldo FLOAT,
    acciones JSON NOT NULL, 
    FOREIGN KEY (id_inversor) REFERENCES inversores(id_inversor)
);

