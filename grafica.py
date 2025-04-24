import tkinter as tk
from tkinter import messagebox
from datetime import date
from db import conectar_db, cerrar_conexion

# Función para agregar gasto
def agregar_gasto(tipo_de_gasto, monto_del_gasto, descripcion_de_gasto):
    fecha = date.today().isoformat()
    gasto = {
        'TIPO': tipo_de_gasto,
        'FECHA': fecha,
        'MONTO': monto_del_gasto,
        'DESCRIPCION': descripcion_de_gasto
    }

    # CONEXION A BD
    conexion = conectar_db()
    cursor = conexion.cursor()

    # INSERT DE GASTO A LA TABLA 'GASTOS'
    cursor.execute("""
        INSERT INTO gastos (tipo, fecha, monto, descripcion)
        VALUES (?, ?, ?, ?)
    """, (gasto['TIPO'], gasto['FECHA'], gasto['MONTO'], gasto['DESCRIPCION']))

    conexion.commit()
    conexion.close()

    print("El gasto fue registrado con éxito!")

# Función para mostrar los gastos
def mostrar_gastos():
    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute("Select * from GASTOS")
    gastos = cursor.fetchall()

    # Crear una nueva ventana para mostrar los gastos
    mostrar_window = tk.Toplevel()
    mostrar_window.title("Mostrar Gastos")

    if gastos:
        for gasto in gastos:
            gasto_text = f"ID: {gasto[0]}, TIPO: {gasto[1]}, FECHA: {gasto[2]}, MONTO: ${gasto[3]}, DESCRIPCION: {gasto[4]}"
            tk.Label(mostrar_window, text=gasto_text).pack(pady=5)
    else:
        tk.Label(mostrar_window, text="No hay gastos registrados aún.").pack(pady=5)

    cerrar_conexion(conexion)

# Función para crear la ventana de agregar gasto
def agregar_gasto_ventana():
    def submit_gasto():
        tipo = tipo_entry.get()
        monto = monto_entry.get()
        descripcion = descripcion_entry.get()

        # Validación simple
        if tipo and monto and descripcion:
            try:
                monto = float(monto)
                agregar_gasto(tipo, monto, descripcion)
                messagebox.showinfo("Éxito", "Gasto registrado con éxito.")
                agregar_gasto_window.destroy()  # Cerrar la ventana de agregar gasto
            except ValueError:
                messagebox.showerror("Error", "Por favor ingrese un monto válido.")
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")

    agregar_gasto_window = tk.Toplevel()
    agregar_gasto_window.title("Agregar Gasto")

    # Campos de entrada
    tk.Label(agregar_gasto_window, text="Tipo de Gasto:").pack()
    tipo_entry = tk.Entry(agregar_gasto_window)
    tipo_entry.pack()

    tk.Label(agregar_gasto_window, text="Monto:").pack()
    monto_entry = tk.Entry(agregar_gasto_window)
    monto_entry.pack()

    tk.Label(agregar_gasto_window, text="Descripción:").pack()
    descripcion_entry = tk.Entry(agregar_gasto_window)
    descripcion_entry.pack()

    # Botón para enviar el formulario
    submit_button = tk.Button(agregar_gasto_window, text="Agregar Gasto", command=submit_gasto)
    submit_button.pack()

# Crear la ventana principal
def main_window():
    root = tk.Tk()
    root.title("CONTROL DE GASTOS")

    # Título de la ventana
    title_label = tk.Label(root, text="CONTROL DE GASTOS", font=("Helvetica", 16, "bold"))
    title_label.pack(pady=20)

    # Botón para agregar gasto
    agregar_button = tk.Button(root, text="Agregar Gasto", command=agregar_gasto_ventana)
    agregar_button.pack(pady=10)

    # Botón para mostrar los gastos
    mostrar_button = tk.Button(root, text="Mostrar Gastos", command=mostrar_gastos)
    mostrar_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main_window()
