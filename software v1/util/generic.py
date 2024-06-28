import os
import ssl
import smtplib
from email.message import EmailMessage
import random


def Email_Sender(email):
    codigo=[]
    codigo.append(random.randrange(1,10000))
    Sender = 'inventarioproyecto644@gmail.com'
    password = 'ljfv ueme bxsm nkno'
    Reciver = email
    
    subject = 'Recuperacion de clave'
    
    body = f'El codigo es: {codigo[0]}'
    
    em = EmailMessage()
    em['From'] = Sender
    em['To'] = Reciver
    em['Subject'] = subject
    em.set_content(body)
    
    context = ssl.create_default_context()
    
    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(Sender,password)
        smtp.sendmail(Sender, Reciver, em.as_string())
    return codigo[0]
    
def centrar_ventana(ventana, aplicacion_ancho, aplicacion_largo):
    pantall_ancho = ventana.winfo_screenwidth()
    pantall_largo = ventana.winfo_screenheight()
    x = int((pantall_ancho/2) - (aplicacion_ancho/2))
    y = int((pantall_largo/2) - (aplicacion_largo/2))
    return ventana.geometry(f"{aplicacion_ancho}x{aplicacion_largo}+{x}+{y}")