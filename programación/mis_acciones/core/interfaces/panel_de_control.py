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
    # print(f"||| Total invertido: ${total_invested:<20} |||")
    # print(f"||| Rendimiento: {performance:<26} |||")
    # print(f"||| Saldo disponible: ${available_balance:<17} |||")
    print("|||-------------------------------------|||")
    print("||| Activos:                           |||")

    # Imprimir lista de activos
    # for idx, asset in enumerate(assets, start=1):
    #     print(f"||| {idx}. {asset:<33} |||")

    # Cerrar el panel
    print("|||-------------------------------------|||")
