CREATE DATABASE arg_broker;

USE arg_broker;

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
    pregunta VARCHAR(100), 
    respuesta VARCHAR(100),
    
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
    precio_compra_actual  FLOAT NOT NULL,
    precio_venta_actual FLOAT NOT NULL
);

CREATE TABLE historico_cotizaciones (
    id_historico INT PRIMARY KEY AUTO_INCREMENT,
    fecha_cotizacion DATE NOT NULL,
    precio_compra FLOAT NOT NULL,
    precio_venta FLOAT NOT NULL,
    cantidad_venta INT NOT NULL,
    cantidad_compra INT NOT NULL,
    id_accion INT NOT NULL
);


CREATE TABLE transaccion (
    id_transaccion INT PRIMARY KEY AUTO_INCREMENT,
    id_inversor INT,
    tipo_operacion VARCHAR(6) NOT NULL,  -- "compra" o "venta"
    fecha DATE NOT NULL,
    monto FLOAT NOT NULL,
    comisión FLOAT NOT NULL
);

   CREATE TABLE portafolio (
    id_portafolio INT PRIMARY KEY AUTO_INCREMENT,
    id_inversor INT,
    total_invertido FLOAT,
    saldo FLOAT,
    id_accion INT NOT NULL
);


-CREAR LAS FK, QUE CONCUERDEN CON EL MODELO RELACIONAL 
ALTER TABLE inversor
ADD CONSTRAINT fk_id_contacto FOREIGN KEY (id_contacto) REFERENCES tipo_contacto(id_contacto);


ALTER TABLE inversor
ADD CONSTRAINT fk_id_tipo_inversor FOREIGN KEY (id_tipo_inversor) REFERENCES tipo_inversor(id_tipo_inversor);
ADD CONSTRAINT fk_id_tipo_contacto FOREIGN KEY ( id_contacto ) REFERENCES tipo_contacto( id_contacto );


ALTER TABLE portafolio
ADD CONSTRAINT fk_id_inversor FOREIGN KEY (id_inversor) REFERENCES inversor(id_inversor);
ADD CONSTRAINT fk_id_accion_portafolio FOREIGN KEY (id_accion)REFERENCES accion(id_accion)

ALTER TABLE transaccion
ADD CONSTRAINT fk_id_inversor_transaccion FOREIGN KEY (id_inversor) REFERENCES inversor(id_inversor);
ADD CONSTRAINT fk_id_accion_transaccion FOREIGN KEY (id_accion)REFERENCES accion(id_accion);

ALTER TABLE historico_cotizaciones
ADD CONSTRAINT fk_id_accion_cotizaciones FOREIGN KEY (id_accion)REFERENCES accion(id_accion)




