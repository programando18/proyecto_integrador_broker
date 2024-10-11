
def validar_email(email): #validacion de mail y contraseña
    
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(patron, email) is not None

def validar_contraseña(contraseña):
   
    return len(contraseña) >= 8

def main():
    email, contraseña = formulario_login()
    
    if not validar_email(email):
        print("El correo electrónico no es válido.")
    elif not validar_contraseña(contraseña):
        print("La contraseña debe tener al menos 8 caracteres.")
    else:
        print("Inicio de sesión exitoso.")

if __name__ == "__main__":
    main()