import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from mysql.connector import Error
from util.generic import centrar_ventana
# Creacion y diseño de la self.ventana principal

class verAlmacen():
    
    def toPrincipal(self):
        from interfaces.VENTANA_PRINCIPAL import admin
        self.ventana.destroy()
        admin()
    
    def toAgregar(self):
        from interfaces.REGISTRO_DE_ALMACEN_VENTANA import almacen
        self.ventana.destroy()
        almacen()
        
    def RecibirAlmacen(self):
        try:
            from database.module_bdd import DatabaseManager
            db = DatabaseManager()
            almacen = db.read_data_Almacen()    
            db.close_connection()
        except Error as e:
            messagebox.showerror(title="Error de conexión", message=f"No se pudo conectar a la base de idp: {e}")
        return almacen

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Registro de producto")
        self.ventana.geometry("600x400")
        self.ventana.resizable (0,0)
        self.ventana.overrideredirect(True)
        self.ventana.configure(bg = "lavender")
        centrar_ventana(self.ventana,800,500)

        # Codigo del panel verde ubicado en la zona izquierda de la self.ventana 
        
        frame_superior = tk.Frame(self.ventana)
        frame_superior.configure(width = 800, height = 50, bg = "palegreen4", bd = 5)
        frame_superior.pack(fill="x")
        
        # Botón de salir
        imgsSalir = tk.PhotoImage(file='C://Users/Usuario/Documents/inventario/software v1/images/atras.png')
        self.salir = tk.Button(frame_superior, image=imgsSalir, command=self.toPrincipal, bg="palegreen4", borderwidth=0)
        self.salir.pack(side="right", padx=10)

        entry1 = tk.Entry(self.ventana)
        entry1.config(fg = "gray", bg = "white", font = ("Arial", 12), relief= "raised", width= 50)
        entry1.place(x = 261,y = 100)
        imgBuscar = tk.PhotoImage(file='C://Users/Usuario/Documents/inventario/software v1/images/buscar (1).png')
        boton_buscar = tk.Button(self.ventana, image=imgBuscar,command=self.toAgregar)
        boton_buscar.config(bg = "medium sea green", relief="groove")
        boton_buscar.place(x = 715, y = 100)


        boton_añadir = tk.Button(self.ventana, text = "Añadir almacen")
        boton_añadir.config(width=13, fg = "white", bg = "medium sea green", font = ("Arial", 14), relief="groove",command=self.toAgregar)
        boton_añadir.place(x = 20, y = 140)

        boton_modif = tk.Button(self.ventana, text = "Modificar almacen")
        boton_modif.config(width=13, fg = "white", bg = "medium sea green", font = ("Arial", 14), relief="groove")
        boton_modif.place(x = 20, y = 200)

        boton_del = tk.Button(self.ventana, text = "Eliminar almacen")
        boton_del.config(width=13, fg = "white", bg = "medium sea green", font = ("Arial", 14), relief="groove")
        boton_del.place(x = 20, y = 260)

        '''
        boton_añadir2 = tk.Button(self.ventana, text = "Añadir nuevo almacen")
        boton_añadir2.config(width=50, fg = "white", bg = "medium sea green", font = ("Arial", 14), relief="groove")
        boton_añadir2.place(x = 200, y = 400)
        '''
        
        # Crear la ventana y el treeview
        tree = ttk.Treeview(self.ventana)
        tree["columns"] = ("Nombre Almacén", "Ubicación", "Telefono")
        tree.column("#0", width=100)
        tree.column("#1", width=100)
        tree.column("#2", width=100)
        tree.heading("#0",text="Nombre Almacen")
        tree.heading("#1", text="Ubicacion")
        tree.heading("#2", text="Telefono")
        tree.place(x=260,y=140)

        # Llenar el treeview con los datos de la base de datos
        data = self.RecibirAlmacen()
        print(data)
        for item in data:
            tree.insert(parent="", index="end", text=item[0], values=(item[1], item[2]))
                
        self.ventana.mainloop()

