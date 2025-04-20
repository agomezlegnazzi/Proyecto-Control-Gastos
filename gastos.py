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