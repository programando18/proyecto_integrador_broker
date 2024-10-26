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

    def descontar_acciones(self, simbolo: str, cantidad: int) -> bool:
        query = """
            UPDATE acciones 
            SET cantidad = cantidad - %s 
            WHERE simbolo = %s
        """

        with connection_mysql() as conn:
            try:
                cursor = conn.cursor()
                cursor.execute(query, (cantidad, simbolo))
                conn.commit()
                return True
            except mysql.connector.Error as err:
                print(f"Error al descontar las acciones: {err}")
                return False
