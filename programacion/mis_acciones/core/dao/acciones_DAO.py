import mysql.connector
import json


class AccionesDAO:
    def __init__(self, conexion):
        self.conexion = conexion

    def obtener_acciones(self):
        query = "SELECT * FROM acciones"

        try:
            cursor = self.conexion.cursor(dictionary=True)
            cursor.execute(query)
            acciones = cursor.fetchall()
            return acciones
        except mysql.connector.Error as err:
            print(f"Error al obtener las acciones: {err}")
            return None

    def obtener_precio_accion(self, simbolo: str):
        query = "SELECT precio_compra_actual FROM acciones WHERE simbolo = %s"

        try:
            cursor = self.conexion.cursor(dictionary=True)
            cursor.execute(query, (simbolo,))
            precio = cursor.fetchone()
            return precio["precio_compra_actual"]
        except mysql.connector.Error as err:
            print(f"Error al obtener el precio de la acción: {err}")
            return None

    def descontar_acciones(self, simbolo: str, cantidad: int) -> bool:
        query = """
            UPDATE acciones 
            SET cantidad = cantidad - %s 
            WHERE simbolo = %s
        """

        try:
            cursor = self.conexion.cursor()
            cursor.execute(query, (cantidad, simbolo))
            self.conexion.commit()
            return True
        except mysql.connector.Error as err:
            print(f"Error al descontar las acciones: {err}")
            return False

    def agregar_acciones(self, simbolo: str, cantidad: int) -> bool:
        query = """
            UPDATE acciones 
            SET cantidad = cantidad + %s 
            WHERE simbolo = %s
        """

        try:
            cursor = self.conexion.cursor()
            cursor.execute(query, (cantidad, simbolo))
            self.conexion.commit()
            return True
        except mysql.connector.Error as err:
            print(f"Error al agregar las acciones: {err}")
            return False
