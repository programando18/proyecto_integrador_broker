class Inversor:
    def __init__(
        self, nombre, apellido, cuil, email, contraseña, tasa_interes, rendimiento
    ):
        # FALTA LOS DEMAS ATRIBUTOS, ENTRAN EN SPRINT 2 FRANCO SE ENCARGA
        self.__nombre = nombre
        self.__historial = []
        self.__saldo = 0
        self.__monto = 0
        self.__tasa_interes = 0
        self.__rendimiento = 0

    def agregar_a_historial(self, actividad):
        self.__historial.append(actividad)

    def obtener_historial(self):
        return self.__historial

    def agregar_saldo(self, monto):
        """Agrega un monto al saldo del inversor."""

    if monto > 0:
        self.__saldo += monto
        self.agregar_a_historial(f"XSe agregó ${monto} al saldo.")
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
