import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from mysql.connector import Error
from util.generic import centrar_ventana

class verProducto():
    
    def regresar(self):
        from interfaces.VENTANA_PRINCIPAL import admin
        self.ventana.destroy()
        admin()
    
    def toAgregar(self):
        from interfaces.REGISTRO_DE_PRODUCTO_VENTANA import registrar_producto
        self.ventana.destroy()
        registrar_producto()
        
    def Recibirproductos(self):
        try:
            from database.module_bdd import DatabaseManager
            db = DatabaseManager()
            datos = db.read_data_producto_almacen()    
            db.close_connection()
        except Error as e:
            messagebox.showerror(title="Error de conexión", message=f"No se pudo conectar a la base de idp: {e}")
        return datos
        
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.overrideredirect(True)
        self.ventana.title("Registro de producto")
        self.ventana.geometry("600x400")
        self.ventana.resizable (0,0)
        self.ventana.configure(bg = "lavender")
        centrar_ventana(self.ventana,800,500)

        # Codigo del panel verde ubicado en la zona izquierda de la self.ventana 


        frame_superior = tk.Frame(self.ventana)
        frame_superior.configure(width = 800, height = 50, bg = "palegreen4", bd = 5)
        frame_superior.pack(fill="x")
        
        # Botón de salir
        imgsSalir = tk.PhotoImage(file='C://Users/Usuario/Documents/inventario/software v1/images/atras.png')
        self.salir = tk.Button(frame_superior, image=imgsSalir, command=self.regresar, bg="palegreen4", borderwidth=0)
        self.salir.pack(side="right", padx=10)

        entry1 = tk.Entry(self.ventana)
        entry1.config(fg = "gray", bg = "white", font = ("Arial", 12), relief= "raised", width= 50)
        entry1.place(x = 260,y = 70)
        imgBuscar = tk.PhotoImage(file='C://Users/Usuario/Documents/inventario/software v1/images/buscar (1).png')
        boton_buscar = tk.Button(self.ventana, image=imgBuscar,command=self.toAgregar)
        boton_buscar.config(bg = "medium sea green", relief="groove")
        boton_buscar.place(x = 715, y = 71)

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
        
        # Crear la ventana y el treeview
        tree = ttk.Treeview(self.ventana)
        tree["columns"] = ("Marca", "Tipo Neumático", "Índice Carga", "Índice Velocidad", "Nombre Almacén", "Ubicación")
        tree.column("#0", width=100)
        tree.column("#1", width=100)
        tree.column("#2", width=100)
        tree.column("#3", width=100)
        tree.column("#4", width=100)
        tree.column("#5", width=100)
        tree.heading("#0",text="Marca")
        tree.heading("#1", text="Tipo Neumático")
        tree.heading("#2", text="Índice Carga")
        tree.heading("#3", text="Índice Velocidad")
        tree.heading("#4", text="Nombre Almacén")
        tree.heading("#5", text="Ubicación")
        tree.place(x=200,y=100)

        # Llenar el treeview con los datos de la base de datos
        data = self.Recibirproductos()
        print(data)
        for item in data:
            tree.insert(parent="", index="end", text=item[0], values=(item[1], item[2], item[3], item[4], item[5]))
                
        self.ventana.mainloop()

