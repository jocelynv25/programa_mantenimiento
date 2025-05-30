from tkinter import messagebox
import subprocess

import colores
import sys
import csv
import shutil
from tkinter import filedialog
from PIL import Image, ImageTk
import unicodedata
import platform

import tkinter as tk

def volverBuscador():
    subprocess.Popen(['python', 'Buscador.py'])
    ventana.destroy()

def volverMenu():
    subprocess.Popen(['python', 'Menu.py'])
    ventana.destroy()

def on_closing():
    if messagebox.askokcancel("Salir", "¿Seguro que quieres salir?"):
        ventana.destroy()

def cargar_info_maquina(nombre, codigo):
    global ruta_ficha, ruta_mantenimiento
    
    with open("bd_maquinas.csv", newline='', encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)  # Saltar encabezados

        for fila in reader:
            if normalizar(fila[0]) == normalizar(nombre) or normalizar(fila[1]) == normalizar(codigo):
                entryNombre.insert(0, fila[0])
                entryCodigo.insert(0, fila[1])
                entryModelo.insert(0, fila[2])
                entryFabMarca.insert(0, fila[3])
                entryUbicacion.insert(0, fila[4])
                entrySeccion.insert(0, fila[5])
                entryDimensiones.insert(0, fila[6])
                entryPeso.insert(0, fila[7])
                entryVoltaje.insert(0, fila[8])
                entryPotencia.insert(0, fila[9])

                entryNombre.config(state="readonly")
                entryCodigo.config(state="readonly")
                entryModelo.config(state="readonly")
                entryFabMarca.config(state="readonly")
                entryUbicacion.config(state="readonly")
                entrySeccion.config(state="readonly")
                entryDimensiones.config(state="readonly")
                entryPeso.config(state="readonly")
                entryVoltaje.config(state="readonly")
                entryPotencia.config(state="readonly")

                ruta_ficha = fila[10]
                ruta_mantenimiento = fila[11]
                return
        messagebox.showwarning("Error", "Máquina no encontrada.")

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

#Normalizar para buscar sin importar mayusculas ni acentos
def normalizar(texto):
    if not texto:
        return ""
    texto = texto.lower()
    texto = unicodedata.normalize('NFD', texto)
    texto = ''.join(c for c in texto if unicodedata.category(c) != 'Mn')
    return texto.strip()

nombre = sys.argv[1]
codigo = sys.argv[2]

# Crear ventana
ventana = tk.Tk()
ventana.title("Información de la máquina")

# Obtener dimensiones de la pantalla
screen_width = ventana.winfo_screenwidth()
screen_height = ventana.winfo_screenheight()

# Definir dimensiones y calcular posición para centrar la ventana
window_width = 850
window_height = 400
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# Establecer la geometría de la ventana
ventana.geometry(f"{window_width}x{window_height}+{x}+{y}")

ventana.protocol("WM_DELETE_WINDOW", on_closing)
ventana.resizable(False, False)

#Título del formulario
titulo = tk.Label(ventana, text="Información de la máquina", font=("Segoe UI", 14, 'bold'))
titulo.grid(column=0, row=1, columnspan=4, padx=10, pady=10)

# Campo NOMBRE 
labelNombre = tk.Label(ventana, text="Nombre :")
labelNombre.grid(row=5, column=0, padx=10, pady=5)
entryNombre = tk.Entry(ventana, width=40)
entryNombre.grid(row=5, column=1, padx=10, pady=5)

# Campo NUMERO DE SERIE
labelCodigo = tk.Label(ventana, text="Código :")
labelCodigo.grid(row=5, column=2, padx=10, pady=5)
entryCodigo = tk.Entry(ventana, width=40)
entryCodigo.grid(row=5, column=3, padx=10, pady=5)

# Campo 1 
labelModelo = tk.Label(ventana, text="Modelo :")
labelModelo.grid(row=6, column=0, padx=10, pady=5)
entryModelo = tk.Entry(ventana, width=40)
entryModelo.grid(row=6, column=1, padx=10, pady=5)

# Campo 2
labelFabMarca = tk.Label(ventana, text="Fabricante / Marca:")
labelFabMarca.grid(row=6, column=2, padx=10, pady=5)
entryFabMarca = tk.Entry(ventana, width=40)
entryFabMarca.grid(row=6, column=3, padx=10, pady=5)

# Campo 3
labelUbicacion = tk.Label(ventana, text="Ubicación :")
labelUbicacion.grid(row=7, column=0, padx=10, pady=5)
entryUbicacion = tk.Entry(ventana, width=40)
entryUbicacion.grid(row=7, column=1, padx=10, pady=5)

# Campo 4
labelSeccion = tk.Label(ventana, text="Sección :")
labelSeccion.grid(row=7, column=2, padx=10, pady=5)
entrySeccion = tk.Entry(ventana, width=40)
entrySeccion.grid(row=7, column=3, padx=10, pady=5)

# Campo 5 
labelDimensiones = tk.Label(ventana, text="Dimensiones :")
labelDimensiones.grid(row=8, column=0, padx=10, pady=5)
entryDimensiones = tk.Entry(ventana, width=40)
entryDimensiones.grid(row=8, column=1, padx=10, pady=5)

# Campo 6
labelPeso = tk.Label(ventana, text="Peso :")
labelPeso.grid(row=8, column=2, padx=10, pady=5)
entryPeso = tk.Entry(ventana, width=40)
entryPeso.grid(row=8, column=3, padx=10, pady=5)

# Campo 7
labelVoltaje = tk.Label(ventana, text="Voltaje de alimentación :")
labelVoltaje.grid(row=9, column=0, padx=10, pady=5)
entryVoltaje = tk.Entry(ventana, width=40)
entryVoltaje.grid(row=9, column=1, padx=10, pady=5)

# Campo 8
labelPotencia = tk.Label(ventana, text="Potencia :")
labelPotencia.grid(row=9, column=2, padx=10, pady=5)
entryPotencia = tk.Entry(ventana, width=40)
entryPotencia.grid(row=9, column=3, padx=10, pady=5)

cargar_info_maquina(nombre, codigo)

# Botón para procesar los datos
btnFicha = tk.Button(ventana, text="Ver ficha técnica", command=lambda: abrir_archivo(ruta=ruta_ficha), bg=colores.AzulMedio, fg="white",width=20, font=("Seoge UI", 10, 'bold'))
btnFicha.grid(row=10, column=0, columnspan=2, padx=10, pady=10)

btnMantenimiento = tk.Button(ventana, text="Ver mantenimiento", command=lambda: abrir_archivo(ruta=ruta_mantenimiento), bg=colores.AzulMedio, fg="white",width=20, font=("Seoge UI", 10, 'bold'))
btnMantenimiento.grid(row=10, column=2, columnspan=2, padx=10, pady=10)

botonBuscador = tk.Button(ventana, text="Volver al buscador",bg=colores.AzulSucio, fg="white",width=14, font=("Seoge UI", 10), command=volverBuscador)
botonBuscador.grid(row=13, column=1,  padx=5, pady=5)

botonVolver = tk.Button(ventana, text="Ir al menú",bg=colores.AzulSucio, fg="white",width=14, font=("Seoge UI", 10), command=volverMenu)
botonVolver.grid(row=13, column=2,  padx=5, pady=5)


# Iniciar la aplicación
ventana.mainloop()