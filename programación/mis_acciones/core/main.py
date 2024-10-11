from interfaces.bienvenida import bienvenida
from interfaces.panel_de_control import panel_de_control
from forms.login import formulario_login


class Usuario:
    def __init__(self, nombre, total_invertido, rendimiento):
        self.nombre = nombre
        self.total_invertido = total_invertido
        self.rendimiento = rendimiento


def main():
    opcion = bienvenida()

    usuario = Usuario(nombre="Chris", total_invertido="5000", rendimiento="1000")
    if opcion == "4":
        print("Gracias por usar Mis Acciones")
        return
    while opcion != "4":
        if opcion == "1":
            print(formulario_login())
            # print(panel_de_control(usuario))
            # Acá va la lógica de login
        elif opcion == "2":
            # Acá va el formulario de recuperar contraseña
            # Acá va la lógica de recuperar contraseña
            print("Recuperar contraseña")
        elif opcion == "3":
            # Acá va el formulario de registro
            # Acá va la lógica de registro
            print("Registrarse")
        else:
            print("Opción inválida")


main()
