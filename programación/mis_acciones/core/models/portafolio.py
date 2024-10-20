<<<<<<< HEAD
# class Portafolio:
#     def __init__(self, ): 
=======
class Portafolio:
    def __init__(self, id_portafolio: int, totalInvertido: float, rendimiento: float, saldo: float, acciones: list):
        self.id_portafolio = id_portafolio
        self.totalInvertido = totalInvertido
        self.rendimiento = rendimiento
        self.saldo = saldo
        self.acciones = acciones  # Se espera que sea una lista de objetos de tipo Accion

    def __str__(self):
        return (f"Portafolio(id_portafolio={self.id_portafolio}, totalInvertido={self.totalInvertido}, "
                f"rendimiento={self.rendimiento}, saldo={self.saldo}, acciones={self.acciones})")
>>>>>>> 5e75cb9c2d2616f81aefadc7ce0a9607ec43bff8
