def imprimir_lista_acciones(acciones):
    for idx, accion in enumerate(acciones, start=1):
        print(f"{idx}. {accion['nombre']} - Precio: {accion['precio']}")
