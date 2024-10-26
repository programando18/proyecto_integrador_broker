import mysql.connector
import logging
import json
import os

from mysql.connector import errorcode

logger = logging.getLogger("mysql.connector")
logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(stream_handler)


def get_db_config():
    try:
        base_path = os.path.dirname(os.path.abspath(__file__))
        config_path = base_path + "/config.json"
        with open(config_path, "r") as config_file:
            config = json.load(config_file)
            return config
    except FileNotFoundError:
        logger.error("El archivo de configuración no se encontró.")
    except json.JSONDecodeError:
        logger.error("Error al decodificar el archivo de configuración.")
    return None


def connection_mysql():
    config = get_db_config()
    if config is None:
        return None

    try:
        conn = mysql.connector.connect(
            user=config.get("user"),
            password=config.get("password"),
            host=config.get("host"),
            database=config.get("database"),
            port=config.get("port", 3306),  # Default port to 3306 if not specified
        )
        return conn

    except mysql.connector.Error as err:
        # Error de acceso denegado (usuario o contraseña incorrectos)
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            logger.error("Usuario o Password no válido")
        # La base de datos especificada no existe
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            logger.error("La base de datos no existe.")
        else:
            logger.error(f"Error desconocido: {err}")
    return None
