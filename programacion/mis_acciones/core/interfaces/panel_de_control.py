import json

from interfaces.panel_de_compra_acciones import panel_de_compra_acciones
from interfaces.panel_de_venta_acciones import panel_de_venta_acciones

from dao.acciones_DAO import AccionesDAO
from dao.portafolio_DAO import PortafolioDAO
from dao.bd_conexion import conexion_bd

conexion = conexion_bd()

acciones_DAO = AccionesDAO(conexion)
portafolio_DAO = PortafolioDAO(conexion)


def saldo_es_suficiente(saldo, accion, cantidad):
    return saldo >= accion["precio_compra_actual"] * cantidad


def imprimir_panel(usuario, portafolio):
    print("   -------------------------------------   ")
    print("              MIS ACCIONES                 ")
    print("   -------------------------------------   ")
    print(f"    Usuario: {usuario.nombre}")
    print(f"    Apellido: {usuario.apellido}")
    print(
        f"    Total invertido: ${portafolio_DAO.obtener_total_invertido(portafolio.id_inversor, portafolio)}"
    )
    print(
        f"    Rendimiento: ${portafolio_DAO.obtener_rendimiento(portafolio.id_inversor, portafolio)}"
    )
    print(f"    Saldo: ${portafolio.saldo}")
    print("   -------------------------------------   ")
    print("    LISTA DE ACTIVOS/TENENCIAS    ")
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
    print("|||-------Seleccione una opción:--------|||")
    print("||| 1. Comprar Acciones                 |||")
    print("||| 2. Vender Acciones                  |||")
    print("||| 3. Salir                            |||")
    print("|||-------------------------------------|||")


def panel_de_control(usuario, portafolio):
    print(portafolio)

    imprimir_panel(usuario, portafolio)

    opcion = input("    Qué deseas hacer?: ")

    while opcion != "3":
        if opcion == "1":
            seleccion = panel_de_compra_acciones()
            accion = seleccion["accion"]
            cantidad = seleccion["cantidad"]
            comisión = round(float(accion["precio_compra_actual"] * 0.15), 2)

            print(
                "El precio actual de la acción es: $", accion["precio_compra_actual"]
            )  # TODO Mejorar interfaz
            print("El costo de la comisión del broker es: $", comisión)
            opcion = input("¿Desea continuar con la compra? (s/n): ")

            if opcion != "s":
                continue

            if saldo_es_suficiente(portafolio.saldo, accion, cantidad):
                portafolio_DAO.agregar_accion(
                    portafolio.id_inversor,
                    {
                        "simbolo": accion["simbolo"],
                        "nombre": accion["nombre"],
                        "cantidad": cantidad,
                        "precio_compra": accion["precio_compra_actual"],
                    },
                )
                acciones_DAO.descontar_acciones(accion["simbolo"], cantidad)
                portafolio_DAO.descontar_saldo(
                    portafolio.id_inversor,
                    accion["precio_compra_actual"] * cantidad + comisión,
                )
                print("Acción comprada con éxito")  # TODO mejorar interfaz
            else:
                print("Saldo insuficiente")

            imprimir_panel(usuario, portafolio)

            opcion = input("    Qué deseas hacer?: ")

        elif opcion == "2":
            seleccion = panel_de_venta_acciones(json.loads(portafolio.acciones))
            accion = seleccion["accion"]
            cantidad = seleccion["cantidad"]
            precio = acciones_DAO.obtener_precio_accion(accion["simbolo"])
            comisión = round(float(precio * cantidad * 0.15), 2)

            print("El precio actual de la acción es: $", precio)
            print("El costo de la comisión del broker es: $", comisión)
            opcion = input("¿Desea continuar con la venta? (s/n): ")

            if opcion != "s":
                continue
            portafolio_DAO.descontar_accion(
                portafolio.id_inversor, accion["simbolo"], cantidad
            )
            acciones_DAO.agregar_acciones(accion["simbolo"], cantidad)
            portafolio_DAO.aumentar_saldo(portafolio.id_inversor, precio * cantidad)
            print("Acción vendida con éxito")  # TODO mejorar interfaz

            imprimir_panel(usuario, portafolio)

            opcion = input("    Qué deseas hacer?: ")

        elif opcion == "3":
            break
        else:
            raise ("Opción inválida")
