class Contacto:
    def __init__(self, id: int, email: str, telefono: str):
        self.__id = id
        self.__email = email
        self.__telefono = telefono

    def obtener_email(self): 
        return self.__email

    def obtener_telefono(self): 
        return self.__telefono

    def __str__(self):
        return (f"Contacto(id={self.__id}, su email es: '{self.__email}', "
                f"su telefono: ='{self.__telefono}')")