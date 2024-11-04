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
        global logoPage
        
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
            topCars.iconbitmap('./images/CarIcon.ico')
            w,h = topCars.winfo_screenwidth(),topCars.winfo_screenheight() # que la ventana se adapte ala pantalla 
            topCars.geometry("%dx%d+0+0" % (w,h))
            topCars.config(bg='gray')
            utl.center_window(topCars,w,h)
            
            # Scrollbar
            mainFrameCars = Frame(topCars)
            mainFrameCars.pack(fill=BOTH,expand=True)
            my_canvasCar = Canvas(mainFrameCars,bg='blue')
            my_canvasCar.pack(side=LEFT,fill= BOTH,expand=True)
            my_scrollbarCar = ttk.Scrollbar(mainFrameCars,orient=VERTICAL,command=my_canvasCar.yview)
            my_scrollbarCar.pack(side=RIGHT,fill=Y)
            my_canvasCar.config(yscrollcommand=my_scrollbarCar.set)
            #my_canvasCar.bind('<Configure>', lambda e: my_canvasCar.configure(scrollregion=my_canvasCar.bbox('all')))
            secondFrame = Frame(my_canvasCar,bg='GRAY')
            secondFrame.config(width=w,height=h)
            my_canvasCar.create_window((0,0),window=secondFrame,anchor='nw')
            
            # crear 50 botones
            #for thing in range(50):
            #    Button(secondFrame,text=f'Venta {thing}!').pack(pady=10,padx=10)
            
            hiUserlbl = Label(secondFrame,text='Hola Usuario',font=('Arial', 35),bg='GRAY')
            hiUserlbl.place(x=800,y=60)
            
            logoMenu = utl.read_Image('./images/logo.png',(70,70))
            
            def backMenu():
                topCars.withdraw()
                self.menu.deiconify()
            
            logoMenubtn = Button(mainFrameCars,image=logoMenu,command=backMenu,border=0)
            logoMenubtn.place(x=0,y=0)
            
            car1 = utl.read_Image('./images/cars/ChevroletBoltEV.png',(200,170))
            car1lbl = Label(secondFrame,image=car1,border=0)
            car1lbl.place(x=200,y=200)
            
            car2 = utl.read_Image('./images/cars/KiaSoulEV.png',(200,170))
            car2lbl = Label(secondFrame,image=car2,border=0)
            car2lbl.place(x=200,y=450)
            
            car3 = utl.read_Image('./images/cars/MazdaMX-30.png',(200,170))
            car3lbl = Label(secondFrame,image=car3,border=0)
            car3lbl.place(x=200,y=700)
            
            car4 = utl.read_Image('./images/cars/NissanLeaf.png',(200,170))
            car4lbl = Label(secondFrame,image=car4,border=0)
            car4lbl.place(x=200,y=950)
            
            car5 = utl.read_Image('./images/cars/TeslaModel3LongRangeAWD.png',(200,170))
            car5lbl = Label(secondFrame,image=car5,border=0)
            car5lbl.place(x=200,y=1200)
            
            car6 = utl.read_Image('./images/cars/VolkswagenID4.png',(200,170))
            car6lbl = Label(secondFrame,image=car6,border=0)
            car6lbl.place(x=200,y=1450) 
            
            secondFrame.update_idletasks()  # Asegura que todos los elementos estén cargados
            my_canvasCar.config(scrollregion=my_canvasCar.bbox('all'))
            
            # Habilitar scroll con la rueda del mouse
            def _on_mouse_wheel(event):
                my_canvasCar.yview_scroll(-1 * int(event.delta / 120), "units")

            my_canvasCar.bind_all("<MouseWheel>", _on_mouse_wheel)
            
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
            topScooter.iconbitmap('./images/CarIcon.ico')
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
        ToolTip(LogoScooterBtn,msg='Click para ver los scooters')
        
        
        # BIKES PANEL 3 -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        def bikesPanel():
            self.menu.withdraw()
            topBikes = Toplevel()
            topBikes.title('Electric Cars')
            topBikes.iconbitmap('./images/CarIcon.ico')
            w,h = topBikes.winfo_screenwidth(),topBikes.winfo_screenheight() # que la ventana se adapte ala pantalla 
            topBikes.geometry("%dx%d+0+0" % (w,h))
            topBikes.config(bg='gray')
            utl.center_window(topBikes,w,h)
            
            bikeLbl = Label(topBikes,text='Hola Usuario',font=('Arial', 15))
            bikeLbl.pack()
            
            img = utl.read_Image('./images/cars/NissanLeaf.png',(200,170))
            
            def backMenu():
                topBikes.withdraw()
                self.menu.deiconify()
            
            imglbl = Button(topBikes,image=img,command=backMenu)
            imglbl.pack()
            
            topBikes.mainloop()
        
        logoBike = utl.read_Image('./images/bikes/logoBike.png',(200,170))
        logoBikelbl = Label(self.menu,text='Bicicletas',font=('Arial', 25),bg='gray')
        logoBikelbl.place(x=730,y=200)    
        LogoBikeBtn = Button(self.menu,image=logoBike,command=bikesPanel,border=0,bg='black')
        LogoBikeBtn.place(x=700,y=250)
        ToolTip(LogoBikeBtn,msg='Click para ver las bicicletas')
        
            
        self.menu.mainloop()
            
        
    
    

        
    
        
        
