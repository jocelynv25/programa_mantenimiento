import colores
import os
import subprocess
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def showFaceRec():
    print("Abriendo ventana de reconocimiento facial...")
    #subprocess.Popen(['python', 'C:/Users/jocel/Documents/project_SCRUM/Codigo/FaceRecSystem.py'])
    #ventana1.withdraw()

def on_closing():
    if messagebox.askokcancel("Salir", "¿Seguro que quieres salir?"):
        HomeScreen.destroy()

HomeScreen = tk.Tk()
HomeScreen.title("Programa de mantenimiento ALTUS MODA")
HomeScreen.configure(bg=colores.Blanco)  
HomeScreen.resizable(False, False)
HomeScreen.protocol("WM_DELETE_WINDOW", on_closing)

ancho_ventana = 500
alto_ventana = 350
ancho_pan = HomeScreen.winfo_screenwidth()
alto_pan = HomeScreen.winfo_screenheight()
x = (ancho_pan - ancho_ventana) // 2
y = (alto_pan - alto_ventana) // 2
HomeScreen.geometry('{}x{}+{}+{}'.format(ancho_ventana, alto_ventana, x, y)) 

marco_principal = tk.Frame(HomeScreen, bg=colores.AzulRey, padx=10, pady=10)  #  margen azul
marco_principal.pack(expand=True, fill="both")

dir_path = os.path.dirname(os.path.realpath(__file__))
pathIMG = os.path.join(dir_path, 'Imagenes/home.png')
imagen = Image.open(pathIMG)
imagen_tk = ImageTk.PhotoImage(imagen)

imagen_label = tk.Label(HomeScreen, image=imagen_tk, bg=colores.Blanco)
imagen_label.pack(pady=5) 

frame_contenedor = tk.Frame(HomeScreen, bg=colores.Blanco)
frame_contenedor.pack(expand=True)

cuadro_texto = tk.Label(frame_contenedor, text="Programa de mantenimiento\nALTUS MODA", 
                        font=("Segoe UI", 14, 'bold'), bg=colores.Blanco)
cuadro_texto.pack(pady=5) 

boton_entrar = tk.Button(frame_contenedor, text="ENTRAR AL SISTEMA", bg=colores.AzulRey, fg=colores.Blanco, font=("Helvetica", 12), command=showFaceRec)
boton_entrar.pack(pady=5, padx=50, ipadx=10, ipady=3)  

HomeScreen.mainloop()
 