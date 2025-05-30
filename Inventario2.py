import os
import csv
import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import platform
import colores

# Crear ventana
ventana = tk.Tk()
ventana.title("Inventario de máquinas")

# Obtener dimensiones de la pantalla
screen_width = ventana.winfo_screenwidth()
screen_height = ventana.winfo_screenheight()

# Definir dimensiones y calcular posición para centrar la ventana
window_width = screen_width - 20
window_height = 500
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
# Establecer la geometría de la ventana
ventana.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Función para abrir imagen
def abrir_archivo(ruta):
    print("Abrir archivo.")
    if not ruta or ruta == "NULL":
        messagebox.showwarning("Advertencia", "No hay archivo para mostrar.")
        return
    if platform.system() == "Windows":
        os.startfile(ruta)
    elif platform.system() == "Darwin":
        subprocess.call(("open", ruta))
    else:
        subprocess.call(("xdg-open", ruta))

# Frame principal
frame_principal = tk.Frame(ventana)
frame_principal.grid(row=0, column=0, sticky="nsew")
ventana.grid_rowconfigure(0, weight=1)
ventana.grid_columnconfigure(0, weight=1)

# Tabla
tabla = ttk.Treeview(frame_principal)

# Leer encabezados desde CSV
with open("bd_maquinas.csv", newline='', encoding="utf-8") as f:
    reader = csv.reader(f)
    encabezados = next(reader)
    
    columnas = encabezados[:-2] + ["Ficha", "Mantenimiento"]  # Quitamos rutas
    tabla["columns"] = columnas
    tabla["show"] = "headings"

    for col in columnas:
        tabla.heading(col, text=col)
        tabla.column(col, width=100, anchor="center")

    for fila in reader:
        fila_con_botones = fila[:-2] + ["Abrir", "Abrir"]  # Quitamos rutas
        tabla.insert("", "end", values=fila_con_botones)

# Función para manejar clicks
def click_en_tabla(event):
    print("Se hizo clic en tabla")
    item = tabla.identify_row(event.y)
    col = tabla.identify_column(event.x)
    if not item or not col:
        print("Not item or not col")
        return

    index_col = int(col.replace('#', '')) - 1
    valores = tabla.item(item, "values")

    if columnas[index_col] == "Ficha":
        print(f"Abrir ficha ${valores[-3]}")
        abrir_archivo(valores[-3])
    elif columnas[index_col] == "Mantenimiento":
        print(f"Abrir mantenimiento ${valores[-2]}")
        abrir_archivo(valores[-2])

def volverMenu():
    subprocess.Popen(['python', 'Menu.py'])
    ventana.destroy()

def on_closing():
    if messagebox.askokcancel("Salir", "¿Seguro que quieres salir?"):
        ventana.destroy()

ventana.protocol("WM_DELETE_WINDOW", on_closing)
ventana.resizable(False, False)

# Scrollbar
scrollY = ttk.Scrollbar(frame_principal, orient="vertical", command=tabla.yview)
tabla.configure(yscrollcommand=scrollY.set)
tabla.grid(row=0, column=0, sticky="nsew")

scrollX = ttk.Scrollbar(frame_principal, orient="horizontal", command=tabla.xview)
tabla.configure(xscrollcommand=scrollX.set)
tabla.grid(row=0, column=0, sticky="nsew")

scrollY.grid(row=0, column=1, sticky="ns")
scrollX.grid(row=1, column=0, sticky="ew")

frame_principal.grid_rowconfigure(0, weight=1)
frame_principal.grid_columnconfigure(0, weight=1)

# Botón volver al menú
boton_volver = tk.Button(ventana, text="Volver al menú",bg=colores.AzulSucio, fg="white",width=12, font=("Seoge UI", 10), command=volverMenu)
boton_volver.grid(row=1, column=0, pady=10)

# Eventos
tabla.bind("<Button-1>", click_en_tabla)

ventana.mainloop()

print("VENTANA MAINLOOP")