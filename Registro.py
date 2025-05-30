from tkinter import messagebox
import subprocess

import colores
import csv
import shutil
from tkinter import filedialog
from PIL import Image, ImageTk

import tkinter as tk

def btnGuardar():
    #Obtener los datos ingresados en los campos
    campos = [
        entryNombre.get(),
        entryNumSerie.get(),
        entryCampo1.get(),
        entryCampo2.get(),
        entryCampo3.get(),
        entryCampo4.get(),
        entryCampo5.get(),
        entryCampo6.get(),
        entryCampo7.get(),
        entryCampo8.get()
    ]
    
    nombre_maquina = entryNombre.get().strip().replace(" ", "_")
    ruta_final_ficha = ""
    ruta_final_mantenimiento = ""

    if rutaTempFicha:
        carpeta_fichas = "fichasTecnicas"
        os.makedirs(carpeta_fichas, exist_ok=True)
        ext = os.path.splitext(rutaTempFicha)[1]  # .jpg, .png, etc.
        ruta_final_ficha = os.path.join(carpeta_fichas, f"{nombre_maquina}_ficha{ext}")
        shutil.copy(rutaTempFicha, ruta_final_ficha)
        campos += [ruta_final_ficha]
    else:
        campos += ["NULL"]

    if rutaTempMantenimiento:
        carpeta_mant = "mantenimiento"
        os.makedirs(carpeta_mant, exist_ok=True)
        ext = os.path.splitext(rutaTempMantenimiento)[1]
        ruta_final_mantenimiento = os.path.join(carpeta_mant, f"{nombre_maquina}_mantenimiento{ext}")
        shutil.copy(rutaTempMantenimiento, ruta_final_mantenimiento)
        campos += [ruta_final_mantenimiento]
    else:
        campos += ["NULL"]
    
    # Verifica si todos los campos tienen contenido
    if not all(campo.strip() for campo in campos):
        messagebox.showerror("Error", "Por favor, complete todos los campos.")
        return
    
    try:
        with open('bd_maquinas.csv', mode='a', newline='', encoding='utf-8') as archivo:
            writer = csv.writer(archivo)
            writer.writerow(campos)
        messagebox.showinfo("Éxito", "Datos guardados correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo guardar el archivo: {e}")

rutaTempFicha = ""
rutaTempMantenimiento = ""

def seleccionarImagenFicha():
    global rutaTempFicha, vistaPreviaFicha, imgFichaTk
    ruta = filedialog.askopenfilename(filetypes=[("Imágenes", "*.png *.jpg *.jpeg *.webp *.bmp")])
    if ruta:
        rutaTempFicha = ruta
        image = Image.open(ruta)
        image.thumbnail((50, 50))  # Tamaño miniatura
        imgFichaTk = ImageTk.PhotoImage(image)
        vistaPreviaFicha.config(image=imgFichaTk)
        vistaPreviaFicha.image = imgFichaTk  # Evita que se borre
        #messagebox.showinfo("Imagen seleccionada", "Ficha técnica seleccionada correctamente.")

def seleccionarImagenMantenimiento():
    global rutaTempMantenimiento, vistaPreviaMantenimiento, imgMantTk
    ruta = filedialog.askopenfilename(filetypes=[("Imágenes", "*.png *.jpg *.jpeg *.webp *.bmp")])
    if ruta:
        rutaTempMantenimiento = ruta
        image = Image.open(ruta)
        image.thumbnail((50, 50))
        imgMantTk = ImageTk.PhotoImage(image)
        vistaPreviaMantenimiento.config(image=imgMantTk)
        vistaPreviaMantenimiento.image = imgMantTk
        #messagebox.showinfo("Imagen seleccionada", "Imagen de mantenimiento seleccionada correctamente.")

def volverMenu():
    pathACC = 'Menu.py'
    subprocess.Popen(['python', pathACC])
    RegistroVentana.destroy()

def on_closing():
    if messagebox.askokcancel("Salir", "¿Seguro que quieres salir?"):
        RegistroVentana.destroy()

# Crear ventana
RegistroVentana = tk.Tk()
RegistroVentana.title("Registrar máquina")
# Obtener dimensiones de la pantalla
screen_width = RegistroVentana.winfo_screenwidth()
screen_height = RegistroVentana.winfo_screenheight()
# Definir dimensiones y calcular posición para centrar la ventana
window_width = 850
window_height = 400
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
# Establecer la geometría de la ventana
RegistroVentana.geometry(f"{window_width}x{window_height}+{x}+{y}")

RegistroVentana.protocol("WM_DELETE_WINDOW", on_closing)
RegistroVentana.resizable(False, False)

#Título del formulario
titulo = tk.Label(RegistroVentana, text="Registro de máquina", font=("Segoe UI", 14, 'bold'))
titulo.grid(column=0, row=1, columnspan=4, padx=10, pady=10)

# Campo NOMBRE 
labelNombre = tk.Label(RegistroVentana, text="Nombre :")
labelNombre.grid(row=5, column=0, padx=10, pady=5)
entryNombre = tk.Entry(RegistroVentana, width=40)
entryNombre.grid(row=5, column=1, padx=10, pady=5)

# Campo NUMERO DE SERIE
labelNumSerie = tk.Label(RegistroVentana, text="Código :")
labelNumSerie.grid(row=5, column=2, padx=10, pady=5)
entryNumSerie = tk.Entry(RegistroVentana, width=40)
entryNumSerie.grid(row=5, column=3, padx=10, pady=5)

# Campo 1 
labelCampo1 = tk.Label(RegistroVentana, text="Modelo :")
labelCampo1.grid(row=6, column=0, padx=10, pady=5)
entryCampo1 = tk.Entry(RegistroVentana, width=40)
entryCampo1.grid(row=6, column=1, padx=10, pady=5)

# Campo 2
labelCampo2 = tk.Label(RegistroVentana, text="Fabricante / Marca:")
labelCampo2.grid(row=6, column=2, padx=10, pady=5)
entryCampo2 = tk.Entry(RegistroVentana, width=40)
entryCampo2.grid(row=6, column=3, padx=10, pady=5)

# Campo 3
labelCampo3 = tk.Label(RegistroVentana, text="Ubicación :")
labelCampo3.grid(row=7, column=0, padx=10, pady=5)
entryCampo3 = tk.Entry(RegistroVentana, width=40)
entryCampo3.grid(row=7, column=1, padx=10, pady=5)

# Campo 4
labelCampo4 = tk.Label(RegistroVentana, text="Sección :")
labelCampo4.grid(row=7, column=2, padx=10, pady=5)
entryCampo4 = tk.Entry(RegistroVentana, width=40)
entryCampo4.grid(row=7, column=3, padx=10, pady=5)

# Campo 5 
labelCampo5 = tk.Label(RegistroVentana, text="Dimensiones :")
labelCampo5.grid(row=8, column=0, padx=10, pady=5)
entryCampo5 = tk.Entry(RegistroVentana, width=40)
entryCampo5.grid(row=8, column=1, padx=10, pady=5)

# Campo 6
labelCampo6 = tk.Label(RegistroVentana, text="Peso :")
labelCampo6.grid(row=8, column=2, padx=10, pady=5)
entryCampo6 = tk.Entry(RegistroVentana, width=40)
entryCampo6.grid(row=8, column=3, padx=10, pady=5)

# Campo 7
labelCampo7 = tk.Label(RegistroVentana, text="Voltaje de alimentación :")
labelCampo7.grid(row=9, column=0, padx=10, pady=5)
entryCampo7 = tk.Entry(RegistroVentana, width=40)
entryCampo7.grid(row=9, column=1, padx=10, pady=5)

# Campo 8
labelCampo8 = tk.Label(RegistroVentana, text="Potencia :")
labelCampo8.grid(row=9, column=2, padx=10, pady=5)
entryCampo8 = tk.Entry(RegistroVentana, width=40)
entryCampo8.grid(row=9, column=3, padx=10, pady=5)


#SELECCIÓN DE IMAGENES
btnImagenFicha = tk.Button(RegistroVentana, text="Seleccionar ficha técnica", command=seleccionarImagenFicha)
btnImagenFicha.grid(row=10, column=1, columnspan=2, padx=10, pady=5)

vistaPreviaFicha = tk.Label(RegistroVentana)
vistaPreviaFicha.grid(row=11, column=1, columnspan=2, padx=10, pady=5)


btnImagenMantenimiento = tk.Button(RegistroVentana, text="Seleccionar imagen de mantenimiento", command=seleccionarImagenMantenimiento)
btnImagenMantenimiento.grid(row=10, column=2, columnspan=2, padx=10, pady=5)

vistaPreviaMantenimiento = tk.Label(RegistroVentana)
vistaPreviaMantenimiento.grid(row=11, column=2, columnspan=2, padx=10, pady=5)


# Botón para procesar los datos
boton_procesar = tk.Button(RegistroVentana, text="Guardar", command=btnGuardar, bg=colores.AzulMedio, fg="white",width=20, font=("Seoge UI", 10, 'bold'))
boton_procesar.grid(row=12, column=0, columnspan=4, padx=10, pady=10)

botonVolver = tk.Button(RegistroVentana, text="Volver al menú",bg=colores.AzulSucio, fg="white",width=12, font=("Seoge UI", 10), command=volverMenu)
botonVolver.grid(row=13, column=0, columnspan=4, padx=1, pady=1)

# Iniciar la aplicación
RegistroVentana.mainloop()