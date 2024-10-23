from utils.acciones import formatear_acciones


def panel_de_venta_acciones():
    # Acá vamos a obtener las acciones del portfolio de la BBDD
    # ------------------------------------------------|
    #
    #
    # -------------------------------------------------|

    # Datos falsos
    acciones = [
        {"nombre": "Acción A", "precio": 100},
        {"nombre": "Acción B", "precio": 150},
        {"nombre": "Acción C", "precio": 200},
        {"nombre": "Acción D", "precio": 250},
        {"nombre": "Acción E", "precio": 300},
    ]

    print("|--- Lista de acciones disponibles para vender: ---|")
    print(formatear_acciones(acciones))

    seleccion = input(
        "Seleccione el número de la acción que desea vender (o agregue 'info' para más información): "
    )
    if "info" in seleccion:
        numero_accion = int(seleccion.replace("info", "").strip())
        if 1 <= numero_accion <= len(acciones):
            accion_seleccionada = acciones[numero_accion - 1]
            print(f"Información adicional de {accion_seleccionada['nombre']}:")
            print(f"Precio: {accion_seleccionada['precio']}")
            # Aquí puedes agregar más información si está disponible
        else:
            print("Selección inválida.")
    else:
        numero_accion = int(seleccion)
        if 1 <= numero_accion <= len(acciones):
            accion_seleccionada = acciones[numero_accion - 1]
            return accion_seleccionada
        else:
            print("Selección inválida.")
