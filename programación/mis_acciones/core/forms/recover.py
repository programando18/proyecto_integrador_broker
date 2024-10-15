from validaciones import validar_cuit, validar_respuesta

def recuperar_contraseña(inversor):
    # Solicitar el CUIT del usuario
    cuit = input("Ingrese su CUIT: ")

    if not validar_cuit(cuit): 
        raise ValueError("El CUIT debe tener 11 números.")
    
    if inversor['CUIT'] != cuit:
        raise ValueError("El CUIT no fue encontrado.")

    # Preguntar la pregunta secreta
    pregunta = inversor['Pregunta Secreta']
    respuesta = input(f"{pregunta}: ")

    if not validar_respuesta(respuesta): 
        raise ValueError("La respuesta no puede estar vacía.")

    if respuesta == inversor['Respuesta Secreta']:
        print(f"Su contraseña es: {inversor['Contraseña']}")
    else:
        raise ValueError("Respuesta incorrecta.")

