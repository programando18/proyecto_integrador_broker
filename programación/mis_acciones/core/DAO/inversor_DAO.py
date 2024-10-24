import mysql.connector
import json
from models.inversor import Inversor


class InversorDAO:
    def __init__(self):
        super().__init__()

    def __connect_to_mysql(self):
        try:
            return mysql.connector.connect(
                host="localhost",
                user="root",
                password="ch35578113",
                database="arg_broker",
            )
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                raise ("Usuario o Password no válido")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                raise ("La base de datos no existe.")
            else:
                raise (err)

    def get_inversor(self, id_inversor):
        query = "SELECT * FROM inversor WHERE id_inversor = %s"
        return self.execute_query(query, (id_inversor,))

    def registrar_inversor(self, inversor: Inversor) -> Inversor:
        query = """
        INSERT INTO inversores (cuit, nombre, apellido, email, contraseña, pregunta_secreta, respuesta_secreta)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        portfolio_query = """
        INSERT INTO portafolios (id_inversor, total_invertido, saldo, acciones) 
        VALUES (%s, %s, %s, %s)
        """

        with self.__connect_to_mysql() as conn:
            try:
                cursor = conn.cursor()

                # Ejecutar la consulta usando los atributos del objeto Inversor
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
                print(id_inversor)

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

    def get_inversor_by_email(self, email):
        print("Buscando inversor por email")

    def get_inversor_by_email_and_password(self, email, password):
        print("Buscando inversor por email y password")

    def comprar_accion(self, id_inversor, id_accion):
        print("")

    def vender_accion(self, id_inversor, id_accion):
        print("")
