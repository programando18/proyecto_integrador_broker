from interfaces.bienvenida import bienvenida
from interfaces.panel_de_control import panel_de_control
from forms.login import formulario_login
from forms.register import registrar_inversor
from models.inversor import Inversor
from models.portafolio import Portafolio
from DAO.inversor_DAO import InversorDAO
from forms.recover import ingresar_email, recuperar_contraseña
from utils.validaciones import validar_contraseña, validar_email
from DAO.bd_connection import connection_mysql
import bcrypt

def main():
    connection_mysql()
    opcion = bienvenida()

   

    while True:
        if opcion == "1":
            datos_login = formulario_login()

            while not validar_email(datos_login[0]) or not validar_contraseña(
                datos_login[1]
            ):
                print("Datos inválidos, por favor intente de nuevo")
                datos_login = formulario_login()

            # Acá va la conexión con la BBDD y el chequeo de que el usuario exista
            # Acá tenés que trabajar MILI.
            # TAREAS
            # Crear método en InversorDAO para obtener un inversor por email
            # Si el inversor existe, comparar contraseñas
            # Si las contraseñas coinciden, continuar a lo siguiente (panel_de_control, ya está implementado)
            # ------------------------------------------------|
            inversor_dao = InversorDAO()

            datos_inversor = inversor_dao.get_inversor_by_email(email)
            if email_inversor is None:
                print("Usuario no encontrado.")
            datos_login = formulario_login()
            email, contraseña = datos_login

            # Obtener la contraseña encriptada de los datos del usuario
            contraseña_almacenada = datos_inversor["contraseña"]
            if contraseña_almacenada is None:
                print("Usuario no encontrado.")

            if contraseña_almacenada == datos_inversor: 
                print ("Contraseña correcta. Usuario autenticado exitosamente.")
    
             # 3. Comparar la contraseña con la almacenada en la BBDD
          



            # -------------------------------------------------|

            # Si todo va bien, traemos los datos de la BBDD
            # y creamos una instancia de Inversor:

            inversor = Inversor(
                nombre=datos_usuario["nombre"],
                apellido=datos_usuario["apellido"],
                total_invertido=datos_usuario["total_invertido"],
                rendimiento=datos_usuario["rendimiento"],
                saldo=datos_usuario["saldo"],
                acciones=datos_usuario["acciones"],
            )
            print("Usuario autenticado exitosamente.")
            return inversor

            # ACA hay que usar el id_inversor para obtener el portafolio

            # -------------------------------------------
            #
            #
            # ---------------------------------------------

            # Crear una instancia de Portafolio con datos ficticios
            datos_portafolio = {
                "id_portafolio": 1,
                "total_invertido": 10000,
                "saldo": 5000,
                "acciones": [
                    {"simbolo": "AAPL", "nombre": "Apple Inc.", "cantidad": 10},
                    {"simbolo": "TSLA", "nombre": "Tesla Inc.", "cantidad": 5},
                    {"simbolo": "AMZN", "nombre": "Amazon.com Inc.", "cantidad": 2},
                ],
            }

            portafolio = Portafolio(
                id_portafolio=datos_portafolio["id_portafolio"],
                total_invertido=datos_portafolio["total_invertido"],
                saldo=datos_portafolio["saldo"],
                acciones=datos_portafolio["acciones"],
            )

            panel_de_control(datos_usuario, datos_portafolio)

            opcion = bienvenida()
        elif opcion == "2":
            cuit = ingresar_cuit()

            # Acá nos conectamos con la BBDD y buscamos al usuario
            # ------------------------------------------------|
            #
            #
            # -------------------------------------------------|

            # Si el usuario existe, llenar ésto con su pregunta secreta, respuesta secreta y contraseña
            usuario = {
                "Pregunta Secreta": "¿Cuál es tu color favorito?",
                "Respuesta Secreta": "Rojo",
                "Contraseña": "123456",
            }
            # Si todo va bien hacemos
            recuperar_contraseña(usuario)

            opcion = bienvenida()
        elif opcion == "3":
            datos_inversor = registrar_inversor()

            # Crear instancia de Inversor
            inversor = Inversor(
                cuit=datos_inversor["cuit"],
                nombre=datos_inversor["nombre"],
                apellido=datos_inversor["apellido"],
                email=datos_inversor["email"],
                contraseña=datos_inversor["contraseña"],
                pregunta_secreta=datos_inversor["pregunta_secreta"],
                respuesta_secreta=datos_inversor["respuesta_secreta"],
            )

            inversor_dao.registrar_inversor(inversor)

            # Si todo va bien hacemos
            print("Inversor creado exitosamente")
            opcion = bienvenida()
        elif opcion == "4":
            print("Gracias por usar Mis Acciones")
            return
        else:
            print("Opción inválida")
            opcion = bienvenida()


main()
