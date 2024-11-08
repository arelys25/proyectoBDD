import tkinter as tk
from tkinter.font import BOLD
import util.generic as utl
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tktooltip import ToolTip

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
    
    topUserMenu.mainloop()
    
def userUsInformation ():
    topUserMenu = Toplevel()
    topUserMenu.title('Perfil Information')
    topUserMenu.iconbitmap('./images/CarIcon.ico')
    topUserMenu.geometry('650x600')
    topUserMenu.config(bg='#68D1CD')
    utl.center_window(topUserMenu,650,600)
    topUserMenu.resizable(width=False, height=False)
    
    topUserMenu.mainloop()