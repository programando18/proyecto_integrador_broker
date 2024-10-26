import mysql.connector
import json
from DAO.bd_connection import connection_mysql


class AccionesDAO:
    def __init__(self):
        super().__init__()

    def obtener_acciones(self):
        query = "SELECT * FROM acciones"

        with connection_mysql() as conn:
            try:
                cursor = conn.cursor(dictionary=True)
                cursor.execute(query)
                acciones = cursor.fetchall()
                return acciones

            except mysql.connector.Error as err:
                print(f"Error al obtener las acciones: {err}")
                return None
