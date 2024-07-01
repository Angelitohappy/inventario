import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
# Creacion y diseño de la self.ventana principal
from util.generic import centrar_ventana
import interfaces.VENTANA_PRODUCTOS as rc
import interfaces.VENTANA_ALMACENES as rc2


class admin():
    
    def regresar(self):
        from interfaces.login import Acceso
        self.ventana.destroy()
        Acceso()
    
    def toArticulo(self):
        username=self.username
        from interfaces.VENTANA_PRODUCTOS import verProducto
        self.ventana.destroy()
        rc.verProducto(username)
    
    def toAlmacen(self):
        username=self.username
        from interfaces.VENTANA_ALMACENES import verAlmacen
        self.ventana.destroy()
        rc2.verAlmacen(username)
        
    def __init__(self,username): 
        self.ventana = tk.Tk()
        self.ventana.title("Registro de producto")
        self.ventana.overrideredirect(True)
        self.ventana.geometry("600x400")
        self.ventana.resizable (0,0)
        self.ventana.configure(bg = "PaleGreen3")
        centrar_ventana(self.ventana,800,500)

        self.username = username
        print(self.username)
        
        # Codigo del panel verde ubicado en la zona izquierda de la self.ventana 


        frame1 = tk.Frame(self.ventana)
        frame1.configure(width = 300, height = 500, bg = "lavender", bd = 5)
        frame1.place(x = 0 , y = 0)

        frame2 = tk.Frame(self.ventana)
        frame2.configure(width = 330, height = 330, bg = "lavender", bd = 5)
        frame2.place(x = 390 , y = 60)

        frame_superior = tk.Frame(self.ventana)
        frame_superior.configure(width = 800, height = 50, bg = "palegreen4", bd = 5)
        frame_superior.pack(fill="x")
        
        # Botón de salir
        imgsSalir = tk.PhotoImage(file='C://Users/Usuario/Documents/inventario/software v1/images/atras.png')
        self.salir = tk.Button(frame_superior, image=imgsSalir, command=self.regresar, bg="palegreen4", borderwidth=0)
        self.salir.pack(side="right", padx=10)

        boton_cerrar = tk.Button(self.ventana, text = "Ver articulos", command=self.toArticulo)
        boton_cerrar.config(width=18, fg = "white", bg = "medium sea green", font = ("Arial", 18), relief="groove")
        boton_cerrar.place(x = 430, y = 100)

        boton_cerrar = tk.Button(self.ventana, text = "Ver almacenes")
        boton_cerrar.config(width=18, fg = "white", bg = "medium sea green", font = ("Arial", 18), relief="groove",command=self.toAlmacen)
        boton_cerrar.place(x = 430, y = 160)

        boton_cerrar = tk.Button(self.ventana, text = "Reportes")
        boton_cerrar.config(width=18, fg = "white", bg = "medium sea green", font = ("Arial", 18), relief="groove")
        boton_cerrar.place(x = 430, y = 220)

        boton_cerrar = tk.Button(self.ventana, text = "Usuarios")
        boton_cerrar.config(width=18, fg = "white", bg = "medium sea green", font = ("Arial", 18), relief="groove")
        boton_cerrar.place(x = 430, y = 280)

        ## Botones de la parte inferior izquierda

        # Boton para acceder a las opciones de la cuenta
        boton_cuenta = tk.Button(self.ventana, text = "Cuenta de usuario")
        boton_cuenta.config(width=32, fg = "white", bg = "medium sea green", font = ("Arial", 12), relief="flat")
        boton_cuenta.place(x = 1, y = 335)

        # Boton para acceder a la self.ventana de ayuda
        boton_ayuda = tk.Button(self.ventana, text = "Ayuda")
        boton_ayuda.config(width=32, fg = "white", bg = "medium sea green", font = ("Arial", 12), relief="flat")
        boton_ayuda.place(x = 1, y = 370)

        # Boton para acceder a más informacion del software
        boton_mas = tk.Button(self.ventana, text = "Más")
        boton_mas.config(width=32, fg = "white", bg = "medium sea green", font = ("Arial", 12), relief="flat")
        boton_mas.place(x = 1, y = 405)

        # Boton para cerrar la sesión
        boton_cerrar = tk.Button(self.ventana, text = "Cerrar sesión")
        boton_cerrar.config(width=32, fg = "white", bg = "medium sea green", font = ("Arial", 12), relief="flat")
        boton_cerrar.place(x = 1, y = 440)

        # label donde se le dará la bienvenida al usuario cuando acceda al sistema
        label1 = tk.Label(self.ventana, text = "BIENVENIDO, USUARIO")
        label1.config(fg ="black", bg = "lavender", font = ("Arial", 14))
        label1.place(x = 40 , y = 240)

        imgusuario = tk.PhotoImage(file = "C://Users/Usuario/Documents/inventario/software v1/images/imagenes-de-usuario.png")
        label = tk.Label(image = imgusuario)
        label.place(x = 90, y = 80)        


        self.ventana.mainloop()
