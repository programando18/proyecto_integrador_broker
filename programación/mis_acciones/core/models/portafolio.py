class Portafolio:
    def __init__(self, id_portafolio=0, saldo=0.0, acciones=[], id_inversor=0):
        self.id_portafolio = id_portafolio
        self.saldo = saldo
        self.acciones = acciones
        self.id_inversor = id_inversor

    def __str__(self):
        return f"Portafolio {self.id_portafolio} - Saldo: {self.saldo} - Acciones: {self.acciones}"
