def panel_de_control(usuario):
    print("|||-------------------------------------|||")
    print("|||           MIS ACCIONES              |||")
    print("|||-------------------------------------|||")
    if len(usuario.nombre) > 29:
        print(f"||| Usuario: {usuario.nombre[:26]}... |||")
    else:
        print(f"||| Usuario: {usuario.nombre:<29} |||")
    if len(usuario.total_invertido) > 29:
        print(f"||| Total invertido: {usuario.total_invertido[:17]}... |||")
    else:
        print(f"||| Total invertido: {usuario.total_invertido:<21} |||")
    if len(usuario.rendimiento) > 29:
        print(f"||| Rendimiento: {usuario.nombre[:23]}... |||")
    else:
        print(f"||| Rendimiento: {usuario.nombre:<26} |||")
    if len(usuario.saldo) > 29:
        print(f"||| Saldo: {usuario.saldo[:23]}... |||")
    else:
        print(f"||| Saldo: {usuario.saldo:<26} |||")
    print("|||-------------------------------------|||")
    print("||| Activos:                           |||")

    for i, accion in enumerate(usuario.acciones, start=1):
        print(f"||| {i}. {accion:<33} |||")

    print("|||-------------------------------------|||")

    print("Seleccione una opción:")
    print("1. Comprar Acciones")
    print("2. Vender Acciones")
    print("3. Ver gráfico")
    print("4. Salir")
    opcion = input("Qué deseas hacer?: ")
    return opcion
