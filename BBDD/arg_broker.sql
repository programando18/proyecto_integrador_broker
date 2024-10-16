CREATE DATABASE arg_Broker;

USE arg_Broker;

CREATE TABLE inversor (
    id_inversor INT PRIMARY KEY AUTO_INCREMENT,
    cuit VARCHAR(11) NOT NULL,  
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    contraseña VARCHAR(100) NOT NULL,
    saldo FLOAT DEFAULT 0,  
    id_contacto INT,
    id_tipo_inversor INT,
    fecha_alta DATE,
    FOREIGN KEY (id_contacto) REFERENCES Tipo_contacto(id_contacto),
    FOREIGN KEY (id_tipo_inversor) REFERENCES Tipo_inversor(id_tipo_inversor)
);


CREATE TABLE tipo_contacto (
    id_contacto INT PRIMARY KEY AUTO_INCREMENT,
    telefono VARCHAR(20),
    email VARCHAR(100) NOT NULL
);

CREATE TABLE tipo_inversor (
    id_tipo_inversor INT PRIMARY KEY AUTO_INCREMENT,
    descripcion_inversor VARCHAR(100) NOT NULL
);

CREATE TABLE acción (
    id_accion INT PRIMARY KEY AUTO_INCREMENT,
    simbolo_accion VARCHAR(10) NOT NULL,
    nombre_accion VARCHAR(100) NOT NULL,
    ultimo_operando FLOAT NOT NULL,
    precio_venta_actual FLOAT NOT NULL
);

CREATE TABLE historico_cotizaciones (
    id_historico INT PRIMARY KEY AUTO_INCREMENT,
    id_accion INT,
    fecha_cotizacion DATE NOT NULL,
    precio_compra FLOAT NOT NULL,
    precio_venta FLOAT NOT NULL,
    FOREIGN KEY (id_accion) REFERENCES Accion(id_accion)
);

CREATE TABLE portafolio (
    id_portafolio INT PRIMARY KEY AUTO_INCREMENT,
    id_inversor INT,
    id_accion INT,
    cantidad_acciones INT NOT NULL,
    rendimiento FLOAT,
    total_invertido FLOAT,
    saldo FLOAT,
    FOREIGN KEY (id_inversor) REFERENCES Inversor(id_inversor),
    FOREIGN KEY (id_accion) REFERENCES Accion(id_accion)
);

CREATE TABLE transaccion (
    id_transaccion INT PRIMARY KEY AUTO_INCREMENT,
    id_inversor INT,
    id_accion INT,
    tipo_operacion VARCHAR(6) NOT NULL,  -- "compra" o "venta"
    fecha DATE NOT NULL,
    monto FLOAT NOT NULL,
    comisión FLOAT NOT NULL,
    FOREIGN KEY (id_inversor) REFERENCES Inversor(id_inversor),
    FOREIGN KEY (id_accion) REFERENCES Accion(id_accion)
);