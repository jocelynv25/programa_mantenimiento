import os, cv2
from tkinter import messagebox
import subprocess
import tkinter as tk
import colores

def btnBuscar():
    nombre = entryNombre.get()
    codigo = entryCodigo.get()
    print("BUSCADOR")
    print(f"nombre: {nombre}")
    print(f"codigo: {codigo}")

    if nombre.strip() == '' and codigo.strip() == '':
        messagebox.showerror("Error", "Inserte el nombre de la máquina o el código para hacer la búsqueda.")
    elif nombre.strip() != '' and codigo.strip() != '':
        messagebox.showerror("Error", "Solamente inserte un campo para buscar")
    else:
        #Enviar datos a info
        subprocess.Popen(['python', 'MaquinaInfo.py', nombre, codigo])
        Ventana.withdraw()

def volverMenu():
    subprocess.Popen(['python', 'Menu.py'])
    Ventana.destroy()

def on_closing():
    if messagebox.askokcancel("Salir", "¿Seguro que quieres salir?"):
        Ventana.destroy()

# Crear ventana
Ventana = tk.Tk()
Ventana.title("Buscador")

# Obtener dimensiones de la pantalla
screen_width = Ventana.winfo_screenwidth()
screen_height = Ventana.winfo_screenheight()
# Definir dimensiones y calcular posición para centrar la ventana
window_width = 450
window_height = 200
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
# Establecer la geometría de la ventana
Ventana.geometry(f"{window_width}x{window_height}+{x}+{y}")

Ventana.protocol("WM_DELETE_WINDOW", on_closing)
Ventana.resizable(False, False)

# Etiqueta y entrada para Nombre
labelNombre = tk.Label(Ventana, text="Nombre de la máquina:")
labelNombre.grid(row=0, column=0, padx=10, pady=5)
entryNombre = tk.Entry(Ventana, width=40)
entryNombre.grid(row=0, column=1, padx=10, pady=5)

# Etiqueta y entrada para Dirección
labelCodigo = tk.Label(Ventana, text="Código:")
labelCodigo.grid(row=1, column=0, padx=10, pady=5)
entryCodigo = tk.Entry(Ventana, width=40)
entryCodigo.grid(row=1, column=1, padx=10, pady=5)


# Botón para procesar los datos
botonBuscar = tk.Button(Ventana, text="Buscar", command=btnBuscar, bg=colores.AzulMedio, fg="white",width=12, font=("Seoge UI", 10))
botonBuscar.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

volverbt = tk.Button(Ventana, text="Volver al menú",bg=colores.AzulSucio,fg="white",width=12, font=("Seoge UI", 10), command=volverMenu)
volverbt.grid(row=3, column=0, columnspan=1, padx=1, pady=1)

# Iniciar la aplicación
Ventana.mainloop()
#cv2.destroyAllWindows()