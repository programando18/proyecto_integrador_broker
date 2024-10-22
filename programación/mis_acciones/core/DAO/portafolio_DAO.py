from ast import With
from sqlite3 import connect
import mysql.connector
import logging
from mysql.connector import errorcode
from Portafolio import Portafolio

class PortafolioDao(DataAccessDAO):

 def get(self,id_portafolio:int)->object:
     
       With self.__connection_mysql() as connect:
     
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
               
 def Update(Self,portafolio:Portafolio):
      
       With Self.__connection_mysql() as connect:
            
            try:
             cursor= connect.cursor()
             query=" UPDATE Portafolio SET totalInvertido=%s, saldo=%s, acciones=%s"
             cursor.execute(query,(portafolio.totalInvertido,portafolio.saldo,portafolio.acciones))
             connect.commit()
              
            except mysql.connector.Error as err:
                   raise err                