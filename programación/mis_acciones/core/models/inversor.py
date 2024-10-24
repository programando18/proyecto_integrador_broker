from models.tipo_inversor import Tipo_Inversor


class Inversor:
    def __init__(
        self,
        cuit="",
        nombre="",
        apellido="",
        email="",
        contraseña="",
        pregunta_secreta="",
        respuesta_secreta="",
        tipo_inversor="",
        total_invertido="",
        rendimiento="",
        saldo="",
        acciones=(),
    ):
        self.cuit = cuit
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.contraseña = contraseña
        self.pregunta_secreta = pregunta_secreta
        self.respuesta_secreta = respuesta_secreta
        self.tipo_inversor = tipo_inversor
        self.total_invertido = total_invertido
        self.rendimiento = rendimiento
        self.saldo = saldo
        self.acciones = acciones
        self.historial = []
        self.monto = 0
        self.tasa_interes = 0
