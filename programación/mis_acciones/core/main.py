from interfaces.bienvenida import bienvenida
from forms.login import formulario_login


def main():
    opcion = bienvenida()
    if opcion == "4":
        print("Gracias por usar Mis Acciones")
        return
    while opcion != "4":
        if opcion == "1":
            print(formulario_login())
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
