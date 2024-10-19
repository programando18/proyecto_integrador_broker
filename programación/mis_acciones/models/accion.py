class Accion:
    def __init__(self, idAccion: int, nombre: str, idEmpresa: int,
                 cantidadCompraDiaria: float, cantidadVentaDiaria: float,
                 precioCompraActual: float, precioVentaActual: float,
                 minimoDiario: float, maximoDiario: float,
                 precioApertura: float, precioUltCierre: float):
        self.idAccion = idAccion
        self.nombre = nombre
        self.idEmpresa = idEmpresa
        self.cantidadCompraDiaria = cantidadCompraDiaria
        self.cantidadVentaDiaria = cantidadVentaDiaria
        self.precioCompraActual = precioCompraActual
        self.precioVentaActual = precioVentaActual
        self.minimoDiario = minimoDiario
        self.maximoDiario = maximoDiario
        self.precioApertura = precioApertura
        self.precioUltCierre = precioUltCierre

    def __str__(self):
        return (f"Accion(idAccion={self.idAccion}, nombre='{self.nombre}', "
                f"idEmpresa={self.idEmpresa}, cantidadCompraDiaria={self.cantidadCompraDiaria}, "
                f"cantidadVentaDiaria={self.cantidadVentaDiaria}, precioCompraActual={self.precioCompraActual}, "
                f"precioVentaActual={self.precioVentaActual}, minimoDiario={self.minimoDiario}, "
                f"maximoDiario={self.maximoDiario}, precioApertura={self.precioApertura}, "
                f"precioUltCierre={self.precioUltCierre})")