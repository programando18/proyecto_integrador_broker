from interfaces.bienvenida import bienvenida
from interfaces.panel_de_control import panel_de_control

from forms.inicio_sesion import formulario_inicio_sesion
from forms.registrar import formulario_registrar_inversor
from forms.recuperar_contraseña import (
    formulario_ingresar_email,
    formulario_pregunta_secreta,
)

from models.inversor import Inversor
from models.portafolio import Portafolio

from utils.validaciones import validar_contraseña, validar_email

from dao.inversor_DAO import InversorDAO
from dao.portafolio_DAO import PortafolioDAO
from dao.acciones_DAO import AccionesDAO
from dao.registro_transacciones_DAO import RegistroTransaccionesDAO
from dao.bd_conexion import conexion_bd


def main():
    opcion = bienvenida()

    conexion = conexion_bd()

    inversor_dao = InversorDAO(conexion)
    portafolio_dao = PortafolioDAO(conexion)
    acciones_dao = AccionesDAO(conexion)
    registro_transacciones_dao = RegistroTransaccionesDAO(conexion)

    while True:
        if opcion == "1":
            datos_login = formulario_inicio_sesion()

            while not validar_email(datos_login[0]) or not validar_contraseña(
                datos_login[1]
            ):
                print(
                    "Datos inválidos, por favor intente de nuevo"
                )  # TODO Mejorar interfaz
                datos_login = formulario_inicio_sesion()

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

            panel_de_control(
                inversor,
                portafolio,
                portafolio_dao,
                acciones_dao,
                registro_transacciones_dao,
            )

            opcion = bienvenida()
        elif opcion == "2":
            email = formulario_ingresar_email()

            usuario = {
                "Pregunta Secreta": "¿Cuál es tu color favorito?",
                "Respuesta Secreta": "Rojo",
                "Contraseña": "123456",
            }
            # Si todo va bien hacemos
            formulario_pregunta_secreta(inversor)

            opcion = bienvenida()
        elif opcion == "3":
            datos_inversor = formulario_registrar_inversor()

            inversor = Inversor(
                cuit=datos_inversor["cuit"],
                nombre=datos_inversor["nombre"],
                apellido=datos_inversor["apellido"],
                email=datos_inversor["email"],
                contraseña=datos_inversor["contraseña"],
                pregunta_secreta=datos_inversor["pregunta_secreta"],
                respuesta_secreta=datos_inversor["respuesta_secreta"],
            )

            inversor_dao.formulario_registrar_inversor(inversor)

            print("Inversor creado exitosamente")  # TODO Mejorar interfaz
            opcion = bienvenida()
        elif opcion == "4":
            print("Gracias por usar Mis Acciones")  # TODO Mejorar interfaz
            return
        else:
            print("Opción inválida")  # TODO Mejorar interfaz
            opcion = bienvenida()


main()
