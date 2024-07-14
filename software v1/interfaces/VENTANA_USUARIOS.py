import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from mysql.connector import Error
from util.generic import centrar_ventana
import interfaces.REGISTRO_DE_ALMACEN_VENTANA as rc2
import interfaces.editar_almacen as rc4
# Creacion y diseño de la self.ventana principal

class verUsuarios():
    
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

    def RecibirRegistro(self):
        try:
            from database.module_bdd import DatabaseManager
            db = DatabaseManager()
            control = db.read_data_movimiento_usuario()    
            db.close_connection()
        except Error as e:
            messagebox.showerror(title="Error de conexión", message=f"No se pudo conectar a la base de idp: {e}")
        return control
    
    def remove(self):
        x = self.tree.selection()
        for records in x:
            self.tree.delete(records)

    def __init__(self,username):
        self.ventana = tk.Tk()
        self.ventana.title("Registro Usuario")
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
        frame.configure(width = 140, height = 50, bg = "palegreen4", bd = 5)
        frame.place(x=300,y=140)
        
        # Titulo de la pagina
        label1 = tk.Label(frame_superior, text = "Auditoria de Usuarios")
        label1.config(bg = "palegreen4", font = ("Arial", 8, "bold"))
        label1.place(x = 320 , y = 0)
        
        # Botón de salir
        imgsSalir = tk.PhotoImage(file='C://Users/Usuario/Documents/inventario/software v1/images/atras.png')
        self.salir = tk.Button(frame_superior, image=imgsSalir, command=self.toPrincipal, bg="palegreen4", borderwidth=0)
        self.salir.pack(side="right", padx=10)

        boton_modif = tk.Button(self.ventana, text = "Modificar Permisos")
        boton_modif.config(width=13, fg = "white", bg = "medium sea green", font = ("Arial", 14), relief="groove",command=self.toEdit)
        boton_modif.place(x = 20, y = 200)

        '''
        boton_del = tk.Button(self.ventana, text = "Eliminar Usuario")
        boton_del.config(width=13, fg = "white", bg = "medium sea green", font = ("Arial", 14), relief="groove",command=self.remove)
        boton_del.place(x = 20, y = 260)
        '''
        scrollbar = ttk.Scrollbar(frame)
        scrollbar.pack(side="right", fill="y")
        # Crear la ventana y el treeview
        self.tree = ttk.Treeview(frame,yscrollcommand=scrollbar.set, selectmode="extended")
        self.tree.pack()
        scrollbar.config(command=self.tree.yview)  
        self.tree["columns"] = ("Nombre", "Usuario", "Tipo de Movimiento","YYYY/MM/DD/Min/Seg")
        self.tree.column("#0", width=0,stretch=False)
        self.tree.column("Nombre",anchor="w", width=100)
        self.tree.column("Usuario", anchor="center",width=100)
        self.tree.column("Tipo de Movimiento", anchor="center",width=100)
        self.tree.column("YYYY/MM/DD/Min/Seg", anchor="center",width=100)
        
        self.tree.heading("#0",text="",anchor="w")
        self.tree.heading("Nombre",text="Nombre",anchor="w")
        self.tree.heading("Usuario", text="Usuario",anchor="center")
        self.tree.heading("Tipo de Movimiento", text="Tipo de Movimiento",anchor="center")
        self.tree.heading("YYYY/MM/DD/Min/Seg", text="YYYY/MM/DD/Min/Seg",anchor="center")
        
        # Llenar el treeview con los datos de la base de datos
        
        data1 = self.RecibirRegistro()
        print(data1)
        if data1:
            for item in data1:
                self.tree.insert(parent="", index="end", text="", values=(item[0],item[1], item[2],item[3]))
        
                
        self.ventana.mainloop()

