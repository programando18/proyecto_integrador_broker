class Portafolio:
    def __init__(
        self, total_invertido: float, saldo: float, acciones: list, id_inversor: int
    ):
        self.total_invertido = total_invertido
        self.saldo = saldo
        self.acciones = acciones
        self.id_inversor = id_inversor
