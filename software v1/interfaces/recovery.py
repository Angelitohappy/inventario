import tkinter as tk
from tkinter import messagebox
from tkinter import font
from util.generic import centrar_ventana
from util.generic import Email_Sender
from util.verifies import same_password
from util.verifies import VerifyUser
from util.verifies import verify_clave
from mysql.connector import Error
import interfaces.recovery as rc
import sys
        

class recuperar1():
    
    def regresar(self):
        from interfaces.login import Acceso
        self.pantalla.destroy()
        Acceso()
    
    def exit(self):
        self.pantalla.destroy()
        sys.exit()
        
    def recuperar(self):
        print('hello')
        username = self.EntryU.get()
        try:
            from database.module_bdd import DatabaseManager
            db = DatabaseManager()
            email_exists = db.read_data_email(username)
            print(email_exists)
            if VerifyUser(username):
                if email_exists:
                    print(email_exists[0])
                    messagebox.showinfo(title="Aviso!", message="Se ha enviado un correo con el codigo de verificacion")
                    codex = Email_Sender(email_exists[0])
                    print(codex)
                    self.pantalla.destroy()
                    rc.recuperar2(codex,username)
                else:
                    messagebox.showwarning(title="Error", message="Nombre de usuario")
                
                db.close_connection()
        except Error as e:
            messagebox.showerror(title="Error de conexión", message=f"No se pudo conectar a la base de datos: {e}")
    
    def __init__(self):
        self.pantalla = tk.Tk()
        self.pantalla.overrideredirect(True)
        self.pantalla.geometry("300x300")
        self.pantalla.config(background="#EAF6F6")
        self.pantalla.resizable(False, False) 
        centrar_ventana(self.pantalla, 300, 300)
        
        # Marco superior
        top_frame = tk.Frame(self.pantalla, bg="#004A2F", height=50)
        top_frame.pack(fill="x")
        
        # Configuración de la fuente
        label_font = font.Font(family="Helvetica", size=12)
        
        # Título de la empresa
        company_label = tk.Label(top_frame, text="Ruedas La Mundial", bg="#004A2F", fg="white", font=label_font)
        company_label.pack(side="left", padx=10)
        
        # Botón de regresar
        imgRegresar = tk.PhotoImage(file='C://Users/Usuario/Documents/software v1/images/atras.png')
        self.btnRegresar = tk.Button(top_frame, image=imgRegresar, command=self.regresar, bg="#004A2F", borderwidth=0)
        self.btnRegresar.pack(side="right", padx=5)
        
        # Marco central
        center_frame = tk.Frame(self.pantalla, bg="#EAF6F6")
        center_frame.pack(expand=True)
        
        # Icono de usuario
        user_icon = tk.PhotoImage(file="C://Users/Usuario/Documents/software v1/images/restablecer-la-contrasena (1).png")
        user_icon_label = tk.Label(center_frame, image=user_icon, bg="#EAF6F6")
        user_icon_label.pack(pady=10)
        
        # Campo de usuario
        user_frame = tk.Frame(center_frame, bg="#EAF6F6")
        user_frame.pack(pady=5,anchor="center")
        user_label = tk.Label(user_frame, text="Usuario:", bg="#EAF6F6", font=label_font)
        user_label.pack(side="left")
        self.EntryU = tk.Entry(user_frame, font=label_font, bd=2, relief="groove")
        self.EntryU.pack(side="left")
        
        # Campo de contraseña
        password_frame = tk.Frame(center_frame, bg="#EAF6F6")
        password_frame.pack(pady=5, anchor="center")
        password_label = tk.Label(password_frame, text="Cedula:", bg="#EAF6F6", font=label_font)
        password_label.pack(side="left",padx=1)
        self.EntryC = tk.Entry(password_frame, font=label_font, bd=2, relief="groove", show="*")
        self.EntryC.pack(side="left")
        
        # Botón de aceptar
        self.BtnIniciar = tk.Button(center_frame, text="Aceptar",relief="flat",background="#004A2F",foreground="white",command=self.recuperar, borderwidth=0)
        self.BtnIniciar.pack(side="left",pady=20,padx=10,anchor="center")
        
        self.pantalla.mainloop()
        
    
        
class recuperar2():
    
    def regresar(self):
        from interfaces.recovery import recuperar1
        self.pantalla.destroy()
        recuperar1()
    
    def recuperar(self):
        codigo1 = self.recuperar2_codigo
        usernamex = self.usuariox
        print(codigo1)
        codigo2 = self.cod.get()
        print(codigo2)
        if str(codigo1) == codigo2:
            from interfaces.recovery import recuperar3
            self.pantalla.destroy()
            recuperar3(usernamex)
        else:
            messagebox.showwarning(title="Aviso!", message="El codigo es incorrecto")
    
            
    def __init__(self,codigo,username):
            self.pantalla = tk.Tk()
            self.pantalla.overrideredirect(True)
            self.pantalla.geometry("300x300")
            self.pantalla.config(background="#EAF6F6")
            self.pantalla.resizable(False, False) 
            centrar_ventana(self.pantalla, 300, 300)
            
            self.usuariox = username
            self.recuperar2_codigo = codigo
            print(f'MI CODIGO ES: {self.recuperar2_codigo} ')
            print(f'MI CODIGO ES: {self.usuariox} ')
            # Marco superior
            top_frame = tk.Frame(self.pantalla, bg="#004A2F", height=50)
            top_frame.pack(fill="x")
            
            # Configuración de la fuente
            label_font = font.Font(family="Helvetica", size=12)
            
            # Título de la empresa
            company_label = tk.Label(top_frame, text="Ruedas La Mundial", bg="#004A2F", fg="white", font=label_font)
            company_label.pack(side="left", padx=10)
            
            # Botón de regresar
            imgRegresar = tk.PhotoImage(file='C://Users/Usuario/Documents/software v1/images/atras.png')
            self.btnRegresar = tk.Button(top_frame, image=imgRegresar, command=self.regresar, bg="#004A2F", borderwidth=0)
            self.btnRegresar.pack(side="right", padx=5)
            
            # Marco central
            center_frame = tk.Frame(self.pantalla, bg="#EAF6F6")
            center_frame.pack(expand=True)
            
            # Icono de usuario
            user_icon = tk.PhotoImage(file="C://Users/Usuario/Documents/software v1/images/restablecer-la-contrasena (1).png")
            user_icon_label = tk.Label(center_frame, image=user_icon, bg="#EAF6F6")
            user_icon_label.pack(pady=10)
            
            # Campo de usuario
            user_frame = tk.Frame(center_frame, bg="#EAF6F6")
            user_frame.pack(pady=5,anchor="center")
            user_label = tk.Label(user_frame, text="Codigo de seguridad:", bg="#EAF6F6", font=label_font)
            user_label.pack(side="left")
            self.cod = tk.Entry(user_frame, font=label_font, bd=2, relief="groove")
            self.cod.pack(side="left")
            
            # Botón de aceptar
            self.BtnIniciar = tk.Button(center_frame, text="Aceptar",relief="flat",background="#004A2F",foreground="white",command=self.recuperar, borderwidth=0)
            self.BtnIniciar.pack(side="left",pady=20,padx=10,anchor="center")
            
            self.pantalla.mainloop()    
            
    
            
class recuperar3():
    
    def regresar(self):
        from interfaces.login import Acceso
        self.pantalla.destroy()
        Acceso()
    
    def cambiar(self):
        from interfaces.recovery import recuperar1
        username = self.usuariox
        clave1 = self.clave1.get()
        clave2 = self.clave2.get()
        try:
            if verify_clave(clave1):
                if same_password(clave1,clave2):
                    from database.module_bdd import DatabaseManager
                    db = DatabaseManager()
                    update = db.update_data_clave(clave1=clave1,username=username)
                    messagebox.showinfo(title="Aviso!", message="Se ha actualizado su contraseña correctamente")
                    from interfaces.login import Acceso
                    self.pantalla.destroy()
                    Acceso()
                    db.close_connection()
        except Error as e:
            messagebox.showerror(title="Error de conexión", message=f"No se pudo conectar a la base de datos: {e}")
    
    def __init__(self,username):
        self.pantalla = tk.Tk()
        self.pantalla.overrideredirect(True)
        self.pantalla.geometry("300x300")
        self.pantalla.config(background="#EAF6F6")
        self.pantalla.resizable(False, False) 
        centrar_ventana(self.pantalla, 300, 300)

        self.usuariox = username
        # Marco superior
        top_frame = tk.Frame(self.pantalla, bg="#004A2F", height=50)
        top_frame.pack(fill="x")
        
        # Configuración de la fuente
        label_font = font.Font(family="Helvetica", size=12)
        
        # Título de la empresa
        company_label = tk.Label(top_frame, text="Ruedas La Mundial", bg="#004A2F", fg="white", font=label_font)
        company_label.pack(side="left", padx=10)
        
        # Botón de regresar
        imgRegresar = tk.PhotoImage(file='C://Users/Usuario/Documents/software v1/images/atras.png')
        self.btnRegresar = tk.Button(top_frame, image=imgRegresar, command=self.regresar, bg="#004A2F", borderwidth=0)
        self.btnRegresar.pack(side="right", padx=5)
        
        # Marco central
        center_frame = tk.Frame(self.pantalla, bg="#EAF6F6")
        center_frame.pack(expand=True)
        
        # Icono de usuario
        user_icon = tk.PhotoImage(file="C://Users/Usuario/Documents/software v1/images/restablecer-la-contrasena (1).png")
        user_icon_label = tk.Label(center_frame, image=user_icon, bg="#EAF6F6")
        user_icon_label.pack(pady=10)
        
        # Campo de usuario
        user_frame = tk.Frame(center_frame, bg="#EAF6F6")
        user_frame.pack(pady=5,anchor="center")
        user_label = tk.Label(user_frame, text="Clave:", bg="#EAF6F6", font=label_font)
        user_label.pack(side="left")
        self.e1_str=tk.StringVar()
        self.clave1 = tk.Entry(user_frame,textvariable=self.e1_str,show='*', font=label_font, bd=2, relief="groove")
        self.clave1.pack(side="left")
        
        # Campo de contraseña
        password_frame = tk.Frame(center_frame, bg="#EAF6F6")
        password_frame.pack(pady=5, anchor="center")
        password_label = tk.Label(password_frame, text="confirmar:", bg="#EAF6F6", font=label_font)
        password_label.pack(side="left",padx=1)
        self.e2_str=tk.StringVar()
        self.clave2 = tk.Entry(password_frame,textvariable=self.e2_str, font=label_font, bd=2, relief="groove", show="*")
        self.clave2.pack(side="left")
        
        # Botón de aceptar
        self.BtnIniciar = tk.Button(center_frame, text="Aceptar",relief="flat",background="#004A2F",foreground="white",command=self.cambiar, borderwidth=0)
        self.BtnIniciar.pack(side="left",pady=20,padx=10,anchor="center")
        
        self.c_v1=tk.IntVar(value=0)
        self.c1 = tk.Checkbutton(center_frame,text='Mostrar contraseña', variable=self.c_v1,onvalue=1,offvalue=0,command=self.my_show)
        self.c1.pack(side="right")
        
        self.pantalla.mainloop()
        
    def my_show(self):
        if(self.c_v1.get()==1):
            self.clave1.config(show='')
            self.clave2.config(show='')
        else:
            self.clave1.config(show='*')
            self.clave2.config(show='*')