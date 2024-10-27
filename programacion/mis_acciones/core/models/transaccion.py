class Transaccion:
    def __init__(
        self,
        id_inversor: int,
        nombre_inversor: str,
        tipo_operacion: str,
        simbolo: str,
        cantidad: int,
        precio_unidad: float,
        precio_total: float,
    ):
        self.id_inversor = id_inversor
        self.nombre_inversor = nombre_inversor
        self.tipo_operacion = tipo_operacion
        self.simbolo = simbolo
        self.cantidad = cantidad
        self.precio_unidad = precio_unidad
        self.precio_total = precio_total
