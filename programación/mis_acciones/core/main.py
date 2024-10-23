from interfaces.bienvenida import bienvenida
from interfaces.panel_de_control import panel_de_control
from forms.login import formulario_login
from forms.register import registrar_inversor
from forms.recover import recuperar_contraseña, ingresar_cuit
from utils.validaciones import validar_contraseña, validar_email


def main():
    opcion = bienvenida()

    while opcion <= "4":
        if opcion == "1":
            datos_login = formulario_login()

            while not validar_email(datos_login[0]) or not validar_contraseña(
                datos_login[1]
            ):
                print("Datos inválidos, por favor intente de nuevo")
                datos_login = formulario_login()

            # Acá va la conexión con la BBDD y el chequeo de que el usuario exista
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
                "dni": "123123",
                "telefono": "123123",
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

            usuario = {
                "Pregunta Secreta": "¿Cuál es tu color favorito?",
                "Respuesta Secreta": "Rojo",
                "Contraseña": "123456",
            }
            # Si todo va bien hacemos
            recuperar_contraseña(usuario)

            opcion = bienvenida()
        elif opcion == "3":
            inversor = registrar_inversor()

            # Acá nos conectamos con la BBDD y registramos al usuario
            # ------------------------------------------------|
            #
            #
            # -------------------------------------------------|

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
