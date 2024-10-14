import re
from inversor import inversor

def validar_cuit(cuit):
 """Valida que el CUIT tenga 11 dígitos numéricos."""
 return len(cuit) == 11 and cuit.isdigit()
 
def validar_nombre(nombre): 
    return nombre.isalpha()

def validar_apellido(apellido): 
    return apellido.isalpha()

def validar_email(email): #validacion de mail
    """Valida el formato del correo electrónico."""
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(patron, email) is not None

def validar_contraseña(contraseña):
       while len(contraseña) < 6: 
        raise ValueError("Error: La contraseña debe tener al menos 6 caracteres.")
return len(contraseña) >= 8

def validar_pregunta(pregunta): 
    "Valida que la pregunta secreta no esté vacía."""
    return  bool(pregunta.strip())


def validar_respuesta(respuesta): 
    "Valida que la respuesta secreta no esté vacía."""
    return  bool(respuesta.strip())


def main():
    email, contraseña = formulario_login()
    
    if not validar_email(email):
       raise ValueError("El correo electrónico no es válido.")
    elif not validar_contraseña(contraseña):
        raise ValueError("La contraseña debe tener al menos 8 caracteres.")
    else:
        print("Inicio de sesión exitoso.")

if __name__ == "__main__":
    main()