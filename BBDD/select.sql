
SELECT * FROM inversor;


SELECT t.telefono, t.email 
FROM tipo_contacto t;


SELECT descripcion_inversor 
FROM tipo_inversor;


SELECT simbolo_accion, nombre_accion, precio_compra_actual, precio_venta_actual 
FROM acción;


SELECT fecha_cotizacion, precio_compra, precio_venta 
FROM historico_cotizaciones 
WHERE id_accion = (SELECT id_accion FROM acción WHERE simbolo_accion = 'AAPL');


SELECT id_portafolio, total_invertido 
FROM portafolio;


SELECT * 
FROM transaccion 
WHERE id_inversor = 1;


SELECT AVG(rendimiento) AS promedio_rendimiento 
FROM portafolio;