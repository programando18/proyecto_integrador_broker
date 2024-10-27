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
    precio_compra_actual  FLOAT NOT NULL,
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

INSERT INTO acciones (simbolo, nombre, precio_compra_actual, precio_venta_actual, cantidad)
VALUES ('AAPL', 'Apple Inc.', 150.25, 152.00, 100);
INSERT INTO acciones (simbolo, nombre, precio_compra_actual, precio_venta_actual, cantidad)
VALUES ('GOOGL', 'Alphabet Inc.', 2800.75, 2825.50, 50);
INSERT INTO acciones (simbolo, nombre, precio_compra_actual, precio_venta_actual, cantidad)
VALUES ('AMZN', 'Amazon.com, Inc.', 3400.30, 3420.10, 30);
INSERT INTO acciones (simbolo, nombre, precio_compra_actual, precio_venta_actual, cantidad)
VALUES ('TSLA', 'Tesla, Inc.', 720.15, 725.40, 75);
INSERT INTO acciones (simbolo, nombre, precio_compra_actual, precio_venta_actual, cantidad)
VALUES ('MSFT', 'Microsoft Corporation', 299.90, 305.00, 200);
INSERT INTO acciones (simbolo, nombre, precio_compra_actual, precio_venta_actual, cantidad)
VALUES ('NFLX', 'Netflix, Inc.', 645.50, 650.75, 60);
INSERT INTO acciones (simbolo, nombre, precio_compra_actual, precio_venta_actual, cantidad)
VALUES ('NVDA', 'NVIDIA Corporation', 220.15, 225.30, 120);
INSERT INTO acciones (simbolo, nombre, precio_compra_actual, precio_venta_actual, cantidad)
VALUES ('FB', 'Meta Platforms, Inc.', 330.20, 335.10, 80);
INSERT INTO acciones (simbolo, nombre, precio_compra_actual, precio_venta_actual, cantidad)
VALUES ('BABA', 'Alibaba Group Holding Limited', 180.30, 185.00, 90);

