import mysql.connector
import json

from models.inversor import Inversor
from DAO.bd_connection import connection_mysql


class InversorDAO:
    def __init__(self):
        super().__init__()

    def get_inversor(self, id_inversor):
        query = "SELECT * FROM inversor WHERE id_inversor = %s"
        return self.execute_query(query, (id_inversor,))

    def registrar_inversor(self, inversor: Inversor) -> Inversor:
        conn = connection_mysql()

        if conn is None:
            logging.info("No se pudo establecer la conexión con la base de datos.")
            return None

        query = """
        INSERT INTO inversores (cuit, nombre, apellido, email, contraseña, pregunta_secreta, respuesta_secreta)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        portfolio_query = """
        INSERT INTO portafolios (id_inversor, total_invertido, saldo, acciones) 
        VALUES (%s, %s, %s, %s)
        """

        with connection_mysql() as conn:
            try:
                cursor = conn.cursor()

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
                conn.commit()

                id_inversor = cursor.lastrowid

                acciones_json = json.dumps({})

                cursor.execute(
                    portfolio_query, (id_inversor, 0.0, 1000000.0, acciones_json)
                )

                conn.commit()

                if cursor.rowcount > 0:
                    print("Inversor registrado exitosamente.")
                    return inversor
                else:
                    print("No se pudo registrar el inversor.")
                    return None

            except mysql.connector.Error as err:
                print(f"Error al registrar el inversor: {err}")
                return None

    def obtener_inversor_por_email(self, email):
        conn = connection_mysql()

        if conn is None:
            logging.info("No se pudo establecer la conexión con la base de datos.")
            return None

        query = "SELECT * FROM inversores WHERE email = %s"
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(query, (email,))
            result = cursor.fetchone()
            if result:
                return result
            else:
                return None
        except mysql.connector.Error as err:
            print(f"Error al obtener el inversor: {err}")
            return None

    # hacer hoy
    def get_inversor_by_email_and_password(self, email, password):
        print("Buscando inversor por email y password")

    # hacer hoy:
    def comparar_password(self):
        return ""

    def comprar_accion(self, id_inversor, id_accion):
        print("")

    def vender_accion(self, id_inversor, id_accion):
        print("")
