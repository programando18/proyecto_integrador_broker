class Contacto:
    def __init__(self, id: int, email: str, telefono: str):
        self.id = id
        self.email = email
        self.telefono = telefono

    def __str__(self):
        return (f"Contacto(id={self.id}, email='{self.email}', "
                f"telefono='{self.telefono}')")