from gastos import agregar_gasto, mostrar_gastos,mostrar_total_gastado,mostrar_total_por_mes, mostrar_total_por_tipo_mes, eliminar_gasto

def main(): 

    while True:
        print("\nMenu de gastos de Ale : ")
        print("\n1. Agregar gasto")
        print("\n2. Mostrar gastos")
        print("\n3. Mostrar total gastado (Historico)")
        print("\n4. Mostrar total gastado por mes.")
        print("\n5. Mostrar total gastado por tipo (mensual).")
        print("\n6. Eliminar un gasto.")
        print("\n7 Salir")
        opcion = input("\nElija la opcion : ")

        if opcion == '1':
            tipo_de_gasto = input("Ingrese el tipo de gasto : ").capitalize()
            monto_del_gasto = float(input("Ingrese el monto de su gasto : "))
            descripcion_de_gasto = input("Ingrese la descripcion del gasto : ").capitalize()
            agregar_gasto(tipo_de_gasto,monto_del_gasto,descripcion_de_gasto)
        elif opcion == '2':
            mostrar_gastos()
        elif opcion == '3':
            mostrar_total_gastado()
        elif opcion == '4':
            mostrar_total_por_mes()
        elif opcion == '5':
            mostrar_total_por_tipo_mes()
        elif opcion == '6':
            eliminar_gasto()
        elif opcion == '7':
            break
        else:
            print("Opcion no valida, intente de nuevo")

if __name__ == "__main__":
    main()
