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
   print("Registro exitoso!")import re 

def ingresar_email(self):
        print("---------- Ingreso de Correo Electrónico ----------")
        while True: 
            email_input = input("Ingrese su email: ")
            if self.validar_email(email_input):
                print(f"Correo electrónico ingresado correctamente, su email es: {email_input}.")
                self.email = email_input  # Guardamos el email ingresado
                break
            else:
                print("Correo electrónico no válido. Intente nuevamente.")
        print("---------------------------------------------------")
        return self.email

def validar_email(self, email):
        """Encapsula la validación del formato del correo electrónico."""
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return True
        return False

def obtener_email(self):
        """Permite acceder al email almacenado de forma controlada."""
        if self.email:
            return self.email
        else:
            return "No se ha ingresado un correo electrónico."


form_ingreso_email()    

