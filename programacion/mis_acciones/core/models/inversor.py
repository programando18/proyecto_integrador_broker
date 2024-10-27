class Inversor:
    def __init__(
        self,
        id_inversor,
        cuit="",
        nombre="",
        apellido="",
        email="",
        contraseña="",
        pregunta_secreta="",
        respuesta_secreta="",
    ):
        self.id_inversor = id_inversor
        self.cuit = cuit
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.contraseña = contraseña
        self.pregunta_secreta = pregunta_secreta
        self.respuesta_secreta = respuesta_secreta

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.id_inversor}"
