import sys
import tkinter as tk
from PIL import Image, ImageTk

ruta = sys.argv[1]
tipo = sys.argv[2]

ventana = tk.Tk()
ventana.title(tipo)

# Obtener dimensiones de la pantalla
screen_width = ventana.winfo_screenwidth()
screen_height = ventana.winfo_screenheight()

# Definir dimensiones y calcular posición para centrar la ventana
window_width = 500
window_height = 500

x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# Establecer la geometría de la ventana
ventana.geometry(f"{window_width}x{window_height}+{x}+{y}")

ventana.resizable(False, False)

# Cargar imagen
img = Image.open(ruta)
img.thumbnail((window_width, window_height), Image.Resampling.LANCZOS)

imagen_tk = ImageTk.PhotoImage(img)

canvas = tk.Canvas(ventana, width=window_width, height=window_height)
canvas.pack(padx=20, pady=20)

# Calcular posición para centrar imagen
x = (window_width - img.width) // 2
y = (window_height - img.height) // 2

canvas.create_image(x, y, anchor="nw", image=imagen_tk)

ventana.mainloop()
