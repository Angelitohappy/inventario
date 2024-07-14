import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from util.generic import centrar_ventana
from util.verifies import Verify_cedula
from tkinter import messagebox
from mysql.connector import Error

class registrar_producto():
    
    
    def regresar(self):
        username = self.username
        from interfaces.VENTANA_PRODUCTOS import verProducto
        self.ventana.destroy()
        verProducto(username)
    
    def insert_data(self):
        marca = self.entrada_marca.get()
        tipo_neumatico = self.entrada_tipo.get()
        anchura = self.entrada_ancho.get()
        perfil = self.entrada_perfil.get()
        radio = self.entrada_radio.get()
        indice_carga = self.entrada_IndCarga.get()+'kg'
        indice_velocidad = self.entrada_IndVel.get()+'km/h'
        cod = self.entrada_cantidad.get()
        almacen = self.Almacen.get()
        username = self.username
        print(username)
        try:
            from database.module_bdd import DatabaseManager
            db = DatabaseManager()
            idUsuario=db.read_data_id(username)
            idAl = db.read_data_idAlmacen(almacen)
            print(idAl[0])
            db.insert_data_producto(marca,tipo_neumatico,anchura,perfil,radio,indice_carga,indice_velocidad,cod.upper())
            idPro = db.read_data_ultimo_id_producto()
            print(idPro[0][0])
            db.insert_data_producto_almacen(str(idPro[0][0]),str(idAl[0]))
            db.insert_data_registro_insert(str(idUsuario[0]))
            db.close_connection()
            from interfaces.VENTANA_PRODUCTOS import verProducto
            self.ventana.destroy()
            verProducto(username)
            messagebox.showinfo(title="Aviso!", message="Se ha registrado exitosamente!")
        except Error as e:
            messagebox.showerror(title="Error de conexión", message=f"No se pudo conectar a la base de datos: {e}")
            
    def buscar_almacen(self):
        try:
            from database.module_bdd import DatabaseManager
            db = DatabaseManager()
            datos = db.read_data_cod_almacen()
            db.close_connection()
        except Error as e:
            messagebox.showerror(title="Error de conexión", message=f"No se pudo conectar a la base de datos: {e}") 
        return datos
    
    def __init__(self,username):
        # Creacion y diseño de la self.ventana principal
        self.ventana = tk.Tk()
        self.ventana.title("Registro de producto")
        self.ventana.geometry("600x400")
        self.ventana.overrideredirect(True)
        self.ventana.resizable (0,0)
        self.ventana.configure(bg = "white smoke")
        centrar_ventana(self.ventana,800,600)
        
        self.username = username
        print(self.username)
        
        frame_superior = tk.Frame(self.ventana)
        frame_superior.configure(width = 800, height = 50, bg = "palegreen4", bd = 5)
        frame_superior.pack(fill="x")
        
        # Titulo de la pagina
        label1 = tk.Label(frame_superior, text = "REGISTRO DE PRODUCTO")
        label1.config(bg = "palegreen4", font = ("Arial", 8, "bold"))
        label1.place(x = 320 , y = 0)
        
        # Label que funcionará como el fondo donde estarán ubicadas las  etiquetas 
        frame1 = tk.Frame(self.ventana)
        frame1.configure(width = 750, height = 515, bg = "PaleGreen3", bd = 5)
        frame1.place(x = 25 , y = 50)

        frame2 = tk.Frame(self.ventana)
        frame2.configure(width = 250, height =475, bg = "white smoke", bd = 5)
        frame2.place(x = 50 , y = 70)
        
        # Botón de salir
        imgsSalir = tk.PhotoImage(file='C://Users/Usuario/Documents/inventario/software v1/images/atras.png')
        self.salir = tk.Button(frame_superior, image=imgsSalir, command=self.regresar, bg="palegreen4", borderwidth=0)
        self.salir.pack(side="right", padx=10)

        # Botón para confirmar el envio de los datos
        s = ttk.Style()
        s.configure("BotonEnviar.TButton", foreground="black",
            background="SpringGreen4",
            padding=4,
            font=("Arial", 12),
            anchor="w"
        )
        
        boton = ttk.Button(self.ventana, text = "Enviar datos", style = "BotonEnviar.TButton",command=self.insert_data)
        boton.place(x = 650, y = 500)
        
        label = tk.Label(self.ventana, text = "Almacen")
        label.config(bg = "white smoke", font = ("Arial", 12))
        label.place(x = 75 , y = 480)
        
        datos = self.buscar_almacen()
        if datos:
            self.Almacen=ttk.Combobox(self.ventana,width=20, height=5 ,values=['prueba'], state="readonly", font = ("Arial", 12))
            self.Almacen["values"] = [fila[0] for fila in datos]
            self.Almacen.current(0)
            self.Almacen.place(x = 75, y = 510)
        else:
            messagebox.showwarning(title="Aviso!", message="Debe Registrar primero un almacen!")
            username = self.username
            from interfaces.VENTANA_PRODUCTOS import verProducto
            self.ventana.destroy()
            verProducto(username)
        
        label1 = tk.Label(self.ventana, text = "Marca")
        label1.config(bg = "white smoke", font = ("Arial", 12))
        label1.place(x = 75 , y = 75)

        self.entrada_marca=ttk.Combobox(self.ventana,width=10, height=5 ,values=['Michelini','Pirelli','Bridgestone','Goodyear'], state="readonly", font = ("Arial", 12))
        self.entrada_marca.current(0)
        self.entrada_marca.place(x = 75,y = 100)

        # Esta linea crea la etiqueta donde se va a introducir el ID del producto

        label2 = tk.Label(self.ventana, text = "Tipo de neumatico")
        label2.config(bg = "white smoke", font = ("Arial", 12))
        label2.place(x = 75 , y = 125)

        self.entrada_tipo = ttk.Combobox(self.ventana,width=10, height=5 ,values=['Verano','Invierno','Deportivo','Pista','Todoterreno'], state="readonly", font = ("Arial", 12))
        self.entrada_tipo.current(0)
        self.entrada_tipo.place(x = 75,y = 150)

        # Esta linea crea la etiqueta donde se va a introducir el indice de carga

        label3 = tk.Label(self.ventana, text = "Indice de carga")
        label3.config(bg = "white smoke", font = ("Arial", 12))
        label3.place(x = 75 , y = 175)
        labela = tk.Label(self.ventana, text = "Kg",bg = "white smoke", font = ("Arial", 12))
        labela.place(x = 175 , y = 200)
        self.carga = tk.StringVar()
        self.entrada_IndCarga = tk.Entry(self.ventana,fg = "gray", bg = "white", font = ("Arial", 12), width = 10,textvariable=self.carga)
        self.entrada_IndCarga.config(validate='key',validatecommand=(self.entrada_IndCarga.register(Verify_cedula), '%S'))
        self.entrada_IndCarga.place(x = 75, y = 200)
        
        label4 = tk.Label(self.ventana, text = "Indice de Velocidad")
        label4.config(bg = "white smoke", font = ("Arial", 12))
        label4.place(x = 75 , y = 225)
        labela = tk.Label(self.ventana, text = "Km/h",bg = "white smoke", font = ("Arial", 12))
        labela.place(x = 175 , y = 250)
        self.velocidad = tk.StringVar()
        self.entrada_IndVel = tk.Entry(self.ventana,fg = "gray", bg = "white", font = ("Arial", 12), width = 10,textvariable=self.velocidad)
        self.entrada_IndVel.config(validate='key',validatecommand=(self.entrada_IndVel.register(Verify_cedula), '%S'))
        self.entrada_IndVel.place(x = 75,y = 250)

        # Esta linea crea la etiqueta donde se va a introducir la cantidad

        label5 = tk.Label(self.ventana, text = "Codigo")
        label5.config(bg = "white smoke", font = ("Arial", 12))
        label5.place(x = 75 , y = 425) 
        self.cantidad = tk.StringVar()
        self.entrada_cantidad = tk.Entry(self.ventana,fg = "gray", bg = "white", font = ("Arial", 12), width = 10,textvariable=self.cantidad)
        self.entrada_cantidad.place(x = 75,y = 450) 

        # Esta linea crea la etiqueta donde se va a introducir el radio del neumatico

        label6 = tk.Label(self.ventana, text = "Diametro exterior")
        label6.config(bg = "white smoke", font = ("Arial", 12))
        label6.place(x = 75 , y = 325)
        self.radio = tk.StringVar()
        self.entrada_radio = tk.Entry(self.ventana,fg = "gray", bg = "white", font = ("Arial", 12), width = 10,textvariable=self.radio)
        self.entrada_radio.config(validate='key',validatecommand=(self.entrada_radio.register(Verify_cedula), '%S'))
        self.entrada_radio.place(x = 75,y = 350)

        # Esta linea crea la etiqueta donde se va a introducir el ancho del neumatico

        label7 = tk.Label(self.ventana, text = "Anchura")
        label7.config(bg = "white smoke", font = ("Arial", 12))
        label7.place(x = 75 , y = 275)
        self.ancho = tk.StringVar()
        self.entrada_ancho = tk.Entry(self.ventana,fg = "gray", bg = "white", font = ("Arial", 12), width = 10,textvariable=self.ancho)
        self.entrada_ancho.config(validate='key',validatecommand=(self.entrada_ancho.register(Verify_cedula), '%S'))
        self.entrada_ancho.place(x = 75,y = 300)
        
        label8 = tk.Label(self.ventana, text = "Perfil")
        label8.config(bg = "white smoke", font = ("Arial", 12))
        label8.place(x = 75 , y = 375)
        self.perfil = tk.StringVar()
        self.entrada_perfil = tk.Entry(self.ventana,fg = "gray", bg = "white", font = ("Arial", 12), width = 10,textvariable=self.perfil)
        self.entrada_perfil.config(validate='key',validatecommand=(self.entrada_perfil.register(Verify_cedula), '%S'))
        self.entrada_perfil.place(x = 75,y = 400)

        imgneumatico = Image.open('C://Users/Usuario/Documents/inventario/software v1/images/imagen.jpeg')
        imagen_redimensionada = imgneumatico.resize((400,410))
        imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)

        labelimagen = tk.Label(self.ventana, image = imagen_tk)
        labelimagen.place(x = 350, y = 70)
        self.ventana.mainloop()