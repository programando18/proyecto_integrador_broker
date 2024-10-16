from interfaces.bienvenida import bienvenida
from interfaces.panel_de_control import panel_de_control
from forms.login import formulario_login
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

            # Si todo va bien:

            opcionPanel = panel_de_control(usuario)
            while opcionPanel != "4":
                if opcionPanel == "1":
                    print("Comprar")
                elif opcionPanel == "2":
                    print("Vender")
                elif opcionPanel == "3":
                    print("Ver gráfico")
                else:
                    print("Opción inválida")
            # Acá va la lógica de login
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
