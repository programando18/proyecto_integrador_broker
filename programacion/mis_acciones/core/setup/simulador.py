import mysql.connector
import random
import time
from threading import Thread

# Configuración de la conexión a la base de datos
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "ch35578113",
    "database": "arg_broker",
}


# Conexión a la base de datos
def conectar_db():
    try:
        return mysql.connector.connect(**db_config)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None


# Obtener las acciones de la tabla
def obtener_acciones(db_conn):
    cursor = db_conn.cursor(dictionary=True)
    cursor.execute(
        "SELECT id_accion, precio_compra_actual, precio_venta_actual FROM acciones"
    )
    acciones = cursor.fetchall()
    cursor.close()
    return acciones


# Modificar el precio de compra y venta
def modificar_precios(db_conn):
    acciones = obtener_acciones(db_conn)
    cursor = db_conn.cursor()

    for accion in acciones:
        variacion_compra = random.randint(-2, 2)
        variacion_venta = random.randint(-2, 2)

        nuevo_precio_compra = accion["precio_compra_actual"] + variacion_compra
        nuevo_precio_venta = accion["precio_venta_actual"] + variacion_venta

        cursor.execute(
            """
            UPDATE acciones
            SET precio_compra_actual = %s, precio_venta_actual = %s
            WHERE id_accion = %s
        """,
            (nuevo_precio_compra, nuevo_precio_venta, accion["id_accion"]),
        )

    db_conn.commit()
    cursor.close()


# Loop que se ejecuta en el background
def loop_actualizacion():
    db_conn = conectar_db()
    if db_conn:
        while True:
            modificar_precios(db_conn)
            print("Precios actualizados.")
            time.sleep(2)
    else:
        print("No se pudo conectar a la base de datos.")


# Ejecutar el loop en un hilo separado
def iniciar_app():
    thread = Thread(target=loop_actualizacion)
    thread.daemon = True
    thread.start()
    print("Simulador de variación de precios iniciado...")


# Iniciar la app
iniciar_app()

# Mantener la app corriendo
while True:
    time.sleep(1)
