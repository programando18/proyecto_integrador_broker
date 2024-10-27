def formatear_acciones(lista_acciones):
    acciones_formateadas = []
    for idx, accion in enumerate(acciones, start=1):
        acciones_formateadas.append(
            f"{idx}. {accion['nombre']} - Precio: {accion['precio']}"
        )
    return acciones_formateadas
