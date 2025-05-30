import os
import csv
import tkinter as tk
from tkinter import ttk, messagebox
import subprocess

ventana = tk.Tk()
ventana.title("Inventario de máquinas")
ventana.geometry("1000x500")

# Función para abrir imagen
import platform
import webbrowser

def abrir_archivo(ruta):
    if not ruta or ruta == "NULL":
        messagebox.showwarning("Advertencia", "No hay archivo para mostrar.")
        return
    if platform.system() == "Windows":
        os.startfile(ruta)
    elif platform.system() == "Darwin":
        subprocess.call(("open", ruta))
    else:
        subprocess.call(("xdg-open", ruta))

# Tabla
tabla = ttk.Treeview(ventana)

# Leer encabezados desde CSV
with open("bd_maquinas.csv", newline='', encoding="utf-8") as f:
    reader = csv.reader(f)
    encabezados = next(reader)
    columnas = encabezados + ["Ver ficha", "Ver mantenimiento"]
    tabla["columns"] = columnas
    tabla["show"] = "headings"

    for col in columnas:
        tabla.heading(col, text=col)
        tabla.column(col, width=100, anchor="center")

    for fila in reader:
        fila_con_botones = fila + ["Abrir", "Abrir"]
        tabla.insert("", "end", values=fila_con_botones)

# Función para manejar clicks
def click_en_tabla(event):
    item = tabla.identify_row(event.y)
    col = tabla.identify_column(event.x)
    if not item or not col:
        return

    index_col = int(col.replace('#', '')) - 1
    valores = tabla.item(item, "values")

    if columnas[index_col] == "Ver ficha":
        abrir_archivo(valores[-3])
    elif columnas[index_col] == "Ver mantenimiento":
        abrir_archivo(valores[-2])

# Scrollbar
scroll = ttk.Scrollbar(ventana, orient="vertical", command=tabla.yview)
tabla.configure(yscrollcommand=scroll.set)
tabla.pack(side="left", fill="both", expand=True)
scroll.pack(side="right", fill="y")

tabla.bind("<Button-1>", click_en_tabla)

ventana.mainloop()
