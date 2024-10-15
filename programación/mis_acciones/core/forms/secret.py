from validaciones import validar_pregunta, validar_respuesta,validar_contraseña


def configurar_pregunta_secreta():
    pregunta = input("Establezca su pregunta secreta: ")
    while not validar_pregunta(pregunta): 
        raise ValueError("Error,la pregunta no debe estar vacia.")


    respuesta = input("Establezca la respuesta a su pregunta secreta: ")
    while not validar_respuesta(respuesta): 
        raise ValueError("Error,la respuesta no debe estar vacia.")

    contraseña = input("Establezca su contraseña: ")
    validar_contraseña(contraseña)  

    return pregunta, respuesta, contraseña
   

def recuperar_contraseña(inversor):
    pregunta = inversor['Pregunta Secreta']
    respuesta_usuario = input(f"{pregunta} ")
    
    if respuesta_usuario == inversor['Respuesta Secreta']:
        return "Respuesta correcta. Su contraseña es: 'mi_contraseña_secreta'"
    else:
        return "Respuesta incorrecta. No se puede recuperar la contraseña."