import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
# Creacion y diseño de la ventana principal

ventana = tk.Tk()
ventana.title("Registro de producto")
ventana.geometry("600x400")
ventana.resizable (0,0)
ventana.configure(bg = "lavender")

# Estas dos lineas obtienen el tamaño de la pantalla

wtotal = ventana.winfo_screenwidth()
htotal = ventana.winfo_screenheight()

# Aqui se define el tamaño que tendra la ventana

wventana = 800
hventana = 500

# Aqui se divide el total del ancho y la altura para determinar el punto medio

pwidth = round(wtotal/2-wventana/2)
pheight = round(htotal/2-hventana/2)

ventana.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))

# Codigo del panel verde ubicado en la zona izquierda de la ventana 

frame_superior = tk.Frame(ventana)
frame_superior.configure(width = 800, height = 50, bg = "palegreen4", bd = 5)
frame_superior.place(x = 0, y = 0)


## Botones de la parte inferior izquierda

s = ttk.Style()
s.configure("BotonEnviar.TButton", foreground="black",
    background="SpringGreen4",
    padding=4,
    font=("Arial", 12),
    anchor="w"
)
boton = ttk.Button(ventana, text = "Enviar datos", style = "BotonEnviar.TButton")
boton.place(x = 375, y = 320)


imgusuario = tk.PhotoImage(file = "imagenes-de-usuario.png")
label = tk.Label(image = imgusuario)
label.place(x = 350, y = 80)        


ventana.mainloop()
