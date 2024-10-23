class Accion:
    def __init__(self, idAccion: int, nombre: str, simbolo: str,
                 precioCompraActual: float, precioVentaActual: float):
        self.idAccion = idAccion
        self.nombre = nombre
        self.simbolo = simbolo
        self.precioCompraActual = precioCompraActual
        self.precioVentaActual = precioVentaActual

    def __str__(self):
        return (f"Accion(idAccion={self.idAccion}, nombre='{self.nombre}', "
                f"simbolo='{self.simbolo}', precioCompraActual={self.precioCompraActual}, "
                f"precioVentaActual={self.precioVentaActual})")