from ast import With


class PortafolioDao(DataAccessDAO):

 def get(self,id_portafolio:int)->object:
     
    With self.__connection_mysql() as conn:
        try:
             cursor = conn.cursor()
             query="Select saldo, total_invertido,nombre.Inversor + apellido.Inversor,nombre_accion.accion as accion FROM portafolio
                     join Inversor on id_inversor.inversor=id_inversor.portafolio
                     join accion on id_accion.accion=id_accion.portafolio where id_portafolio=s%"
               
             cursor.execute(query,(id,))  
             row = cursor.fetchone()
              if row:
                return object(row[0],row[1],row[2],row[3]) 
              return None
             except mysql.connector.Error as err:
                   raise err   
               
 def Update(self,portafolio:portafolio):
      
       With self.__connect_to_mysql()as conn:
           try:
              cursor= conn.cursor()
              query=" UPDATE Portafolio SET totalInvertido=%s, saldo=%s, acciones=%s"
                     cursor.execute(query,(portafolio.totalInvertido,portafolio.saldo,portafolio.acciones))
              conn.commit()
              
                 exceptmysql.connector.Error as err:
                   raise err                