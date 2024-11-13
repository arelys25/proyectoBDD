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
    topUserMenu.config(bg='#011736')
    utl.center_window(topUserMenu,500,500)
    topUserMenu.resizable(width=False, height=False)
    
    imgPerfil = utl.read_Image('./images/AvatarUser.png',(90,90))
    
    imgPerfillbl = Label(topUserMenu,image=imgPerfil,bg='#011736')
    imgPerfillbl.pack(pady=(40,25))
    
    user = 'user'
    usrlbl = Label(topUserMenu,text=f'Usuario: {user}',fg='#C9C0D9',bg='#011736',font=('Georgia',20))
    usrlbl.pack(pady=20)
    
    correo = 'user@example.com'
    correolbl = Label(topUserMenu,text=f'Correo: {correo}',fg='#C9C0D9',bg='#011736',font=('Georgia',20))
    correolbl.pack(pady=20)
    
    tel = '3357834199'
    telefonolbl = Label(topUserMenu,text=f'Teléfono: {tel}',fg='#C9C0D9',bg='#011736',font=('Georgia',20))
    telefonolbl.pack(pady=20)
    
    pswd = '**********'
    passwdlbl = Label(topUserMenu,text=f'Contraseña: {pswd}',fg='#C9C0D9',bg='#011736',font=('Georgia',20))
    passwdlbl.pack(pady=20)
    
    topUserMenu.mainloop()
    
def userBranchesInformation ():
    topUserMenu = Toplevel()
    topUserMenu.title('Perfil Information')
    topUserMenu.iconbitmap('./images/CarIcon.ico')
    topUserMenu.geometry('650x650')
    topUserMenu.config(bg='#011736')
    utl.center_window(topUserMenu,650,650)
    topUserMenu.resizable(width=False, height=False)
    
    saludo = Label(topUserMenu, text='¡Recoge tu vehículo!',fg='#C9C0D9', font=('Georgia',35,BOLD),bg='#011736')
    saludo.pack(pady=45)
    
    gdl = Label(topUserMenu,text='Sucursal Guadalajara:',fg='#C9C0D9',font=('Georgia',17,BOLD),bg='#011736')
    gdl.pack()
    
    guadalajara = Label(topUserMenu,fg='#C9C0D9',text='Calz. Lázaro Cárdenas 3067, Chapalita, 44500 Guadalajara, Jal.\n(+52)3347995834  |  De 4:00 am a 23:59 pm.',wraplength=400,font=('Georgia',14),bg='#011736')
    guadalajara.pack(pady=20)
    guadalajara.bind("<Button-1>", lambda e: open_link("https://maps.app.goo.gl/sarwFaSyrQkzZ8ZQ7"))
    ToolTip(guadalajara,msg='Abrir en el mapa')
    
    zpn = Label(topUserMenu,text='Sucursal Zapopan:',fg='#C9C0D9',font=('Georgia',17,BOLD),bg='#011736')
    zpn.pack(pady=(10,0))
    
    zapopan = Label(topUserMenu,fg='#C9C0D9',text='Av Manuel J. Clouthier 476, Lomas del Seminario, 45020 Zapopan, Jal.\n(+52)3371469235   |  De 4:00 am a 23:59 pm.',wraplength=400,font=('Georgia',14),bg='#011736')
    zapopan.pack(pady=20)
    zapopan.bind("<Button-1>", lambda e: open_link("https://maps.app.goo.gl/X3S9HqnnP3GDLzK56"))
    ToolTip(zapopan,msg='Abrir en el mapa')
    
    
    ton = Label(topUserMenu,text='Sucursal Tonalá:',fg='#C9C0D9',font=('Georgia',17,BOLD),bg='#011736')
    ton.pack(pady=(10,0))
    
    tonala = Label(topUserMenu,fg='#C9C0D9',text='Av Río Nilo 9000, Loma Dorada (Ejidal), 45402 Tonalá, Jal.\n(+52)3315257812   |  De 4:00 am a 23:59 pm.',wraplength=400,font=('Georgia',14),bg='#011736')
    tonala.pack(pady=20)
    tonala.bind("<Button-1>", lambda e: open_link("https://maps.app.goo.gl/guFZ553T8W7yEoAG7"))
    ToolTip(tonala,msg='Abrir en el mapa')
    
    
    topUserMenu.mainloop()
    
def userUsInformation ():
    topUserMenu = Toplevel()
    topUserMenu.title('Perfil Information')
    topUserMenu.iconbitmap('./images/CarIcon.ico')
    topUserMenu.geometry('600x550')
    topUserMenu.config(bg='#011736')
    utl.center_window(topUserMenu,600,550)
    topUserMenu.resizable(width=False, height=False)
    
    saludo = Label(topUserMenu, text='¡Contáctenos!',fg='#C9C0D9', font=('Georgia',40,BOLD),bg='#011736')
    saludo.pack(pady=45)
    
    oficinas = Label(topUserMenu,text='Oficinas Centrales:',fg='#C9C0D9',font=('Georgia',20,BOLD),bg='#011736')
    oficinas.pack()
    
    direccion = Label(topUserMenu,fg='#C9C0D9',text='Nuevo Perif. Ote. 555, Ejido San José, Tateposco, 45425 Tonalá, Jal.',wraplength=400,font=('Georgia',17),bg='#011736')
    direccion.pack(pady=20)
    direccion.bind("<Button-1>", lambda e: open_link("https://maps.app.goo.gl/iFTMRrNjFaDKmgkMA"))
    ToolTip(direccion,msg='Abrir en el mapa')
    
    tel = Label(topUserMenu,text='Teléfono:',fg='#C9C0D9',font=('Georgia',20,BOLD),bg='#011736')
    tel.pack(pady=(10,0))
    
    telefono = Label(topUserMenu,fg='#C9C0D9',text='(+52)3312207298 / (+52)3378645912',wraplength=400,font=('Georgia',17),bg='#011736')
    telefono.pack(pady=20)
    
    cor = Label(topUserMenu,text='Correo electrónico:',fg='#C9C0D9',font=('Georgia',20,BOLD),bg='#011736')
    cor.pack(pady=(10,0))
    
    correo = Label(topUserMenu,text='eMobility@gmail.com',fg='#C9C0D9',wraplength=400,font=('Georgia',17),bg='#011736')
    correo.pack(pady=20)
    
    topUserMenu.mainloop()
  
# funcion para hipervinculos  
def open_link(url):
    webbrowser.open_new(url)