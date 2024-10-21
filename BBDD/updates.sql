
UPDATE inversor 
SET saldo = saldo + 500 
WHERE id_inversor = 1;


UPDATE tipo_contacto 
SET email = 'new_contact1@example.com' 
WHERE id_contacto = 1;


UPDATE tipo_inversor 
SET descripcion_inversor = 'Inversor Privado' 
WHERE id_tipo_inversor = 1;


UPDATE acción 
SET precio_compra_actual = 155.00 
WHERE simbolo_accion = 'AAPL';


UPDATE portafolio 
SET rendimiento = 7.0 
WHERE id_portafolio = 1;


UPDATE inversor 
SET fecha_alta = '2024-10-22' 
WHERE id_inversor = 2;


UPDATE historico_cotizaciones 
SET cantidad_venta = cantidad_venta + 10 
WHERE id_historico = 1;


UPDATE transaccion 
SET tipo_operacion = 'compra' 
WHERE id_transaccion = 2;