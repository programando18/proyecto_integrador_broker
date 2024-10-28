def imprimir_lista_acciones(acciones):
    for idx, accion in enumerate(acciones, start=1):
        print(
            f"|{idx}. {accion['simbolo']} {accion['nombre']} - Precio Compra: ${accion['precio_compra_actual']} - Precio Venta: ${accion['precio_venta_actual']} - Cantidad: {accion['cantidad']}"
        )
