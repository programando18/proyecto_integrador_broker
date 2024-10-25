from interfaces.bienvenida import bienvenida
from interfaces.panel_de_control import panel_de_control
from forms.login import formulario_login
from forms.register import registrar_inversor
from models.inversor import Inversor
from DAO.inversor_DAO import InversorDAO
from forms.recover import ingresar_email, recuperar_contraseña
from utils.validaciones import validar_contraseña, validar_email


def main():
    opcion = bienvenida()

    inversor_dao = InversorDAO()

    while opcion <= "4":
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

            # Si todo va bien, traemos los datos de la BBDD
            # y creamos una instancia de Inversor:

            # DATOS FALSOS POR AHORA
            usuario = {
                "nombre": "Christian",
                "apellido": "Caracach",
                # Datos de inversor
                "total_invertido": "0",
                "rendimiento": "0",
                "saldo": "0",
                "acciones": ("AAPL", "TSLA", "AMZN"),
            }
            panel_de_control(usuario)  # Acá mandaríamos la instancia

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
