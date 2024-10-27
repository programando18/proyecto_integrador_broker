from interfaces.bienvenida import bienvenida
from interfaces.panel_de_control import panel_de_control
from forms.login import formulario_login
from forms.register import registrar_inversor
from models.inversor import Inversor
from models.portafolio import Portafolio
from forms.recover import ingresar_email, recuperar_contraseña
from utils.validaciones import validar_contraseña, validar_email


from DAO.inversor_DAO import InversorDAO
from DAO.portafolio_DAO import PortafolioDAO


def main():
    opcion = bienvenida()

    inversor_dao = InversorDAO()
    portafolio_dao = PortafolioDAO()

    while True:
        if opcion == "1":
            datos_login = formulario_login()

            while not validar_email(datos_login[0]) or not validar_contraseña(
                datos_login[1]
            ):
                print(
                    "Datos inválidos, por favor intente de nuevo"
                )  # TODO Mejorar interfaz
                datos_login = formulario_login()

            inversor = inversor_dao.obtener_inversor_por_email(datos_login[0])

            if inversor is None:
                print("Usuario no encontrado")  # TODO Mejorar interfaz
                opcion = bienvenida()
                continue

            if inversor.contraseña != datos_login[1]:
                print("Contraseña incorrecta")  # TODO Mejorar interfaz
                opcion = bienvenida()
                continue

            portafolio = portafolio_dao.obtener_portafolio(inversor.id_inversor)

            panel_de_control(inversor, portafolio)

            opcion = bienvenida()
        elif opcion == "2":
            email = ingresar_email()

            # Acá nos conectamos con la BBDD y buscamos al inversor
            # inversor_dao.get_inversor(id_inversor)
            # Si el usuario existe, llenar ésto con su pregunta secreta, respuesta secreta y contraseña
            usuario = {
                "Pregunta Secreta": "¿Cuál es tu color favorito?",
                "Respuesta Secreta": "Rojo",
                "Contraseña": "123456",
            }
            # Si todo va bien hacemos
            recuperar_contraseña(inversor)

            opcion = bienvenida()
        elif opcion == "3":
            datos_inversor = registrar_inversor()

            inversor = Inversor(
                cuit=datos_inversor["cuit"],
                nombre=datos_inversor["nombre"],
                apellido=datos_inversor["apellido"],
                email=datos_inversor["email"],
                contraseña=datos_inversor["contraseña"],
                pregunta_secreta=datos_inversor["pregunta_secreta"],
                respuesta_secreta=datos_inversor["respuesta_secreta"],
            )

            inversor_dao.registrar_inversor(inversor)

            print("Inversor creado exitosamente")  # TODO Mejorar interfaz
            opcion = bienvenida()
        elif opcion == "4":
            print("Gracias por usar Mis Acciones")  # TODO Mejorar interfaz
            return
        else:
            print("Opción inválida")  # TODO Mejorar interfaz
            opcion = bienvenida()


main()
