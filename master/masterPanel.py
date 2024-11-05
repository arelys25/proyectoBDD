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
        self.menu.resizable(width=True, height=True)
        
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
            w, h = topCars.winfo_screenwidth(), topCars.winfo_screenheight()
            topCars.geometry("%dx%d+0+0" % (w, h))
            topCars.config(bg='gray')
            utl.center_window(topCars, w, h)

            

            # Crear elementos dentro de secondFrame usando grid
            hiUserlbl = Label(topCars, text='Hola Usuario', font=('Arial', 35), bg='GRAY')
            hiUserlbl.grid(row=0, column=1, pady=30, padx=30)

            logoMenu = utl.read_Image('./images/logo.png', (70, 70))

            def backMenu():
                topCars.withdraw()
                self.menu.deiconify()

            logoMenubtn = Button(topCars, image=logoMenu, command=backMenu, border=0)
            logoMenubtn.grid(row=0, column=0, padx=10, pady=10)

            # Cargar imágenes de coches y ubicarlas en una cuadrícula
            cars_images = [
                ('./images/cars/ChevroletBoltEV.png', 1),
                ('./images/cars/KiaSoulEV.png', 2),
                ('./images/cars/MazdaMX-30.png', 3),
                ('./images/cars/NissanLeaf.png', 4),
                ('./images/cars/TeslaModel3LongRangeAWD.png', 5),
                ('./images/cars/VolkswagenID4.png', 6)
            ]

            for i, (img_path, row) in enumerate(cars_images):
                car_img = utl.read_Image(img_path, (200, 170))
                car_lbl = Label(topCars, image=car_img, border=0)
                car_lbl.grid(row=row, column=1, pady=30, padx=30)
                car_lbl.image = car_img  # Evitar que la imagen sea recolectada por el garbage collector

            # Actualizar el área de desplazamiento después de agregar todos los elementos
            topCars.update_idletasks()
            

            # Habilitar scroll con la rueda del mouse
            

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
            topScooter.config(bg='pink')
            utl.center_window(topScooter,w,h)
            
            
            # Scrolling 
            scrollbar = tk.Scrollbar(topScooter)
            canvas = Canvas(topScooter,bg='pink',yscrollcommand=scrollbar.set)
            scrollbar.config(command=canvas.yview)
            scrollbar.pack(side=RIGHT,fill=Y)
            secondFrame = Frame(canvas,bg='pink')
            canvas.pack(side='left',fill='both',expand=TRUE)
            canvas.create_window(0,0,window=secondFrame,anchor='n')
            
            secondFrame.grid_columnconfigure(0, weight=1)
            secondFrame.grid_columnconfigure(1, weight=1)
            secondFrame.grid_columnconfigure(2, weight=1)
            
            scooterLbl = Label(secondFrame,text='Hola Usuario',font=('Arial', 15))
            scooterLbl.grid(row=0, column=3)
                        
            # images
            sc1 = utl.read_Image('./images/scooter/City.png',(200,170))
            sc2 = utl.read_Image('./images/scooter/dualtron-thunder-3-electric-scooter-front-left_1200x.png',(200,170))
            sc3 = utl.read_Image('./images/scooter/E300ElectricScooter.png',(200,170))
            sc4 = utl.read_Image('./images/scooter/G-Booster.png',(200,170))
            sc5 = utl.read_Image('./images/scooter/MiElectricScooterPro2.png',(200,170))
            sc6 = utl.read_Image('./images/scooter/NinebotKickScooterMAXG30.png',(200,170))
            sc7 = utl.read_Image('./images/scooter/S2Pro.png',(200,170))
            
            scooterSelect = IntVar()
            
            sc1lbl = Radiobutton(secondFrame,image=sc1,bd=0,value=1,variable=scooterSelect)
            sc1lbl.grid(row=1,column=2, pady=30, padx=30)
            sc2lbl = Radiobutton(secondFrame,image=sc2,bd=0,value=2,variable=scooterSelect)
            sc2lbl.grid(row=1,column=3, pady=30, padx=30)
            sc3lbl = Radiobutton(secondFrame,image=sc3,bd=0,value=3,variable=scooterSelect)
            sc3lbl.grid(row=1,column=4, pady=30, padx=30)
            sc4lbl = Radiobutton(secondFrame,image=sc4,bd=0,value=4,variable=scooterSelect)
            sc4lbl.grid(row=2,column=2, pady=30, padx=30)
            sc5lbl = Radiobutton(secondFrame,image=sc5,bd=0,value=5,variable=scooterSelect)
            sc5lbl.grid(row=2,column=3, pady=30, padx=30)
            sc6lbl = Radiobutton(secondFrame,image=sc6,bd=0,value=6,variable=scooterSelect)
            sc6lbl.grid(row=2,column=4, pady=30, padx=30)
            sc7lbl = Radiobutton(secondFrame,image=sc7,bd=0,value=7,variable=scooterSelect)
            sc7lbl.grid(row=3,column=2, pady=30, padx=30)
            
            #scooter = scooterSelect.get()
            
            
            
            logoPage = utl.read_Image('./images/logo.png', (70, 70))            
            def backMenu():
                topScooter.withdraw()
                self.menu.deiconify()
                            
            imgLogolbl = Button(secondFrame,image=logoPage,command=backMenu,bd=0)
            imgLogolbl.grid(row=0,column=0)
            
            def _on_mouse_wheel(event):
                canvas.yview_scroll(-1 * int(event.delta / 120), "units")

            canvas.bind_all("<MouseWheel>", _on_mouse_wheel)
            
            topScooter.update()
            canvas.config(scrollregion=canvas.bbox('all'))
                        
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
        