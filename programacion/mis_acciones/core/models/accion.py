class Accion:
    def __init__(self, idAccion: int, nombre: str, simbolo: str,
                 precioCompraActual: float, precioVentaActual: float):
        self.__id_accion = id_accion
        self.__nombre = nombre
        self.__simbolo = simbolo
        self.__precio_compra_actual = precio_compra_actual
        self.__precio_venta_actual = precio_venta_actual

        def obtner_precio_compra(self): 
            return self.__precio_compra_actual

        def obtner_precio_venta(self): 
            return self.__precio_venta_actual

        def validar_precios(self):
            if self.precio_compra_actual < 0 or self.precio_venta_actual < 0:
                raise ValueError("Los precios no pueden ser negativos.")

    def __str__(self):
        return (f"Accion(idAccion={self.idAccion}, nombre='{self.nombre}', "
                f"simbolo='{self.simbolo}', precioCompraActual={self.precioCompraActual}, "
                f"precioVentaActual={self.precioVentaActual})")