import mysql.connector
from DAO.DataAccessDAO import DataAccessDAO


class InversorDAO:
    def __init__(self):
        super().__init__()
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="ch35578113",
            database="arg_broker",
        )

    def execute_query(self, query, params=None):
        cursor = self.connection.cursor(dictionary=True)
        try:
            cursor.execute(query, params)
            if query.strip().upper().startswith("SELECT"):
                result = cursor.fetchall()
            else:
                self.connection.commit()
                result = cursor.rowcount
        finally:
            cursor.close()
        return result

    def get_inversor(self, id_inversor):
        query = "SELECT * FROM inversor WHERE id_inversor = %s"
        return self.execute_query(query, (id_inversor,))

    def registrar_inversor(
        self,
        cuit,
        nombre,
        apellido,
        email,
        contraseña,
        pregunta_secreta,
        respuesta_secreta,
    ):
        print("Registrando inversor")
        print(
            cuit,
            nombre,
            apellido,
            email,
            contraseña,
            pregunta_secreta,
            respuesta_secreta,
        )
        query = "INSERT INTO inversor (cuit, nombre, apellido, email, contraseña, pregunta_secreta, respuesta_secreta) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        return self.execute_query(
            query,
            (
                cuit,
                nombre,
                apellido,
                email,
                contraseña,
                pregunta_secreta,
                respuesta_secreta,
            ),
        )

    def get_inversor_by_email(self, email):
        query = "SELECT * FROM inversor WHERE email = %s"
        return self.execute_query(query, (email,))

    def get_inversor_by_email_and_password(self, email, password):
        query = "SELECT * FROM inversor WHERE email = %s AND password = %s"
        return self.execute_query(query, (email, password))

    def comprar_accion(self, id_inversor, id_accion):
        query = "INSERT INTO acciones_inversor (id_inversor, id_accion) VALUES (%s, %s)"
        return self.execute_query(query, (id_inversor, id_accion))

    def vender_accion(self, id_inversor, id_accion):
        query = (
            "DELETE FROM acciones_inversor WHERE id_inversor = %s AND id_accion = %s"
        )
        return self.execute_query(query, (id_inversor, id_accion))
