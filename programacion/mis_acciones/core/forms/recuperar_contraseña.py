import email
from utils.validaciones import validar_cuit, validar_email, validar_respuesta


def formulario_ingresar_email():
    while True:
        print("   ===== RECUPERAR CONTRASEÑA =====")
        email = input("   Ingrese su correo electrónico: ")
        if validar_email(email):
            break
        else:
            print("Error: formato incorrecto")
    return email


def formulario_pregunta_secreta(inversor):
    while True:
        pregunta = inversor.pregunta_secreta
        print("   ===== PREGUNTA SECRETA =====")
        respuesta = input(f"{pregunta}?: ")
        if not validar_respuesta(respuesta):
            print("La respuesta no puede estar vacía.")
        if respuesta == inversor.respuesta_secreta:
            print("   ===== CONTRASEÑA =====")
            print(f"Su contraseña es: {inversor.contraseña}")
            print("   =======================")
            break
        else:
            print("Respuesta incorrecta.")
