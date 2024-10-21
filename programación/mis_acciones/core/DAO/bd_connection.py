import mysql.connector
import logging
from mysql.connector import errorcode

# Configuración del logger
logger = logging.getLogger("mysql.connector")  # Nombre del logger
logger.setLevel(logging.INFO)  # Nivel de registro (puedes ajustar a DEBUG, ERROR, etc.)

# Formateador para los mensajes de registro
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Manejador para mostrar los registros en la consola
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

# Agregar el manejador al logger
logger.addHandler(stream_handler)


def connection_mysql():
    try: 
        conn = mysql.connector.connect(
            user='root', 
            password='34215876a.',
            host='localhost',
            database='arg_broker',
            port=3306   
        )
        logger.info("Conexión exitosa a la base de datos")
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


# Probar la conexión
conn = connection_mysql()


