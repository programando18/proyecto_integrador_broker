import re


def validar_cuit(cuit):
    """Valida que el CUIT tenga 11 dígitos numéricos."""
    return len(cuit) == 11 and cuit.isdigit()


def validar_nombre(nombre):
    return nombre.isalpha()


def validar_apellido(apellido):
    return apellido.isalpha()


def validar_email(email):
    """Valida el formato del correo electrónico."""
    patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(patron, email) is not None


def validar_contraseña(contraseña):
    return (len(contraseña) < 6,)


def validar_pregunta(pregunta):
    "Valida que la pregunta secreta no esté vacía." ""
    return bool(pregunta.strip())


def validar_respuesta(respuesta):
    "Valida que la respuesta secreta no esté vacía." ""
    return bool(respuesta.strip())
