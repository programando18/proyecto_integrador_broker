
import mysql
from programación.mis_acciones.core.DAO import DataAccessCotiDAO


class HistoricoCotizacionDao(DataAccessCotiDAO):
    def getall(self,tipo_operacion:int)->list:
     with self.connection_mysql() as connect:
        try:        
            
           cursor = connect.cursor()
           if tipo_operacion== 1:

                 query= "SELECT fecha_cotizacion,cant_compra,id_accion from historico_cotizacion where fecha_cotizacion== today()"
                 cursor.execute(query)          
                 rows= cursor.fetchall()
                 if rows:
                    return [historicoCotizacion(row[1],row[5],row[6]) for row in rows]
                 return None  
       
           if tipo_operacion== 2:
                  query= "SELECT fecha_cotizacion,cant_venta,id_accion from historico_cotizacion where fecha_cotizacion== today()"
                  cursor.execute(query)    
                  rows= cursor.fetchall()
                  if rows:
                    return [historicoCotizacion(row[1],row[4],row[6]) for row in rows]
                    return None  
        except mysql.connector.Error as err:
                   raise err        