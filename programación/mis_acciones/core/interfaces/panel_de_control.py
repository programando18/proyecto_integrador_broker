from interfaces.panel_de_compra_acciones import panel_de_compra_acciones
from interfaces.panel_de_venta_acciones import panel_de_venta_acciones


def panel_de_control(usuario):
    print("   -------------------------------------   ")
    print("              MIS ACCIONES                 ")
    print("   -------------------------------------   ")
    if len(usuario["nombre"]) > 29:
        print(f"    Usuario: {usuario['nombre'][:26]}")
    else:
        print(f"    Usuario: {usuario['nombre']}")
    if len(usuario["apellido"]) > 29:
        print(f"    Apellido: {usuario['apellido'][:26]}")
    else:
        print(f"    Apellido: {usuario['apellido']}")
    if len(usuario["total_invertido"]) > 29:
        print(f"    Total invertido: {usuario['total_invertido'][:17]}")
    else:
        print(f"    Total invertido: {usuario['total_invertido']}")
    if len(usuario["rendimiento"]) > 29:
        print(f"    Rendimiento: {usuario['rendimiento'][:23]}")
    else:
        print(f"    Rendimiento: {usuario['rendimiento']}")
    if len(usuario["saldo"]) > 29:
        print(f"    Saldo: {usuario['saldo'][:23]}")
    else:
        print(f"    Saldo: {usuario['saldo']}")
    print("   -------------------------------------   ")
    print("    LISTA DE ACTIVOS/TENENCIAS (simple)    ")
    print("   -------------------------------------   ")

    for i, accion in enumerate(usuario["acciones"], start=1):
        print(f"    {i}. {accion}")
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
            print("Opción inválida")
