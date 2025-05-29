import os
import subprocess
import colores
import tkinter as tk
from tkinter import messagebox

import cv2
def salir():
    # Llamada llamar el método mainloop() para cambiar de ventana 
    if messagebox.askokcancel("Salir", "¿Seguro que quieres salir del programa?"):
        menuScreen.destroy()

def showRegistro():
    menuScreen.destroy()
    print(" Show registro ")
    subprocess.Popen(['python', 'Registro.py'])

def showBorrar():
    print(" showBorrar ")
    #subprocess.Popen(['python', 'C:/Users/jocel/Documents/project_SCRUM/Codigo/Karla/sistema.py'])
    menuScreen.withdraw()

def showConsultarInq():
    print(" showConsultarInq ")
    #subprocess.Popen(['python', 'Codigo/Antonio/interfaz_inquilinos.py'])
    menuScreen.withdraw()


    
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

menuScreen.resizable(False, False)
 
titulo = tk.Label(menuScreen, text="Programa de mantenimiento \n ALTUS MODA", font=("Segoe UI", 14, 'bold'))
titulo.grid(column=0,row=1,padx=2, pady=2)


#Botones
boton1=tk.Button(menuScreen, text="Registro", command = showRegistro, fg="white", font=("Segoe UI", 12),width=20, height=1, bg=colores.AzulMedio)
boton1.grid(column=0,row=3, padx=5, pady=5)

boton2=tk.Button(menuScreen, text="Consultar inquilinos", command = showConsultarInq, fg="white",  font=("Segoe UI", 12),width=20, height=1,bg=colores.AzulMedio)
boton2.grid(column=0,row=4, padx=5, pady=5)


boton5=tk.Button(menuScreen, text="Salir", command = salir, fg="white",  font=("Segoe UI", 10),bg=colores.Rojo)
boton5.grid(column=0, row=12, padx=8, pady=8)

#   messagebox.showinfo("Acceso correcto", "Ha accedido como administrador.")
menuScreen.mainloop()