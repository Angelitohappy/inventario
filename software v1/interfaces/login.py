import tkinter as tk
from tkinter import font
from tkinter import messagebox
from mysql.connector import Error
from util.generic import centrar_ventana


import sys

class Acceso:
    
    def toRevery(self):
        from interfaces.recovery import recuperar1
        self.pantalla.destroy()
        recuperar1()
    
    def inicio_facial(self):
        from util.face import login_facial
        user = self.EntryU.get()
        holis=login_facial(user)
        if holis :
            from interfaces.VENTANA_PRINCIPAL import admin
            self.pantalla.destroy()
            admin()
        
    def VerifyEntry(self):
        confirm = False
        if len(self.EntryU.get()) > 0 or len(self.EntryC.get()) > 0:
            confirm = True
        return confirm
    
    def exit(self):
        self.pantalla.destroy()
        sys.exit()
    
    def toRegistro(self):
        from interfaces.register import registro
        self.pantalla.destroy()
        registro()
    
    def toInventario(self):
        # Función de ejemplo para el botón de inicio de sesión
        username = self.EntryU.get()
        password = self.EntryC.get()
        # Validación de credenciales
        try:
            from database.module_bdd import DatabaseManager
            db = DatabaseManager()
            user_exists = db.read_data_user(username, password)
            if self.VerifyEntry():
                if user_exists:
                    messagebox.showinfo(title="Acceso", message="Inicio de sesión exitoso.")
                    from interfaces.VENTANA_PRINCIPAL import admin
                    self.pantalla.destroy()
                    admin()
                    
                else:
                    messagebox.showwarning(title="Error", message="Nombre de usuario o contraseña incorrectos.")
                
                db.close_connection()
        except Error as e:
            messagebox.showerror(title="Error de conexión", message=f"No se pudo conectar a la base de datos: {e}")

            
    
    def __init__(self):
        self.pantalla = tk.Tk()
        self.pantalla.overrideredirect(True)
        self.pantalla.geometry("800x450")
        self.pantalla.config(background="#EAF6F6")
        self.pantalla.resizable(False, False) 
        centrar_ventana(self.pantalla, 800, 450)
        
        # Configuración de la fuente
        title_font = font.Font(family="Helvetica", size=24, weight="bold")
        label_font = font.Font(family="Helvetica", size=12)
        
        # Marco superior
        top_frame = tk.Frame(self.pantalla, bg="#004A2F", height=50)
        top_frame.pack(fill="x")
        
        # Título de la empresa
        company_label = tk.Label(top_frame, text="Ruedas La Mundial", bg="#004A2F", fg="white", font=label_font)
        company_label.pack(side="left", padx=10)
        
        # Botón de salir
        imgsSalir = tk.PhotoImage(file='C://Users/Usuario/Documents/Software/icons/cerrar-sesion.png')
        self.salir = tk.Button(top_frame, image=imgsSalir, command=self.exit, bg="#004A2F", borderwidth=0)
        self.salir.pack(side="right", padx=10)
        
        # Marco central
        center_frame = tk.Frame(self.pantalla, bg="#EAF6F6")
        center_frame.pack(expand=True)
        
        # Título de inicio de sesión
        title_label = tk.Label(center_frame, text="Inicio de sesión", bg="#EAF6F6", font=title_font)
        title_label.pack(pady=20)
        
        # Icono de usuario
        user_icon = tk.PhotoImage(file="C://Users/Usuario/Documents/software v1/images/usuario.png")
        user_icon_label = tk.Label(center_frame, image=user_icon, bg="#EAF6F6")
        user_icon_label.pack(pady=10)
        
        # Campo de usuario
        user_frame = tk.Frame(center_frame, bg="#EAF6F6")
        user_frame.pack(pady=5,anchor="center")
        user_label = tk.Label(user_frame, text="Usuario:", bg="#EAF6F6", font=label_font)
        user_label.pack(side="left",padx=13)
        self.EntryU = tk.Entry(user_frame, font=label_font, bd=2, relief="groove")
        self.EntryU.pack(side="left")
        
        
        # Campo de contraseña
        password_frame = tk.Frame(center_frame, bg="#EAF6F6")
        password_frame.pack(pady=5, anchor="center")
        password_label = tk.Label(password_frame, text="Contraseña:", bg="#EAF6F6", font=label_font)
        password_label.pack(side="left")
        self.e1_string = tk.StringVar()
        self.EntryC = tk.Entry(password_frame, font=label_font,textvariable=self.e1_string, bd=2, relief="groove", show="*")
        self.EntryC.pack(side="left")
        self.c_v1=tk.IntVar(value=0)
        
        
        
        self.c1 = tk.Checkbutton(center_frame,text='Mostrar contraseña', variable=self.c_v1,onvalue=1,offvalue=0,command=self.my_show)
        self.c1.pack(side="bottom")
        
        
        # Botón de rostro
        imgBtnface = tk.PhotoImage(file='C://Users/Usuario/Documents/software v1/images/reconocimiento-facial.png')
        self.BtnRostro = tk.Button(center_frame, image=imgBtnface, bg="#004A2F", borderwidth=0,command=self.inicio_facial)
        self.BtnRostro.pack(side="right",pady=20)
        
        # Botón de aceptar
        self.BtnIniciar = tk.Button(center_frame, text="Aceptar",relief="flat",background="#004A2F",foreground="white",command=self.toInventario, borderwidth=0)
        self.BtnIniciar.pack(side="left",pady=20,padx=10,anchor="center")
        
        # Botón de registrio
        self.BtnRegistrar = tk.Button(center_frame, text="Registar",relief="flat",background="#004A2F",foreground="white",command=self.toRegistro, borderwidth=0)
        self.BtnRegistrar.pack(side="left",pady=20,anchor="center")
        
        # Botón de registrio
        self.BtnRecuperar = tk.Button(center_frame, text="Recuperar",relief="flat",background="#004A2F",foreground="white",command=self.toRevery, borderwidth=0)
        self.BtnRecuperar.pack(side="left",pady=20,padx=10,anchor="center")
        
        self.pantalla.mainloop()
        
    def my_show(self):
        if(self.c_v1.get()==1):
            self.EntryC.config(show='')
        else:
            self.EntryC.config(show='*')

if __name__ == "__main__":
    Acceso()