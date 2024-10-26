from interfaces.lista_acciones import imprimir_lista_acciones
from DAO.acciones_DAO import AccionesDAO

acciones_DAO = AccionesDAO()


def panel_de_compra_acciones():
    accion_seleccionada = {}
    cantidad = 0

    acciones = acciones_DAO.obtener_acciones()

    print("|--- Lista de acciones disponibles para comprar: ---|")
    imprimir_lista_acciones(acciones)

    seleccion = input(
        "Seleccione el número de la acción que desea comprar (o agregue 'info' para más información): "
    )
    if "info" in seleccion:
        numero_accion = int(seleccion.replace("info", "").strip())
        if 1 <= numero_accion <= len(acciones):
            accion_seleccionada = acciones[numero_accion - 1]
            print(f"Información adicional de {accion_seleccionada['nombre']}:")
            print(f"Precio: {accion_seleccionada['precio']}")
        else:
            print("Selección inválida.")
    else:
        numero_accion = int(seleccion)
        if 1 <= numero_accion <= len(acciones):
            accion_seleccionada = acciones[numero_accion - 1]
        else:
            print("Selección inválida.")
    cantidad = int(input("Ingrese la cantidad de acciones que desea comprar: "))
    return {"accion": accion_seleccionada, "cantidad": cantidad}
