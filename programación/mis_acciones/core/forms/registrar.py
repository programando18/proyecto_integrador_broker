import re

from utils.validaciones import (
    validar_cuit,
    validar_nombre,
    validar_email,
    validar_contraseña,
    validar_pregunta,
    validar_respuesta,
)


def registrar_inversor():
    print("---------- Registro de Inversor ----------")

    while True:
        cuit = input("Ingrese por favor su CUIT: ").strip()
        if validar_cuit(cuit):
            break
        else:
            print("Error: El CUIT debe tener 11 dígitos numéricos.")

    while True:
        nombre = input("Ingrese su nombre: ").strip()
        if validar_nombre(nombre):
            break
        else:
            print("Error: El nombre solo debe contener letras.")

    while True:
        apellido = input("Ingrese su apellido: ").strip()
        if validar_nombre(apellido):
            break
        else:
            print("Error: El apellido solo debe contener letras.")

    while True:
        email = input("Ingrese su email: ").strip()
        if validar_email(email):
            break
        else:
            print("Error: El correo electrónico no es válido.")

    while True:
        contraseña = input("Elija una contraseña: ").strip()
        if validar_contraseña(contraseña):
            break
        else:
            print("Error: La contraseña debe tener al menos 8 caracteres.")

    while True:
        pregunta_secreta = input("Ingrese su pregunta secreta: ")
        if validar_pregunta(pregunta_secreta):
            break
        else:
            print("Error: La pregunta no puede estar vacía.")

    while True:
        respuesta_secreta = input("Ingrese su respuesta secreta: ").strip()
        if validar_respuesta(respuesta_secreta):
            break
        else:
            print("Error: La respuesta no puede estar vacía.")

    inversor = {
        "cuit": cuit,
        "nombre": nombre,
        "apellido": apellido,
        "email": email,
        "contraseña": contraseña,
        "pregunta_secreta": pregunta_secreta,
        "respuesta_secreta": respuesta_secreta,
    }
    return inversor
