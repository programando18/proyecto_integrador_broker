import mysql.connector
from DAO.DataAccessDAO import DataAccessDAO
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
        INSERT INTO inversor (cuit, nombre, apellido, email, contraseña, pregunta_secreta, respuesta_secreta)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        # Manejo de la conexión a la base de datos
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
        # print("Buscando inversor por email")
        with self.__connect_to_mysql() as conn:
            try:
                cursor = conn.cursor()
                query = "SELECT * FROM inversor WHERE email=%s"
                cursor.execute(query, (email,))
                row = cursor.fetchone()
                if row:
                    return object(
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        row[5],
                        row[6],
                        row[7],
                        row[8],
                        row[9],
                        row[10],
                        row[11],
                    )
                return None
            except mysql.connector.Error as err:
                raise err

    def get_inversor_by_email_and_password(self, email, password):
        print("Buscando inversor por email y password")

    def comprar_accion(self, id_inversor, id_accion):
        print("")

    def vender_accion(self, id_inversor, id_accion):
        print("")
