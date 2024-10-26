def imprimir_lista_acciones(acciones):
    for idx, accion in enumerate(acciones, start=1):
        print(
            f"{idx}. {accion['simbolo']} {accion['nombre']} - Precio: {accion['precio_compra_actual']} - Cantidad: {accion['cantidad']}"
        )
