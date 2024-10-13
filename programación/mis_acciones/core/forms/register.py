import re

def registrar_inversor():

   cuit=input("Ingrese por favor su cuit:")
   nombre=input("Ingrese su nombre:")
   apellido=input("Ingrese su apellido: ")
   email=input("Ingrese su mail")
   contraseña= input("Elija una contraseña")
   pregunta_secreta = input("Ingrese su pregunta secreta: ")
   respuesta_secreta = input("Ingrese su respuesta secreta: ")

   inversor = {
             'CUIT':  cuit,
             'Nombre': nombre,
             'Apellido': apellido,
             'Email': email,
             'Contraseña': contraseña,
             'Pregunta Secreta': pregunta_secreta,
             'Respuesta Secreta': respuesta_secreta
    }
   print("Registro exitoso!") 






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