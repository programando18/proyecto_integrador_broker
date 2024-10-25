import mysql.connector
import json
import logging
from models.inversor import Inversor
from DAO.bd_connection import connection_mysql   



class InversorDAO:
    def __init__(self):
        super().__init__()
        

    def get_inversor(self, id_inversor):
        query = "SELECT * FROM inversor WHERE id_inversor = %s"
        return self.execute_query(query, (id_inversor,))

    @staticmethod
    def registrar_inversor(inversor: Inversor) -> Inversor:
        # 1. Conectarse a la base de datos  
        conn = connection_mysql()

        if conn is None:
            logging.info("No se pudo establecer la conexión con la base de datos.")
            return None

        # 2. Crear la consulta SQL de inserción
        query = """
            INSERT INTO inversor (cuit, nombre, apellido, email, contraseña, pregunta_secreta, respuesta_secreta)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        datos = (
            inversor.cuit,
            inversor.nombre,
            inversor.apellido,
            inversor.email,
            inversor.contraseña,
            inversor.pregunta_secreta,
            inversor.respuesta_secreta,
        )

        logging.info(f"Datos a insertar: {datos}")

        try:
            cursor = conn.cursor()
            cursor.execute(query, datos)
            conn.commit()

            # Verificar si se ha insertado el inversor
            if cursor.rowcount > 0:
                logging.info("Inversor registrado exitosamente.")
                return Inversor
            else:
                logging.info("No se pudo registrar el inversor.")
                return None

        except Exception as e:
            logging.error(f"Error al registrar el inversor: {e}")
            return None
        finally:
            conn.close()

# Crear una instancia de Inversor
nuevo_inversor = Inversor(cuit='12345678', nombre='Juan', apellido='Pérez', email='juan@example.com', contraseña='password123', pregunta_secreta='¿Tu color favorito?', respuesta_secreta='Azul')

# Llamar al método para registrar el inversor
resultado = InversorDAO.registrar_inversor(nuevo_inversor)

if resultado:
    print("Registro exitoso")
else:
    print("Error en el registro")







#hacer hoy
#     def get_inversor_by_email(self, email):
#         print("Buscando inversor por email")


# #hacer hoy
#     def get_inversor_by_email_and_password(self, email, password):
#         print("Buscando inversor por email y password")

#  #hacer hoy: 
#     def comparar_password(self): 
#         return ""


#     def comprar_accion(self, id_inversor, id_accion):
#         print("")
 
#     def vender_accion(self, id_inversor, id_accion):
#         print("")