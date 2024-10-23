from abc import ABC,abstractmethod

class DataAccessCotiDAO(ABC): 

    @abstractmethod  
    def get_all(self,id:int):
         pass