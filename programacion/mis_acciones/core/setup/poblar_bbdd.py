import mysql.connector
import json
import os

from mysql.connector import Error


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


def ejecutar_query():
    conexion = conexion_bd()

    queries = [
        "INSERT INTO acciones (simbolo, nombre, precio_compra_actual, precio_venta_actual, cantidad) VALUES ('AAPL', 'Apple Inc.', 150.25, 152.00, 100);",
        "INSERT INTO acciones (simbolo, nombre, precio_compra_actual, precio_venta_actual, cantidad) VALUES ('GOOGL', 'Alphabet Inc.', 2800.75, 2825.50, 50);",
        "INSERT INTO acciones (simbolo, nombre, precio_compra_actual, precio_venta_actual, cantidad) VALUES ('AMZN', 'Amazon.com, Inc.', 3400.30, 3420.10, 30);",
        "INSERT INTO acciones (simbolo, nombre, precio_compra_actual, precio_venta_actual, cantidad) VALUES ('TSLA', 'Tesla, Inc.', 720.15, 725.40, 75);",
        "INSERT INTO acciones (simbolo, nombre, precio_compra_actual, precio_venta_actual, cantidad) VALUES ('MSFT', 'Microsoft Corporation', 299.90, 305.00, 200);",
        "INSERT INTO acciones (simbolo, nombre, precio_compra_actual, precio_venta_actual, cantidad) VALUES ('NFLX', 'Netflix, Inc.', 645.50, 650.75, 60);",
        "INSERT INTO acciones (simbolo, nombre, precio_compra_actual, precio_venta_actual, cantidad) VALUES ('NVDA', 'NVIDIA Corporation', 220.15, 225.30, 120);",
        "INSERT INTO acciones (simbolo, nombre, precio_compra_actual, precio_venta_actual, cantidad) VALUES ('FB', 'Meta Platforms, Inc.', 330.20, 335.10, 80);",
        "INSERT INTO acciones (simbolo, nombre, precio_compra_actual, precio_venta_actual, cantidad) VALUES ('BABA', 'Alibaba Group Holding Limited', 180.30, 185.00, 90);",
    ]

    try:
        cursor = conexion.cursor()
        for query in queries:
            cursor.execute(query)
        conexion.commit()
        print("Base de datos poblada con éxito.")
    except mysql.connector.Error as e:
        print(f"Error al ejecutar la query: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()


ejecutar_query()
