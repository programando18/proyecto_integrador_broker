from interfaces.panel_de_compra_acciones import panel_de_compra_acciones
from interfaces.panel_de_venta_acciones import panel_de_venta_acciones
from DAO.acciones_DAO import AccionesDAO
from DAO.portafolio_DAO import PortafolioDAO
import json

acciones_DAO = AccionesDAO()
portafolio_DAO = PortafolioDAO()


def saldo_es_suficiente(saldo, accion, cantidad):
    return saldo >= accion["precio_compra_actual"] * cantidad


def panel_de_control(usuario, portafolio):
    print("   -------------------------------------   ")
    print("              MIS ACCIONES                 ")
    print("   -------------------------------------   ")
    print(f"    Usuario: {usuario.nombre}")
    print(f"    Apellido: {usuario.apellido}")
    print(f"    Total invertido: ${portafolio.total_invertido}")
    # print(f"    Rendimiento: {portafolio.obtener_rendimiento()}")
    print(f"    Saldo: ${portafolio.saldo}")
    print("   -------------------------------------   ")
    print("    LISTA DE ACTIVOS/TENENCIAS (simple)    ")
    print("   -------------------------------------   ")

    if not portafolio.acciones:
        print("    No hay acciones")  # TODO mejorar interfaz
    else:
        json_acciones = json.loads(portafolio.acciones)
        for i, accion in enumerate(json_acciones, start=1):
            print(
                f"    {i}. {accion['simbolo']} - {accion['nombre']} - Cantidad: {accion['cantidad']}"
            )

    print(" ")
    print(" ")
    print("   -------------------------------------   ")
    print("   --------------ACCIONES---------------   ")
    print("   -------------------------------------   ")
    print(" ")
    print("|||-------Seleccione una opción:--------|||")
    print("||| 1. Comprar Acciones                 |||")
    print("||| 2. Vender Acciones                  |||")
    print("||| 3. Salir                            |||")
    print("|||-------------------------------------|||")

    opcion = input("    Qué deseas hacer?: ")

    while opcion != "3":
        if opcion == "1":
            seleccion = panel_de_compra_acciones()
            accion = seleccion["accion"]
            cantidad = seleccion["cantidad"]

            print(accion)
            if saldo_es_suficiente(portafolio.saldo, accion, cantidad):
                portafolio_DAO.agregar_accion(
                    portafolio.id_inversor,
                    {
                        "simbolo": accion["simbolo"],
                        "nombre": accion["nombre"],
                        "cantidad": cantidad,
                    },
                )
                acciones_DAO.descontar_acciones(accion["simbolo"], cantidad)
                portafolio_DAO.descontar_saldo(
                    portafolio.id_inversor, accion["precio_compra_actual"] * cantidad
                )
                print("Acción comprada con éxito")
                print(portafolio)
            else:
                print("Saldo insuficiente")

            opcion = input("¿Deseas hacer algo más? (s/n): ")
        elif opcion == "2":
            accion = panel_de_venta_acciones()

            # Acá nos conectamos con la BBDD y procesamos la venta
            # ------------------------------------------------|
            #
            #
            # -------------------------------------------------|

            print(accion)

            opcion = input("¿Deseas hacer algo más? (s/n): ")
        elif opcion == "3":
            break
        else:
            raise ("Opción inválida")
