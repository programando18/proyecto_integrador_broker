from utils.validaciones import validar_cuit, validar_respuesta


def ingresar_cuit():
    while True:
        cuit = input("Ingrese por favor su CUIT: ")
        if validar_cuit(cuit):
            break
        else:
            print("Error: El CUIT debe tener 11 dígitos numéricos.")
    return cuit


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
