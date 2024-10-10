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