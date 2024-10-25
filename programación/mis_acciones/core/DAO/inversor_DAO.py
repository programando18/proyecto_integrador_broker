from pyclbr import Class
import string
import mysql.connector
import logging
from mysql.connector import errorcode
from programación.mis_acciones.core.DAO import data_access_dao
from inversor_DAO import inversor

Class inversorDAO (DataAccessInversorDAO): 
    
def get_inversor(self,email:string)->object:
        
  with self.__connect_to_mysql()as conn:
        try:
            cursor = conn.cursor()
            query="Select * from inversor where email=%s"
               
            cursor.execute(query,(id,))  
            row = cursor.fetchone()
            if row:
                return object(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11])          
                    return None
        except mysql.connector.Error as err:
                   raise err   
         