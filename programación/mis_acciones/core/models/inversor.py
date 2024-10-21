
from tipo_inversor import Tipo_Inversor

class Inversor:
    def __init__(self, nombre, apellido,tipo_inversor,  total_invertido, rendimiento, saldo, acciones):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__tipo_inversor = tipo_inversor
        self.__total_invertido = total_invertido
        self.__rendimiento = rendimiento
        self.__saldo = saldo
        self.__acciones = acciones
        self.__historial = []
        self.__monto = 0
        self.__tasa_interes = 0 

    def obtener_tipo_inversor(self): 
        return self.__tipo_inversor 

    def agregar_a_historial(self, actividad):
        return self.__historial.append(actividad)

    def agregar_saldo(self, monto):
        """Agrega un monto al saldo del inversor."""
        if monto > 0:
            self.__saldo += monto
            self.agregar_a_historial(f"Se agregó ${monto} al saldo.")
        else:
            raise ValueError("El valor debe ser mayor a 0")

    def obtener_saldo(self):
        return self.__saldo

    def calcular_rendimiento(self, tasa_interes):
        """Calcula el rendimiento basado en una tasa de interés."""
        if tasa_interes > 0:
            rendimiento = self.__saldo * (tasa_interes / 100)
            self.__rendimiento += rendimiento
            self.__saldo += rendimiento
            self.agregar_a_historial(f"Se calculó un rendimiento de ${rendimiento}.")
        else:
            raise ValueError("El valor de la tasa de interes debe ser mayor a 0")

    def obtener_rendimiento(self):
        return self.__rendimiento
