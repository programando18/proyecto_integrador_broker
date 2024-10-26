import mysql.connector
import json

from DAO.bd_connection import connection_mysql
from models.portafolio import Portafolio


class PortafolioDAO:
    def __init__(self):
        super().__init__()

    def obtener_portafolio(self, id_inversor: int) -> Portafolio:

        query = "SELECT * FROM portafolios WHERE id_portafolio = %s"

        with connection_mysql() as conn:

            try:
                cursor = conn.cursor(dictionary=True)
                cursor.execute(query, (id_inversor,))
                row = cursor.fetchone()
                if row:
                    return row
                else:
                    return None
            except mysql.connector.Error as err:
                print(f"Error al obtener el portafolio: {err}")
                return None
