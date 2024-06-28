import cv2
import os
import numpy as np
from matplotlib import pyplot 
from mtcnn.mtcnn import MTCNN
from tkinter import messagebox

def registro_facial(username):
            
    #Vamos a capturar el rostro
    cap = cv2.VideoCapture(0)               #Elegimos la camara con la que vamos a hacer la deteccion
    while(True):
        ret,frame = cap.read()              #Leemos el video
        cv2.imshow('Registro Facial',frame)         #Mostramos el video en pantalla
        if cv2.waitKey(1) == 27:            #Cuando oprimamos "Escape" rompe el video
            break
    usuario_img = username
    cv2.imwrite(usuario_img+".jpg",frame)       #Guardamos la ultima caputra del video como imagen y asignamos el nombre del usuario
    cap.release()                               #Cerramos
    cv2.destroyAllWindows()

    #self.EntryNombre.delete(0, END)   #Limpiamos los text variables
    #----------------- Detectamos el rostro y exportamos los pixeles --------------------------
    
    def reg_rostro(img, lista_resultados):
        data = pyplot.imread(img)
        for i in range(len(lista_resultados)):
            x1,y1,ancho, alto = lista_resultados[i]['box']
            x2,y2 = x1 + ancho, y1 + alto
            pyplot.subplot(1, len(lista_resultados), i+1)
            pyplot.axis('off')
            cara_reg = data[y1:y2, x1:x2]
            cara_reg = cv2.resize(cara_reg,(150,200), interpolation = cv2.INTER_CUBIC) #Guardamos la imagen con un tamaño de 150x200
            cv2.imwrite(usuario_img+".jpg",cara_reg)
            pyplot.imshow(data[y1:y2, x1:x2])
        pyplot.show()

    img = usuario_img+".jpg"
    pixeles = pyplot.imread(img)
    detector = MTCNN()
    caras = detector.detect_faces(pixeles)
    reg_rostro(img, caras)

def login_facial(username):
    #------------------------------Vamos a capturar el rostro-----------------------------------------------------
        cap = cv2.VideoCapture(0)               #Elegimos la camara con la que vamos a hacer la deteccion
        while(True):
            ret,frame = cap.read()              #Leemos el video
            cv2.imshow('Login Facial',frame)         #Mostramos el video en pantalla
            if cv2.waitKey(1) == 27:            #Cuando oprimamos "Escape" rompe el video
                break
        usuario_login = username   #Con esta variable vamos a guardar la foto pero con otro nombre para no sobreescribir
        cv2.imwrite(usuario_login+"LOG.jpg",frame)       #Guardamos la ultima caputra del video como imagen y asignamos el nombre del usuario
        cap.release()                               #Cerramos
        cv2.destroyAllWindows()

        #----------------- Funcion para guardar el rostro --------------------------
        
        def log_rostro(img, lista_resultados):
            data = pyplot.imread(img)
            for i in range(len(lista_resultados)):
                x1,y1,ancho, alto = lista_resultados[i]['box']
                x2,y2 = x1 + ancho, y1 + alto
                pyplot.subplot(1, len(lista_resultados), i+1)
                pyplot.axis('off')
                cara_reg = data[y1:y2, x1:x2]
                cara_reg = cv2.resize(cara_reg,(150,200), interpolation = cv2.INTER_CUBIC) #Guardamos la imagen 150x200
                cv2.imwrite(usuario_login+"LOG.jpg",cara_reg)
                return pyplot.imshow(data[y1:y2, x1:x2])
            pyplot.show()

        #-------------------------- Detectamos el rostro-------------------------------------------------------
        
        img = usuario_login+"LOG.jpg"
        pixeles = pyplot.imread(img)
        detector = MTCNN()
        caras = detector.detect_faces(pixeles)
        log_rostro(img, caras)

        #-------------------------- Funcion para comparar los rostros --------------------------------------------
        def orb_sim(img1,img2):
            orb = cv2.ORB_create()  #Creamos el objeto de comparacion

            kpa, descr_a = orb.detectAndCompute(img1, None)  #Creamos descriptor 1 y extraemos puntos claves
            kpb, descr_b = orb.detectAndCompute(img2, None)  #Creamos descriptor 2 y extraemos puntos claves

            comp = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True) #Creamos comparador de fuerza

            matches = comp.match(descr_a, descr_b)  #Aplicamos el comparador a los descriptores

            regiones_similares = [i for i in matches if i.distance < 70] #Extraemos las regiones similares en base a los puntos claves
            if len(matches) == 0:
                return 0
            return len(regiones_similares)/len(matches)  #Exportamos el porcentaje de similitud
            
        #---------------------------- Importamos las imagenes y llamamos la funcion de comparacion ---------------------------------
        cd = False
        im_archivos = os.listdir()   #Vamos a importar la lista de archivos con la libreria os
        if usuario_login+".jpg" in im_archivos:   #Comparamos los archivos con el que nos interesa
            rostro_reg = cv2.imread(usuario_login+".jpg",0)     #Importamos el rostro del registro
            rostro_log = cv2.imread(usuario_login+"LOG.jpg",0)  #Importamos el rostro del inicio de sesion
            similitud = orb_sim(rostro_reg, rostro_log)

            if similitud >= 0.98:
                messagebox.showinfo(title='Info',message=f'Inicio de sesion exitoso!: {similitud}')
                cd = True
            else:
                messagebox.showwarning(title='Incompatibilidad de rostros',message='Rostro incorrecto, Cerifique su usuario!\n'+f"Compatibilidad con la foto del registro: {similitud}")
                cd=False
        else:
            messagebox.showinfo(title='Info',message='Usuario no encontrado')
        return cd

            

