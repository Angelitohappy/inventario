import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from mysql.connector import Error
from util.generic import centrar_ventana
# Creacion y diseño de la self.ventana principal


def formatear_lineas(lineas):
    # Obtener la longitud máxima de cada campo
    marca_max_len = max(len(linea[0]) for linea in lineas)
    tipo_max_len = max(len(linea[1]) for linea in lineas)
    anchura_max_len = max(len(linea[2]) for linea in lineas)
    perfil_max_len = max(len(linea[3]) for linea in lineas)
    radio_max_len = max(len(linea[4]) for linea in lineas)
    carga_max_len = max(len(linea[5]) for linea in lineas)
    velocidad_max_len = max(len(linea[6]) for linea in lineas)
    cantidad_max_len = max(len(str(linea[7])) for linea in lineas)
    
    # Crear una cadena de formato para ajustar el ancho de los campos de texto
    formato = "{:<{marca}} |  {:<{tipo}} | {:<{anchura}} | {:<{perfil}} | {:<{radio}} | {:<{carga}} | {:<{velocidad}} | {:<{cantidad}}"

    # Crear una lista con las líneas formateadas
    lineas_formateadas = [formato.format(linea[0], linea[1], linea[2], linea[3], linea[4], linea[5], linea[6], linea[7],
                                        marca=marca_max_len, tipo=tipo_max_len,
                                        anchura=anchura_max_len, perfil=perfil_max_len,
                                        radio=radio_max_len, carga=carga_max_len,
                                        velocidad=velocidad_max_len, cantidad=cantidad_max_len) for linea in lineas]

    return lineas_formateadas

class verProducto():
    
    def marcaLista(self):
        global dato0
        idm = self.lista.selection_get()
        print(idm)
        idm = idm.split("|")
        print(idm)
        dato0 = idm[0]
        dato0 = dato0.replace(' ','')
        dato0 = dato0
        return  dato0

    def tipoLista(self):
        global dato1
        idt = self.lista.selection_get()
        print(idt)
        idt = idt.split("|")
        print(idt)
        dato1 = idt[1]
        dato1 = dato1.replace(' ','')
        dato1 = dato1 
        return  dato1
    
    def anchuraLista(self):
        global dato2
        ida = self.lista.selection_get()
        print(ida)
        ida = ida.split("|")
        print(ida)
        dato2 = ida[2]
        dato2 = dato2.replace(' ','')
        dato2 = dato2 
        return  dato2
    
    def perfilLista(self):
        global dato3
        idp = self.lista.selection_get()
        print(idp)
        idp = idp.split("|")
        print(idp)
        dato3 = idp[3]
        dato3 = dato3.replace(' ', '')
        dato3 = dato3
        return dato3
    
    def radioLista(self):
        global dato4
        idr = self.lista.selection_get()
        print(idr)
        idr = idr.split("|")
        print(idr)
        dato4 = idr[4]
        dato4 = dato4
        return  dato4

    def cargaLista(self):
        global dato5
        idc = self.lista.selection_get()
        print(idc)
        idC = idc.split("|")
        print(idc)
        dato5 = idc[5]
        dato5 = dato5.replace(' ','')
        dato5 = dato5 
        return  dato5
    
    def velocidadLista(self):
        global dato6
        idv = self.lista.selection_get()
        print(idv)
        idv = idv.split("|")
        print(idv)
        dato6 = idv[6]
        dato6 = dato6.replace(' ','')
        dato6 = dato6 
        return  dato6
    
    def cantidadLista(self):
        global dato7
        datos = self.lista.selection_get()
        print(datos)
        datos = datos.split("|")
        print(datos)
        dato7 = datos[7]
        dato7 = dato7.replace(' ', '')
        dato7 = dato7
        return dato7
    
    def toAgregar(self):
        from interfaces.REGISTRO_DE_PRODUCTO_VENTANA import registrar_producto
        self.ventana.destroy()
        registrar_producto()
        
    def Recibirproductos(self):
        try:
            from database.module_bdd import DatabaseManager
            db = DatabaseManager()
            productos = db.read_data_producto()    
            db.close_connection()
        except Error as e:
            messagebox.showerror(title="Error de conexión", message=f"No se pudo conectar a la base de idp: {e}")
        return productos

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
        
        FrameL = tk.Frame(self.ventana, highlightbackground="black",
                        highlightthickness=0)
        self.lista = tk.Listbox(FrameL, background="#FFE7DB",
                                relief=tk.SOLID, bd=0, selectmode="SINGLE")
        self.lista.config(font=("Arial", 14),
                            foreground="#420000", justify="left", selectbackground="red")
        FrameL.place(relx=0.600, rely=0.200, relwidth=0.650,
                        relheight=0.585, anchor='n')
        
        productos = self.Recibirproductos()
        print(productos)
        productos = formatear_lineas(productos)
        for producto in productos:
            self.lista.insert(tk.END, producto)
        
        scrollbar = tk.Scrollbar(FrameL, troughcolor="maroon",
                                highlightcolor="maroon")
        scrollbar.pack(side='right', fill='y')
        self.lista.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.lista.yview)

        self.ventana.mainloop()

