from tkinter import messagebox
import subprocess
import tkinter as tk
import colores
import csv
import colores

maquina_seleccionada = None

def volverMenu():
    subprocess.Popen(['python', 'Menu.py'])
    Ventana.destroy()

def on_closing():
    if messagebox.askokcancel("Salir", "¿Seguro que quieres salir?"):
        Ventana.destroy()

def verRecomendaciones():
    if maquina_seleccionada == None:
        messagebox.showerror("Error", "Seleccione una máquina y su respectiva falla para ver las recomendaciones.")
    else:
        subprocess.Popen(['python', 'Recomendaciones.py', maquina_seleccionada])
        Ventana.destroy()

def cargar_maquinas():
    maquinas = set()
    with open("bd_maquinas.csv", newline='', encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)
        for fila in reader:
            maquinas.add(fila[0])
    return sorted(maquinas)

def cargar_fallas():
    fallas_dict = {}
    with open("fallas_maquinas.csv", newline='', encoding="utf-8") as f:
        reader = csv.reader(f)
        for fila in reader:
            maquina = fila[0]
            falla = fila[1]
            if maquina in fallas_dict:
                fallas_dict[maquina].append(falla)
            else:
                fallas_dict[maquina] = [falla]
    return fallas_dict

def actualizar_fallas(*args):
    global maquina_seleccionada
    maquina_seleccionada = var_maquina.get()
    opciones_fallas = fallas_dict.get(maquina_seleccionada, ["No hay fallas registradas."])
    
    # Limpiar el menú anterior
    menu_fallas['menu'].delete(0, 'end')
    for falla in opciones_fallas:
        menu_fallas['menu'].add_command(label=falla, command=tk._setit(var_falla, falla))
    
    # Seleccionar la primera falla por defecto
    if opciones_fallas:
        var_falla.set(opciones_fallas[0])
    else:
        var_falla.set("")

# Crear ventana
Ventana = tk.Tk()
Ventana.title("Reportar falla")

# Obtener dimensiones de la pantalla
screen_width = Ventana.winfo_screenwidth()
screen_height = Ventana.winfo_screenheight()
# Definir dimensiones y calcular posición para centrar la ventana
window_width = 300
window_height = 300
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
# Establecer la geometría de la ventana
Ventana.geometry(f"{window_width}x{window_height}+{x}+{y}")

Ventana.protocol("WM_DELETE_WINDOW", on_closing)
Ventana.resizable(False, False)

maquinas = cargar_maquinas()
fallas_dict = cargar_fallas()

labelTitulo = tk.Label(Ventana, text="Reportar falla", font=("Segoe UI", 14, 'bold'))
labelTitulo.grid(row=0, column=0, padx=10, pady=5)

# Etiqueta y entrada para Nombre
labelNombre = tk.Label(Ventana, text="Nombre de la máquina:")
labelNombre.grid(row=1, column=0, padx=80, pady=5)

var_maquina = tk.StringVar()
var_maquina.trace("w", actualizar_fallas)
menu_maquinas = tk.OptionMenu(Ventana, var_maquina, *maquinas)
menu_maquinas.grid(row=2, column=0, padx=10, pady=5, sticky="we")

# Etiqueta y entrada para falla
labelFalla = tk.Label(Ventana, text="Tipo de falla:")
labelFalla.grid(row=3, column=0, sticky="w", padx=10)

var_falla = tk.StringVar()
menu_fallas = tk.OptionMenu(Ventana, var_falla, "")
menu_fallas.grid(row=4, column=0, padx=10, pady=5, sticky="we")


# Botón para procesar los datos
botonBuscar = tk.Button(Ventana, text="Ver recomendaciones", command=verRecomendaciones, bg=colores.AzulMedio, fg="white",width=20, font=("Seoge UI", 10))
botonBuscar.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

volverbt = tk.Button(Ventana, text="Volver al menú",bg=colores.AzulSucio,fg="white",width=12, font=("Seoge UI", 10), command=volverMenu)
volverbt.grid(row=6, column=0, columnspan=1, padx=1, pady=1)

# Iniciar la aplicación
Ventana.mainloop()