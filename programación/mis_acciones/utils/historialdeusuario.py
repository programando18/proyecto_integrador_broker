class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.historial = []

    def agregar_a_historial(self, actividad):
        self.historial.append(actividad)

    def obtener_historial(self):
        return self.historial