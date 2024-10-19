from interfaces.bienvenida import bienvenida
from interfaces.panel_de_control import panel_de_control
from forms.login import formulario_login
from utils.validaciones import validar_contraseña, validar_email
from models.inversor import Inversor


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

            opcionPanel = panel_de_control(usuario)  # Acá mandaríamos la instancia

            # Usuario selecciona opción del panel
            while opcionPanel != "4":
                if opcionPanel == "1":
                    print("Comprar")
                elif opcionPanel == "2":
                    print("Vender")
                elif opcionPanel == "3":
                    print("Ver gráfico")
                elif opcionPanel == "4":
                    break
                else:
                    print("Opción inválida")

            opcion = bienvenida()

        elif opcion == "2":
            # Acá va el formulario de recuperar contraseña
            # Acá va la lógica de recuperar contraseña
            print("Recuperar contraseña")
        elif opcion == "3":
            # Acá va el formulario de registro
            # Acá va la lógica de registro
            print("Registrarse")
        elif opcion == "4":
            print("Gracias por usar Mis Acciones")
            return
        else:
            print("Opción inválida")


main()
