#!/usr/bin/python
#-*- coding: latin-1 -*-

from tkinter import *

import customtkinter
from customtkinter import *
from tkinter import messagebox as msg
import os
import subprocess
import re
from playsound import playsound

#####################################################################
###################### DIRECTORIOS DE IMAGENES ######################
#####################################################################

directorio_principal = os.path.dirname(__file__)
carpeta_sonido = os.path.join(directorio_principal, "sonido")
carpeta_imagenes = os.path.join(directorio_principal, "img_wifi")

#####################################################################
####################### CONFIGURACION VENTANA #######################
#####################################################################
negro = "#010101"
ventana = CTk()
###################### LADO LATERAL HIZQUIERDO #####################
miFrame = CTkFrame(ventana, width=30, height=450, fg_color= negro)
miFrame.grid(column=0, row = 0, sticky='nsew',padx=10, pady =40)

################################ CENTRO #############################
miFrame1 = CTkFrame(ventana, width=400, height=450)
#miFrame1.grid(column=1, row = 0, sticky='nsew',padx=10, pady =40)

miFrame2 = CTkFrame(ventana, width=400, height=450)
#miFrame2.grid(column=1, row = 0, sticky='nsew',padx=10, pady =40)

miFrame3 = CTkFrame(ventana, width=400, height=450)

ventana.columnconfigure(0, weight=1)
ventana.rowconfigure(0, weight=1)
ventana.resizable(False,False)
ventana.iconbitmap(os.path.join(carpeta_imagenes, "Bird.ico"))
ventana.title("Gohse7-Sys7em WIFI-PASSWORD")

#####################################################################
########################## CARGAR IMAGENES ##########################
#####################################################################
img_logo = PhotoImage(file= os.path.join(carpeta_imagenes, "logo_goset5.png"))
img_wifi_3 = PhotoImage(file= os.path.join(carpeta_imagenes, "wifi_3.png"))
img_wifi_1 = PhotoImage(file= os.path.join(carpeta_imagenes, "wifi_1.png"))
img_wifi2_3 = PhotoImage(file= os.path.join(carpeta_imagenes, "wifi2_3.png"))
img_wifi2_2 = PhotoImage(file= os.path.join(carpeta_imagenes, "wifi2_2.png"))
img_wifi22 = PhotoImage(file= os.path.join(carpeta_imagenes, "wifi22.png"))
img_wifi_clave2 = PhotoImage(file= os.path.join(carpeta_imagenes, "wifi-clave2.png"))
img_wifi_clave21 = PhotoImage(file= os.path.join(carpeta_imagenes, "wifi-clave21.png"))
img_wifi_copia = PhotoImage(file= os.path.join(carpeta_imagenes, "wifi_copia.png"))
#####################################################################

lblusuario = CTkLabel(miFrame, text="", fg_color="transparent")
lblusuario.grid(row=1, column=0)
def usuario():
    nombre = os.getenv("UserName")
    lblusuario.configure(text=nombre)
usuario()
#############################################################################
################### Elementos del centro del programa #######################
#############################################################################

def logo_centro(): #Cargar logo principal de inicio
    miFrame3.destroy()
    miFrame2.destroy()
    miFrame1 = CTkFrame(ventana, width=400, height=450)
    miFrame1.grid(column=1, row=0, sticky='nsew', padx=10, pady=40)
    lblimagencentro = CTkLabel(miFrame1, text=" ", image=img_logo, fg_color="transparent",  width=400, height=250)
    lblimagencentro.grid(row=0, column=1)
logo_centro()
global texto
global txtbuscar
def cuadro_informacion():

    miFrame3.destroy()
    miFrame1.destroy()
    miFrame2 = CTkFrame(ventana, width=400, height=450)
    miFrame2.grid(column=1, row=0, sticky='nsew', padx=10, pady=40)
    global texto
    texto = CTkTextbox(miFrame2, font=("Consolas", 11), width=400, height=250)
    texto.grid(row=0, column=1)
    texto.configure(state="disabled")

    #logo()
def cuadro_clave_perfil():
    global txtbuscar
    miFrame2.destroy()
    miFrame1.destroy
    miFrame3 = CTkFrame(ventana, width=400, height=250)
    miFrame3.grid(column=1, row = 0, sticky='nsew',padx=10, pady =40)

    txtbuscar = CTkEntry(miFrame3, font=("Consolas", 11), width=150)
    #txtbuscar.grid(row=2, column=3)
    txtbuscar.place(x=150, y=70)
    txtbuscar.insert(0, "Nombre del Perfil")

    lblimagencentro = CTkLabel(miFrame3, text=" ", image=img_wifi_copia, fg_color="transparent", width=100, height=150)
    #lblimagencentro.grid(row=0, column=1)
    lblimagencentro.place(x=30, y=30)

    btnbuscar = CTkButton(miFrame3, fg_color="transparent", text=" ", image=img_wifi22, command=clave_perfil, border_width=0,
                             hover_color='lime', width=15, height=15)
    #btnbuscar.grid(row=3, column=3)
    btnbuscar.place(x=170, y=100)

    lbldetalle = CTkLabel(miFrame3, text="")
    lbldetalle.place(x=30, y=200)
    lbldetalle.configure(text="Esbriba el nombre correcto de la red wifi sin espacios...")

def logo():
    texto.configure(state="normal")
    texto.configure(font = ("Consolas", 8))
    a10 = " "
    a1 = "      @@@@@@@@               @@                                                    "
    a2 = "   @@                        @@                            @@                       "
    a3 = "  @@              @@@@@@    @@@@@@@@    @@@@@@    @@@@  @@@@@@@ @@@@@@@@@  @@@@@@@@@"
    a4 = "   @@    @@@@@@  @@    @@    @@    @@    @@      @@    @@  @@          @@         @@"
    a5 = "   II        II  II    II    II    II    IIIIII  IIIIIIII  II         II         II"
    a6 = "   IIII      II  II    II    II    II        II  II        II        II         II  "
    a7 = "       IIIIIIII  IIIIIIII    II    II    IIIIII    IIIIII  IIIIII    II        II  "
    a8 = "                                                                    II        II  "
    a9 = "                                                                    II        II  "
    texto.insert("0.0", "\n" + a9)
    texto.insert("0.0", "\n" + a8)
    texto.insert("0.0", "\n" + a7)
    texto.insert("0.0", "\n" + a6)
    texto.insert("0.0", "\n" + a5)
    texto.insert("0.0", "\n" + a4)
    texto.insert("0.0", "\n" + a3)
    texto.insert("0.0", "\n" + a2)
    texto.insert("0.0", "\n" + a1)
    texto.insert("0.0", "\n\n\n\n\n\n\n\n\n" + a10)
    texto.configure(state="disabled")

#####################################################################
######################## FUNCIONES-CALCULOS #########################
#####################################################################
def info():

    dr1 = txtbuscar.get()
    if os.path.exists(dr1) == True:  # Si existe la carpeta pasa de largo
        try:
            texto.configure(state="normal")
            texto.configure(font=("Consolas", 11))
            texto.delete("0.0", 'end')
            for archivo in os.listdir(dr1):
                # if archivo.endswith(".docx") or archivo.endswith(".doc"):
                d = os.path.join(dr1, archivo)
                texto.insert("0.0", "\n" + d)
            texto.configure(state="disabled")
            # print(d)
        except IOError:
            pass
def perfileswifi():
    cuadro_informacion()

    texto.configure(state="normal")
    texto.configure(font=("Consolas", 11))
    texto.delete("0.0", 'end')

    command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True).stdout.decode(
        'latin-1 -*-')

    texto.insert("0.0", "\n" + command_output)
    texto.configure(state="disabled")
def clave_perfil():
    global txtbuscar
    name = txtbuscar.get()
    wifi_profile = {}
    wifi_profile["ssid"] = name

    comando = f"netsh wlan show profile {name} key=clear"
    profile_info_pass = subprocess.run(comando, capture_output=True).stdout.decode('latin-1 -*-')
    # print("clave", profile_info_pass)
    password = (re.search("Contenido de la clave  :(.*)\r", profile_info_pass))
    if password == None:
        wifi_profile["clave"] = None
    else:
        wifi_profile["clave"] = password[1]
    msg.showinfo("Clave Wifi", wifi_profile)
def perfiles_detallado():
    cuadro_informacion()
    command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True).stdout.decode(
        'latin-1 -*-')
    profile_names = (re.findall("Perfil de todos los usuarios     :(.*)\r", command_output))

    texto.configure(state="normal")
    texto.configure(font=("Consolas", 11))
    texto.delete("0.0", 'end')

    for name in profile_names:

        wifi_profile = {}
        wifi_profile["ssid"] = name

        comando = f"netsh wlan show profile {name} key=clear"
        profile_info_pass = subprocess.run(comando, capture_output=True).stdout.decode('latin-1 -*-')

        texto.insert("0.0", "\n" + profile_info_pass)
    texto.configure(state="disabled")

def informacion():
    msg.showinfo("Listo","[*] Encriptacion / Desencriptacion completa...")


#############################################################################
############ [NOMBRE DE BOTONES] Etiqueta que muestra el nombre  ############
#############################################################################
lblinfo = CTkLabel(miFrame, text=" ")
lblinfo.grid(row=0, column=0)

#############################################################################
############ Eventos de los Boton del lado izquierdo ########################
#############################################################################
def info_btninfo1(event):
    lblinfo.configure(text="Perfiles wifi")
    funsion_btnclaveperfil()
    funsion_btninfo2()
    funsion_perfilesdetallado()
def info_btnclaveperfil(event):
    lblinfo.configure(text="Claves x Perfil")
    funsion_btninfo1()
    funsion_btnclaveperfil2()
    funsion_perfilesdetallado()

def info_btnperfilcompleto(event):
    lblinfo.configure(text="Perfil detallado")
    funsion_perfilesdetallado2()
    funsion_btnclaveperfil()
    funsion_btninfo1()
def info_fuera(event):
    lblinfo.configure(text=" ")
    funsion_btninfo1()
    funsion_btnclaveperfil()
    funsion_perfilesdetallado()
    logo_centro()

miFrame.bind("<Motion>", info_fuera)

#############################################################################
############# [1 CREAR BOTONES] del lado izquierdo con funsiones ############
#############################################################################
#global btninfo
def funsion_btninfo1():
    global btninfo
    btninfo = CTkButton(miFrame, fg_color="#010101", text=" ", image=img_wifi_3, border_width=0,
                        hover_color='#010101', width=15, height=15)
    btninfo.grid(row=3, column=0)
    btninfo.bind("<Motion>", info_btninfo1)

def funsion_btnclaveperfil():
    global btnclaveperfil
    btnclaveperfil = CTkButton(miFrame, fg_color="#010101", text=" ", image=img_wifi2_3, border_width=0,
                        hover_color='#010101', width=15, height=15)
    btnclaveperfil.grid(row=4, column=0)
    btnclaveperfil.bind("<Motion>", info_btnclaveperfil)

def funsion_perfilesdetallado():
    global perfilesdetallado
    btnperfilcompleto = CTkButton(miFrame, fg_color="transparent", text=" ", image=img_wifi_clave2, border_width=0,
                               hover_color='#010101', width=15, height=15)
    btnperfilcompleto.grid(row=5, column=0)
    btnperfilcompleto.bind("<Motion>", info_btnperfilcompleto)
#############################################################################
#################### [CARGAR BOTONES] del lado izquierdo ####################
#############################################################################
funsion_btninfo1()
funsion_btnclaveperfil()
funsion_perfilesdetallado()

#############################################################################
############ [2 CREAR BOTONES] del lado izquierdo para <Eventos> ############
#############################################################################
global btninfo2
global btnclaveperfil2
def funsion_btninfo2():
    global btninfo2
    btninfo2 = CTkButton(miFrame, fg_color="#010101", text=" ", width=15, height=15, image=img_wifi_1, command=perfileswifi, border_width=0, hover_color='#010101')
    btninfo2.grid(row=3, column=0)

def funsion_btnclaveperfil2():
    global btnclaveperfil2
    btnclaveperfil2 = CTkButton(miFrame, fg_color="#010101",width=15, height=15, text=" ", image=img_wifi2_2, command=cuadro_clave_perfil, border_width=0,
                        hover_color='#010101')
    btnclaveperfil2.grid(row=4, column=0)

def funsion_perfilesdetallado2():
    global perfilesdetallado2
    btnperfilcompleto2 = CTkButton(miFrame, fg_color="#010101", text=" ", image=img_wifi_clave21, command=perfiles_detallado, border_width=0,
                               hover_color='#010101', width=15, height=15)
    btnperfilcompleto2.grid(row=5, column=0)



#ventana.call('wm', 'iconphoto', ventana._w, logo)
ventana.mainloop()
