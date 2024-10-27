from interfaces.lista_acciones import imprimir_lista_acciones

from DAO.acciones_DAO import AccionesDAO
from DAO.bd_conexion import conexion_bd

conexion = conexion_bd()

acciones_DAO = AccionesDAO(conexion)


def panel_de_compra_acciones():
    accion_seleccionada = {}
    cantidad = 0

    acciones = acciones_DAO.obtener_acciones()

    print("   -------------------------------------   ")
    print("       LISTA DE ACCIONES DISPONIBLES    ")
    print("   -------------------------------------   ")
    imprimir_lista_acciones(acciones)
    print("   -------------------------------------   ")

    seleccion = input("Seleccione el número de la acción que desea comprar: ")

    numero_accion = int(seleccion)
    if 1 <= numero_accion <= len(acciones):
        accion_seleccionada = acciones[numero_accion - 1]
    else:
        print("Selección inválida.")

    cantidad = int(input("Ingrese la cantidad de acciones que desea comprar: "))
    return {"accion": accion_seleccionada, "cantidad": cantidad}
