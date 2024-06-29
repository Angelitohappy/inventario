import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from mysql.connector import Error
from util.generic import centrar_ventana
# Creacion y diseño de la self.ventana principal


def formatear_lineas(lineas):
    # Obtener la longitud máxima de cada campo
    almacen_max_len = max(len(linea[0]) for linea in lineas)
    # Crear una cadena de formato para ajustar el ancho de los campos de texto
    formato = "{:<{almacen}} "

    # Crear una lista con las líneas formateadas
    lineas_formateadas = [formato.format(linea[0],
                                        almacen=almacen_max_len) for linea in lineas]

    return lineas_formateadas

class almacenx():
    
    def toAgregar(self):
        from interfaces.REGISTRO_DE_ALMACEN_VENTANA import almacen
        self.ventana.destroy()
        almacen()
        
    def RecibirAlmacen(self):
        try:
            from database.module_bdd import DatabaseManager
            db = DatabaseManager()
            almacen = db.read_data_nombreAlmacen()    
            db.close_connection()
        except Error as e:
            messagebox.showerror(title="Error de conexión", message=f"No se pudo conectar a la base de idp: {e}")
        return almacen

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
        
        FrameL = tk.Frame(self.ventana, highlightbackground="black",
                        highlightthickness=0)
        self.lista = tk.Listbox(FrameL, background="#FFE7DB",
                                relief=tk.SOLID, bd=0, selectmode="SINGLE")
        self.lista.config(font=("Arial", 14),
                            foreground="#420000", justify="left", selectbackground="red")
        FrameL.place(relx=0.650, rely=0.250, relwidth=0.650,
                        relheight=0.585, anchor='n')
        
        almacenes = self.RecibirAlmacen()
        print(almacenes)
        almacenes = formatear_lineas(almacenes)
        for almacen in almacenes:
            self.lista.insert(tk.END, almacen)
        
        scrollbar = tk.Scrollbar(FrameL, troughcolor="maroon",
                                highlightcolor="maroon")
        scrollbar.pack(side='right', fill='y')
        self.lista.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.lista.yview)



        self.ventana.mainloop()

