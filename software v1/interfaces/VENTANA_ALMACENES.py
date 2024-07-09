import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from mysql.connector import Error
from util.generic import centrar_ventana
import interfaces.REGISTRO_DE_ALMACEN_VENTANA as rc2
import interfaces.editar_almacen as rc4
# Creacion y diseño de la self.ventana principal

class verAlmacen():
    
    def toEdit(self):
        username = self.username 
        from interfaces.editar_almacen import edit_alamacen
        self.ventana.destroy()
        rc4.edit_alamacen(username)
    
    def toPrincipal(self):
        username = self.username 
        from interfaces.VENTANA_PRINCIPAL import admin
        self.ventana.destroy()
        admin(username)
    
    def toAgregar(self):
        username = self.username 
        from interfaces.REGISTRO_DE_ALMACEN_VENTANA import almacen
        self.ventana.destroy()
        rc2.almacen(username)
        
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
        
    def RecibirAlmacen(self):
        try:
            from database.module_bdd import DatabaseManager
            db = DatabaseManager()
            almacen = db.read_data_Almacen()    
            db.close_connection()
        except Error as e:
            messagebox.showerror(title="Error de conexión", message=f"No se pudo conectar a la base de idp: {e}")
        return almacen
    
    def remove(self):
        x = self.tree.selection()
        for records in x:
            self.tree.delete(records)

    def __init__(self,username):
        self.ventana = tk.Tk()
        self.ventana.title("Registro de producto")
        self.ventana.geometry("600x400")
        self.ventana.resizable (0,0)
        self.ventana.overrideredirect(True)
        self.ventana.configure(bg = "lavender")
        centrar_ventana(self.ventana,800,500)

        # Codigo del panel verde ubicado en la zona izquierda de la self.ventana 
        self.username = username
        print(self.username)
        
        frame_superior = tk.Frame(self.ventana)
        frame_superior.configure(width = 800, height = 50, bg = "palegreen4", bd = 5)
        frame_superior.pack(fill="x")
        
        frame = tk.Frame(self.ventana)
        frame.configure(width = 100, height = 50, bg = "palegreen4", bd = 5)
        frame.place(x=300,y=140)
        
        # Botón de salir
        imgsSalir = tk.PhotoImage(file='C://Users/Usuario/Documents/inventario/software v1/images/atras.png')
        self.salir = tk.Button(frame_superior, image=imgsSalir, command=self.toPrincipal, bg="palegreen4", borderwidth=0)
        self.salir.pack(side="right", padx=10)
        
        
        buscar=tk.StringVar()
        self.entry1 = tk.Entry(self.ventana,textvariable=buscar)
        self.entry1.config(fg = "gray", bg = "white", font = ("Arial", 12), relief= "raised", width= 50)
        self.entry1.place(x = 261,y = 100)
        imgBuscar = tk.PhotoImage(file='C://Users/Usuario/Documents/inventario/software v1/images/buscar (1).png')
        boton_buscar = tk.Button(self.ventana, image=imgBuscar,command=self.buscador)
        boton_buscar.config(bg = "medium sea green", relief="groove")
        boton_buscar.place(x = 715, y = 100)
        
        


        boton_añadir = tk.Button(self.ventana, text = "Añadir almacen")
        boton_añadir.config(width=13, fg = "white", bg = "medium sea green", font = ("Arial", 14), relief="groove",command=self.toAgregar)
        boton_añadir.place(x = 20, y = 140)

        boton_modif = tk.Button(self.ventana, text = "Modificar almacen")
        boton_modif.config(width=13, fg = "white", bg = "medium sea green", font = ("Arial", 14), relief="groove",command=self.toEdit)
        boton_modif.place(x = 20, y = 200)

        boton_del = tk.Button(self.ventana, text = "Eliminar almacen")
        boton_del.config(width=13, fg = "white", bg = "medium sea green", font = ("Arial", 14), relief="groove",command=self.remove)
        boton_del.place(x = 20, y = 260)

        '''
        boton_añadir2 = tk.Button(self.ventana, text = "Añadir nuevo almacen")
        boton_añadir2.config(width=50, fg = "white", bg = "medium sea green", font = ("Arial", 14), relief="groove")
        boton_añadir2.place(x = 200, y = 400)
        '''
        scrollbar = ttk.Scrollbar(frame)
        scrollbar.pack(side="right", fill="y")
        # Crear la ventana y el treeview
        self.tree = ttk.Treeview(frame,yscrollcommand=scrollbar.set, selectmode="extended")
        self.tree.pack()
        scrollbar.config(command=self.tree.yview)  
        self.tree["columns"] = ("Nombre Almacen", "Ubicacion", "Telefono")
        self.tree.column("#0", width=0,stretch=False)
        self.tree.column("Nombre Almacen",anchor="w", width=140)
        self.tree.column("Telefono", anchor="center",width=100)
        
        self.tree.heading("#0",text="",anchor="w")
        self.tree.heading("Nombre Almacen",text="Marca",anchor="center")
        self.tree.heading("Ubicacion", text="Tipo Neumático",anchor="center")
        self.tree.heading("Telefono", text="Índice Carga",anchor="center")

        # Llenar el treeview con los datos de la base de datos
        data1 = self.RecibirAlmacen()
        
        print(data1)
        if data1:
            for item in data1:
                self.tree.insert(parent="", index="end", text="", values=(item[0],item[1], item[2]))
        elif self.buscador():
            #self.tree.destroy()
            for item in self.buscador:
                self.tree.insert(parent="", index="end", text="", values=(item[0],item[1], item[2])) 
        
                
        self.ventana.mainloop()

