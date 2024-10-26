class Portafolio:
    def __init__(
        self,
        id_portafolio: int,
        total_invertido: float,
        saldo: float,
        acciones: list,
    ):
        self.id_portafolio = id_portafolio
        self.total_invertido = total_invertido
        self.saldo = saldo
        self.acciones = acciones

    def obtener_rendimiento(self):
        return "10.00"

    def comprar_accion(self, accion):
        self.acciones.append(accion)

    def __str__(self):
        return (
            f"Portafolio(id_portafolio={self.id_portafolio}, total_invertido={self.total_invertido}, "
            f"rendimiento={self.rendimiento}, saldo={self.saldo}, acciones={self.acciones})"
        )
