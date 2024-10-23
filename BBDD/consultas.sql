--Ver todas las transacciones realizadas por cada inversor
SELECT i.nombre, i.apellido, ti.descripcion_inversor, SUM(t.monto) AS total_transacciones
FROM transaccion t
JOIN inversor i ON t.id_inversor = i.id_inversor
JOIN tipo_inversor ti ON i.id_tipo_inversor = ti.id_tipo_inversor
GROUP BY i.nombre, i.apellido, ti.descripcion_inversor;


--  Consultar inversores, su contacto y tipo de inversor
SELECT inversor.nombre, inversor.apellido, tipo_contacto.telefono, tipo_contacto.email, tipo_inversor.descripcion_inversor
FROM inversor
INNER JOIN tipo_contacto ON inversor.id_contacto = tipo_contacto.id_contacto
INNER JOIN tipo_inversor ON inversor.id_tipo_inversor = tipo_inversor.id_tipo_i

--Mostrar solo las cotizaciones más recientes
SELECT accion.nombre_accion, historico_cotizaciones.fecha_cotizacion, historico_cotizaciones.precio_compra, historico_cotizaciones.precio_venta
FROM historico_cotizaciones
INNER JOIN accion ON historico_cotizaciones.id_accion = accion.id_accion
WHERE accion.simbolo_accion = 'AAPL' AND historico_cotizaciones.fecha_cotizacion >= CURDATE() - INTERVAL 7 DAY;

--Mostrar solo los inversores cuyo rendimiento supera un cierto valor
SELECT inversor.nombre, accion.nombre_accion, portafolio.total_invertido, portafolio.rendimiento
FROM portafolio
INNER JOIN inversor ON portafolio.id_inversor = inversor.id_inversor
INNER JOIN accion ON accion.id_accion = portafolio.id_accion
WHERE portafolio.rendimiento > 10;

-- Obtener el rendimiento promedio de todos los inversores agrupado por tipo de inversor y cantidad de cada tipo de inversor.
SELECT t.descripcion_inversor, AVG(p.rendimiento) AS promedio_rendimiento, COUNT(i.id_inversor) AS num_inversores
FROM portafolio p
JOIN inversor i ON p.id_inversor = i.id_inversor
JOIN tipo_inversor t ON i.id_tipo_inversor = t.id_tipo_inversor
GROUP BY t.descripcion_inversor;
