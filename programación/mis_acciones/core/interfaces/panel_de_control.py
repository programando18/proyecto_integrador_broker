def panel_de_control(usuario):
    print(usuario["nombre"])
    print("|||-------------------------------------|||")
    print("|||           MIS ACCIONES              |||")
    print("|||-------------------------------------|||")
    if len(usuario["nombre"]) > 29:
        print(f"||| Usuario: {usuario['nombre'][:26]}")
    else:
        print(f"||| Usuario: {usuario['nombre']}")
    if len(usuario["apellido"]) > 29:
        print(f"||| Apellido: {usuario['apellido'][:26]}")
    else:
        print(f"||| Apellido: {usuario['apellido']}")
    if len(usuario["total_invertido"]) > 29:
        print(f"||| Total invertido: {usuario['total_invertido'][:17]}")
    else:
        print(f"||| Total invertido: {usuario['total_invertido']}")
    if len(usuario["rendimiento"]) > 29:
        print(f"||| Rendimiento: {usuario['rendimiento'][:23]}")
    else:
        print(f"||| Rendimiento: {usuario['rendimiento']}")
    if len(usuario["saldo"]) > 29:
        print(f"||| Saldo: {usuario['saldo'][:23]}")
    else:
        print(f"||| Saldo: {usuario['saldo']}")
    print("|||-------------------------------------|||")
    print("||| Activos:                            |||")

    for i, accion in enumerate(usuario["acciones"], start=1):
        print(f"||| {i}. {accion}")

    print("|||-------------------------------------|||")

    print("Seleccione una opción:")
    print("1. Comprar Acciones")
    print("2. Vender Acciones")
    print("3. Ver gráfico")
    print("4. Salir")
    opcion = input("Qué deseas hacer?: ")

    while opcion != "4":
        if opcion == "1":
            print("Comprar")
        elif opcion == "2":
            print("Vender")
        elif opcion == "3":
            print("Ver gráfico")
        elif opcion == "4":
            break
        else:
            print("Opción inválida")
