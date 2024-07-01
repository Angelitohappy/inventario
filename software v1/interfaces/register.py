import tkinter as tk
import sys
from tkinter import font
from tkinter import PhotoImage
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from mysql.connector import Error
from util.generic import centrar_ventana
from util.verifies import VerifyNombre
from util.verifies import VerifyApellido
from util.verifies import same_password
from util.verifies import verify_clave
from util.verifies import Verify_cedula
from util.verifies import Verify_telefono
from util.face import registro_facial
from string import punctuation as p
import email.utils
from util.verifies import validar_email


class registro():
    
    def email_v(self):
        cd = False
        email = self.email
        if validar_email(email)==True:
            cd = True
        else:
            messagebox.showwarning(title="Aviso!", message="Por favor, ingrese una sintaxis de correo valida ejemplo:\n user@gmail.com")
            cd = False
        return cd
    
    def minimize_window(self):
        self.pantalla1.iconify()
        
    def take_photo(self):
        User = self.EntryAlias.get()
        registro_facial(username=User)
    
    def VerifyEntry(self):
        confirm = False
        if len(self.EntryAlias.get()) > 0 or len(self.EntryNombre.get()) > 0 or len(self.EntryCorreo.get()) > 0 or len(self.EntryCedula.get()) > 0 or len(self.EntryTelefono.get()) > 0 or len(self.txtDireccion.get('1.0','end')) or len(self.EntryPassword.get()) > 0 or len(self.EntryPasswordr.get()) > 0 or len(self.EntryApellido.get()) > 0:
            confirm = True
        else:
            messagebox.showwarning(title="Aviso!", message="Por favor, ingrese todos los campos requeridos")

        return confirm

    def confirm(self):
        username=self.EntryAlias.get()
        name=self.EntryNombre.get()
        lastname=self.EntryApellido.get()
        fullname=name+' '+lastname
        print(fullname)
        c1=self.cboCedula.get()
        c2=self.EntryCedula.get()
        id=""+c1+""+c2+""
        password1=self.EntryPassword.get()
        password2=self.EntryPasswordr.get()
        t1=self.cboTelefono.get()
        t2=self.EntryTelefono.get()
        phone=""+t1+""+t2+""
        self.email=self.EntryCorreo.get()
        address=self.txtDireccion.get('1.0','end')
        face = ''
        entries = self.VerifyEntry()
        if entries:
            if verify_clave(password1):
                if same_password(password1=password1,password2=password2):
                    if self.email_v():
                        try:
                            from database.module_bdd import DatabaseManager
                            db = DatabaseManager()
                            db.insert_data_usuario(id=id,name=fullname,user=username,password=password1,phone=phone,email=self.email,address=address,face=face)
                            db.close_connection()
                            messagebox.showinfo(title="Aviso!", message="Se ha registrado exitosamente!")
                            from interfaces.login import Acceso
                            self.pantalla1.destroy()
                            Acceso()
                        except Error as e:
                            messagebox.showerror(title="Error de conexión", message=f"No se pudo conectar a la base de datos: {e}")
        
    def regresar(self):
        from interfaces.login import Acceso
        self.pantalla1.destroy()
        Acceso()
        
    def exit(self):
        self.pantalla1.destroy()
        sys.exit()
    
    def validar(self):
        texto = self.EntryNombre.get()
        VerifyNombre(texto=texto)
    
    def validar2(self):
        numero = self.EntryCedula.get()
        Verify_cedula(numero=numero)
    
    def validar3(self):
        num = self.EntryTelefono.get()
        Verify_telefono(num=num)

    def __init__(self):
        self.pantalla1 = tk.Tk()
        self.pantalla1.title("Ruedas La Mundial")
        self.pantalla1.geometry("800x450")
        self.pantalla1.config(bg="#EAF6F6")
        self.pantalla1.overrideredirect(True)
        self.pantalla1.resizable(False, False) 
        centrar_ventana(self.pantalla1, 800, 450)

        # Colores
        bg_color = "#EAF6F6" 
        top_panel_color = "palegreen4"
        input_panel_color = "#2F6E4E"
        
        # Fuente
        title_font = font.Font(family="Helvetica", size=16, weight="bold")
        button_font = font.Font(family="Helvetica", size=12)

        # Panel superior
        top_frame = tk.Frame(self.pantalla1, bg=top_panel_color, height=50)
        top_frame.pack(fill="x")
        
        self.frame = tk.Frame(self.pantalla1, bg=input_panel_color, width=400, height=420)
        self.frame.place(x=0,y=30)
        
        label_font = font.Font(family="Helvetica", size=12)
        
        company_label = tk.Label(top_frame, text="Ruedas La Mundial", bg=top_panel_color, fg="white", font=title_font)
        company_label.pack(side="left", padx=10)
        
        # Botón de salir
        imgRegresar = tk.PhotoImage(file='C://Users/Usuario/Documents/inventario/software v1/images/atras.png')
        self.btnRegresar = tk.Button(top_frame, image=imgRegresar, command=self.regresar, bg=top_panel_color, borderwidth=0)
        self.btnRegresar.pack(side="right", padx=5)
        
        #Alias
        self.lblAlias=Label(self.pantalla1,text="Alias:",foreground="white",bg="#2F6E4E",font=("Cascadia Mono",11,),justify='left')
        self.lblAlias.place(x=10,y=32)
        self.EntryAlias = Entry(self.pantalla1,width=40,background="white",relief=tk.FLAT, font=("Cascadia Mono",9,"bold"),justify="left")
        self.EntryAlias.place(x=110,y=36)
        
        #Apellido
        self.lblApellido=Label(self.pantalla1,text="Apellido:",foreground="white",bg="#2F6E4E",font=("Cascadia Mono",11,),justify='left')
        self.lblApellido.place(x=10,y=102)
        self.apellido = StringVar()
        self.EntryApellido = Entry(self.pantalla1,width=40,background="white",relief=tk.FLAT, font=("Cascadia Mono",9,"bold"),justify="left",textvariable=self.apellido)
        self.EntryApellido.config(validate='key',validatecommand=(self.EntryApellido.register(VerifyApellido), '%S'))
        self.EntryApellido.place(x=110,y=104)
        
        #Nombre
        self.lblNombre=Label(self.pantalla1,text="Nombre:",foreground="white",bg="#2F6E4E",font=("Cascadia Mono",11,),justify='left')
        self.lblNombre.place(x=10,y=66)
        self.nombre = StringVar()
        self.EntryNombre = Entry(self.pantalla1,width=40,background="white",relief=tk.FLAT, font=("Cascadia Mono",9,"bold"),justify="left",textvariable=self.nombre)
        self.EntryNombre.config(validate='key',validatecommand=(self.EntryNombre.register(VerifyNombre), '%S'))
        self.EntryNombre.place(x=110,y=68)
        
        #Cedula
        self.lblCedula=Label(self.pantalla1,text="Cedula:",foreground="white",bg="#2F6E4E",font=("Cascadia Mono",11,),justify='left')
        self.lblCedula.place(x=10,y=138)
        self.cboCedula = ttk.Combobox(self.pantalla1,width=2, height=5 ,values=['V-','E-'], state="readonly")
        self.cboCedula.current(0)
        self.cboCedula.place(x=110,y=139)
        self.numero = StringVar()
        self.EntryCedula=Entry(self.pantalla1,width=35,foreground="black",bg="WHITE",relief=tk.FLAT,font=("Cascadia Mono",9,"bold"),justify='left',textvariable=self.numero)
        self.EntryCedula.config(validate='key',validatecommand=(self.EntryCedula.register(Verify_cedula), '%S'))
        self.EntryCedula.place(x=145,y=140)
        
        #Telefono
        self.lblTelefono=Label(self.pantalla1,text="Telefono:",foreground="white",bg="#2F6E4E",font=("Cascadia Mono",11,),justify='left')
        self.lblTelefono.place(x=10,y=178)
        self.cboTelefono = ttk.Combobox(self.pantalla1, width=4, height=5 ,values=["+58", "+57", "+54","+55","+51"], state="readonly")
        self.cboTelefono.current(0)
        self.num = StringVar()
        self.cboTelefono.place(x=107,y=179)
        self.EntryTelefono = Entry(self.pantalla1,width=34,background="white",relief=tk.FLAT,font=("Cascadia Mono",9,"bold"),justify="left",textvariable=self.num)
        self.EntryTelefono.config(validate='key',validatecommand=(self.EntryCedula.register(Verify_cedula), '%S'))
        self.EntryTelefono.place(x=152,y=180)

        #Correo
        self.lblCorreo=Label(self.pantalla1,text="Correo:",foreground="white",bg="#2F6E4E",font=("Cascadia Mono",11,),justify='left')
        self.lblCorreo.place(x=10,y=218)
        self.EntryCorreo = Entry(self.pantalla1,width=40,background="white",relief=tk.FLAT,font=("Cascadia Mono",9,"bold"),justify="left") 
        self.EntryCorreo.place(x=110,y=220)

        #Password
        self.lblPassword=Label(self.pantalla1,text="Clave:",foreground="white",bg="#2F6E4E",font=("Cascadia Mono",11,),justify='left')
        self.lblPassword.place(x=10,y=258)
        self.e1_str=StringVar()
        self.EntryPassword = Entry(self.pantalla1,textvariable=self.e1_str,width=40,background="white",show='*',relief=tk.FLAT,font=("Cascadia Mono",9,"bold"),justify="left") 
        self.EntryPassword.place(x=110,y=260)
        
        #Passwordr
        self.lblPasswordr=Label(self.pantalla1,text="Confirmar:",foreground="white",bg="#2F6E4E",font=("Cascadia Mono",11,),justify='left')
        self.lblPasswordr.place(x=10,y=298)
        self.e2_str=StringVar()
        self.EntryPasswordr = Entry(self.pantalla1,textvariable=self.e2_str,width=40,background="white",show='*',relief=tk.FLAT,font=("Cascadia Mono",9,"bold"),justify="left") #Creamos un text variable para que el usuario ingrese la contra
        self.EntryPasswordr.place(x=110,y=300)

        #Direccion
        self.lblDireccion=Label(self.pantalla1,text="Direccion:",foreground="white",bg="#2F6E4E",font=("Cascadia Mono",11,),justify='left')
        self.lblDireccion.place(x=10,y=358)
        self.txtDireccion=Text(self.pantalla1,width = 40,height=5,background="white",foreground="black",font=("Cascadia Mono",9,"bold"))
        self.txtDireccion.place(x=110,y=360)

        # Panel de foto
        photo_frame = tk.Frame(self.pantalla1, bg="#EAF6F6", width=150, height=150)
        photo_frame.place(x=530, y=100)

        take_photo_button = tk.Button(self.pantalla1, text="Tomar foto", bg=top_panel_color, fg="white",relief="groove", font=button_font, command=self.take_photo)
        take_photo_button.place(x=555, y=270)

        camera_icon = PhotoImage(file='C://Users/Usuario/Documents/inventario/software v1/images/imagenes-de-usuario.png')  # Ruta al icono de la cámara
        marco = Label(photo_frame, image=camera_icon, bg=bg_color)
        marco.pack()

        # Botón de confirmar
        self.confirm_button = tk.Button(self.pantalla1, text="Confirmar", bg=top_panel_color, fg="white", relief="groove",font=button_font, command=self.confirm)
        self.confirm_button.place(x=700, y=400)
        
        self.c_v1=IntVar(value=0)
        self.c1 = tk.Checkbutton(self.pantalla1,text='Mostrar contraseña',bg=input_panel_color, variable=self.c_v1,onvalue=1,offvalue=0,command=self.my_show)
        self.c1.place(x=110,y=330)
        
        
        
        self.pantalla1.mainloop()
    def my_show(self):
        if(self.c_v1.get()==1):
            self.EntryPassword.config(show='')
            self.EntryPasswordr.config(show='')
        else:
            self.EntryPassword.config(show='*')
            self.EntryPasswordr.config(show='*')