from inversor import inversor

def validar_cuit():
    #   cuit = input("Ingrese por favor su CUIT (11 dígitos): ")
    # while len(cuit) != 11 or not cuit.isdigit():
    #     print("Error: El CUIT debe tener 11 dígitos numéricos.")
    #     cuit = input("Ingrese por favor su CUIT (11 dígitos): ")
    return ""

def validar_nombre(nombre): 
    #  while not nombre.isalpha():
    #     print("Error: El nombre debe contener solo letras.")
    #     nombre = input("Ingrese su nombre: ")
    return nombre.isalpha()

def validar_apellido(apellido): 
    #falta logica similar al nombre
    return apellido.isalpha()


def validar_email(email): #validacion de mail
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(patron, email) is not None


def validar_contraseña(contraseña):
    #    while len(contraseña) < 6: modificar esto
    #     print("Error: La contraseña debe tener al menos 6 caracteres.")
    return len(contraseña) >= 8

def validar_pregunta(): 
    "Valida que la pregunta secreta no esté vacía."""
    return ""


def validar_respuesta(): 
    "Valida que la respuesta secreta no esté vacía."""
    return ""


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