import tkinter as tk
from tkinter.font import BOLD
import util.generic as utl
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tktooltip import ToolTip


class MasterPanel:
    def __init__(self):
        #MENU PANEL 1
        
        self.menu = tk.Tk()
        self.menu.title("eMOBILITY")
        self.menu.iconbitmap('./images/CarIcon.ico')
        self.menu.geometry('1000x600')
        utl.center_window(self.menu,1000,600)
        self.menu.config(bg='gray')
        self.menu.resizable(width=0, height=0)
        
        logoPage = utl.read_Image('./images/logo.png',(70,70))
        logoPageLbl = Label(self.menu,image=logoPage,border=0)
        logoPageLbl.place(x=0,y=0)
        
        logoCar = utl.read_Image('./images/cars/ChevroletBoltEV.png',(200,170))
        
        hiUser = Label(self.menu,text='¡Hola! ¿Que vehículo deseas rentar hoy?',font=('Arial', 30,BOLD),bg='gray',pady=25)
        hiUser.pack()
        
        # CARS PANEL 2 -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        def carsPanel():
            self.menu.withdraw()
            topCars = Toplevel()
            topCars.title('Electric Cars')
            w,h = topCars.winfo_screenwidth(),topCars.winfo_screenheight() # que la ventana se adapte ala pantalla 
            topCars.geometry("%dx%d+0+0" % (w,h))
            topCars.config(bg='gray')
            utl.center_window(topCars,w,h)
            
            carsLbl = Label(topCars,text='Hola Usuario',font=('Arial', 15))
            carsLbl.pack()
            
            img = utl.read_Image('./images/cars/NissanLeaf.png',(200,170))
            
            def backMenu():
                topCars.withdraw()
                self.menu.deiconify()
            
            imglbl = Button(topCars,image=img,command=backMenu)
            imglbl.pack()
            
            topCars.mainloop()
        
        logoCarlbl = Label(self.menu,text='Coche',font=('Arial', 25),bg='gray')
        logoCarlbl.place(x=150,y=200)    
        LogoCarBtn = Button(self.menu,image=logoCar,command=carsPanel,border=0,bg='black')
        LogoCarBtn.place(x=100,y=250)
        ToolTip(LogoCarBtn,msg='Click para ver los coches')
        
        # SCOOTER PANEL 2 -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        def scooterPanel():
            self.menu.withdraw()
            topScooter = Toplevel()
            topScooter.title('Electric Scooters')
            w,h = topScooter.winfo_screenwidth(),topScooter.winfo_screenheight() # que la ventana se adapte ala pantalla 
            topScooter.geometry("%dx%d+0+0" % (w,h))
            topScooter.config(bg='gray')
            utl.center_window(topScooter,w,h)
            
            scooterLbl = Label(topScooter,text='Hola Usuario',font=('Arial', 15))
            scooterLbl.pack()
            
            img = utl.read_Image('./images/cars/MazdaMX-30.png',(200,170))
            
            def backMenu():
                topScooter.withdraw()
                self.menu.deiconify()
            
            imglbl = Button(topScooter,image=img,command=backMenu)
            imglbl.pack()
            
            topScooter.mainloop()
        
        logoScooter = utl.read_Image('./images/scooter/logoScooter.png',(200,170))
        logoScooterlbl = Label(self.menu,text='Scooter',font=('Arial', 25),bg='gray')
        logoScooterlbl.place(x=450,y=200)    
        LogoScooterBtn = Button(self.menu,image=logoScooter,command=scooterPanel,border=0,bg='black')
        LogoScooterBtn.place(x=400,y=250)
        ToolTip(LogoScooterBtn,msg='Click para ver los coches')
        
        
            
        self.menu.mainloop()
            
        
    
    

        
    
        
        
