import mysql
from programación.mis_acciones.core.DAO import bd_connection
from programación.mis_acciones.core.DAO import data_access_coti_dao
from programación.mis_acciones.core.models.historico_cotizacion import (
    HistoricoCotizacion,
)


class HistoricoCotizacionDao(data_access_coti_dao):
    def getall(self, tipo_operacion: int) -> list:
        with self.connection_mysql() as connect:
            try:

                cursor = connect.cursor()
                if tipo_operacion == 1:

                    query = "SELECT fecha_cotizacion,precio_compra,id_accion,cant_compra from historico_cotizacion where fecha_cotizacion= CURDATE()"
                    cursor.execute(query)
                    rows = cursor.fetchall()
                    if rows:
                        return [
                            HistoricoCotizacion(row[1], row[2], row[4], row[6])
                            for row in rows
                        ]
                    return None

                if tipo_operacion == 2:
                    query = "SELECT fecha_cotizacion,precio_venta,id_accion ,cant_venta from historico_cotizacion where fecha_cotizacion= CURDATE()"
                    cursor.execute(query)
                    rows = cursor.fetchall()
                    if rows:
                        return [
                            HistoricoCotizacion(row[1], row[3], row[4], row[5])
                            for row in rows
                        ]
                        return None
            except mysql.connector.Error as err:
                raise err
