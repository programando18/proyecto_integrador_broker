import re 

def ingresar_email(self):
        print("---------- Ingreso de Correo Electrónico ----------")
        while True: 
            email_input = input("Ingrese su email: ")

            if self.validar_email(email_input):
                print(f"Correo electrónico ingresado correctamente, su email es: {email_input}.")
                self.__email = email_input  # Guardamos el email ingresado
                break
            else:
                print("Correo electrónico no válido. Intente nuevamente.")
        print("---------------------------------------------------")
        return self.__email

def validar_email(self, email):
        """Encapsula la validación del formato del correo electrónico."""
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return True
        return False

def obtener_email(self):
        """Permite acceder al email almacenado de forma controlada."""
        if self.__email:
            return self.__email
        else:
            return "No se ha ingresado un correo electrónico."


ingresar_email()    

# Falta llamar a la clase y sus metodos con su objeto. 