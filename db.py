import sqlite3

def conectar_db():
    return sqlite3.connect("gastos.db")

def cerrar_conexion(conexion):
    conexion.close()

def crear_tabla():
    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS gastos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo TEXT NOT NULL,
            fecha TEXT NOT NULL,
            monto REAL NOT NULL,
            descripcion TEXT
        )
    """)
    conexion.commit()
    cerrar_conexion(conexion)
