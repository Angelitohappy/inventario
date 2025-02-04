import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from mysql.connector import Error
from util.generic import centrar_ventana
import interfaces.cambio_almacen as rc3


class verMovimientos():
    
    def toPrincipal(self):
        username = self.username 
        from interfaces.VENTANA_PRINCIPAL import admin
        self.ventana.destroy()
        admin(username)
    
    def toCambiar(self):
        username = self.username 
        from interfaces.cambio_almacen import cambiar_almacen
        self.ventana.destroy()
        rc3.cambiar_almacen(username)
        
    def buscador(self):
        value = self.entry1.get()
        if len(value)>0:
            try:
                from database.module_bdd import DatabaseManager
                db = DatabaseManager()
                self.marca = db.read_data_Almacen_buscador(value)
                db.close_connection()
            except Error as e:
                messagebox.showerror(title="Error de conexión", message=f"No se pudo conectar a la base de idp: {e}")
            return self.marca
        else:
            return False
        
    def RecibirMovimientos(self):
        try:
            from database.module_bdd import DatabaseManager
            db = DatabaseManager()
            movimiento = db.read_data_movimiento()    
            db.close_connection()
        except Error as e:
            messagebox.showerror(title="Error de conexión", message=f"No se pudo conectar a la base de idp: {e}")
        return movimiento
    
    def remove(self):
        x = self.tree.selection()
        for records in x:
            self.tree.delete(records)

    def __init__(self,username):
        self.ventana = tk.Tk()
        self.ventana.title("Movimientos")
        self.ventana.geometry("600x400")
        self.ventana.resizable (0,0)
        self.ventana.overrideredirect(True)
        self.ventana.configure(bg = "lavender")
        centrar_ventana(self.ventana,700,400)

        self.username = username
        print(self.username)
        
        frame_superior = tk.Frame(self.ventana)
        frame_superior.configure(width = 800, height = 50, bg = "palegreen4", bd = 5)
        frame_superior.pack(fill="x")
        
        frame = tk.Frame(self.ventana)
        frame.configure(width = 100, height = 50, bg = "palegreen4", bd = 5)
        frame.place(x=120,y=60)
        
        # Botón de salir
        imgsSalir = tk.PhotoImage(file='C://Users/Usuario/Documents/inventario/software v1/images/atras.png')
        self.salir = tk.Button(frame_superior, image=imgsSalir, command=self.toPrincipal, bg="palegreen4", borderwidth=0)
        self.salir.pack(side="right", padx=10)
        
        boton_añadir2 = tk.Button(self.ventana, text = "Cambiar almacen")
        boton_añadir2.config(width=50, fg = "white", bg = "medium sea green", font = ("Arial", 14), relief="groove",command=self.toCambiar)
        boton_añadir2.place(x = 70, y = 300)

        scrollbar = ttk.Scrollbar(frame)
        scrollbar.pack(side="right", fill="y")
        # Crear la ventana y el treeview
        self.tree = ttk.Treeview(frame,yscrollcommand=scrollbar.set, selectmode="extended")
        self.tree.pack()
        scrollbar.config(command=self.tree.yview)  
        self.tree["columns"] = ("Codigo", "Marca", "Nombre Almacen", "Ubicacion")
        self.tree.column("#0", width=0,stretch=False)
        self.tree.column("Codigo",anchor="w", width=80)
        self.tree.column("Marca", anchor="center",width=100)
        self.tree.column("Nombre Almacen",anchor="center", width=140)
        self.tree.column("Ubicacion", anchor="center",width=100)
        
        self.tree.heading("#0",text="",anchor="w")
        self.tree.heading("Codigo", text="Codigo",anchor="w")
        self.tree.heading("Marca",text="Marca",anchor="center")
        self.tree.heading("Nombre Almacen",text="Nombre Almacen",anchor="center")
        self.tree.heading("Ubicacion", text="Ubicacion",anchor="center")
        

        # Llenar el treeview con los datos de la base de datos
        data1 = self.RecibirMovimientos()
        for item in data1:
            self.tree.insert(parent="", index="end", text="", values=(item[0],item[1], item[2],item[3]))

        self.ventana.mainloop()

