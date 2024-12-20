-- Inserción de datos en la tabla acciones
INSERT INTO acciones (simbolo, nombre, precio_compra_actual, precio_venta_actual, cantidad)
VALUES 
    ('AAPL', 'Apple Inc.', 150.25, 152.00, 100),
    ('GOOGL', 'Alphabet Inc.', 2800.75, 2825.50, 50),
    ('AMZN', 'Amazon.com, Inc.', 3400.30, 3420.10, 30),
    ('TSLA', 'Tesla, Inc.', 720.15, 725.40, 75),
    ('MSFT', 'Microsoft Corporation', 299.90, 305.00, 200),
    ('NFLX', 'Netflix, Inc.', 645.50, 650.75, 60),
    ('NVDA', 'NVIDIA Corporation', 220.15, 225.30, 120),
    ('FB', 'Meta Platforms, Inc.', 330.20, 335.10, 80),
    ('BABA', 'Alibaba Group Holding Limited', 180.30, 185.00, 90);

-- Inserción de datos en la tabla inversores
INSERT INTO inversores (cuit, nombre, apellido, email, contraseña, saldo, pregunta_secreta, respuesta_secreta) 
VALUES 
    ('20123456789', 'Juan', 'Pérez', 'juanperez@gmail.com', 'password123', 1000.00, '¿Tu color favorito?', 'Azul'),
    ('20987654321', 'María', 'Gómez', 'mariagomez@gmail.com', 'password456', 2000.00, '¿Tu mascota?', 'Perro'),
    ('27296078889', 'Evelin', 'Checa', 'evecheca@gmail.com', 'sole1234', 3000.00, '¿nombre de tu canario?', 'viejito');

-- Inserción de datos en la tabla historico_cotizaciones
INSERT INTO historico_cotizaciones (fecha_cotizacion, precio_compra, precio_venta, cantidad_venta, cantidad_compra, id_accion) 
VALUES 
    ('2024-10-20', 150.00, 155.00, 100, 150, 1),
    ('2024-10-19', 2800.00, 2850.00, 50, 75, 2),
    ('2024-10-20', 150.00, 155.00, 100, 150, 3),
    ('2024-10-25', 2600.00, 2550.00, 80, 95, 4);

-- Inserción de datos en la tabla portafolios (usando JSON para almacenar las acciones)
INSERT INTO portafolios (id_inversor, total_invertido, saldo, acciones) 
VALUES 
    (1, 3000.00, 1000.00, '[{"simbolo": "AAPL", "nombre": "Apple Inc.", "precio_compra": 150.00, "precio_venta": 155.00, "cantidad": 300}]'),
    (2, 5000.00, 2000.00, '[{"simbolo": "AMZN", "nombre": "Amazon Inc.", "precio_compra": 670.00, "precio_venta": 690.00, "cantidad": 250}]');

-- Inserción de datos en la tabla registro_transacciones
INSERT INTO registro_transacciones (id_inversor, nombre_inversor, tipo_operacion, simbolo, cantidad, precio_unidad, precio_total) 
VALUES 
    (1, 'Juan Pérez', 'compra', 'AAPL', 5, 150.00, 750.00),
    (2, 'María Gómez', 'venta', 'GOOGL', 3, 2800.00, 8400.00);

-- Actualización de datos en varias tablas
UPDATE inversores 
SET saldo = saldo + 500 
WHERE id_inversor = 1;

UPDATE acciones 
SET precio_compra_actual = 155.00 
WHERE simbolo = 'AAPL';

UPDATE portafolios 
SET total_invertido = 4000.00
WHERE id_portafolio = 1;

UPDATE inversores 
SET nombre = "Magaly"
WHERE id_inversor = 2;

UPDATE historico_cotizaciones 
SET cantidad_venta = cantidad_venta + 10 
WHERE id_historico = 1;

-- Consultas de selección
SELECT cuit, nombre, apellido, email, contraseña, saldo, pregunta_secreta, respuesta_secreta 
FROM inversores;

SELECT simbolo, nombre, precio_compra_actual, precio_venta_actual, cantidad 
FROM acciones;

SELECT fecha_cotizacion, precio_compra, precio_venta 
FROM historico_cotizaciones 
WHERE id_accion = (SELECT id_accion FROM acciones WHERE simbolo = 'AAPL');

SELECT id_portafolio, total_invertido 
FROM portafolios;

SELECT tipo_operacion, fecha, cantidad, precio_total
FROM registro_transacciones
WHERE id_inversor = 1;

-- Consultas multitabla

-- Ver todas las transacciones realizadas por cada inversor
SELECT i.nombre, i.apellido, SUM(t.precio_total) AS total_transacciones
FROM registro_transacciones t
JOIN inversores i ON t.id_inversor = i.id_inversor
GROUP BY i.nombre, i.apellido;

-- Mostrar solo las cotizaciones más recientes
SELECT a.nombre AS nombre_accion, h.fecha_cotizacion, h.precio_compra, h.precio_venta
FROM historico_cotizaciones h
INNER JOIN acciones a ON h.id_accion = a.id_accion
WHERE a.simbolo = 'AAPL' AND h.fecha_cotizacion >= CURDATE() - INTERVAL 7 DAY;

-- Mostrar solo los inversores cuyo rendimiento supera un cierto valor
SELECT i.nombre, a.nombre AS nombre_accion, p.total_invertido 
FROM portafolios p
INNER JOIN inversores i ON p.id_inversor = i.id_inversor
INNER JOIN acciones a ON JSON_CONTAINS(p.acciones, JSON_OBJECT("simbolo", a.simbolo))
WHERE p.total_invertido > 10;






