from datetime import date 
from db import conectar_db,  cerrar_conexion

def agregar_gasto(tipo_de_gasto,monto_del_gasto,descripcion_de_gasto):
    fecha = date.today().isoformat()
    gasto = {
        'TIPO' : tipo_de_gasto,
        'FECHA' : fecha,
        'MONTO' : monto_del_gasto,
        'DESCRIPCION' : descripcion_de_gasto
    }

    # CONEXION A BD

    conexion = conectar_db()
    cursor = conexion.cursor()

    # INSERT DE GASTO A LA TABLA 'GASTOS'

    cursor.execute("""
        INSERT INTO gastos (tipo,fecha,monto,descripcion)
        VALUES (? ,? ,? ,?)
    """, (gasto['TIPO'],gasto['FECHA'],gasto['MONTO'],gasto['DESCRIPCION']))

    conexion.commit()
    conexion.close()

    print("El gasto fue registrado con exito!")

def mostrar_gastos():
    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute("Select * from GASTOS")
    gastos = cursor.fetchall()

    if gastos :
        for gasto in gastos:
            print(f"ID: {gasto[0]},TIPO: {gasto[1]},FECHA: {gasto[2]},MONTO: ${gasto[3]},DESCRIPCION: {gasto[4]},")
    else : 
        print("No hay gastos registrados aun.")
    cerrar_conexion(conexion)

def mostrar_total_gastado():

    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute("select sum(monto) from gastos")
    resultado = cursor.fetchone()

    total = resultado[0] if resultado[0] is not None else 0

    print(f"Total gastado : ${total:.2f}")

    cerrar_conexion(conexion)


def mostrar_total_por_mes():

    conexion = conectar_db()
    cursor = conexion.cursor()

    año = input("Ingrese el año que quiere saber los gastos (ejemplo : 2025) : ")
    mes = input("Ingrese el mes que quiere saber los gastos (ejemplo : 04) : ")

    fecha_prefijo = f"{año}-{mes}"

    cursor.execute("select sum(monto) from gastos where fecha like ?", (f"{fecha_prefijo}%",))

    resultado = cursor.fetchone()

    total = resultado[0] if resultado[0] is not None else 0

    print(f"\nEl total gastado en {mes}/{año}: ${total:.2f}")


def mostrar_total_por_tipo_mes():

    conexion = conectar_db()
    cursor = conexion.cursor()

    año = input("Ingrese el año que quiere saber los gastos (ejemplo : 2025) : ")
    mes = input("Ingrese el mes que quiere saber los gastos (ejemplo : 04) : ")

    fecha_prefijo = f"{año}-{mes}"

    cursor.execute("select tipo, sum(monto) from gastos where fecha like ? group by tipo", (f"{fecha_prefijo}%",))

    resultados = cursor.fetchall()

    if resultados : 
        print(f"\nEl total gastado en {mes}/{año}:")
        for tipo, monto in resultados: 
             print(f"{tipo} : ${monto:.2f}")
    else : 
        print("No hay gastos cargados.")

    cerrar_conexion(conexion)


def eliminar_gasto():

    conexion = conectar_db()
    cursor = conexion.cursor()

    print("\nA continuacion visualizara todos sus gastos : ")
    mostrar_gastos()

    gasto_id = int(input("Ingrese el ID del gasto que desea eliminar : "))

    confirmacion = input(f"Esta seguro que va a eliminar el gasto ID : {gasto_id}? (S/N) : ").upper()

    if confirmacion == 'S':
        cursor.execute("delete from gastos where id = ?",(gasto_id,))
        conexion.commit()
        print("Gasto eliminado! La lista quedo actualizada : ")
        mostrar_gastos()

    elif confirmacion == 'N':
        print("El gasto no fue eliminado!")

    else : 
        print("El gasto no fue encontrado.")    
    
    cerrar_conexion(conexion)

def editar_gasto():

    conexion = conectar_db()
    cursor = conexion.cursor()

    print("\nA continuacion visualizara todos sus gastos : ")
    mostrar_gastos()

    gasto_id = int(input("Ingrese el ID del gasto a editar : "))

    editar = input("Ingrese la categoria a editar (TIPO : 'T' / MONTO : 'M' / DESCRIPCION : 'D' / CANCELAR : 'C') : ").upper()

    while True : 
        if editar == 'T':
            nuevo_tipo = input("Ingrese el nuevo tipo : ").capitalize()
            cursor.execute(f"update gastos set tipo = ? where id = ?",(nuevo_tipo,gasto_id))
            conexion.commit()
            print("Gasto editado!")
            break
        
        elif editar == 'M':
            nuevo_monto = float(input("Ingrese el nuevo tipo : "))
            cursor.execute(f"update gastos set monto = ? where id = ?",(nuevo_monto,gasto_id))
            conexion.commit()
            print("Gasto editado!")
            break
        
        elif editar == 'D':
            nueva_descripcion = input("Ingrese la nueva descripcion : ").capitalize()
            cursor.execute(f"update gastos set descripcion = ? where id = ?",(nueva_descripcion,gasto_id))
            conexion.commit()
            print("Gasto editado!")
            break

        elif editar == 'C':
            print("Edicion cancelada!")
            break
        
        else:
            print("Gasto no encontrado!")
            break
        
        cerrar_conexion(conexion)