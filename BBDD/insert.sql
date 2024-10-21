
INSERT INTO tipo_contacto (telefono, email) VALUES 
('1234567890', 'contact1@example.com'),
('0987654321', 'contact2@example.com');


INSERT INTO tipo_inversor (descripcion_inversor) VALUES 
('Inversor Individual'),
('Inversor Institucional');


INSERT INTO inversor (cuit, nombre, apellido, contraseña, saldo, id_contacto, id_tipo_inversor, fecha_alta, pregunta, respuesta) VALUES 
('20-12345678-9', 'Juan', 'Pérez', 'password123', 1000.00, 1, 1, '2024-10-21', '¿Tu color favorito?', 'Azul'),
('20-98765432-1', 'María', 'Gómez', 'password456', 2000.00, 2, 2, '2024-10-21', '¿Tu mascota?', 'Perro');


INSERT INTO acción (simbolo_accion, nombre_accion, precio_compra_actual, precio_venta_actual) VALUES 
('AAPL', 'Apple Inc.', 150.00, 155.00),
('GOOGL', 'Alphabet Inc.', 2800.00, 2850.00);


INSERT INTO historico_cotizaciones (fecha_cotizacion, precio_compra, precio_venta, cantidad_venta, cantidad_compra, id_accion) VALUES 
('2024-10-20', 150.00, 155.00, 100, 150, 1),
('2024-10-19', 2800.00, 2850.00, 50, 75, 2);


INSERT INTO portafolio (id_inversor, rendimiento, total_invertido, saldo) VALUES 
(1, 5.0, 1000.00, 1000.00),
(2, 10.0, 2000.00, 2000.00);


INSERT INTO transaccion (id_inversor, tipo_operacion, fecha, monto, comision) VALUES 
(1, 'compra', '2024-10-21', 500.00, 5.00),
(2, 'venta', '2024-10-21', 1000.00, 10.00);