import tkinter as tk
from tkinter.font import BOLD
import util.generic as utl
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tktooltip import ToolTip
from master import coche, scooter, bike


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
            w,h = topCars.winfo_screenwidth(),topCars.winfo_screenheight() # que la ventana se adapte ala pantalla 
            topCars.geometry("%dx%d+0+0" % (w,h))
            topCars.config(bg='gray')
            utl.center_window(topCars,w,h)
            
            # Scrolling 
            scrollbar = tk.Scrollbar(topCars)
            canvas = Canvas(topCars,bg='pink',yscrollcommand=scrollbar.set)
            scrollbar.config(command=canvas.yview)
            scrollbar.pack(side=RIGHT,fill=Y)
            secondFrame = Frame(canvas,bg='pink')
            canvas.pack(side='left',fill='both',expand=TRUE)
            canvas.create_window(0,0,window=secondFrame,anchor='n')
        
            # Crear elementos dentro de secondFrame usando grid
            hiUserlbl = Label(secondFrame, text='Sección de carros eléctricos', font=('Arial', 35,BOLD), bg='pink')
            hiUserlbl.place(x=300,y=20)

            logoMenu = utl.read_Image('./images/logo.png', (70, 70))

            def backMenu():
                topCars.withdraw()
                self.menu.deiconify()

            logoMenubtn = Button(secondFrame, image=logoMenu, command=backMenu, border=0)
            logoMenubtn.grid(row=0,column=0)

            car1 = utl.read_Image('./images/cars/ChevroletBoltEV.png',(200, 170))
            car2 = utl.read_Image('./images/cars/KiaSoulEV.png',(200, 170))
            car3 = utl.read_Image('./images/cars/MazdaMX-30.png',(200, 170))
            car4 = utl.read_Image('./images/cars/NissanLeaf.png',(200, 170))
            car5 = utl.read_Image('./images/cars/TeslaModel3LongRangeAWD.png',(200, 170))
            car6 = utl.read_Image('./images/cars/VolkswagenID4.png',(200, 170))
            car7 = utl.read_Image('./images/cars/TeslaModel3StandardRangePlus.png',(200, 170))
            car8 = utl.read_Image('./images/cars/RenaultZoe.png',(200, 170))
            
            # 
            def mostrarinfocar1():
                coche.infoPanelCar1()
                
            def mostrarinfocar2():
                coche.infoPanelCar2()
                
            def mostrarinfocar3():
                coche.infoPanelCar3()
                
            def mostrarinfocar4():
                coche.infoPanelCar4()
                
            def mostrarinfocar5():
                coche.infoPanelCar5()
                
            def mostrarinfocar6():
                coche.infoPanelCar6()
                
            def mostrarinfocar7():
                coche.infoPanelCar7()
                
            def mostrarinfocar8():
                coche.infoPanelCar8()
                
            
            # colocacion de imagenes
            car1btn = Button(secondFrame,image=car1,bd=0,command=mostrarinfocar1)
            car1btn.grid(row=1,column=2, pady=(30,5), padx=40)
            car2btn = Button(secondFrame,image=car2,bd=0,command=mostrarinfocar2)
            car2btn.grid(row=1,column=3, pady=(30,5), padx=40)
            car3btn = Button(secondFrame,image=car3,bd=0,command=mostrarinfocar3)
            car3btn.grid(row=1,column=4, pady=(30,5), padx=40)
            car4btn = Button(secondFrame,image=car4,bd=0,command=mostrarinfocar4)
            car4btn.grid(row=3,column=2, pady=(30,5), padx=40)
            car5btn = Button(secondFrame,image=car5,bd=0,command=mostrarinfocar5)
            car5btn.grid(row=3,column=3, pady=(30,5), padx=40)
            car6btn = Button(secondFrame,image=car6,bd=0,command=mostrarinfocar6)
            car6btn.grid(row=3,column=4, pady=(30,5), padx=40)
            car7btn = Button(secondFrame,image=car7,bd=0,command=mostrarinfocar7)
            car7btn.grid(row=1,column=5, pady=(30,5), padx=40)
            car8btn = Button(secondFrame,image=car8,bd=0,command=mostrarinfocar8)
            car8btn.grid(row=3,column=5, pady=(30,5), padx=40)
            
            
            
            # informcaracion de los carros
            txtcar1 = 'Chevrolet Bolt EV\nCapacidad: 5 personas\nMaletero: 381 lts\n$90 dls /dia'
            infocar1 = Label(secondFrame,wraplength=300,text=txtcar1,font=('Arial', 15),anchor='w',justify='left',bg='white')
            infocar1.grid(row=2,column=2,pady=(0,20))
            
            txtcar2 = 'Kia Soul EV\nCapacidad: 5 personas\nMaletero: 315 lts\n$65 dls /dia'
            infocar2 = Label(secondFrame,wraplength=300,text=txtcar2,font=('Arial', 15),anchor='w',justify='left',bg='white')
            infocar2.grid(row=2,column=3,pady=(0,20))
            
            txtcar3 = 'Mazda MX-30\nCapacidad: 5 personas\nMaletero: 366 lts\n$120 dls /dia'
            infocar3 = Label(secondFrame,wraplength=300,text=txtcar3,font=('Arial', 15),anchor='w',justify='left',bg='white')
            infocar3.grid(row=2,column=4,pady=(0,20))
            
            txtcar4 = 'Nissan Leaf\nCapacidad: 5 personas\nMaletero: 435 lts\n$85 dls /dia'
            infocar4 = Label(secondFrame,wraplength=300,text=txtcar4,font=('Arial', 15),anchor='w',justify='left',bg='white')
            infocar4.grid(row=4,column=2,pady=(0,20))
            
            txtcar5 = 'Tesla Model 3 \nLong Range AWD\nCapacidad: 5 personas\nMaletero: 425 lts\n$130 dls /dia'
            infocar5 = Label(secondFrame,wraplength=300,text=txtcar5,font=('Arial', 15),anchor='w',justify='left',bg='white')
            infocar5.grid(row=4,column=3,pady=(20,20))
            
            txtcar6 = 'Volkswagen ID.4\nCapacidad: 5 personas\nMaletero: 543 lts\n$125 dls /dia'
            infocar6 = Label(secondFrame,wraplength=300,text=txtcar6,font=('Arial', 15),anchor='w',justify='left',bg='white')
            infocar6.grid(row=4,column=4,pady=(0,20))
            
            txtcar7 = 'Tesla Model 3 \nStandard Range Plus\nCapacidad: 5 personas\nMaletero: 425 lts\n$128 dls /dia'
            infocar7 = Label(secondFrame,wraplength=300,text=txtcar7,font=('Arial', 15),anchor='w',justify='left',bg='white')
            infocar7.grid(row=2,column=5,pady=(20,20))
            
            txtcar8 = 'Renault Zoe\nCapacidad: 5 personas\nMaletero: 338 lts\n$45 dls /dia'
            infocar8 = Label(secondFrame,wraplength=300,text=txtcar8,font=('Arial', 15),anchor='w',justify='left',bg='white')
            infocar8.grid(row=4,column=5,pady=(20,20))

            # Actualizar el área de desplazamiento después de agregar todos los elementos
            def _on_mouse_wheel(event):
                canvas.yview_scroll(-1 * int(event.delta / 120), "units")

            canvas.bind_all("<MouseWheel>", _on_mouse_wheel)
            
            topCars.update()
            topCars.update_idletasks()
            canvas.config(scrollregion=canvas.bbox('all'))

            topCars.mainloop()
        
        logoCarlbl = Label(self.menu,text='Coche',font=('Arial', 25),bg='gray')
        logoCarlbl.place(x=150,y=200)    
        LogoCarBtn = Button(self.menu,image=logoCar,command=carsPanel,border=0,bg='black')
        LogoCarBtn.place(x=100,y=250)
        ToolTip(LogoCarBtn,msg='Click para ver los coches')
        
        # SCOOTER PANEL 2 -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        def scooterPanel():
            self.menu.withdraw()
            topScooters = Toplevel()
            topScooters.title('Electric Scooters')
            topScooters.iconbitmap('./images/CarIcon.ico')
            w,h = topScooters.winfo_screenwidth(),topScooters.winfo_screenheight() # que la ventana se adapte ala pantalla 
            topScooters.geometry("%dx%d+0+0" % (w,h))
            topScooters.config(bg='gray')
            utl.center_window(topScooters,w,h)
            
            # Scrolling 
            scrollbar = tk.Scrollbar(topScooters)
            canvas = Canvas(topScooters,bg='pink',yscrollcommand=scrollbar.set)
            scrollbar.config(command=canvas.yview)
            scrollbar.pack(side=RIGHT,fill=Y)
            secondFrame = Frame(canvas,bg='pink')
            canvas.pack(side='left',fill='both',expand=TRUE)
            canvas.create_window(0,0,window=secondFrame,anchor='n')
        
            # Crear elementos dentro de secondFrame usando grid
            hiUserlbl = Label(secondFrame, text='Sección de scooters eléctricos', font=('Arial', 35,BOLD), bg='pink')
            hiUserlbl.place(x=300,y=20)

            logoMenu = utl.read_Image('./images/logo.png', (70, 70))

            def backMenu():
                topScooters.withdraw()
                self.menu.deiconify()

            logoMenubtn = Button(secondFrame, image=logoMenu, command=backMenu, border=0)
            logoMenubtn.grid(row=0,column=0)

            sc1 = utl.read_Image('./images/scooter/City.png',(200, 170))
            sc2 = utl.read_Image('./images/scooter/dualtron-thunder-3-electric-scooter-front-left_1200x.png',(200, 170))
            sc3 = utl.read_Image('./images/scooter/E300ElectricScooter.png',(200, 170))
            sc4 = utl.read_Image('./images/scooter/G-Booster.png',(200, 170))
            sc5 = utl.read_Image('./images/scooter/MiElectricScooterPro2.png',(200, 170))
            sc6 = utl.read_Image('./images/scooter/NinebotKickScooterMAXG30.png',(200, 170))
            sc7 = utl.read_Image('./images/scooter/OXSuper.png',(200, 170))
            sc8 = utl.read_Image('./images/scooter/S2Pro.png',(200, 170))
            
            # 
            def mostrarinfoSc1():
                scooter.infoPanelSc1()
                
            def mostrarinfoSc2():
                scooter.infoPanelSc2()
                
            def mostrarinfoSc3():
                scooter.infoPanelSc3()
                
            def mostrarinfoSc4():
                scooter.infoPanelSc4()
                
            def mostrarinfoSc5():
                scooter.infoPanelSc5()
                
            def mostrarinfoSc6():
                scooter.infoPanelSc6()
                
            def mostrarinfoSc7():
                scooter.infoPanelSc7()
                
            def mostrarinfoSc8():
                scooter.infoPanelSc8()
                
            
            # colocacion de imagenes
            sc1btn = Button(secondFrame,image=sc1,bd=0,command=mostrarinfoSc1)
            sc1btn.grid(row=1,column=2, pady=(30,20), padx=40)
            sc2btn = Button(secondFrame,image=sc2,bd=0,command=mostrarinfoSc2)
            sc2btn.grid(row=1,column=3, pady=(30,5), padx=40)
            sc3btn = Button(secondFrame,image=sc3,bd=0,command=mostrarinfoSc3)
            sc3btn.grid(row=1,column=4, pady=(30,5), padx=40)
            sc4btn = Button(secondFrame,image=sc4,bd=0,command=mostrarinfoSc4)
            sc4btn.grid(row=3,column=2, pady=(30,0), padx=40)
            sc5btn = Button(secondFrame,image=sc5,bd=0,command=mostrarinfoSc5)
            sc5btn.grid(row=3,column=3, pady=(30,0), padx=40)
            sc6btn = Button(secondFrame,image=sc6,bd=0,command=mostrarinfoSc6)
            sc6btn.grid(row=3,column=4, pady=(30,5), padx=40)
            sc7btn = Button(secondFrame,image=sc7,bd=0,command=mostrarinfoSc7)
            sc7btn.grid(row=1,column=5, pady=(30,5), padx=40)
            sc8btn = Button(secondFrame,image=sc8,bd=0,command=mostrarinfoSc8)
            sc8btn.grid(row=3,column=5, pady=(30,5), padx=40)
            
            
            
            # informcaracion de los carros
            txtsc1 = 'Apollo City\nVelocidad máx: 40 km/h\nPeso máx: 120 kg\n$12 dls /hora'
            infoSc1 = Label(secondFrame,wraplength=300,text=txtsc1,font=('Arial', 15),anchor='w',justify='left',bg='white')
            infoSc1.grid(row=2,column=2,pady=(0,20))
            
            txtsc2 = 'Dualtron Thunder\nVelocidad máx: 80 km/h\nPeso máx: 150 kg\n$15 dls /hora'
            infoSc2 = Label(secondFrame,wraplength=300,text=txtsc2,font=('Arial', 15),anchor='w',justify='left',bg='white')
            infoSc2.grid(row=2,column=3,pady=(0,20))
            
            txtsc3 = 'Razor E300 \nVelocidad máx: 24 km/h\nPeso máx: 100 kg\n$7 dls /hora'
            infoSc3 = Label(secondFrame,wraplength=300,text=txtsc3,font=('Arial', 15),anchor='w',justify='left',bg='white')
            infoSc3.grid(row=2,column=4,pady=(0,20))
            
            txtsc4 = 'Kugoo G-Booster\nVelocidad máx: 55 km/h\nPeso máx: 150 kg\n$14 dls /hora'
            infoSc4 = Label(secondFrame,wraplength=300,text=txtsc4,font=('Arial', 15),anchor='w',justify='left',bg='white')
            infoSc4.grid(row=4,column=2,pady=(0,20))
            
            txtsc5 = 'Mi Electric Pro 2\nVelocidad máx: 25 km/h\nPeso máx: 100 kg\n$8 dls /hora'
            infoSc5 = Label(secondFrame,wraplength=300,text=txtsc5,font=('Arial', 15),anchor='w',justify='left',bg='white')
            infoSc5.grid(row=4,column=3,pady=(0,20))
            
            txtsc6 = 'Segway Ninebot \nKickScooter\nMAX G30\nVelocidad máx: 25 km/h\nPeso máx: 100 kg\n$10 dls /hora'
            infoSc6 = Label(secondFrame,wraplength=300,text=txtsc6,font=('Arial', 15),anchor='w',justify='left',bg='white')
            infoSc6.grid(row=4,column=4,pady=(40,20))
            
            txtsc7 = 'Inokim OX Super\nVelocidad máx: 45 km/h\nPeso máx: 120 kg\n$13 dls /hora'
            infoSc7 = Label(secondFrame,wraplength=300,text=txtsc7,font=('Arial', 15),anchor='w',justify='left',bg='white')
            infoSc7.grid(row=2,column=5,pady=(15,20))
            
            txtsc8 = 'Hiboy S2 Pro\nVelocidad máx: 30 km/h\nPeso máx: 120 kg\n$9 dls /hora'
            infoSc8 = Label(secondFrame,wraplength=300,text=txtsc8,font=('Arial', 15),anchor='w',justify='left',bg='white')
            infoSc8.grid(row=4,column=5,pady=(0,20))

            # Actualizar el área de desplazamiento después de agregar todos los elementos
            def _on_mouse_wheel(event):
                canvas.yview_scroll(-1 * int(event.delta / 120), "units")

            canvas.bind_all("<MouseWheel>", _on_mouse_wheel)
            
            topScooters.update()
            topScooters.update_idletasks()
            canvas.config(scrollregion=canvas.bbox('all'))

            topScooters.mainloop()
        
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
            topBikes.title('Electric Bikes')
            topBikes.iconbitmap('./images/CarIcon.ico')
            w,h = topBikes.winfo_screenwidth(),topBikes.winfo_screenheight() # que la ventana se adapte ala pantalla 
            topBikes.geometry("%dx%d+0+0" % (w,h))
            topBikes.config(bg='gray')
            utl.center_window(topBikes,w,h)
            
            # Scrolling 
            scrollbar = tk.Scrollbar(topBikes)
            canvas = Canvas(topBikes,bg='pink',yscrollcommand=scrollbar.set)
            scrollbar.config(command=canvas.yview)
            scrollbar.pack(side=RIGHT,fill=Y)
            secondFrame = Frame(canvas,bg='pink')
            canvas.pack(side='left',fill='both',expand=TRUE)
            canvas.create_window(0,0,window=secondFrame,anchor='n')
        
            # Crear elementos dentro de secondFrame usando grid
            hiUserlbl = Label(secondFrame, text='Sección de bicicletas eléctricas', font=('Arial', 35,BOLD), bg='pink')
            hiUserlbl.place(x=300,y=20)

            logoMenu = utl.read_Image('./images/logo.png', (70, 70))

            def backMenu():
                topBikes.withdraw()
                self.menu.deiconify()

            logoMenubtn = Button(secondFrame, image=logoMenu, command=backMenu, border=0)
            logoMenubtn.grid(row=0,column=0)

            bike1 = utl.read_Image('./images/bikes/Allant7.png',(200, 170))
            bike2 = utl.read_Image('./images/bikes/D11.png',(200, 170))
            bike3 = utl.read_Image('./images/bikes/ElectricCLine.png',(200, 170))
            bike4 = utl.read_Image('./images/bikes/HimoC26.png',(200, 170))
            bike5 = utl.read_Image('./images/bikes/PowerPlus.png',(200, 170))
            bike6 = utl.read_Image('./images/bikes/Supercharger2.png',(200, 170))
            bike7 = utl.read_Image('./images/bikes/TurboVadoSL40.png',(200, 170))
            bike8 = utl.read_Image('./images/bikes/VanMoofS3.png',(200, 170))
            
            # 
            def mostrarinfoBike1():
                bike.infoPanelBk1()
                
            def mostrarinfoBike2():
                bike.infoPanelBk2()
                
            def mostrarinfoBike3():
                bike.infoPanelBk3()
                
            def mostrarinfoBike4():
                bike.infoPanelBk4()
                
            def mostrarinfoBike5():
                bike.infoPanelBk5()
                
            def mostrarinfoBike6():
                bike.infoPanelBk6()
                
            def mostrarinfoBike7():
                bike.infoPanelBk7()
                
            def mostrarinfoBike8():
                bike.infoPanelBk8()
                
            
            # colocacion de imagenes
            bike1btn = Button(secondFrame,image=bike1,bd=0,command=mostrarinfoBike1)
            bike1btn.grid(row=1,column=2, pady=(30,20), padx=40)
            bike2btn = Button(secondFrame,image=bike2,bd=0,command=mostrarinfoBike2)
            bike2btn.grid(row=1,column=3, pady=(30,5), padx=40)
            bike3btn = Button(secondFrame,image=bike3,bd=0,command=mostrarinfoBike3)
            bike3btn.grid(row=1,column=4, pady=(30,5), padx=40)
            bike4btn = Button(secondFrame,image=bike4,bd=0,command=mostrarinfoBike4)
            bike4btn.grid(row=3,column=2, pady=(30,0), padx=40)
            bike5btn = Button(secondFrame,image=bike5,bd=0,command=mostrarinfoBike5)
            bike5btn.grid(row=3,column=3, pady=(30,0), padx=40)
            bike6btn = Button(secondFrame,image=bike6,bd=0,command=mostrarinfoBike6)
            bike6btn.grid(row=3,column=4, pady=(30,5), padx=40)
            bike7btn = Button(secondFrame,image=bike7,bd=0,command=mostrarinfoBike7)
            bike7btn.grid(row=1,column=5, pady=(30,5), padx=40)
            bike8btn = Button(secondFrame,image=bike8,bd=0,command=mostrarinfoBike8)
            bike8btn.grid(row=3,column=5, pady=(30,5), padx=40)
            
            
            
            # informcaracion de los carros
            txtBike1 = 'Allant+7\nVelocidad máx: 32 km/h\nPeso máx: 136 kg\n$16 dls /hora'
            infoBike1 = Label(secondFrame,wraplength=300,text=txtBike1,font=('Arial', 15),anchor='w',justify='left',bg='white')
            infoBike1.grid(row=2,column=2,pady=(0,20))
            
            txtBike2 = 'Fiido D11\nVelocidad máx: 25 km/h\nPeso máx: 120 kg\n$8 dls /hora'
            infoBike2 = Label(secondFrame,wraplength=300,text=txtBike2,font=('Arial', 15),anchor='w',justify='left',bg='white')
            infoBike2.grid(row=2,column=3,pady=(0,20))
            
            txtBike3 = 'Brompton Electric C\nLine\nVelocidad máx: 25 km/h\nPeso máx: 105 kg\n$12 dls /hora'
            infoBike3 = Label(secondFrame,wraplength=300,text=txtBike3,font=('Arial', 15),anchor='w',justify='left',bg='white')
            infoBike3.grid(row=2,column=4,pady=(20,20))
            
            txtBike4 = 'Xiaomi Himo C26\nVelocidad máx: 25 km/h\nPeso máx: 100 kg\n$6 dls /hora'
            infoBike4 = Label(secondFrame,wraplength=300,text=txtBike4,font=('Arial', 15),anchor='w',justify='left',bg='white')
            infoBike4.grid(row=4,column=2,pady=(0,20))
            
            txtBike5 = 'Ancheer Power Plus\nVelocidad máx: 25 km/h\nPeso máx: 120 kg\n$7 dls /hora'
            infoBike5 = Label(secondFrame,wraplength=300,text=txtBike5,font=('Arial', 15),anchor='w',justify='left',bg='white')
            infoBike5.grid(row=4,column=3,pady=(0,20))
            
            txtBike6 = 'Riese & Müller\nSupercharger2\nVelocidad máx: 45 km/h\nPeso máx: 140 kg\n$20 dls /hora'
            infoBike6 = Label(secondFrame,wraplength=300,text=txtBike6,font=('Arial', 15),anchor='w',justify='left',bg='white')
            infoBike6.grid(row=4,column=4,pady=(20,20))
            
            txtBike7 = 'Specialized Turbo\nVado SL 4.0\nVelocidad máx: 45 km/h\nPeso máx: 120 kg\n$15 dls /hora'
            infoBike7 = Label(secondFrame,wraplength=300,text=txtBike7,font=('Arial', 15),anchor='w',justify='left',bg='white')
            infoBike7.grid(row=2,column=5,pady=(20,20))
            
            txtBike8 = 'VanMoof S3\nVelocidad máx: 32 km/h\nPeso máx: 120 kg\n$14 dls /hora'
            infoBike8 = Label(secondFrame,wraplength=300,text=txtBike8,font=('Arial', 15),anchor='w',justify='left',bg='white')
            infoBike8.grid(row=4,column=5,pady=(0,20))

            # Actualizar el área de desplazamiento después de agregar todos los elementos
            def _on_mouse_wheel(event):
                canvas.yview_scroll(-1 * int(event.delta / 120), "units")

            canvas.bind_all("<MouseWheel>", _on_mouse_wheel)
            
            topBikes.update()
            topBikes.update_idletasks()
            canvas.config(scrollregion=canvas.bbox('all'))

            topBikes.mainloop()
        
        logoBike = utl.read_Image('./images/bikes/logoBike.png',(200,170))
        logoBikelbl = Label(self.menu,text='Bicicletas',font=('Arial', 25),bg='gray')
        logoBikelbl.place(x=730,y=200)    
        LogoBikeBtn = Button(self.menu,image=logoBike,command=bikesPanel,border=0,bg='black')
        LogoBikeBtn.place(x=700,y=250)
        ToolTip(LogoBikeBtn,msg='Click para ver las bicicletas')
        
            
        self.menu.mainloop()
        