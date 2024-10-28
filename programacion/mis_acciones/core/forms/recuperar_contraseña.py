import email
from utils.validaciones import validar_cuit, validar_email, validar_respuesta


def formulario_ingresar_email():
    while True:
        email = input("Ingrese por favor su email: ")
        if validar_email(email):
            break
        else:
            print("Error: el mail debe tener el formato info@proveedor.com")
    return email


def formulario_pregunta_secreta(inversor):
    while True:
        pregunta = inversor.pregunta_secreta
        respuesta = input(f"{pregunta}?: ")
        if not validar_respuesta(respuesta):
            print("La respuesta no puede estar vacía.")
        if respuesta == inversor.respuesta_secreta:
            print(f"Su contraseña es: {inversor.contraseña}")
            break
        else:
            print("Respuesta incorrecta.")
