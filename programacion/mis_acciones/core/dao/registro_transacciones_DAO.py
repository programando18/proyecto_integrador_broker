import mysql.connector

from models.transaccion import Transaccion


class RegistroTransaccionesDAO:
    def __init__(self, conexion):
        self.conexion = conexion

    def registrar_transaccion(self, transaccion: Transaccion) -> Transaccion:
        query = "INSERT INTO registro_transacciones (id_inversor, nombre_inversor, tipo_operacion, simbolo, cantidad, precio_unidad, precio_total) VALUES (%s, %s, %s, %s, %s, %s, %s)"

        if not self.conexion.is_connected():
            self.conexion.reconnect()

        try:
            cursor = self.conexion.cursor()
            cursor.execute(
                query,
                (
                    transaccion.id_inversor,
                    transaccion.nombre_inversor,
                    transaccion.tipo_operacion,
                    transaccion.simbolo,
                    transaccion.cantidad,
                    transaccion.precio_unidad,
                    transaccion.precio_total,
                ),
            )
            self.conexion.commit()
            if cursor.rowcount == 0:
                return None
        except mysql.connector.Error as err:
            raise (f"Error al registrar la transacción: {err}")
            return None

    def obtener_lista_transacciones(self, id_inversor: int) -> list:
        query = "SELECT * FROM registro_transacciones WHERE id_inversor = %s"

        if not self.conexion.is_connected():
            self.conexion.reconnect()

        try:
            cursor = self.conexion.cursor(dictionary=True)
            cursor.execute(query, (id_inversor,))
            return cursor.fetchall()
        except mysql.connector.Error as err:
            raise (f"Error al obtener la lista de transacciones: {err}")
            return None
