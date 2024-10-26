import mysql.connector
import json

from mis_acciones.core.models.inversor import Inversor
from DAO.bd_connection import connection_mysql   



class InversorDAO:
    def __init__(self):
        # super().__init__()
        
        def get_inversor(self, id_inversor):
            query = "SELECT * FROM inversor WHERE id_inversor = %s"
        return self.execute_query(query, (id_inversor,))


    def registrar_inversor(inversor: Inversor) -> Inversor:
        # 1. Conectarse a la base de datos
        conn = connection_mysql()

        if conn is None:
            logging.info("No se pudo establecer la conexión con la base de datos.")
            return None

        # 2. Crear la consulta SQL de inserción
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
                    raise("No se pudo registrar el inversor.")
                    return None

            except mysql.connector.Error as err:
               raise(f"Error al registrar el inversor: {err}")
               return None

   
    def get_inversor_by_email(self, email):
        query = "SELECT * FROM inversor WHERE email = %s"
    resultado = self.execute_query(query, (email))
    if resultado:
        return Inversor(*resultado)
    else:
        raise("No se encontró ningún inversor con ese email.")


 
    def get_password_by_email(self, password):
         query = "SELECT contraseña FROM inversor WHERE email = %s"
         resultado = self.execute_query(query, (email))

         if resultado:
            return resultado[0]  # Retorna la contraseña encriptada
         else:
            print("No se encontró ningún inversor con ese email.")
          

    # hacer hoy:gi
    def comparar_password(self):
        return ""

    def comprar_accion(self, id_inversor, id_accion):
        print("")

    def vender_accion(self, id_inversor, id_accion):
        print("")
