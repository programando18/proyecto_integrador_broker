from typing import Self
from programación.mis_acciones.core.models import accion
import bd


class HistoricoCotizacion:
    
    def __init__(self,fecha,precio_compra,precio_venta,cant_compra,cant_venta,accion:accion):
        self.fecha=fecha
        self.precio_compra=precio_compra
        self.precio_venta=precio_venta
        self.cant_compra=cant_compra
        self.cant_venta=cant_venta
        self.accion=accion
    
    def mostrar_historico():
     return "Fecha: {},precio para la compra: {}, precio_venta:{},cantidad para la compra:{},cantidad para la venta: {}.".format(Self.fecha, Self.precio, Self.cantidadprecio_compra,Self.precio_venta,Self.cantidad,Self.cantidad_compra,Self.cantidad_venta)
   