import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from mysql.connector import Error
from util.generic import centrar_ventana
import interfaces.movimiento as rc3
import sys

class cambiar_almacen():
    
    def toMovimiento(self):
        username = self.username 
        from interfaces.movimiento import verMovimientos
        self.ventana.destroy()
        rc3.verMovimientos(username)
        
    def buscar_almacen(self):
        try:
            from database.module_bdd import DatabaseManager
            db = DatabaseManager()
            datos = db.read_data_nombreAlmacen()
            db.close_connection()
        except Error as e:
            messagebox.showerror(title="Error de conexión", message=f"No se pudo conectar a la base de datos: {e}") 
        return datos
    
    def buscar_codigo(self):
        try:
            from database.module_bdd import DatabaseManager
            db = DatabaseManager()
            datos = db.read_data_codProducto()
            db.close_connection()
        except Error as e:
            messagebox.showerror(title="Error de conexión", message=f"No se pudo conectar a la base de datos: {e}") 
        return datos
    
    def move(self):
        cod=self.codigo.get()
        alma = self.Almacen.get()
        try:
            from database.module_bdd import DatabaseManager
            db = DatabaseManager()
            idPro = db.read_data_idProducto(cod)
            print(idPro)
            idAl = db.read_data_idAlmacen(alma)
            print(idAl)
            db.update_data_producto_almacen(idPro=str(idPro[0]),idAl=str(idAl[0]))
            username = self.username 
            iduser=db.read_data_id(username=username)
            db.insert_data_registro_move(str(iduser[0]))
            from interfaces.movimiento import verMovimientos
            self.ventana.destroy()
            rc3.verMovimientos(username)
            db.close_connection()
        except Error as e:
            messagebox.showerror(title="Error de conexión", message=f"No se pudo conectar a la base de datos: {e}") 
            

    def __init__(self,username):
        self.ventana = tk.Tk()
        self.ventana.title("Movimientos")
        self.ventana.geometry("400x200")
        self.ventana.resizable (0,0)
        self.ventana.overrideredirect(True)
        self.ventana.configure(bg = "lavender")
        centrar_ventana(self.ventana,400,200)
        
        self.username = username
        print(self.username)
        
        frame_superior = tk.Frame(self.ventana)
        frame_superior.configure(width = 800, height = 50, bg = "palegreen4", bd = 5)
        frame_superior.pack(fill="x")

        titulo = tk.Label(self.ventana, text = "Movimiento")
        titulo.config(bg = "palegreen4", anchor="center", font = ("Arial", 12))
        titulo.place(x=150,y=0)

        frame = tk.LabelFrame(self.ventana,text="Cambiar Almacen")
        frame.configure(width = 350, height = 90, bg = "lavender", bd = 5)
        frame.place(x=55,y=70)
        
        label1 = tk.Label(frame, text = "Codigo")
        label1.config(bg = "lavender", anchor="w", font = ("Arial", 8))
        label1.grid(row=0,column=0)

        cod = self.buscar_codigo()
        self.codigo=ttk.Combobox(frame,width=20, height=5 ,values=['prueba'], state="readonly", font = ("Arial", 8))
        self.codigo["values"] = [fila[0] for fila in cod]
        self.codigo.current(0)
        self.codigo.grid(row=1,column=0)

        label2 = tk.Label(frame, text = "Almacen")
        label2.config(bg = "lavender", anchor="w", font = ("Arial", 8))
        label2.grid(row=0,column=1)

        alma = self.buscar_almacen()
        self.Almacen=ttk.Combobox(frame,width=20, height=5 ,values=['prueba'], state="readonly", font = ("Arial", 8))
        self.Almacen["values"] = [fila[0] for fila in alma]
        self.Almacen.current(0)
        self.Almacen.grid(row=1,column=1)
        
        # Botón de salir
        imgsSalir = tk.PhotoImage(file='C://Users/Usuario/Documents/inventario/software v1/images/atras.png')
        self.salir = tk.Button(frame_superior, image=imgsSalir, command=self.toMovimiento, bg="palegreen4", borderwidth=0)
        self.salir.pack(side="right", padx=10)
        
        boton_añadir2 = tk.Button(self.ventana, text = "Confirmar")
        boton_añadir2.config(width=15, fg = "white", bg = "medium sea green", font = ("Arial", 14), relief="groove",command=self.move)
        boton_añadir2.place(x = 130, y = 140)

        self.ventana.mainloop()