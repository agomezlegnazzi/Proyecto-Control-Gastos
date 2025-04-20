import tkinter as tk
from tkinter import messagebox
from gastos import agregar_gasto, mostrar_gastos, eliminar_gasto, mostrar_total_por_mes, mostrar_total_por_tipo_mes,eliminar_gasto


class GastosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Control de Gastos")
        self.root.geometry("400x400")
        
        # Títulos y botones
        self.title_label = tk.Label(self.root, text="Control de Gastos", font=("Arial", 16))
        self.title_label.pack(pady=20)
        
        self.btn_agregar = tk.Button(self.root, text="Agregar Gasto", command=self.agregar)
        self.btn_agregar.pack(pady=5)

        self.btn_mostrar = tk.Button(self.root, text="Mostrar Gastos", command=self.mostrar)
        self.btn_mostrar.pack(pady=5)

        self.btn_eliminar = tk.Button(self.root, text="Eliminar Gasto", command=self.eliminar)
        self.btn_eliminar.pack(pady=5)

        self.btn_total_mes = tk.Button(self.root, text="Total por Mes", command=self.total_mes)
        self.btn_total_mes.pack(pady=5)

        self.btn_total_tipo = tk.Button(self.root, text="Total por Tipo", command=self.total_tipo)
        self.btn_total_tipo.pack(pady=5)

    def agregar(self):
        tipo = self.ask_input("Tipo de Gasto")
        monto = self.ask_input("Monto del Gasto")
        descripcion = self.ask_input("Descripción del Gasto")

        agregar_gasto(tipo, monto, descripcion)
        messagebox.showinfo("Éxito", "Gasto agregado correctamente!")

    def mostrar(self):
        mostrar_gastos()
        
    def eliminar(self):
        gasto_id = self.ask_input("ID del Gasto a Eliminar")
        eliminar_gasto(gasto_id)
        
    def total_mes(self):
        año = self.ask_input("Año")
        mes = self.ask_input("Mes")
        mostrar_total_por_mes(año, mes)
        
    def total_tipo(self):
        año = self.ask_input("Año")
        mes = self.ask_input("Mes")
        mostrar_total_por_tipo(año, mes)

    def ask_input(self, label_text):
        input_value = tk.simpledialog.askstring("Input", label_text)
        return input_value

# Crear la ventana principal
if __name__ == "__main__":
    root = tk.Tk()
    app = GastosApp(root)
    root.mainloop()
