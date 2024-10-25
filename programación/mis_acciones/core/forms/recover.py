import email
from utils.validaciones import validar_cuit, validar_email, validar_respuesta


def ingresar_email():
    while True:
        email = input("Ingrese por favor su email: ")
        if validar_email(email):
            break
        else:
            print("Error: el mail debe tener el formato info@proveedor.com")
    return email


def recuperar_contraseña(inversor):
    while True:
        pregunta = inversor["Pregunta Secreta"]
        respuesta = input(f"{pregunta}: ")
        if not validar_respuesta(respuesta):
            print("La respuesta no puede estar vacía.")
        if respuesta == inversor["Respuesta Secreta"]:
            print(f"Su contraseña es: {inversor['Contraseña']}")
            break
        else:
            print("Respuesta incorrecta.")
