import tkinter as tk
from util.generic import centrar_ventana
from tkinter import messagebox
from mysql.connector import Error

class almacen():
    
    def regresar(self):
        from interfaces.VENTANA_ALMACENES import verAlmacen
        self.ventana.destroy()
        verAlmacen()
    
    def insert_alamcen(self):
        nombre=self.entrada_almacen.get()
        ubicacion=self.entrada_ubicacion.get()
        nro=self.entrada_nro.get()
        try:
            from database.module_bdd import DatabaseManager
            db=DatabaseManager()
            db.insert_data_alamcen(nombre,ubicacion,nro)
            db.close_connection()
        except Error as e:
            messagebox.showerror(title="Error de conexión", message=f"No se pudo conectar a la base de datos: {e}")
            
    def __init__(self):
        # Creacion y diseño de la self.ventana principal
        self.ventana = tk.Tk()
        self.ventana.title("Registro de almacen")
        self.ventana.overrideredirect(True)
        self.ventana.geometry("600x400")
        self.ventana.resizable (0,0)
        self.ventana.configure(bg = "white smoke")
        centrar_ventana(self.ventana,600,400)
        
        frame_superior = tk.Frame(self.ventana)
        frame_superior.configure(width = 800, height = 50, bg = "palegreen4", bd = 5)
        frame_superior.pack(fill="x")
        
        label1 = tk.Label(frame_superior, text = "REGISTRO DE ALMACEN")
        label1.config(bg = "palegreen4", font = ("Arial", 8, "bold"))
        label1.place(x = 0 , y = 0)

        # Label que funcionará como el fondo donde estarán ubicadas las etiquetas 

        frame1 = tk.Frame(self.ventana)
        frame1.configure(width = 550, height = 315, bg = "PaleGreen3", bd = 5)
        frame1.place(x = 25 , y = 50)
        
        
        # Botón de salir
        imgsSalir = tk.PhotoImage(file='C://Users/Usuario/Documents/inventario/software v1/images/atras.png')
        self.salir = tk.Button(frame_superior, image=imgsSalir, command=self.regresar, bg="palegreen4", borderwidth=0)
        self.salir.pack(side="right", padx=10)

        frame2 = tk.Frame(self.ventana)
        frame2.configure(width = 290, height = 245, bg = "white smoke", bd = 5)
        frame2.place(x = 170 , y = 70)

        # Botón para confirmar el envio de los datos

        boton = tk.Button(self.ventana, text = "Enviar datos")
        boton.config(fg = "white", bg = "green", font = ("Arial", 12),command=self.insert_alamcen)
        boton.place(x = 250, y = 250)

        # Esta linea crea la etiqueta donde se va a introducir el ID del almacen

        label1 = tk.Label(self.ventana, text = "Nombre del Almacen")
        label1.config(bg = "white smoke", font = ("Arial", 12))
        label1.place(x = 220 , y = 85)

        self.entrada_almacen= tk.Entry(self.ventana, textvariable = "")
        self.entrada_almacen.config(fg = "gray", bg = "white", font = ("Arial", 12), width = 25)
        self.entrada_almacen.place(x = 220,y = 110)


        # Esta linea crea la etiqueta donde se va a introducir la dirección del almacen

        label3 = tk.Label(self.ventana, text = "Localización")
        label3.config(bg = "white smoke", font = ("Arial", 12))
        label3.place(x = 220 , y = 135)

        self.entrada_ubicacion = tk.Entry(self.ventana)
        self.entrada_ubicacion.config(fg = "gray", bg = "white", font = ("Arial", 12))
        self.entrada_ubicacion.place(x = 220 ,y = 160)

        # Esta linea crea la etiqueta donde se va a introducir el numero de telefono del almacen

        label3 = tk.Label(self.ventana, text = "Nro de telefono")
        label3.config(bg = "white smoke", font = ("Arial", 12))
        label3.place(x = 220 , y = 185)

        self.entrada_nro = tk.Entry(self.ventana)
        self.entrada_nro.config(fg = "gray", bg = "white", font = ("Arial", 12))
        self.entrada_nro.place(x = 220 ,y = 210)

        self.ventana.mainloop()