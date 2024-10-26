from interfaces.panel_de_compra_acciones import panel_de_compra_acciones
from interfaces.panel_de_venta_acciones import panel_de_venta_acciones
from DAO.acciones_DAO import AccionesDAO

acciones_DAO = AccionesDAO()


def panel_de_control(usuario, portafolio):
    print(portafolio)
    print("   -------------------------------------   ")
    print("              MIS ACCIONES                 ")
    print("   -------------------------------------   ")
    print(f"    Usuario: {usuario['nombre']}")
    print(f"    Apellido: {usuario['apellido']}")
    print(f"    Total invertido: {portafolio['total_invertido']}")
    # print(f"    Rendimiento: {portafolio.obtener_rendimiento()}")
    print(f"    Saldo: {portafolio['saldo']}")
    print("   -------------------------------------   ")
    print("    LISTA DE ACTIVOS/TENENCIAS (simple)    ")
    print("   -------------------------------------   ")

    for i, accion in enumerate(portafolio["acciones"], start=1):
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
            accion = panel_de_compra_acciones()

            # Acá nos conectamos con la BBDD y procesamos la compra
            # ------------------------------------------------|
            #
            #
            # -------------------------------------------------|

            print(accion)

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
           raise("Opción inválida")
