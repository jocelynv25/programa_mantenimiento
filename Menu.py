import os
import subprocess
import colores
import tkinter as tk
from tkinter import messagebox

import cv2

def showRegistro():
    menuScreen.destroy()
    subprocess.Popen(['python', 'Registro.py'])

def showInventario():
    menuScreen.destroy()
    subprocess.Popen(['python', 'Inventario3.py'])

def showBuscador():
    menuScreen.destroy()
    subprocess.Popen(['python', 'Buscador.py'])

def showReportar():
    menuScreen.destroy()
    subprocess.Popen(['python', 'Reportar.py'])

def on_closing():
    if messagebox.askokcancel("Salir", "¿Seguro que quieres salir?"):
        menuScreen.destroy()
    
menuScreen = tk.Tk()
menuScreen.title("Programa de mantenimiento ALTUS MODA")

#Ajusta la ventana 
ancho_ventana = 320
alto_ventana = 480

menuScreen.minsize(width=ancho_ventana, height=alto_ventana)
menuScreen.maxsize(width=ancho_ventana, height=alto_ventana)
menuScreen.config(padx=35, pady=35)

ancho_pan = menuScreen.winfo_screenwidth()
alto_pan = menuScreen.winfo_screenheight()
x = (ancho_pan - ancho_ventana) // 2
y = (alto_pan - alto_ventana) // 2
menuScreen.geometry('{}x{}+{}+{}'.format(ancho_ventana, alto_ventana, x, y)) 

#Logotipo del menú
dir_path = os.path.dirname(os.path.realpath(__file__))
path = os.path.join(dir_path, 'Imagenes/casa.png')
img = tk.PhotoImage(file=path)
img = img.subsample(7, 7)  

# mostrar la imagen como icono
lbl_icono = tk.Label(menuScreen, image=img)
lbl_icono.grid(column=0, row=0, padx=1, pady=1, sticky="nsew") 

menuScreen.grid_rowconfigure(2, weight=1)
menuScreen.grid_columnconfigure(2, weight=1)

menuScreen.protocol("WM_DELETE_WINDOW", on_closing)
menuScreen.resizable(False, False)
 
titulo = tk.Label(menuScreen, text="Programa de mantenimiento \n ALTUS MODA", font=("Segoe UI", 14, 'bold'))
titulo.grid(column=0,row=1,padx=2, pady=2)


#Botones
boton1=tk.Button(menuScreen, text="Registro", command = showRegistro, fg="white", font=("Segoe UI", 12),width=20, height=1, bg=colores.AzulMedio)
boton1.grid(column=0,row=3, padx=5, pady=5)

boton2=tk.Button(menuScreen, text="Inventario", command = showInventario, fg="white",  font=("Segoe UI", 12),width=20, height=1,bg=colores.AzulMedio)
boton2.grid(column=0,row=4, padx=5, pady=5)

boton3=tk.Button(menuScreen, text="Buscador", command = showBuscador, fg="white",  font=("Segoe UI", 12),width=20, height=1,bg=colores.AzulMedio)
boton3.grid(column=0, row=5, padx=5, pady=5)

boton4=tk.Button(menuScreen, text="Reportar falla", command = showReportar, fg="white",  font=("Segoe UI", 12),width=20, height=1,bg=colores.AzulMedio)
boton4.grid(column=0, row=6, padx=5, pady=5)

botonSalir=tk.Button(menuScreen, text="Salir", command = on_closing, fg="white",  font=("Segoe UI", 10),bg=colores.Rojo)
botonSalir.grid(column=0, row=12, padx=8, pady=8)

#   messagebox.showinfo("Acceso correcto", "Ha accedido como administrador.")
menuScreen.mainloop()