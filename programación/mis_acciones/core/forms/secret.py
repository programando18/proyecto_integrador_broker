def configurar_pregunta_secreta():
    pregunta = input("Establezca su pregunta secreta: ")
    respuesta = input("Establezca la respuesta a su pregunta secreta: ")
    return pregunta, respuesta

def recuperar_contrasena(pregunta, respuesta_correcta):
    respuesta_usuario = input(f"{pregunta} ")
    
    if respuesta_usuario == respuesta_correcta:
        return "Respuesta correcta. Su contraseña es: 'mi_contraseña_secreta'"
    else:
        return "Respuesta incorrecta. No se puede recuperar la contraseña."