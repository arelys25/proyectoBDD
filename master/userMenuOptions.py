import tkinter as tk
from tkinter.font import BOLD
import util.generic as utl
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tktooltip import ToolTip
import webbrowser

def userPerfilInformation ():
    topUserMenu = Toplevel()
    topUserMenu.title('Perfil Information')
    topUserMenu.iconbitmap('./images/CarIcon.ico')
    topUserMenu.geometry('500x500')
    topUserMenu.config(bg='#68D1CD')
    utl.center_window(topUserMenu,500,500)
    topUserMenu.resizable(width=False, height=False)
    
    imgPerfil = utl.read_Image('./images/AvatarUser.png',(90,90))
    
    imgPerfillbl = Label(topUserMenu,image=imgPerfil,bg='#68D1CD')
    imgPerfillbl.pack(pady=(40,25))
    
    user = 'user'
    usrlbl = Label(topUserMenu,text=f'Usuario: {user}',bg='#68D1CD',font=('Arial',20))
    usrlbl.pack(pady=20)
    
    correo = 'user@example.com'
    correolbl = Label(topUserMenu,text=f'Correo: {correo}',bg='#68D1CD',font=('Arial',20))
    correolbl.pack(pady=20)
    
    tel = '3357834199'
    telefonolbl = Label(topUserMenu,text=f'Teléfono: {tel}',bg='#68D1CD',font=('Arial',20))
    telefonolbl.pack(pady=20)
    
    pswd = '**********'
    passwdlbl = Label(topUserMenu,text=f'Contraseña: {pswd}',bg='#68D1CD',font=('Arial',20))
    passwdlbl.pack(pady=20)
    
    topUserMenu.mainloop()
    
def userBranchesInformation ():
    topUserMenu = Toplevel()
    topUserMenu.title('Perfil Information')
    topUserMenu.iconbitmap('./images/CarIcon.ico')
    topUserMenu.geometry('650x600')
    topUserMenu.config(bg='#68D1CD')
    utl.center_window(topUserMenu,650,600)
    topUserMenu.resizable(width=False, height=False)
    
    saludo = Label(topUserMenu, text='¡Recoge tu vehículo!', font=('Arial',40,BOLD),bg='#68D1CD')
    saludo.pack(pady=45)
    
    gdl = Label(topUserMenu,text='Sucursal Guadalajara:',font=('Arial',20,BOLD),bg='#68D1CD')
    gdl.pack()
    
    guadalajara = Label(topUserMenu,text='Calz. Lázaro Cárdenas 3067, Chapalita, 44500 Guadalajara, Jal.',wraplength=400,font=('Arial',17),bg='#68D1CD')
    guadalajara.pack(pady=20)
    guadalajara.bind("<Button-1>", lambda e: open_link("https://maps.app.goo.gl/sarwFaSyrQkzZ8ZQ7"))
    ToolTip(guadalajara,msg='Abrir en el mapa')
    
    zpn = Label(topUserMenu,text='Sucursal Zapopan:',font=('Arial',20,BOLD),bg='#68D1CD')
    zpn.pack(pady=(10,0))
    
    zapopan = Label(topUserMenu,text='Av Manuel J. Clouthier 476, Lomas del Seminario, 45020 Zapopan, Jal.',wraplength=400,font=('Arial',17),bg='#68D1CD')
    zapopan.pack(pady=20)
    zapopan.bind("<Button-1>", lambda e: open_link("https://maps.app.goo.gl/X3S9HqnnP3GDLzK56"))
    ToolTip(zapopan,msg='Abrir en el mapa')
    
    
    ton = Label(topUserMenu,text='Sucursal Tonalá:',font=('Arial',20,BOLD),bg='#68D1CD')
    ton.pack(pady=(10,0))
    
    tonala = Label(topUserMenu,text='Av Río Nilo 9000, Loma Dorada (Ejidal), 45402 Tonalá, Jal.',wraplength=400,font=('Arial',17),bg='#68D1CD')
    tonala.pack(pady=20)
    tonala.bind("<Button-1>", lambda e: open_link("https://maps.app.goo.gl/guFZ553T8W7yEoAG7"))
    ToolTip(tonala,msg='Abrir en el mapa')
    
    
    topUserMenu.mainloop()
    
def userUsInformation ():
    topUserMenu = Toplevel()
    topUserMenu.title('Perfil Information')
    topUserMenu.iconbitmap('./images/CarIcon.ico')
    topUserMenu.geometry('600x550')
    topUserMenu.config(bg='#68D1CD')
    utl.center_window(topUserMenu,600,550)
    topUserMenu.resizable(width=False, height=False)
    
    saludo = Label(topUserMenu, text='¡Contáctenos!', font=('Arial',40,BOLD),bg='#68D1CD')
    saludo.pack(pady=45)
    
    oficinas = Label(topUserMenu,text='Oficinas Centrales:',font=('Arial',20,BOLD),bg='#68D1CD')
    oficinas.pack()
    
    direccion = Label(topUserMenu,text='Nuevo Perif. Ote. 555, Ejido San José, Tateposco, 45425 Tonalá, Jal.',wraplength=400,font=('Arial',17),bg='#68D1CD')
    direccion.pack(pady=20)
    direccion.bind("<Button-1>", lambda e: open_link("https://maps.app.goo.gl/iFTMRrNjFaDKmgkMA"))
    ToolTip(direccion,msg='Abrir en el mapa')
    
    tel = Label(topUserMenu,text='Teléfono:',font=('Arial',20,BOLD),bg='#68D1CD')
    tel.pack(pady=(10,0))
    
    telefono = Label(topUserMenu,text='(+52)3312207298 / (+52)3378645912',wraplength=400,font=('Arial',17),bg='#68D1CD')
    telefono.pack(pady=20)
    
    cor = Label(topUserMenu,text='Correo electrónico:',font=('Arial',20,BOLD),bg='#68D1CD')
    cor.pack(pady=(10,0))
    
    correo = Label(topUserMenu,text='eMobility@gmail.com',wraplength=400,font=('Arial',17),bg='#68D1CD')
    correo.pack(pady=20)
    
    topUserMenu.mainloop()
  
# funcion para hipervinculos  
def open_link(url):
    webbrowser.open_new(url)