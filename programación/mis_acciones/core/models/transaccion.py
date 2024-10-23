class Transaccion: 
    def __init__(self, id_transaccion,inversor,tipo_operacion,fecha, monto, comision): 
        self.__id_transaccion: id_transaccion
        self.__inversor = inversor
        self.__tipo = tipo_operacion
        self.__fecha = fecha
        self.__monto = monto
        self.__comision = comision 

    def obtener_id_transaccion(self): 
        return self.__id_transaccion

    def tipo_operacion(self): 
        return self.__tipo

    def realizar_transaccion(self,inversor,monto): 
          if inversor.validar_saldo_suficiente(monto):
            inversor.descontar_saldo(monto)
            # Registrar la transacción, guardar en BD, etc.
            self.__monto = monto
            self.__comision = inversor.calcular_comision(monto)
            inversor.agregar_a_historial(f"Transacción realizada por ${monto}.")
          else:
            raise ValueError("Saldo insuficiente para realizar la transacción.")

    def obtener_fecha(self): 
        return self.__fecha

    def obtener_monto(self): 
        return self.__monto

    def calcular_comision(self): 
        """Calcula la comisión como el 1.5% del monto de la transacción."""
        return self.__monto * 0.015

    def obtener_comision(self): 
        return self.__comision

