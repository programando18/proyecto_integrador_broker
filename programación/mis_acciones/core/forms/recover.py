def recuperar_contraseña(inversor):
    # Solicitar el CUIT del usuario
    cuit = input("Ingrese su CUIT: ")
    
    # Verificar si el CUIT coincide
    if inversor['CUIT'] == cuit:
        # Preguntar la pregunta secreta
        respuesta = input(f"Pregunta secreta: {inversor['Pregunta Secreta']}\nRespuesta: ")
        
        # Verificar la respuesta
        if respuesta == inversor['Respuesta Secreta']:
            print(f"Su contraseña es: {inversor['Contraseña']}")
        else:
            print("Respuesta incorrecta.")
    else:
        print("CUIT no encontrado.")