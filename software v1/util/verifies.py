from string import punctuation as p
from tkinter import messagebox
import re

def VerifyNombre(texto):
    if texto.isalpha():
        while not any([True if i in p else False for i in texto]):
                return True
    else:
        return False

def VerifyApellido(texto):
    if texto.isalpha():
        while not any([True if i in p else False for i in texto]):
                return True
    else:
        return False
    
def Verify_cedula(numero):
    if numero.isdigit():
        while not any([True if i in p else False for i in numero]):
                return True
    else:
        return False

def Verify_telefono(num):
    if num.isdigit():
        while not any([True if i in p else False for i in num]):
                return True
    else:
        return False

def verify_clave(cts):
    if len(cts) < 7 or len(cts) > 18:
        messagebox.showwarning(title="Aviso!", message="La contraseña debe de tener entre 8 y 16 carácteres")
    elif not any([c.isdigit() for c in cts]):
        messagebox.showwarning(title="Aviso!", message="La contraseña ha de contener algun digito")
    elif not any([c.islower() for c in cts]):
        messagebox.showwarning(title="Aviso!", message="La contraseña ha de contener alguna minúscula")
    elif not any([c.isupper() for c in cts]):
        messagebox.showwarning(title="Aviso!", message="La contraseña ha de contener alguna mayúscula")
    elif not any([True if c in p else False for c in cts]):
        messagebox.showwarning(title="Aviso!", message="La contraseña ha de contener algun carácter especial")
    else:
        return True
    return False

def same_password(password1,password2):
        if password1 == password2:
            return True
        else:
            messagebox.showwarning(title="Atencion", message="Las contraseñas no coinciden")
            return False
        
def validate_entry(text):
    return text.isdecimal()

def VerifyUser(username):
            confirm = False
            if len(username) > 0:
                confirm = True
            return confirm

def validar_email(email):
    hola = bool(re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',email))    
    return hola
