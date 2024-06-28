import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from util.generic import centrar_ventana

class registrar_producto():
    
    def __init__(self):
        # Creacion y diseño de la self.ventana principal
        self.ventana = tk.Tk()
        self.ventana.title("Registro de producto")
        self.ventana.geometry("600x400")
        self.ventana.resizable (0,0)
        self.ventana.configure(bg = "white smoke")
        centrar_ventana(self.ventana,800,600)

        # Titulo de la pagina

        label1 = tk.Label(self.ventana, text = "REGISTRO DE PRODUCTO")
        label1.config(bg = "white smoke", font = ("Arial", 16, "bold"))
        label1.place(x = 260 , y = 15)

        # Label que funcionará como el fondo donde estarán ubicadas las  etiquetas 

        frame1 = tk.Frame(self.ventana)
        frame1.configure(width = 750, height = 515, bg = "PaleGreen3", bd = 5)
        frame1.place(x = 25 , y = 50)

        frame2 = tk.Frame(self.ventana)
        frame2.configure(width = 250, height = 415, bg = "white smoke", bd = 5)
        frame2.place(x = 50 , y = 70)

        # Botón para confirmar el envio de los datos

        s = ttk.Style()
        s.configure("BotonEnviar.TButton", foreground="black",
            background="SpringGreen4",
            padding=4,
            font=("Arial", 12),
            anchor="w"
        )
        boton = ttk.Button(self.ventana, text = "Enviar datos", style = "BotonEnviar.TButton")
        boton.place(x = 165, y = 420)

        # Esta linea crea la etiqueta donde se va a introducir el nombre del producto 

        label1 = tk.Label(self.ventana, text = "Marca")
        label1.config(bg = "white smoke", font = ("Arial", 12))
        label1.place(x = 75 , y = 85)

        entrada_marca= tk.Entry(self.ventana, textvariable = "")
        entrada_marca.config(fg = "gray", bg = "white", font = ("Arial", 12))
        entrada_marca.place(x = 75,y = 110)


        # Esta linea crea la etiqueta donde se va a introducir el ID del producto

        label3 = tk.Label(self.ventana, text = "ID del Producto")
        label3.config(bg = "white smoke", font = ("Arial", 12))
        label3.place(x = 75 , y = 135)

        entrada_id = tk.Entry(self.ventana)
        entrada_id.config(fg = "gray", bg = "white", font = ("Arial", 12))
        entrada_id.place(x = 75,y = 160)

        # Esta linea crea la etiqueta donde se va a introducir el indice de carga

        label1 = tk.Label(self.ventana, text = "Indice de carga")
        label1.config(bg = "white smoke", font = ("Arial", 12))
        label1.place(x = 75 , y = 185)

        entrada_IndCarga = tk.Entry(self.ventana)
        entrada_IndCarga.config(fg = "gray", bg = "white", font = ("Arial", 12))
        entrada_IndCarga.place(x = 75,y = 210)

        # Esta linea crea la etiqueta donde se va a introducir la cantidad

        label1 = tk.Label(self.ventana, text = "Cantidad")
        label1.config(bg = "white smoke", font = ("Arial", 12))
        label1.place(x = 75 , y = 235)

        entrada_cantidad = tk.Entry(self.ventana)
        entrada_cantidad.config(fg = "gray", bg = "white", font = ("Arial", 12), width = 10)
        entrada_cantidad.place(x = 75,y = 260)

        # Esta linea crea la etiqueta donde se va a introducir el radio del neumatico

        label1 = tk.Label(self.ventana, text = "Radio")
        label1.config(bg = "white smoke", font = ("Arial", 12))
        label1.place(x = 75 , y = 285)

        entrada_radio = tk.Entry(self.ventana)
        entrada_radio.config(fg = "gray", bg = "white", font = ("Arial", 12), width = 10)
        entrada_radio.place(x = 75,y = 310)

        # Esta linea crea la etiqueta donde se va a introducir el ancho del neumatico

        label1 = tk.Label(self.ventana, text = "Anchura")
        label1.config(bg = "white smoke", font = ("Arial", 12))
        label1.place(x = 75 , y = 335)

        entrada_ancho = tk.Entry(self.ventana)
        entrada_ancho.config(fg = "gray", bg = "white", font = ("Arial", 12), width = 10)
        entrada_ancho.place(x = 75,y = 360)

        imgneumatico = Image.open('C://Users/Usuario/Documents/inventario/software v1/images/imagen.jpeg')
        imagen_redimensionada = imgneumatico.resize((400,410))
        imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)

        labelimagen = tk.Label(self.ventana, image = imagen_tk)
        labelimagen.place(x = 350, y = 70)
        self.ventana.mainloop()