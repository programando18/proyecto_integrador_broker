import mysql.connector
import random
import time
import json
import os

from threading import Thread


def obtener_config_db():
    try:
        base_path = os.path.dirname(os.path.abspath(__file__))
        config_path = base_path.replace("/setup", "") + "/config/config.json"
        with open(config_path, "r") as config_file:
            config = json.load(config_file)
            return config
    except FileNotFoundError:
        exit(1)
    except json.JSONDecodeError:
        exit(1)
    return None


def conexion_bd():
    config = obtener_config_db()
    if config is None:
        return None

    try:
        conn = mysql.connector.connect(
            user=config.get("user"),
            password=config.get("password"),
            host=config.get("host"),
            database=config.get("database"),
            port=config.get("port", 3306),
        )
        return conn

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print(
                "------------------------------------------------------------------------------------------"
            )
            logger.error("  Usuario o Password no válido       |")
            print(
                "Por favor configure correctamente sus credenciales en el archivo core/DAO/config.json    |"
            )
            print(
                "------------------------------------------------------------------------------------------"
            )
            exit(1)
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            logger.error("La base de datos no existe.")
        else:
            logger.error(f"Error desconocido: {err}")
    return None


def obtener_acciones(conexion):
    cursor = conexion.cursor(dictionary=True)
    cursor.execute(
        "SELECT id_accion, precio_compra_actual, precio_venta_actual FROM acciones"
    )
    acciones = cursor.fetchall()
    cursor.close()
    return acciones


def modificar_precios(conexion):
    acciones = obtener_acciones(conexion)
    cursor = conexion.cursor()

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

    conexion.commit()
    cursor.close()


def loop_actualizacion():
    conexion = conexion_bd()
    if conexion:
        while True:
            modificar_precios(conexion)
            print("Precios actualizados.")
            time.sleep(60)
    else:
        print("No se pudo conectar a la base de datos.")


def iniciar_simulador():
    thread = Thread(target=loop_actualizacion)
    thread.daemon = True
    thread.start()
    print("Simulador de variación de precios iniciado...")


iniciar_simulador()

while True:
    time.sleep(1)
