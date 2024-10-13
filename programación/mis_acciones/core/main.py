from interfaces.bienvenida import bienvenida
from interfaces.panel_de_control import panel_de_control
from forms.login import formulario_login


class Usuario:
    def __init__(self, nombre, total_invertido, rendimiento):
        self.nombre = nombre
        self.total_invertido = total_invertido
        self.rendimiento = rendimiento
        self.saldo = "1000"
        self.acciones = ["AAPL", "AMZN", "GOOGL", "MSFT", "TSLA"]


def main():
    opcion = bienvenida()

    usuario = Usuario(nombre="Chris", total_invertido="5000", rendimiento="1000")
    if opcion == "4":
        print("Gracias por usar Mis Acciones")
        return
    while opcion != "4":
        if opcion == "1":
            datos_login = formulario_login()

            # Validar datos_login
            # Si están validados entonces:
            opcion = panel_de_control(usuario)

            while opcion != "4":
                if opcion == "1":
                    print("Comprar")
                elif opcion == "2":
                    print("Vender")
                elif opcion == "3":
                    print("Ver gráfico")
                else:
                    print("Opción inválida")
                opcion = panel_de_control(usuario)
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
