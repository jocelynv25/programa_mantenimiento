import tkinter as tk
from tkinter import messagebox
import csv
import subprocess
import colores
import sys

def volverMenu():
    subprocess.Popen(['python', 'Menu.py'])
    Ventana.destroy()

def on_closing():
    if messagebox.askokcancel("Salir", "¿Seguro que quieres salir?"):
        Ventana.destroy()

def volverReportar():
    subprocess.Popen(['python', 'Reportar.py'])
    Ventana.destroy()

def generarReporte():
    subprocess.Popen(['python', 'GenerarReporte.py', maquinaSelected])
    Ventana.destroy()

def mostrar_recomendaciones(nombre):
    for widget in marco_recomendaciones.winfo_children():
        widget.destroy()

    recomendaciones = []
    with open("recomendaciones_maquinas.csv", newline='', encoding="utf-8") as f:
        reader = csv.reader(f)
        for fila in reader:
            if fila[0].strip().lower() == nombre.lower():
                recomendaciones.append(fila[1])

    if recomendaciones:
        for rec in recomendaciones:
            tk.Label(marco_recomendaciones, text=f"• {rec}", anchor="w", wraplength=350, justify="left").pack(fill="x", padx=10, pady=2)
    else:
        tk.Label(marco_recomendaciones, text="No se encontraron recomendaciones.", fg="red").pack(pady=10)

maquinaSelected= sys.argv[1]

# Crear ventana
Ventana = tk.Tk()
Ventana.title("Recomendaciones")

# Obtener dimensiones de la pantalla
screen_width = Ventana.winfo_screenwidth()
screen_height = Ventana.winfo_screenheight()
# Definir dimensiones y calcular posición para centrar la ventana
window_width = 400
window_height = 400
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
# Establecer la geometría de la ventana
Ventana.geometry(f"{window_width}x{window_height}+{x}+{y}")

Ventana.protocol("WM_DELETE_WINDOW", on_closing)
Ventana.resizable(False, False)

# Título
tk.Label(Ventana, text="Recomendaciones", font=("Segoe UI", 14, 'bold')).pack(pady=0)
tk.Label(Ventana, text=f"{maquinaSelected} ", font=("Segoe UI", 12)).pack(pady=5)

# Área de recomendaciones
marco_recomendaciones = tk.Frame(Ventana)
marco_recomendaciones.pack(fill="both", expand=True, padx=10, pady=5)

mostrar_recomendaciones(nombre=maquinaSelected)

tk.Button(Ventana, text="Generar orden de trabajo", command=generarReporte, 
          bg=colores.AzulMedio, fg="white", width=24, font=("Segoe UI", 10)).pack(pady=15)

tk.Button(Ventana, text="Volver", command=volverReportar, 
          bg=colores.AzulSucio, fg="white", width=15, font=("Segoe UI", 10)).pack(pady=5)

tk.Button(Ventana, text="Ir al menú", command=volverMenu, 
          bg=colores.AzulSucio, fg="white", width=15, font=("Segoe UI", 10)).pack(pady=5)

Ventana.mainloop()
