import re
from validaciones import validar_cuit, validar_nombre, validar_apellido, validar_email, validar_contraseña, validar_pregunta, validar_respuesta

def registrar_inversor():

   cuit=input("Ingrese por favor su cuit:")
   while not validar_cuit(cuit): 
        raise("Error: El CUIT debe tener 11 dígitos numéricos.")

   nombre=input("Ingrese su nombre:")
   while not validar_nombre(nombre): 
    raise("Error: El nombre solo debe contener letras.")

   apellido=input("Ingrese su apellido: ")
   while not validar_nombre(nombre): 
    raise("Error: El apellido solo debe contener letras.")

   email=input("Ingrese su mail")
   while not validar_email(email):
    raise ("Error: El correo electrónico no es válido.")

   contraseña= input("Elija una contraseña")
   while not validar_contraseña(contraseña):
    raise("Error: La contraseña debe tener al menos 8 caracteres.")

   pregunta_secreta = input("Ingrese su pregunta secreta: ")
   while not validar_pregunta(pregunta_secreta):
     raise("Error: La pregunta no puede estar vacia.")

   respuesta_secreta = input("Ingrese su respuesta secreta: ")
   while not validar_respuesta(respuesta_secreta): 
    raise("Error: La respuesta no puede estar vacia.")


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





def ingresar_email():
        print("---------- Ingreso de Correo Electrónico ----------")
        while True: 
            email_input = input("Ingrese su email: ")

            if self.validar_email(email):
                print(f"Correo electrónico ingresado correctamente, su email es: {email_input}.")
                break
            else:
                print("Correo electrónico no válido. Intente nuevamente.")
        print("---------------------------------------------------")
        return email


ingresar_email()    
registrar_inversor()
# Falta llamar a la clase y sus metodos con su objeto. 