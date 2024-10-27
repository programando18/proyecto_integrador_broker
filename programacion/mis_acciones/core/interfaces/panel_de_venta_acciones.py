from utils.acciones import formatear_acciones
from interfaces.lista_acciones import imprimir_lista_acciones


def panel_de_venta_acciones(acciones):
    print("|--- Lista de acciones disponibles para vender: ---|")
    for idx, accion in enumerate(acciones, start=1):
        print(
            f"{idx}. {accion['simbolo']} {accion['nombre']} - Cantidad: {accion['cantidad']}"
        )
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
            raise ("Selección inválida.")
    else:
        numero_accion = int(seleccion)
        if 1 <= numero_accion <= len(acciones):
            accion_seleccionada = acciones[numero_accion - 1]
        else:
            raise ("Selección inválida.")

    cantidad = int(input("Ingrese la cantidad de acciones que desea vender: "))
    return {"accion": accion_seleccionada, "cantidad": cantidad}
