def formulario_inicio_sesion():
    print("   ===== INICIAR SESION =====")
    email = input("   Ingrese su correo electrónico: ")
    contraseña = input("   Ingrese su contraseña: ")
    print("   ==========================")
    return [email.strip(), contraseña.strip()]
