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

    def agregar_accion(self, id_inversor: int, accion: dict) -> bool:

        query = """
            UPDATE portafolios 
            SET acciones = JSON_ARRAY_APPEND(acciones, '$', JSON_OBJECT('simbolo', %s, 'nombre', %s, 'cantidad', %s)) 
            WHERE id_portafolio = %s
        """

        with connection_mysql() as conn:

            try:
                cursor = conn.cursor()
                cursor.execute(
                    query,
                    (
                        accion["simbolo"],
                        accion["nombre"],
                        accion["cantidad"],
                        id_inversor,
                    ),
                )
                conn.commit()
                return True
            except mysql.connector.Error as err:
                print(f"Error al agregar la acción: {err}")
                return False

    def descontar_saldo(self, id_inversor: int, monto: float) -> bool:

        query = """
            UPDATE portafolios 
            SET saldo = saldo - %s 
            WHERE id_inversor = %s
        """

        with connection_mysql() as conn:

            try:
                cursor = conn.cursor()
                cursor.execute(query, (monto, id_inversor))
                conn.commit()
                return True
            except mysql.connector.Error as err:
                print(f"Error al descontar el saldo: {err}")
                return False
