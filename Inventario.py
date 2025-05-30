import os
import csv
import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import colores

InventarioVentana = tk.Tk()
InventarioVentana.title("Inventario de máquinas")
InventarioVentana.geometry("1000x500")

# Función para abrir imagen
import platform

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
tabla = ttk.Treeview(InventarioVentana)

# Leer encabezados desde CSV
with open("bd_maquinas.csv", newline='', encoding="utf-8") as f:
    reader = csv.reader(f)
    encabezados = next(reader)

    # Elimina columnas de Ficha técnica y Mantenimiento
    columnas_visibles = encabezados[:-2] + ["Ver ficha", "Ver mantenimiento"]
    tabla["columns"] = columnas_visibles
    tabla["show"] = "headings"

    for col in columnas_visibles:
        tabla.heading(col, text=col)
        tabla.column(col, width=100, anchor="center")

    for fila in reader:
        datos_visibles = fila[:-2] + ["Abrir", "Abrir"]
        tabla.insert("", "end", values=datos_visibles, tags=(fila[-2], fila[-1]))

# Función para manejar clicks (para abrir ficha o mantenimiento)
def click_en_tabla(event):
    item = tabla.identify_row(event.y)
    col = tabla.identify_column(event.x)
    if not item or not col:
        return

    index_col = int(col.replace('#', '')) - 1
    valores = tabla.item(item, "values")
    tags = tabla.item(item, "tags")

    if columnas_visibles[index_col] == "Ver ficha":
        abrir_archivo(tags[0])
    elif columnas_visibles[index_col] == "Ver mantenimiento":
        abrir_archivo(tags[1])

def volverMenu():
    pathACC = 'Menu.py'
    subprocess.Popen(['python', pathACC])
    InventarioVentana.destroy()

def on_closing():
    InventarioVentana.destroy()
    #if messagebox.askokcancel("Salir", "¿Seguro que quieres salir?"):
    #    InventarioVentana.destroy()

InventarioVentana.protocol("WM_DELETE_WINDOW", on_closing)

# Scrollbar
scroll = ttk.Scrollbar(InventarioVentana, orient="vertical", command=tabla.yview)
tabla.configure(yscrollcommand=scroll.set)
tabla.pack(side="left", fill="both", expand=True)
scroll.pack(side="right", fill="y")

botonVolver = tk.Button(InventarioVentana, text="Volver al menú",bg=colores.AzulSucio, fg="white",width=12, font=("Seoge UI", 10), command=volverMenu)
botonVolver.pack(pady=3)

tabla.bind("<Button-1>", click_en_tabla)

InventarioVentana.mainloop()
