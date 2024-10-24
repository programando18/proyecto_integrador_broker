import mysql.connector
import logging
from mysql.connector import errorcode
from portafolio_DAO import portafolio
from programación.mis_acciones.core.DAO import DataAccessDAO
from programación.mis_acciones.core.DAO import bd_connection
from programación.mis_acciones.core.models import accion, portafolio

class PortafolioDao(DataAccessDAO):

  def get(self,id_portafolio:int)->object:
     
       with self.connection_mysql() as connect:
     
          try:
            cursor = connect.cursor()
            query= "SELECT saldo, total_invertido, id_accion FROM Portafolio  WHERE id_portafolio=%s "
            cursor.execute(query,(id,))  
            row = cursor.fetchone()   
               
            
            if row:
                return object(row[0],row[1],row[2],row[3]) 
            return None
          except mysql.connector.Error as err:
                   raise err   
               
  def Update(self,portafolio:portafolio):
      
       with self.connection_mysql() as connect:
            
          try:
             cursor= connect.cursor()
             query="UPDATE Portafolio SET totalInvertido=%s, saldo=%s, acciones=%s"
             cursor.execute(query,(portafolio.totalInvertido,portafolio.saldo,portafolio.acciones))
             connect.commit()
              
          except mysql.connector.Error as err:
                   raise err                
               
  def get_all(self,id_portafolio:int)->list:            
        with self.connection_mysql() as connect:
            
           try:
                cursor = connect.cursor()
                query=" SELECT simbolo_accion,nombre_accion,precio_compra_actual,precio_venta_actual FROM accion,portafolio WHERE accion.id_accion =portafolio.id_accion AND portafolio.id_portafolio = %s"
                cursor.execute(query)
                rows = cursor.fetchall()
                return [accion (row[1],row[2],row[3],row[4]) for row in rows]
           
           except mysql.connector.Error as err:
                   raise err         
  def Create(self,portafolio:portafolio):
       with  self.connection_mysql() as connect:           
       
          try:
                cursor = connect.cursor()    
                query="INSERT INTO portafolio (id_inversor,id_accion,saldo,total_invertido)VALUES(%s,%s,%s,%s,%s)" 
                cursor.execute(query,(portafolio.id_inversor,portafolio.id_accion,portafolio.saldo,portafolio.total_invertido)) 
                connect.commit()
       
          except mysql.connector.Error as err:
                   raise err   

  def Delete (self,id_portafolio:int):
      with self.connection_mysql() as connect:  
          
          try:    
             cursor = connect.cursor()  
             query = "DELETE FROM portafolio WHERE id_portafolio = %s"
             cursor.execute(query,(id_portafolio))   
             connect.commit()      
          except mysql.connector.Error as err:  
               
