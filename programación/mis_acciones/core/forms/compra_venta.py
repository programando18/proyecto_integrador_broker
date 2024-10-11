def mostrar_opciones():
    print("\n--- Menú de Acciones ---")
    print("1. Comprar Acciones")
    print("2. Vender Acciones")
    print("3. Salir")

def comprar_acciones():
    simbolo = input("Ingrese el símbolo de la acción a comprar: ")
    cantidad = int(input("Ingrese la cantidad de acciones a comprar: "))
    precio = float(input("Ingrese el precio por acción: "))
    
    total = cantidad * precio
    print(f"Ha comprado {cantidad} acciones de {simbolo} a ${precio:.2f} cada una. Total: ${total:.2f}")

def vender_acciones():
    simbolo = input("Ingrese el símbolo de la acción a vender: ")
    cantidad = int(input("Ingrese la cantidad de acciones a vender: "))
    precio = float(input("Ingrese el precio por acción: "))
    
    total = cantidad * precio
    print(f"Ha vendido {cantidad} acciones de {simbolo} a ${precio:.2f} cada una. Total: ${total:.2f}")

def main():
    while True:
        mostrar_opciones()
        opcion = input("Seleccione una opción (1-3): ")
        
        if opcion == '1':
            comprar_acciones()
        elif opcion == '2':
            vender_acciones()
        elif opcion == '3':
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
