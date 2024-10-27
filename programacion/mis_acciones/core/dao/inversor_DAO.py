import mysql.connector
import json

from models.inversor import Inversor


class InversorDAO:
    def __init__(self, conexion):
        self.conexion = conexion

    def registrar_inversor(self, inversor: Inversor) -> Inversor:

        query = """
        INSERT INTO inversores (cuit, nombre, apellido, email, contraseña, pregunta_secreta, respuesta_secreta)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        portfolio_query = """
        INSERT INTO portafolios (id_inversor, total_invertido, saldo, acciones) 
        VALUES (%s, %s, %s, %s)
        """

        try:
            cursor = self.conexion.cursor()
            cursor.execute(
                query,
                (
                    inversor.cuit,
                    inversor.nombre,
                    inversor.apellido,
                    inversor.email,
                    inversor.contraseña,
                    inversor.pregunta_secreta,
                    inversor.respuesta_secreta,
                ),
            )
            id_inversor = cursor.lastrowid
            acciones_json = json.dumps([])
            cursor.execute(
                portfolio_query, (id_inversor, 0.0, 1000000.0, acciones_json)
            )
            self.conexion.commit()
            if cursor.rowcount > 0:
                print("Inversor registrado exitosamente.")
                return inversor
            else:
                raise ("No se pudo registrar el inversor.")
                return None
        except mysql.connector.Error as err:
            raise (f"Error al registrar el inversor: {err}")
            return None

    def obtener_inversor_por_email(self, email: str) -> Inversor:
        query = "SELECT * FROM inversores WHERE email = %s"

        try:
            cursor = self.conexion.cursor(dictionary=True)
            cursor.execute(query, (email,))
            result = cursor.fetchone()
            cursor.close()
            if result:
                return Inversor(
                    id_inversor=result["id_inversor"],
                    cuit=result["cuit"],
                    nombre=result["nombre"],
                    apellido=result["apellido"],
                    email=result["email"],
                    contraseña=result["contraseña"],
                    pregunta_secreta=result["pregunta_secreta"],
                    respuesta_secreta=result["respuesta_secreta"],
                )
            else:
                return None
        except mysql.connector.Error as err:
            print(f"Error al obtener el inversor: {err}")
            return None
