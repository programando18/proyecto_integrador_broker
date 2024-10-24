from interfaces.bienvenida import bienvenida
from interfaces.panel_de_control import panel_de_control
from forms.login import formulario_login
from forms.register import registrar_inversor
from models.inversor import Inversor
from models.portafolio import Portafolio
from DAO.inversor_DAO import InversorDAO
from forms.recover import recuperar_contraseña, ingresar_cuit
from utils.validaciones import validar_contraseña, validar_email
from DAO.bd_connection import connection_mysql


def main():
    connection_mysql()
    opcion = bienvenida()

    inversor_dao = InversorDAO()

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
            #
            #
            # -------------------------------------------------|

            # ACA, MILI. Si el usuario existe y la contraseña es correcta, tenemos que usar sus datos para crear ésta instancia de Inversor
            datos_usuario = {
                # Datos de contacto
                "nombre": "Christian",
                "apellido": "Caracach",
                # Datos de inversor
                "total_invertido": "0",
                "rendimiento": "0",
                "saldo": "0",
                "acciones": ("AAPL", "TSLA", "AMZN"),
            }

            # Creamos una instancia de Inversor con los datos obtenidos
            usuario = Inversor(
                nombre=datos_usuario["nombre"],
                apellido=datos_usuario["apellido"],
                total_invertido=datos_usuario["total_invertido"],
                rendimiento=datos_usuario["rendimiento"],
                saldo=datos_usuario["saldo"],
                acciones=datos_usuario["acciones"],
            )

            # ACA hay que usar el id_inversor para obtener el portafolio

            # -------------------------------------------
            #
            #
            # ---------------------------------------------

            portafolio = Portafolio()

            panel_de_control(datos_usuario, datos_portafolio)

            opcion = bienvenida()
        elif opcion == "2":
            # Cambiar ésto, tiene que ser email
            cuit = ingresar_cuit()

            # Acá nos conectamos con la BBDD y buscamos al usuario
            # ACA TENES QUE TRABAJAR EVE.
            # TAREAS
            # Pedirle al usuario que ingrese el email, no el CUIT.
            # Crear método en InversorDAO para obtener un inversor por email.
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
