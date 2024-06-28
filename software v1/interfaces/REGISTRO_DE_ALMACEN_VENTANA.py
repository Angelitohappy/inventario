import tkinter as tk
from util.generic import centrar_ventana

class almacen():
    
    def __init__(self):
        # Creacion y diseño de la self.ventana principal
        self.ventana = tk.Tk()
        self.ventana.title("Registro de almacen")
        self.ventana.geometry("600x400")
        self.ventana.resizable (0,0)
        self.ventana.configure(bg = "white smoke")
        centrar_ventana(self.ventana,600,400)

        # Titulo de la pagina

        label1 = tk.Label(self.ventana, text = "REGISTRO DE ALMACEN")
        label1.config(bg = "white smoke", font = ("Arial", 16, "bold"))
        label1.place(x = 200 , y = 15)

        # Label que funcionará como el fondo donde estarán ubicadas las etiquetas 

        frame1 = tk.Frame(self.ventana)
        frame1.configure(width = 550, height = 315, bg = "PaleGreen3", bd = 5)
        frame1.place(x = 25 , y = 50)

        frame2 = tk.Frame(self.ventana)
        frame2.configure(width = 290, height = 245, bg = "white smoke", bd = 5)
        frame2.place(x = 200 , y = 70)

        # Botón para confirmar el envio de los datos

        boton = tk.Button(self.ventana, text = "Enviar datos")
        boton.config(fg = "white", bg = "green", font = ("Arial", 12))
        boton.place(x = 250, y = 250)

        # Esta linea crea la etiqueta donde se va a introducir el ID del almacen

        label1 = tk.Label(self.ventana, text = "Nro de identificación")
        label1.config(bg = "white smoke", font = ("Arial", 12))
        label1.place(x = 250 , y = 85)

        entrada_marca= tk.Entry(self.ventana, textvariable = "")
        entrada_marca.config(fg = "gray", bg = "white", font = ("Arial", 12), width = 25)
        entrada_marca.place(x = 250,y = 110)


        # Esta linea crea la etiqueta donde se va a introducir la dirección del almacen

        label3 = tk.Label(self.ventana, text = "Localización")
        label3.config(bg = "white smoke", font = ("Arial", 12))
        label3.place(x = 250 , y = 135)

        entrada_id = tk.Entry(self.ventana)
        entrada_id.config(fg = "gray", bg = "white", font = ("Arial", 12))
        entrada_id.place(x = 250 ,y = 160)

        # Esta linea crea la etiqueta donde se va a introducir el numero de telefono del almacen

        label3 = tk.Label(self.ventana, text = "Nro de telefono")
        label3.config(bg = "white smoke", font = ("Arial", 12))
        label3.place(x = 250 , y = 185)

        entrada_id = tk.Entry(self.ventana)
        entrada_id.config(fg = "gray", bg = "white", font = ("Arial", 12))
        entrada_id.place(x = 250 ,y = 210)

        self.ventana.mainloop()