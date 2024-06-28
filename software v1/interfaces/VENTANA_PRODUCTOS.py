import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from util.generic import centrar_ventana
# Creacion y diseño de la self.ventana principal

class add_item():
    
    def toAgregar(self):
        from interfaces.REGISTRO_DE_PRODUCTO_VENTANA import registrar_producto
        self.ventana.destroy()
        registrar_producto()
        
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Registro de producto")
        self.ventana.geometry("600x400")
        self.ventana.resizable (0,0)
        self.ventana.configure(bg = "lavender")
        centrar_ventana(self.ventana,800,500)

        # Codigo del panel verde ubicado en la zona izquierda de la self.ventana 


        frame_superior = tk.Frame(self.ventana)
        frame_superior.configure(width = 800, height = 50, bg = "palegreen4", bd = 5)
        frame_superior.place(x = 0, y = 0)

        entry1 = tk.Entry(self.ventana)
        entry1.config(fg = "gray", bg = "white", font = ("Arial", 12), relief= "raised", width= 50)
        entry1.place(x = 300,y = 100)

        boton_cerrar = tk.Button(self.ventana, text = "Añadir articulo",command=self.toAgregar)
        boton_cerrar.config(width=12, fg = "white", bg = "medium sea green", font = ("Arial", 14), relief="groove")
        boton_cerrar.place(x = 50, y = 140)

        boton_cerrar = tk.Button(self.ventana, text = "Modificar articulo")
        boton_cerrar.config(width=12, fg = "white", bg = "medium sea green", font = ("Arial", 14), relief="groove")
        boton_cerrar.place(x = 50, y = 200)

        boton_cerrar = tk.Button(self.ventana, text = "Eliminar articulo")
        boton_cerrar.config(width=12, fg = "white", bg = "medium sea green", font = ("Arial", 14), relief="groove")
        boton_cerrar.place(x = 50, y = 260)

        boton_añadir2 = tk.Button(self.ventana, text = "Añadir nuevo almacen")
        boton_añadir2.config(width=50, fg = "white", bg = "medium sea green", font = ("Arial", 14), relief="groove")
        boton_añadir2.place(x = 200, y = 400)




        self.ventana.mainloop()

