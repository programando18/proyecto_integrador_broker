import json

from interfaces.panel_de_compra_acciones import panel_de_compra_acciones
from interfaces.panel_de_venta_acciones import panel_de_venta_acciones

from models.transaccion import Transaccion


def saldo_es_suficiente(saldo, accion, cantidad):
    return saldo >= accion["precio_compra_actual"] * cantidad


def imprimir_panel(usuario, portafolio_DAO):
    portafolio = portafolio_DAO.obtener_portafolio(usuario.id_inversor)

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
    print("||| 3. Mostrar últimas transacciones    |||")
    print("||| 4. Salir                            |||")
    print("|||-------------------------------------|||")


def panel_de_control(
    usuario, portafolio, portafolio_DAO, acciones_DAO, registro_transacciones_DAO
):

    imprimir_panel(usuario, portafolio_DAO)

    opcion = input("    Qué deseas hacer?: ")

    while opcion != "4":
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
                transaccion = Transaccion(
                    portafolio.id_inversor,
                    usuario.nombre,
                    "compra",
                    accion["simbolo"],
                    cantidad,
                    accion["precio_compra_actual"],
                    accion["precio_compra_actual"] * cantidad,
                )
                registro_transacciones_DAO.registrar_transaccion(transaccion)

                print("Acción comprada con éxito")  # TODO mejorar interfaz
            else:
                print("Saldo insuficiente")

            imprimir_panel(usuario, portafolio_DAO)

            opcion = input("    Qué deseas hacer?: ")

        elif opcion == "2":
            seleccion = panel_de_venta_acciones(usuario.id_inversor, portafolio_DAO)
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
            transaccion = Transaccion(
                portafolio.id_inversor,
                usuario.nombre,
                "venta",
                accion["simbolo"],
                cantidad,
                precio,
                precio * cantidad,
            )
            registro_transacciones_DAO.registrar_transaccion(transaccion)
            print("Acción vendida con éxito")  # TODO mejorar interfaz

            imprimir_panel(usuario, portafolio_DAO)

            opcion = input("    Qué deseas hacer?: ")

        elif opcion == "3":
            transacciones = registro_transacciones_DAO.obtener_lista_transacciones(
                usuario.id_inversor
            )
            print("   ---------------ULTIMAS TRANSACCIONES--------------------   ")
            if not transacciones:
                print("No hay transacciones recientes.")
            for idx, transaccion in enumerate(transacciones, start=1):
                print(
                    f"|{idx}. {transaccion['fecha']} {transaccion['tipo_operacion']} {transaccion['simbolo']} - Cantidad: {transaccion['cantidad']} - Precio Unidad: {transaccion['precio_unidad']} - Precio Total: {transaccion['precio_total']}    "
                )
            print("   --------------------------------------------------------   ")

            opcion = input("    Qué deseas hacer?: ")

        elif opcion == "4":
            break
        else:
            raise ("Opción inválida")
