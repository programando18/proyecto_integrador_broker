import mysql.connector
import json

from models.portafolio import Portafolio


class PortafolioDAO:
    def __init__(self, conexion):
        self.conexion = conexion

    def obtener_portafolio(self, id_inversor: int) -> Portafolio:

        if not self.conexion.is_connected():
            self.conexion.reconnect()

        query = "SELECT * FROM portafolios WHERE id_inversor = %s"

        try:
            cursor = self.conexion.cursor(dictionary=True)
            cursor.execute(query, (id_inversor,))
            result = cursor.fetchone()
            cursor.close()
            if result:
                return Portafolio(
                    id_portafolio=result["id_portafolio"],
                    saldo=result["saldo"],
                    acciones=result["acciones"],
                    id_inversor=result["id_inversor"],
                )
            else:
                return None
        except mysql.connector.Error as err:
            print(f"Error al obtener el portafolio: {err}")
            return None

    def agregar_accion(self, id_inversor: int, accion: dict) -> bool:

        if not self.conexion.is_connected():
            self.conexion.reconnect()

        query = """
            UPDATE portafolios 
            SET acciones = JSON_ARRAY_APPEND(acciones, '$', JSON_OBJECT('simbolo', %s, 'nombre', %s, 'cantidad', %s, 'precio_compra', %s)) 
            WHERE id_portafolio = %s
        """

        try:
            cursor = self.conexion.cursor()
            cursor.execute(
                query,
                (
                    accion["simbolo"],
                    accion["nombre"],
                    accion["cantidad"],
                    accion["precio_compra"],
                    id_inversor,
                ),
            )
            self.conexion.commit()
            return True
        except mysql.connector.Error as err:
            print(f"Error al agregar la acción: {err}")
            return False

    def descontar_accion(self, id_inversor: int, simbolo: str, cantidad: int) -> bool:

        if not self.conexion.is_connected():
            self.conexion.reconnect()

        query_select = """
            SELECT JSON_EXTRACT(acciones, '$') AS acciones 
            FROM portafolios 
            WHERE id_portafolio = %s
        """

        query_update = """
            UPDATE portafolios 
            SET acciones = %s 
            WHERE id_portafolio = %s
        """

        try:
            cursor = self.conexion.cursor(dictionary=True)
            cursor.execute(query_select, (id_inversor,))
            row = cursor.fetchone()
            if row and row["acciones"]:
                acciones = json.loads(row["acciones"])
                for accion in acciones:
                    if accion["simbolo"] == simbolo:
                        if accion["cantidad"] >= cantidad:
                            accion["cantidad"] -= cantidad
                            if accion["cantidad"] == 0:
                                acciones.remove(accion)
                            break
                        else:
                            print("Cantidad insuficiente de acciones para descontar")
                            return False
                else:
                    print("Acción no encontrada en el portafolio")
                    return False
                acciones_json = json.dumps(acciones)
                cursor.execute(query_update, (acciones_json, id_inversor))
                self.conexion.commit()
                return True
            else:
                print("Portafolio no encontrado o sin acciones")
                return False
        except mysql.connector.Error as err:
            print(f"Error al descontar la acción: {err}")
            return False

    def descontar_saldo(self, id_inversor: int, monto: float) -> bool:

        if not self.conexion.is_connected():
            self.conexion.reconnect()

        query = """
            UPDATE portafolios 
            SET saldo = saldo - %s 
            WHERE id_inversor = %s
        """

        try:
            cursor = self.conexion.cursor()
            cursor.execute(query, (monto, id_inversor))
            self.conexion.commit()
            return True
        except mysql.connector.Error as err:
            print(f"Error al descontar el saldo: {err}")
            return False

    def aumentar_saldo(self, id_inversor: int, monto: float) -> bool:

        if not self.conexion.is_connected():
            self.conexion.reconnect()

        query = """
                UPDATE portafolios 
                SET saldo = saldo + %s 
                WHERE id_inversor = %s
            """

        try:
            cursor = self.conexion.cursor()
            cursor.execute(query, (monto, id_inversor))
            self.conexion.commit()
            return True
        except mysql.connector.Error as err:
            print(f"Error al aumentar el saldo: {err}")
            return False

    def obtener_rendimiento(self, id_inversor: int, portafolio: Portafolio) -> float:

        if not self.conexion.is_connected():
            self.conexion.reconnect()

        query_accion = """
            SELECT precio_venta_actual 
            FROM acciones 
            WHERE simbolo = %s
        """

        try:
            cursor = self.conexion.cursor(dictionary=True)
            if portafolio and portafolio.acciones:
                acciones = json.loads(portafolio.acciones)
                rendimiento_total = 0.0
                for accion in acciones:
                    cursor.execute(query_accion, (accion["simbolo"],))
                    accion_data = cursor.fetchone()
                    if accion_data:
                        precio_actual = accion_data["precio_venta_actual"]
                        rendimiento = (
                            precio_actual - accion["precio_compra"]
                        ) * accion["cantidad"]
                        rendimiento_total += rendimiento
                return round(float(rendimiento_total), 2)
            else:
                print("Portafolio no encontrado o sin acciones")
                return 0.0
        except mysql.connector.Error as err:
            print(f"Error al obtener el rendimiento: {err}")
            return 0.0

    def obtener_total_invertido(
        self, id_inversor: int, portafolio: Portafolio
    ) -> float:

        try:
            if portafolio and portafolio.acciones:
                acciones = json.loads(portafolio.acciones)
                total_invertido = 0.0
                for accion in acciones:
                    total_invertido += accion["precio_compra"] * accion["cantidad"]
                return round(float(total_invertido), 2)
            else:
                return 0.0
        except mysql.connector.Error as err:
            print(f"Error al obtener el total invertido: {err}")
            return 0.0
