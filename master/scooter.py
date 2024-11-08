import tkinter as tk
from tkinter.font import BOLD
import util.generic as utl
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tktooltip import ToolTip

def infoPanelSc1 ():
    topVehiculo = Toplevel()
    topVehiculo.title('Electric Scooter Information')
    topVehiculo.iconbitmap('./images/CarIcon.ico')
    topVehiculo.geometry('650x600')
    topVehiculo.config(bg='gray')
    utl.center_window(topVehiculo,650,600)
    topVehiculo.resizable(width=False, height=False)
    
    # Leer y cargar la imagen
    vehiculo = utl.read_Image('./images/scooter/City.png',(200, 170))
    
    vehiculolbl = Label(topVehiculo, image=vehiculo, bd=0)
    vehiculolbl.place(x=40, y=55)  
    
    txtVehiculo1 = 'Apollo City\nVelocidad máx: 40 km/h\nPeso máx: 120 kg\nTamaño: 1210x620x1240 mm\nPeso: 18 kg\nTiempo de carga: 8 hrs\nPlegable: Sí\nVoltaje: 48 V\nSeguro: Sí\n$12 dls /hora'
    infoVehiculo = Label(topVehiculo,wraplength=800,text=txtVehiculo1,font=('Arial', 12),anchor='w',justify='left',bg='white')
    infoVehiculo.place(x=270,y=40)
    
    disponibilidad = False
    
    if disponibilidad == True:
        estado = 'DISPONIBLE'
    else:
        estado = 'NO DISPONIBLE'
    
    estadolbl = Label(topVehiculo,text='Estado: '+estado,font=('Arial', 12,BOLD),bg='gray')
    estadolbl.place(x=40,y=20)
    
    
    fechaSalida = StringVar()
    fechaLlegada = StringVar()
    titularTarjeta = StringVar()
    numTarjeta = StringVar()
    expiTarjeta = StringVar()
    cvv = StringVar()
    sucursalSeleccionada = StringVar()
    
        
    fechaSalidalbl = Label(topVehiculo,text='Fecha de salida (dd/mm/yyyy): ',bg='gray')
    fechaSalidalbl.place(x=40,y=250) 
    fSalida = Entry(topVehiculo,font=('Arial', 11),textvariable=fechaSalida,bd=2)
    fSalida.place(x=220,y=250)
    
    fechaLlegadalbl = Label(topVehiculo,text='Fecha de llegada (dd/mm/yyyy): ',bg='gray')
    fechaLlegadalbl.place(x=40,y=300) 
    fLlegada = Entry(topVehiculo,font=('Arial', 11),textvariable=fechaLlegada,bd=2)
    fLlegada.place(x=220,y=300)   
    
    titularTarjetalbl = Label(topVehiculo,text='Titular de la tarjeta: ',bg='gray')
    titularTarjetalbl.place(x=98,y=350) 
    titularTarjetaEny = Entry(topVehiculo,font=('Arial', 11),textvariable=titularTarjeta,bd=2)
    titularTarjetaEny.place(x=220,y=350)
    
    numTarjetalbl = Label(topVehiculo,text='Numero de tarjeta: ',bg='gray')
    numTarjetalbl.place(x=98,y=400) 
    numTarjetaEny = Entry(topVehiculo,font=('Arial', 11),textvariable=numTarjeta,bd=2)
    numTarjetaEny.place(x=220,y=400)
    
    expiTarjetalbl = Label(topVehiculo,text='Fecha de expiracion (mm/yy): ',bg='gray')
    expiTarjetalbl.place(x=40,y=450) 
    expiTarjetaEny = Entry(topVehiculo,font=('Arial', 11),textvariable=expiTarjeta,bd=2)
    expiTarjetaEny.place(x=220,y=450)
    
    cvvlbl = Label(topVehiculo,text='CVV: ',bg='gray')
    cvvlbl.place(x=174,y=500) 
    cvvEny = Entry(topVehiculo,font=('Arial', 11),textvariable=cvv,bd=2)
    cvvEny.place(x=220,y=500)
    
    
    def rentar ():
        if disponibilidad == True:
            if not (fechaSalida.get() and fechaLlegada.get() and titularTarjeta.get() and numTarjeta.get() and expiTarjeta.get() and cvv.get()):
                messagebox.showerror("Error", "Todos los campos son obligatorios")
                return  
            else: 
                if sucursalSeleccionada.get() == 'Seleccione una sucursal':
                    messagebox.showerror("Error", "Por favor seleccione una sucursal")
                    return
                else:
                    # Validación de que CVV sea un número
                    try:
                        cvv_value = int(cvv.get())  # Intenta convertir el CVV a un entero
                
                        vehiculoNom = 'Apollo City'
            
                        txt = f'Transaccion exitosa. Usted rento un {vehiculoNom} del {fechaSalida.get()} al {fechaLlegada.get()}. Favor de recoger el vehiculo en la sucursal {sucursalSeleccionada.get()}'
                        messagebox.showinfo("Transaccion exitosa", txt)
                    except ValueError:
                        messagebox.showerror("Error", "El CVV debe contener solo números")
                        return
        else:
            messagebox.showerror("Error", "No puede rentar ahora porque el coche no esta disponible. Por favor haga una reservación.")
        
    def reservar ():
        if not (fechaSalida.get() and fechaLlegada.get() and titularTarjeta.get() and numTarjeta.get() and expiTarjeta.get() and cvv.get()):
                messagebox.showerror("Error", "Todos los campos son obligatorios")
                return  
        else: 
            if sucursalSeleccionada.get() == 'Seleccione una sucursal':
                messagebox.showerror("Error", "Por favor seleccione una sucursal")
                return
            else:
                # Validación de que CVV sea un número
                try:
                    cvv_value = int(cvv.get())  # Intenta convertir el CVV a un entero
                
                    vehiculoNom = 'Apollo City'
            
                    txt = f'Transaccion exitosa. Usted rento un {vehiculoNom} del {fechaSalida.get()} al {fechaLlegada.get()}. Favor de recoger el vehiculo en la sucursal {sucursalSeleccionada.get()}'
                    messagebox.showinfo("Transaccion exitosa", txt)
                except ValueError:
                    messagebox.showerror("Error", "El CVV debe contener solo números")
                    return
    
    rentarbnt = Button(topVehiculo,text='  Rentar  ',font=('Arial',10),command=rentar,bg='pink')
    rentarbnt.place(x=100,y=550)
    
    reservarbnt = Button(topVehiculo,text='  Reservar  ',font=('Arial',10),bg='pink',command=reservar)
    reservarbnt.place(x=250,y=550)
    
    fNODisponibleslbl = Label(topVehiculo,text='Fechas NO disponibles:',font=('Arial',12))
    fNODisponibleslbl.place(x=430,y=250)
    
    fndLbx = Listbox(topVehiculo,width=24,font=('Arial',10))
    fndLbx.insert(0,'13/12/2024 - 26/12/2024')
    fndLbx.insert(1,'03/01/2025 - 07/01/2025')
    fndLbx.place(x=430,y=285)
    
    sucursalSbx = Spinbox(topVehiculo,font=('Arial',12),values=('Seleccione una sucursal','Zapopan','Guadalajara','Tonala'), textvariable=sucursalSeleccionada)
    sucursalSbx.place(x=430,y=490)
    
    topVehiculo.mainloop()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def infoPanelSc2():
    topVehiculo = Toplevel()
    topVehiculo.title('Electric Scooter Information')
    topVehiculo.iconbitmap('./images/CarIcon.ico')
    topVehiculo.geometry('650x600')
    topVehiculo.config(bg='gray')
    utl.center_window(topVehiculo,650,600)
    topVehiculo.resizable(width=False, height=False)
    
    # Leer y cargar la imagen
    vehiculo = utl.read_Image('./images/scooter/dualtron-thunder-3-electric-scooter-front-left_1200x.png',(200, 170))
    
    vehiculolbl = Label(topVehiculo, image=vehiculo, bd=0)
    vehiculolbl.place(x=40, y=55)  
    
    txtVehiculo1 = 'Dualtron Thunder\nVelocidad máx: 80 km/h\nPeso máx: 150 kg\nTamaño: 1238x609x1210 mm\nPeso: 43 kg\nTiempo de carga: 15 hrs\nPlegable: Sí\nVoltaje: 60 V\nSeguro: Sí\n$15 dls /hora'
    infoVehiculo = Label(topVehiculo,wraplength=800,text=txtVehiculo1,font=('Arial', 12),anchor='w',justify='left',bg='white')
    infoVehiculo.place(x=270,y=40)
    
    disponibilidad = False
    
    if disponibilidad == True:
        estado = 'DISPONIBLE'
    else:
        estado = 'NO DISPONIBLE'
    
    estadolbl = Label(topVehiculo,text='Estado: '+estado,font=('Arial', 12,BOLD),bg='gray')
    estadolbl.place(x=40,y=20)
    
    
    fechaSalida = StringVar()
    fechaLlegada = StringVar()
    titularTarjeta = StringVar()
    numTarjeta = StringVar()
    expiTarjeta = StringVar()
    cvv = StringVar()
    sucursalSeleccionada = StringVar()
    
        
    fechaSalidalbl = Label(topVehiculo,text='Fecha de salida (dd/mm/yyyy): ',bg='gray')
    fechaSalidalbl.place(x=40,y=250) 
    fSalida = Entry(topVehiculo,font=('Arial', 11),textvariable=fechaSalida,bd=2)
    fSalida.place(x=220,y=250)
    
    fechaLlegadalbl = Label(topVehiculo,text='Fecha de llegada (dd/mm/yyyy): ',bg='gray')
    fechaLlegadalbl.place(x=40,y=300) 
    fLlegada = Entry(topVehiculo,font=('Arial', 11),textvariable=fechaLlegada,bd=2)
    fLlegada.place(x=220,y=300)   
    
    titularTarjetalbl = Label(topVehiculo,text='Titular de la tarjeta: ',bg='gray')
    titularTarjetalbl.place(x=98,y=350) 
    titularTarjetaEny = Entry(topVehiculo,font=('Arial', 11),textvariable=titularTarjeta,bd=2)
    titularTarjetaEny.place(x=220,y=350)
    
    numTarjetalbl = Label(topVehiculo,text='Numero de tarjeta: ',bg='gray')
    numTarjetalbl.place(x=98,y=400) 
    numTarjetaEny = Entry(topVehiculo,font=('Arial', 11),textvariable=numTarjeta,bd=2)
    numTarjetaEny.place(x=220,y=400)
    
    expiTarjetalbl = Label(topVehiculo,text='Fecha de expiracion (mm/yy): ',bg='gray')
    expiTarjetalbl.place(x=40,y=450) 
    expiTarjetaEny = Entry(topVehiculo,font=('Arial', 11),textvariable=expiTarjeta,bd=2)
    expiTarjetaEny.place(x=220,y=450)
    
    cvvlbl = Label(topVehiculo,text='CVV: ',bg='gray')
    cvvlbl.place(x=174,y=500) 
    cvvEny = Entry(topVehiculo,font=('Arial', 11),textvariable=cvv,bd=2)
    cvvEny.place(x=220,y=500)
    
    
    def rentar ():
        if disponibilidad == True:
            if not (fechaSalida.get() and fechaLlegada.get() and titularTarjeta.get() and numTarjeta.get() and expiTarjeta.get() and cvv.get()):
                messagebox.showerror("Error", "Todos los campos son obligatorios")
                return  
            else: 
                if sucursalSeleccionada.get() == 'Seleccione una sucursal':
                    messagebox.showerror("Error", "Por favor seleccione una sucursal")
                    return
                else:
                    # Validación de que CVV sea un número
                    try:
                        cvv_value = int(cvv.get())  # Intenta convertir el CVV a un entero
                
                        vehiculoNom = 'Dualtron Thunder'
            
                        txt = f'Transaccion exitosa. Usted rento un {vehiculoNom} del {fechaSalida.get()} al {fechaLlegada.get()}. Favor de recoger el vehiculo en la sucursal {sucursalSeleccionada.get()}'
                        messagebox.showinfo("Transaccion exitosa", txt)
                    except ValueError:
                        messagebox.showerror("Error", "El CVV debe contener solo números")
                        return
        else:
            messagebox.showerror("Error", "No puede rentar ahora porque el coche no esta disponible. Por favor haga una reservación.")
        
    def reservar ():
        if not (fechaSalida.get() and fechaLlegada.get() and titularTarjeta.get() and numTarjeta.get() and expiTarjeta.get() and cvv.get()):
                messagebox.showerror("Error", "Todos los campos son obligatorios")
                return  
        else: 
            if sucursalSeleccionada.get() == 'Seleccione una sucursal':
                messagebox.showerror("Error", "Por favor seleccione una sucursal")
                return
            else:
                # Validación de que CVV sea un número
                try:
                    cvv_value = int(cvv.get())  # Intenta convertir el CVV a un entero
                
                    vehiculoNom = 'Dualtron Thunder'
            
                    txt = f'Transaccion exitosa. Usted rento un {vehiculoNom} del {fechaSalida.get()} al {fechaLlegada.get()}. Favor de recoger el vehiculo en la sucursal {sucursalSeleccionada.get()}'
                    messagebox.showinfo("Transaccion exitosa", txt)
                except ValueError:
                    messagebox.showerror("Error", "El CVV debe contener solo números")
                    return
    
    rentarbnt = Button(topVehiculo,text='  Rentar  ',font=('Arial',10),command=rentar,bg='pink')
    rentarbnt.place(x=100,y=550)
    
    reservarbnt = Button(topVehiculo,text='  Reservar  ',font=('Arial',10),bg='pink',command=reservar)
    reservarbnt.place(x=250,y=550)
    
    fNODisponibleslbl = Label(topVehiculo,text='Fechas NO disponibles:',font=('Arial',12))
    fNODisponibleslbl.place(x=430,y=250)
    
    fndLbx = Listbox(topVehiculo,width=24,font=('Arial',10))
    fndLbx.insert(0,'13/12/2024 - 26/12/2024')
    fndLbx.insert(1,'03/01/2025 - 07/01/2025')
    fndLbx.place(x=430,y=285)
    
    sucursalSbx = Spinbox(topVehiculo,font=('Arial',12),values=('Seleccione una sucursal','Zapopan','Guadalajara','Tonala'), textvariable=sucursalSeleccionada)
    sucursalSbx.place(x=430,y=490)
    
    topVehiculo.mainloop()
    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def infoPanelSc3():
    topVehiculo = Toplevel()
    topVehiculo.title('Electric Scooter Information')
    topVehiculo.iconbitmap('./images/CarIcon.ico')
    topVehiculo.geometry('650x600')
    topVehiculo.config(bg='gray')
    utl.center_window(topVehiculo,650,600)
    topVehiculo.resizable(width=False, height=False)
    
    # Leer y cargar la imagen
    vehiculo = utl.read_Image('./images/scooter/E300ElectricScooter.png',(200, 170))
    
    vehiculolbl = Label(topVehiculo, image=vehiculo, bd=0)
    vehiculolbl.place(x=40, y=55)  
    
    txtVehiculo1 = 'Razor E300 \nVelocidad máx: 24 km/h\nPeso máx: 100 kg\nTamaño: 1040x420x950 mm\nPeso: 19.5 kg\nTiempo de carga: 12 hrs\nPlegable: Sí\nVoltaje: 24 V\nSeguro: Sí\n$7 dls /hora'
    infoVehiculo = Label(topVehiculo,wraplength=800,text=txtVehiculo1,font=('Arial', 12),anchor='w',justify='left',bg='white')
    infoVehiculo.place(x=270,y=40)
    
    disponibilidad = False
    
    if disponibilidad == True:
        estado = 'DISPONIBLE'
    else:
        estado = 'NO DISPONIBLE'
    
    estadolbl = Label(topVehiculo,text='Estado: '+estado,font=('Arial', 12,BOLD),bg='gray')
    estadolbl.place(x=40,y=20)
    
    
    fechaSalida = StringVar()
    fechaLlegada = StringVar()
    titularTarjeta = StringVar()
    numTarjeta = StringVar()
    expiTarjeta = StringVar()
    cvv = StringVar()
    sucursalSeleccionada = StringVar()
    
        
    fechaSalidalbl = Label(topVehiculo,text='Fecha de salida (dd/mm/yyyy): ',bg='gray')
    fechaSalidalbl.place(x=40,y=250) 
    fSalida = Entry(topVehiculo,font=('Arial', 11),textvariable=fechaSalida,bd=2)
    fSalida.place(x=220,y=250)
    
    fechaLlegadalbl = Label(topVehiculo,text='Fecha de llegada (dd/mm/yyyy): ',bg='gray')
    fechaLlegadalbl.place(x=40,y=300) 
    fLlegada = Entry(topVehiculo,font=('Arial', 11),textvariable=fechaLlegada,bd=2)
    fLlegada.place(x=220,y=300)   
    
    titularTarjetalbl = Label(topVehiculo,text='Titular de la tarjeta: ',bg='gray')
    titularTarjetalbl.place(x=98,y=350) 
    titularTarjetaEny = Entry(topVehiculo,font=('Arial', 11),textvariable=titularTarjeta,bd=2)
    titularTarjetaEny.place(x=220,y=350)
    
    numTarjetalbl = Label(topVehiculo,text='Numero de tarjeta: ',bg='gray')
    numTarjetalbl.place(x=98,y=400) 
    numTarjetaEny = Entry(topVehiculo,font=('Arial', 11),textvariable=numTarjeta,bd=2)
    numTarjetaEny.place(x=220,y=400)
    
    expiTarjetalbl = Label(topVehiculo,text='Fecha de expiracion (mm/yy): ',bg='gray')
    expiTarjetalbl.place(x=40,y=450) 
    expiTarjetaEny = Entry(topVehiculo,font=('Arial', 11),textvariable=expiTarjeta,bd=2)
    expiTarjetaEny.place(x=220,y=450)
    
    cvvlbl = Label(topVehiculo,text='CVV: ',bg='gray')
    cvvlbl.place(x=174,y=500) 
    cvvEny = Entry(topVehiculo,font=('Arial', 11),textvariable=cvv,bd=2)
    cvvEny.place(x=220,y=500)
    
    
    def rentar ():
        if disponibilidad == True:
            if not (fechaSalida.get() and fechaLlegada.get() and titularTarjeta.get() and numTarjeta.get() and expiTarjeta.get() and cvv.get()):
                messagebox.showerror("Error", "Todos los campos son obligatorios")
                return  
            else: 
                if sucursalSeleccionada.get() == 'Seleccione una sucursal':
                    messagebox.showerror("Error", "Por favor seleccione una sucursal")
                    return
                else:
                    # Validación de que CVV sea un número
                    try:
                        cvv_value = int(cvv.get())  # Intenta convertir el CVV a un entero
                
                        vehiculoNom = 'Razor E300'
            
                        txt = f'Transaccion exitosa. Usted rento un {vehiculoNom} del {fechaSalida.get()} al {fechaLlegada.get()}. Favor de recoger el vehiculo en la sucursal {sucursalSeleccionada.get()}'
                        messagebox.showinfo("Transaccion exitosa", txt)
                    except ValueError:
                        messagebox.showerror("Error", "El CVV debe contener solo números")
                        return
        else:
            messagebox.showerror("Error", "No puede rentar ahora porque el coche no esta disponible. Por favor haga una reservación.")
        
    def reservar ():
        if not (fechaSalida.get() and fechaLlegada.get() and titularTarjeta.get() and numTarjeta.get() and expiTarjeta.get() and cvv.get()):
                messagebox.showerror("Error", "Todos los campos son obligatorios")
                return  
        else: 
            if sucursalSeleccionada.get() == 'Seleccione una sucursal':
                messagebox.showerror("Error", "Por favor seleccione una sucursal")
                return
            else:
                # Validación de que CVV sea un número
                try:
                    cvv_value = int(cvv.get())  # Intenta convertir el CVV a un entero
                
                    vehiculoNom = 'Razor E300'
            
                    txt = f'Transaccion exitosa. Usted rento un {vehiculoNom} del {fechaSalida.get()} al {fechaLlegada.get()}. Favor de recoger el vehiculo en la sucursal {sucursalSeleccionada.get()}'
                    messagebox.showinfo("Transaccion exitosa", txt)
                except ValueError:
                    messagebox.showerror("Error", "El CVV debe contener solo números")
                    return
    
    rentarbnt = Button(topVehiculo,text='  Rentar  ',font=('Arial',10),command=rentar,bg='pink')
    rentarbnt.place(x=100,y=550)
    
    reservarbnt = Button(topVehiculo,text='  Reservar  ',font=('Arial',10),bg='pink',command=reservar)
    reservarbnt.place(x=250,y=550)
    
    fNODisponibleslbl = Label(topVehiculo,text='Fechas NO disponibles:',font=('Arial',12))
    fNODisponibleslbl.place(x=430,y=250)
    
    fndLbx = Listbox(topVehiculo,width=24,font=('Arial',10))
    fndLbx.insert(0,'13/12/2024 - 26/12/2024')
    fndLbx.insert(1,'03/01/2025 - 07/01/2025')
    fndLbx.place(x=430,y=285)
    
    sucursalSbx = Spinbox(topVehiculo,font=('Arial',12),values=('Seleccione una sucursal','Zapopan','Guadalajara','Tonala'), textvariable=sucursalSeleccionada)
    sucursalSbx.place(x=430,y=490)
    
    topVehiculo.mainloop()
    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def infoPanelSc4():
    topVehiculo = Toplevel()
    topVehiculo.title('Electric Scooter Information')
    topVehiculo.iconbitmap('./images/CarIcon.ico')
    topVehiculo.geometry('650x600')
    topVehiculo.config(bg='gray')
    utl.center_window(topVehiculo,650,600)
    topVehiculo.resizable(width=False, height=False)
    
    # Leer y cargar la imagen
    vehiculo = utl.read_Image('./images/scooter/G-Booster.png',(200, 170))
    
    vehiculolbl = Label(topVehiculo, image=vehiculo, bd=0)
    vehiculolbl.place(x=40, y=55)  
    
    txtVehiculo1 = 'Kugoo G-Booster\nVelocidad máx: 55 km/h\nPeso máx: 150 kg\nTamaño: 1200x620x1300 mm\nPeso: 30 kg\nTiempo de carga: 10 hrs\nPlegable: Sí\nVoltaje: 48 V\nSeguro: Sí\n$14 dls /hora'
    infoVehiculo = Label(topVehiculo,wraplength=800,text=txtVehiculo1,font=('Arial', 12),anchor='w',justify='left',bg='white')
    infoVehiculo.place(x=270,y=40)
    
    disponibilidad = False
    
    if disponibilidad == True:
        estado = 'DISPONIBLE'
    else:
        estado = 'NO DISPONIBLE'
    
    estadolbl = Label(topVehiculo,text='Estado: '+estado,font=('Arial', 12,BOLD),bg='gray')
    estadolbl.place(x=40,y=20)
    
    
    fechaSalida = StringVar()
    fechaLlegada = StringVar()
    titularTarjeta = StringVar()
    numTarjeta = StringVar()
    expiTarjeta = StringVar()
    cvv = StringVar()
    sucursalSeleccionada = StringVar()
    
        
    fechaSalidalbl = Label(topVehiculo,text='Fecha de salida (dd/mm/yyyy): ',bg='gray')
    fechaSalidalbl.place(x=40,y=250) 
    fSalida = Entry(topVehiculo,font=('Arial', 11),textvariable=fechaSalida,bd=2)
    fSalida.place(x=220,y=250)
    
    fechaLlegadalbl = Label(topVehiculo,text='Fecha de llegada (dd/mm/yyyy): ',bg='gray')
    fechaLlegadalbl.place(x=40,y=300) 
    fLlegada = Entry(topVehiculo,font=('Arial', 11),textvariable=fechaLlegada,bd=2)
    fLlegada.place(x=220,y=300)   
    
    titularTarjetalbl = Label(topVehiculo,text='Titular de la tarjeta: ',bg='gray')
    titularTarjetalbl.place(x=98,y=350) 
    titularTarjetaEny = Entry(topVehiculo,font=('Arial', 11),textvariable=titularTarjeta,bd=2)
    titularTarjetaEny.place(x=220,y=350)
    
    numTarjetalbl = Label(topVehiculo,text='Numero de tarjeta: ',bg='gray')
    numTarjetalbl.place(x=98,y=400) 
    numTarjetaEny = Entry(topVehiculo,font=('Arial', 11),textvariable=numTarjeta,bd=2)
    numTarjetaEny.place(x=220,y=400)
    
    expiTarjetalbl = Label(topVehiculo,text='Fecha de expiracion (mm/yy): ',bg='gray')
    expiTarjetalbl.place(x=40,y=450) 
    expiTarjetaEny = Entry(topVehiculo,font=('Arial', 11),textvariable=expiTarjeta,bd=2)
    expiTarjetaEny.place(x=220,y=450)
    
    cvvlbl = Label(topVehiculo,text='CVV: ',bg='gray')
    cvvlbl.place(x=174,y=500) 
    cvvEny = Entry(topVehiculo,font=('Arial', 11),textvariable=cvv,bd=2)
    cvvEny.place(x=220,y=500)
    
    
    def rentar ():
        if disponibilidad == True:
            if not (fechaSalida.get() and fechaLlegada.get() and titularTarjeta.get() and numTarjeta.get() and expiTarjeta.get() and cvv.get()):
                messagebox.showerror("Error", "Todos los campos son obligatorios")
                return  
            else: 
                if sucursalSeleccionada.get() == 'Seleccione una sucursal':
                    messagebox.showerror("Error", "Por favor seleccione una sucursal")
                    return
                else:
                    # Validación de que CVV sea un número
                    try:
                        cvv_value = int(cvv.get())  # Intenta convertir el CVV a un entero
                
                        vehiculoNom = 'Kugoo G-Booster'
            
                        txt = f'Transaccion exitosa. Usted rento un {vehiculoNom} del {fechaSalida.get()} al {fechaLlegada.get()}. Favor de recoger el vehiculo en la sucursal {sucursalSeleccionada.get()}'
                        messagebox.showinfo("Transaccion exitosa", txt)
                    except ValueError:
                        messagebox.showerror("Error", "El CVV debe contener solo números")
                        return
        else:
            messagebox.showerror("Error", "No puede rentar ahora porque el coche no esta disponible. Por favor haga una reservación.")
        
    def reservar ():
        if not (fechaSalida.get() and fechaLlegada.get() and titularTarjeta.get() and numTarjeta.get() and expiTarjeta.get() and cvv.get()):
                messagebox.showerror("Error", "Todos los campos son obligatorios")
                return  
        else: 
            if sucursalSeleccionada.get() == 'Seleccione una sucursal':
                messagebox.showerror("Error", "Por favor seleccione una sucursal")
                return
            else:
                # Validación de que CVV sea un número
                try:
                    cvv_value = int(cvv.get())  # Intenta convertir el CVV a un entero
                
                    vehiculoNom = 'Kugoo G-Booster'
            
                    txt = f'Transaccion exitosa. Usted rento un {vehiculoNom} del {fechaSalida.get()} al {fechaLlegada.get()}. Favor de recoger el vehiculo en la sucursal {sucursalSeleccionada.get()}'
                    messagebox.showinfo("Transaccion exitosa", txt)
                except ValueError:
                    messagebox.showerror("Error", "El CVV debe contener solo números")
                    return
    
    rentarbnt = Button(topVehiculo,text='  Rentar  ',font=('Arial',10),command=rentar,bg='pink')
    rentarbnt.place(x=100,y=550)
    
    reservarbnt = Button(topVehiculo,text='  Reservar  ',font=('Arial',10),bg='pink',command=reservar)
    reservarbnt.place(x=250,y=550)
    
    fNODisponibleslbl = Label(topVehiculo,text='Fechas NO disponibles:',font=('Arial',12))
    fNODisponibleslbl.place(x=430,y=250)
    
    fndLbx = Listbox(topVehiculo,width=24,font=('Arial',10))
    fndLbx.insert(0,'13/12/2024 - 26/12/2024')
    fndLbx.insert(1,'03/01/2025 - 07/01/2025')
    fndLbx.place(x=430,y=285)
    
    sucursalSbx = Spinbox(topVehiculo,font=('Arial',12),values=('Seleccione una sucursal','Zapopan','Guadalajara','Tonala'), textvariable=sucursalSeleccionada)
    sucursalSbx.place(x=430,y=490)
    
    topVehiculo.mainloop()
    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def infoPanelSc5():
    topVehiculo = Toplevel()
    topVehiculo.title('Electric Scooter Information')
    topVehiculo.iconbitmap('./images/CarIcon.ico')
    topVehiculo.geometry('650x600')
    topVehiculo.config(bg='gray')
    utl.center_window(topVehiculo,650,600)
    topVehiculo.resizable(width=False, height=False)
    
    # Leer y cargar la imagen
    vehiculo = utl.read_Image('./images/scooter/MiElectricScooterPro2.png',(200, 170))
    
    vehiculolbl = Label(topVehiculo, image=vehiculo, bd=0)
    vehiculolbl.place(x=40, y=55)  
    
    txtVehiculo1 = 'Mi Electric Pro 2\nVelocidad máx: 25 km/h\nPeso máx: 100 kg\nTamaño: 1130x430x1180 mm\nPeso: 14.2 kg\nTiempo de carga: 9 hrs\nPlegable: Sí\nVoltaje: 36 V\nSeguro: Sí\n$8 dls /hora'
    infoVehiculo = Label(topVehiculo,wraplength=800,text=txtVehiculo1,font=('Arial', 12),anchor='w',justify='left',bg='white')
    infoVehiculo.place(x=270,y=40)
    
    disponibilidad = False
    
    if disponibilidad == True:
        estado = 'DISPONIBLE'
    else:
        estado = 'NO DISPONIBLE'
    
    estadolbl = Label(topVehiculo,text='Estado: '+estado,font=('Arial', 12,BOLD),bg='gray')
    estadolbl.place(x=40,y=20)
    
    
    fechaSalida = StringVar()
    fechaLlegada = StringVar()
    titularTarjeta = StringVar()
    numTarjeta = StringVar()
    expiTarjeta = StringVar()
    cvv = StringVar()
    sucursalSeleccionada = StringVar()
    
        
    fechaSalidalbl = Label(topVehiculo,text='Fecha de salida (dd/mm/yyyy): ',bg='gray')
    fechaSalidalbl.place(x=40,y=250) 
    fSalida = Entry(topVehiculo,font=('Arial', 11),textvariable=fechaSalida,bd=2)
    fSalida.place(x=220,y=250)
    
    fechaLlegadalbl = Label(topVehiculo,text='Fecha de llegada (dd/mm/yyyy): ',bg='gray')
    fechaLlegadalbl.place(x=40,y=300) 
    fLlegada = Entry(topVehiculo,font=('Arial', 11),textvariable=fechaLlegada,bd=2)
    fLlegada.place(x=220,y=300)   
    
    titularTarjetalbl = Label(topVehiculo,text='Titular de la tarjeta: ',bg='gray')
    titularTarjetalbl.place(x=98,y=350) 
    titularTarjetaEny = Entry(topVehiculo,font=('Arial', 11),textvariable=titularTarjeta,bd=2)
    titularTarjetaEny.place(x=220,y=350)
    
    numTarjetalbl = Label(topVehiculo,text='Numero de tarjeta: ',bg='gray')
    numTarjetalbl.place(x=98,y=400) 
    numTarjetaEny = Entry(topVehiculo,font=('Arial', 11),textvariable=numTarjeta,bd=2)
    numTarjetaEny.place(x=220,y=400)
    
    expiTarjetalbl = Label(topVehiculo,text='Fecha de expiracion (mm/yy): ',bg='gray')
    expiTarjetalbl.place(x=40,y=450) 
    expiTarjetaEny = Entry(topVehiculo,font=('Arial', 11),textvariable=expiTarjeta,bd=2)
    expiTarjetaEny.place(x=220,y=450)
    
    cvvlbl = Label(topVehiculo,text='CVV: ',bg='gray')
    cvvlbl.place(x=174,y=500) 
    cvvEny = Entry(topVehiculo,font=('Arial', 11),textvariable=cvv,bd=2)
    cvvEny.place(x=220,y=500)
    
    
    def rentar ():
        if disponibilidad == True:
            if not (fechaSalida.get() and fechaLlegada.get() and titularTarjeta.get() and numTarjeta.get() and expiTarjeta.get() and cvv.get()):
                messagebox.showerror("Error", "Todos los campos son obligatorios")
                return  
            else: 
                if sucursalSeleccionada.get() == 'Seleccione una sucursal':
                    messagebox.showerror("Error", "Por favor seleccione una sucursal")
                    return
                else:
                    # Validación de que CVV sea un número
                    try:
                        cvv_value = int(cvv.get())  # Intenta convertir el CVV a un entero
                
                        vehiculoNom = 'Mi Electric Pro 2'
            
                        txt = f'Transaccion exitosa. Usted rento un {vehiculoNom} del {fechaSalida.get()} al {fechaLlegada.get()}. Favor de recoger el vehiculo en la sucursal {sucursalSeleccionada.get()}'
                        messagebox.showinfo("Transaccion exitosa", txt)
                    except ValueError:
                        messagebox.showerror("Error", "El CVV debe contener solo números")
                        return
        else:
            messagebox.showerror("Error", "No puede rentar ahora porque el coche no esta disponible. Por favor haga una reservación.")
        
    def reservar ():
        if not (fechaSalida.get() and fechaLlegada.get() and titularTarjeta.get() and numTarjeta.get() and expiTarjeta.get() and cvv.get()):
                messagebox.showerror("Error", "Todos los campos son obligatorios")
                return  
        else: 
            if sucursalSeleccionada.get() == 'Seleccione una sucursal':
                messagebox.showerror("Error", "Por favor seleccione una sucursal")
                return
            else:
                # Validación de que CVV sea un número
                try:
                    cvv_value = int(cvv.get())  # Intenta convertir el CVV a un entero
                
                    vehiculoNom = 'Mi Electric Pro 2'
            
                    txt = f'Transaccion exitosa. Usted rento un {vehiculoNom} del {fechaSalida.get()} al {fechaLlegada.get()}. Favor de recoger el vehiculo en la sucursal {sucursalSeleccionada.get()}'
                    messagebox.showinfo("Transaccion exitosa", txt)
                except ValueError:
                    messagebox.showerror("Error", "El CVV debe contener solo números")
                    return
    
    rentarbnt = Button(topVehiculo,text='  Rentar  ',font=('Arial',10),command=rentar,bg='pink')
    rentarbnt.place(x=100,y=550)
    
    reservarbnt = Button(topVehiculo,text='  Reservar  ',font=('Arial',10),bg='pink',command=reservar)
    reservarbnt.place(x=250,y=550)
    
    fNODisponibleslbl = Label(topVehiculo,text='Fechas NO disponibles:',font=('Arial',12))
    fNODisponibleslbl.place(x=430,y=250)
    
    fndLbx = Listbox(topVehiculo,width=24,font=('Arial',10))
    fndLbx.insert(0,'13/12/2024 - 26/12/2024')
    fndLbx.insert(1,'03/01/2025 - 07/01/2025')
    fndLbx.place(x=430,y=285)
    
    sucursalSbx = Spinbox(topVehiculo,font=('Arial',12),values=('Seleccione una sucursal','Zapopan','Guadalajara','Tonala'), textvariable=sucursalSeleccionada)
    sucursalSbx.place(x=430,y=490)
    
    topVehiculo.mainloop()
    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def infoPanelSc6():
    topVehiculo = Toplevel()
    topVehiculo.title('Electric Scooter Information')
    topVehiculo.iconbitmap('./images/CarIcon.ico')
    topVehiculo.geometry('650x600')
    topVehiculo.config(bg='gray')
    utl.center_window(topVehiculo,650,600)
    topVehiculo.resizable(width=False, height=False)
    
    # Leer y cargar la imagen
    vehiculo = utl.read_Image('./images/scooter/NinebotKickScooterMAXG30.png',(200, 170))
    
    vehiculolbl = Label(topVehiculo, image=vehiculo, bd=0)
    vehiculolbl.place(x=40, y=55)  
    
    txtVehiculo1 = 'Segway Ninebot KickScooter\nMAX G30\nVelocidad máx: 25 km/h\nPeso máx: 100 kg\nTamaño: 1167x472x1203 mm\nPeso: 18.7 kg\nTiempo de carga: 6 hrs\nPlegable: Sí\nVoltaje: 36 V\nSeguro: Sí\n$10 dls /hora'
    infoVehiculo = Label(topVehiculo,wraplength=800,text=txtVehiculo1,font=('Arial', 12),anchor='w',justify='left',bg='white')
    infoVehiculo.place(x=270,y=40)
    
    disponibilidad = False
    
    if disponibilidad == True:
        estado = 'DISPONIBLE'
    else:
        estado = 'NO DISPONIBLE'
    
    estadolbl = Label(topVehiculo,text='Estado: '+estado,font=('Arial', 12,BOLD),bg='gray')
    estadolbl.place(x=40,y=20)
    
    
    fechaSalida = StringVar()
    fechaLlegada = StringVar()
    titularTarjeta = StringVar()
    numTarjeta = StringVar()
    expiTarjeta = StringVar()
    cvv = StringVar()
    sucursalSeleccionada = StringVar()
    
        
    fechaSalidalbl = Label(topVehiculo,text='Fecha de salida (dd/mm/yyyy): ',bg='gray')
    fechaSalidalbl.place(x=40,y=250) 
    fSalida = Entry(topVehiculo,font=('Arial', 11),textvariable=fechaSalida,bd=2)
    fSalida.place(x=220,y=250)
    
    fechaLlegadalbl = Label(topVehiculo,text='Fecha de llegada (dd/mm/yyyy): ',bg='gray')
    fechaLlegadalbl.place(x=40,y=300) 
    fLlegada = Entry(topVehiculo,font=('Arial', 11),textvariable=fechaLlegada,bd=2)
    fLlegada.place(x=220,y=300)   
    
    titularTarjetalbl = Label(topVehiculo,text='Titular de la tarjeta: ',bg='gray')
    titularTarjetalbl.place(x=98,y=350) 
    titularTarjetaEny = Entry(topVehiculo,font=('Arial', 11),textvariable=titularTarjeta,bd=2)
    titularTarjetaEny.place(x=220,y=350)
    
    numTarjetalbl = Label(topVehiculo,text='Numero de tarjeta: ',bg='gray')
    numTarjetalbl.place(x=98,y=400) 
    numTarjetaEny = Entry(topVehiculo,font=('Arial', 11),textvariable=numTarjeta,bd=2)
    numTarjetaEny.place(x=220,y=400)
    
    expiTarjetalbl = Label(topVehiculo,text='Fecha de expiracion (mm/yy): ',bg='gray')
    expiTarjetalbl.place(x=40,y=450) 
    expiTarjetaEny = Entry(topVehiculo,font=('Arial', 11),textvariable=expiTarjeta,bd=2)
    expiTarjetaEny.place(x=220,y=450)
    
    cvvlbl = Label(topVehiculo,text='CVV: ',bg='gray')
    cvvlbl.place(x=174,y=500) 
    cvvEny = Entry(topVehiculo,font=('Arial', 11),textvariable=cvv,bd=2)
    cvvEny.place(x=220,y=500)
    
    
    def rentar ():
        if disponibilidad == True:
            if not (fechaSalida.get() and fechaLlegada.get() and titularTarjeta.get() and numTarjeta.get() and expiTarjeta.get() and cvv.get()):
                messagebox.showerror("Error", "Todos los campos son obligatorios")
                return  
            else: 
                if sucursalSeleccionada.get() == 'Seleccione una sucursal':
                    messagebox.showerror("Error", "Por favor seleccione una sucursal")
                    return
                else:
                    # Validación de que CVV sea un número
                    try:
                        cvv_value = int(cvv.get())  # Intenta convertir el CVV a un entero
                
                        vehiculoNom = 'Segway Ninebot KickScooter MAX G30'
            
                        txt = f'Transaccion exitosa. Usted rento un {vehiculoNom} del {fechaSalida.get()} al {fechaLlegada.get()}. Favor de recoger el vehiculo en la sucursal {sucursalSeleccionada.get()}'
                        messagebox.showinfo("Transaccion exitosa", txt)
                    except ValueError:
                        messagebox.showerror("Error", "El CVV debe contener solo números")
                        return
        else:
            messagebox.showerror("Error", "No puede rentar ahora porque el coche no esta disponible. Por favor haga una reservación.")
        
    def reservar ():
        if not (fechaSalida.get() and fechaLlegada.get() and titularTarjeta.get() and numTarjeta.get() and expiTarjeta.get() and cvv.get()):
                messagebox.showerror("Error", "Todos los campos son obligatorios")
                return  
        else: 
            if sucursalSeleccionada.get() == 'Seleccione una sucursal':
                messagebox.showerror("Error", "Por favor seleccione una sucursal")
                return
            else:
                # Validación de que CVV sea un número
                try:
                    cvv_value = int(cvv.get())  # Intenta convertir el CVV a un entero
                
                    vehiculoNom = 'Segway Ninebot KickScooter MAX G30'
            
                    txt = f'Transaccion exitosa. Usted rento un {vehiculoNom} del {fechaSalida.get()} al {fechaLlegada.get()}. Favor de recoger el vehiculo en la sucursal {sucursalSeleccionada.get()}'
                    messagebox.showinfo("Transaccion exitosa", txt)
                except ValueError:
                    messagebox.showerror("Error", "El CVV debe contener solo números")
                    return
    
    rentarbnt = Button(topVehiculo,text='  Rentar  ',font=('Arial',10),command=rentar,bg='pink')
    rentarbnt.place(x=100,y=550)
    
    reservarbnt = Button(topVehiculo,text='  Reservar  ',font=('Arial',10),bg='pink',command=reservar)
    reservarbnt.place(x=250,y=550)
    
    fNODisponibleslbl = Label(topVehiculo,text='Fechas NO disponibles:',font=('Arial',12))
    fNODisponibleslbl.place(x=430,y=250)
    
    fndLbx = Listbox(topVehiculo,width=24,font=('Arial',10))
    fndLbx.insert(0,'13/12/2024 - 26/12/2024')
    fndLbx.insert(1,'03/01/2025 - 07/01/2025')
    fndLbx.place(x=430,y=285)
    
    sucursalSbx = Spinbox(topVehiculo,font=('Arial',12),values=('Seleccione una sucursal','Zapopan','Guadalajara','Tonala'), textvariable=sucursalSeleccionada)
    sucursalSbx.place(x=430,y=490)
    
    topVehiculo.mainloop()
    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def infoPanelSc7():
    topVehiculo = Toplevel()
    topVehiculo.title('Electric Scooter Information')
    topVehiculo.iconbitmap('./images/CarIcon.ico')
    topVehiculo.geometry('650x600')
    topVehiculo.config(bg='gray')
    utl.center_window(topVehiculo,650,600)
    topVehiculo.resizable(width=False, height=False)
    
    # Leer y cargar la imagen
    vehiculo = utl.read_Image('./images/scooter/OXSuper.png',(200, 170))
    
    vehiculolbl = Label(topVehiculo, image=vehiculo, bd=0)
    vehiculolbl.place(x=40, y=55)  
    
    txtVehiculo1 = 'Inokim OX Super\nVelocidad máx: 45 km/h\nPeso máx: 120 kg\nTamaño: 1200x600x1300 mm\nPeso: 28 kg\nTiempo de carga: 8 hrs\nPlegable: Sí\nVoltaje: 60 V\nSeguro: Sí\n$13 dls /hora'
    infoVehiculo = Label(topVehiculo,wraplength=800,text=txtVehiculo1,font=('Arial', 12),anchor='w',justify='left',bg='white')
    infoVehiculo.place(x=270,y=40)
    
    disponibilidad = False
    
    if disponibilidad == True:
        estado = 'DISPONIBLE'
    else:
        estado = 'NO DISPONIBLE'
    
    estadolbl = Label(topVehiculo,text='Estado: '+estado,font=('Arial', 12,BOLD),bg='gray')
    estadolbl.place(x=40,y=20)
    
    
    fechaSalida = StringVar()
    fechaLlegada = StringVar()
    titularTarjeta = StringVar()
    numTarjeta = StringVar()
    expiTarjeta = StringVar()
    cvv = StringVar()
    sucursalSeleccionada = StringVar()
    
        
    fechaSalidalbl = Label(topVehiculo,text='Fecha de salida (dd/mm/yyyy): ',bg='gray')
    fechaSalidalbl.place(x=40,y=250) 
    fSalida = Entry(topVehiculo,font=('Arial', 11),textvariable=fechaSalida,bd=2)
    fSalida.place(x=220,y=250)
    
    fechaLlegadalbl = Label(topVehiculo,text='Fecha de llegada (dd/mm/yyyy): ',bg='gray')
    fechaLlegadalbl.place(x=40,y=300) 
    fLlegada = Entry(topVehiculo,font=('Arial', 11),textvariable=fechaLlegada,bd=2)
    fLlegada.place(x=220,y=300)   
    
    titularTarjetalbl = Label(topVehiculo,text='Titular de la tarjeta: ',bg='gray')
    titularTarjetalbl.place(x=98,y=350) 
    titularTarjetaEny = Entry(topVehiculo,font=('Arial', 11),textvariable=titularTarjeta,bd=2)
    titularTarjetaEny.place(x=220,y=350)
    
    numTarjetalbl = Label(topVehiculo,text='Numero de tarjeta: ',bg='gray')
    numTarjetalbl.place(x=98,y=400) 
    numTarjetaEny = Entry(topVehiculo,font=('Arial', 11),textvariable=numTarjeta,bd=2)
    numTarjetaEny.place(x=220,y=400)
    
    expiTarjetalbl = Label(topVehiculo,text='Fecha de expiracion (mm/yy): ',bg='gray')
    expiTarjetalbl.place(x=40,y=450) 
    expiTarjetaEny = Entry(topVehiculo,font=('Arial', 11),textvariable=expiTarjeta,bd=2)
    expiTarjetaEny.place(x=220,y=450)
    
    cvvlbl = Label(topVehiculo,text='CVV: ',bg='gray')
    cvvlbl.place(x=174,y=500) 
    cvvEny = Entry(topVehiculo,font=('Arial', 11),textvariable=cvv,bd=2)
    cvvEny.place(x=220,y=500)
    
    
    def rentar ():
        if disponibilidad == True:
            if not (fechaSalida.get() and fechaLlegada.get() and titularTarjeta.get() and numTarjeta.get() and expiTarjeta.get() and cvv.get()):
                messagebox.showerror("Error", "Todos los campos son obligatorios")
                return  
            else: 
                if sucursalSeleccionada.get() == 'Seleccione una sucursal':
                    messagebox.showerror("Error", "Por favor seleccione una sucursal")
                    return
                else:
                    # Validación de que CVV sea un número
                    try:
                        cvv_value = int(cvv.get())  # Intenta convertir el CVV a un entero
                
                        vehiculoNom = 'Inokim OX Super'
            
                        txt = f'Transaccion exitosa. Usted rento un {vehiculoNom} del {fechaSalida.get()} al {fechaLlegada.get()}. Favor de recoger el vehiculo en la sucursal {sucursalSeleccionada.get()}'
                        messagebox.showinfo("Transaccion exitosa", txt)
                    except ValueError:
                        messagebox.showerror("Error", "El CVV debe contener solo números")
                        return
        else:
            messagebox.showerror("Error", "No puede rentar ahora porque el coche no esta disponible. Por favor haga una reservación.")
        
    def reservar ():
        if not (fechaSalida.get() and fechaLlegada.get() and titularTarjeta.get() and numTarjeta.get() and expiTarjeta.get() and cvv.get()):
                messagebox.showerror("Error", "Todos los campos son obligatorios")
                return  
        else: 
            if sucursalSeleccionada.get() == 'Seleccione una sucursal':
                messagebox.showerror("Error", "Por favor seleccione una sucursal")
                return
            else:
                # Validación de que CVV sea un número
                try:
                    cvv_value = int(cvv.get())  # Intenta convertir el CVV a un entero
                
                    vehiculoNom = 'TInokim OX Super'
            
                    txt = f'Transaccion exitosa. Usted rento un {vehiculoNom} del {fechaSalida.get()} al {fechaLlegada.get()}. Favor de recoger el vehiculo en la sucursal {sucursalSeleccionada.get()}'
                    messagebox.showinfo("Transaccion exitosa", txt)
                except ValueError:
                    messagebox.showerror("Error", "El CVV debe contener solo números")
                    return
    
    rentarbnt = Button(topVehiculo,text='  Rentar  ',font=('Arial',10),command=rentar,bg='pink')
    rentarbnt.place(x=100,y=550)
    
    reservarbnt = Button(topVehiculo,text='  Reservar  ',font=('Arial',10),bg='pink',command=reservar)
    reservarbnt.place(x=250,y=550)
    
    fNODisponibleslbl = Label(topVehiculo,text='Fechas NO disponibles:',font=('Arial',12))
    fNODisponibleslbl.place(x=430,y=250)
    
    fndLbx = Listbox(topVehiculo,width=24,font=('Arial',10))
    fndLbx.insert(0,'13/12/2024 - 26/12/2024')
    fndLbx.insert(1,'03/01/2025 - 07/01/2025')
    fndLbx.place(x=430,y=285)
    
    sucursalSbx = Spinbox(topVehiculo,font=('Arial',12),values=('Seleccione una sucursal','Zapopan','Guadalajara','Tonala'), textvariable=sucursalSeleccionada)
    sucursalSbx.place(x=430,y=490)
    
    topVehiculo.mainloop()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def infoPanelSc8():
    topVehiculo = Toplevel()
    topVehiculo.title('Electric Scooter Information')
    topVehiculo.iconbitmap('./images/CarIcon.ico')
    topVehiculo.geometry('650x600')
    topVehiculo.config(bg='gray')
    utl.center_window(topVehiculo,650,600)
    topVehiculo.resizable(width=False, height=False)
    
    # Leer y cargar la imagen
    vehiculo = utl.read_Image('./images/scooter/S2Pro.png',(200, 170))
    
    vehiculolbl = Label(topVehiculo, image=vehiculo, bd=0)
    vehiculolbl.place(x=40, y=55)  
    
    txtVehiculo1 = 'Hiboy S2 Pro\nVelocidad máx: 30 km/h\nPeso máx: 120 kg\nTamaño: 1180x480x1190 mm\nPeso: 16.5 kg\nTiempo de carga: 6 hrs\nPlegable: Sí\nVoltaje: 36 V\nSeguro: Sí\n$9 dls /hora'
    infoVehiculo = Label(topVehiculo,wraplength=800,text=txtVehiculo1,font=('Arial', 12),anchor='w',justify='left',bg='white')
    infoVehiculo.place(x=270,y=40)
    
    disponibilidad = False
    
    if disponibilidad == True:
        estado = 'DISPONIBLE'
    else:
        estado = 'NO DISPONIBLE'
    
    estadolbl = Label(topVehiculo,text='Estado: '+estado,font=('Arial', 12,BOLD),bg='gray')
    estadolbl.place(x=40,y=20)
    
    
    fechaSalida = StringVar()
    fechaLlegada = StringVar()
    titularTarjeta = StringVar()
    numTarjeta = StringVar()
    expiTarjeta = StringVar()
    cvv = StringVar()
    sucursalSeleccionada = StringVar()
    
        
    fechaSalidalbl = Label(topVehiculo,text='Fecha de salida (dd/mm/yyyy): ',bg='gray')
    fechaSalidalbl.place(x=40,y=250) 
    fSalida = Entry(topVehiculo,font=('Arial', 11),textvariable=fechaSalida,bd=2)
    fSalida.place(x=220,y=250)
    
    fechaLlegadalbl = Label(topVehiculo,text='Fecha de llegada (dd/mm/yyyy): ',bg='gray')
    fechaLlegadalbl.place(x=40,y=300) 
    fLlegada = Entry(topVehiculo,font=('Arial', 11),textvariable=fechaLlegada,bd=2)
    fLlegada.place(x=220,y=300)   
    
    titularTarjetalbl = Label(topVehiculo,text='Titular de la tarjeta: ',bg='gray')
    titularTarjetalbl.place(x=98,y=350) 
    titularTarjetaEny = Entry(topVehiculo,font=('Arial', 11),textvariable=titularTarjeta,bd=2)
    titularTarjetaEny.place(x=220,y=350)
    
    numTarjetalbl = Label(topVehiculo,text='Numero de tarjeta: ',bg='gray')
    numTarjetalbl.place(x=98,y=400) 
    numTarjetaEny = Entry(topVehiculo,font=('Arial', 11),textvariable=numTarjeta,bd=2)
    numTarjetaEny.place(x=220,y=400)
    
    expiTarjetalbl = Label(topVehiculo,text='Fecha de expiracion (mm/yy): ',bg='gray')
    expiTarjetalbl.place(x=40,y=450) 
    expiTarjetaEny = Entry(topVehiculo,font=('Arial', 11),textvariable=expiTarjeta,bd=2)
    expiTarjetaEny.place(x=220,y=450)
    
    cvvlbl = Label(topVehiculo,text='CVV: ',bg='gray')
    cvvlbl.place(x=174,y=500) 
    cvvEny = Entry(topVehiculo,font=('Arial', 11),textvariable=cvv,bd=2)
    cvvEny.place(x=220,y=500)
    
    
    def rentar ():
        if disponibilidad == True:
            if not (fechaSalida.get() and fechaLlegada.get() and titularTarjeta.get() and numTarjeta.get() and expiTarjeta.get() and cvv.get()):
                messagebox.showerror("Error", "Todos los campos son obligatorios")
                return  
            else: 
                if sucursalSeleccionada.get() == 'Seleccione una sucursal':
                    messagebox.showerror("Error", "Por favor seleccione una sucursal")
                    return
                else:
                    # Validación de que CVV sea un número
                    try:
                        cvv_value = int(cvv.get())  # Intenta convertir el CVV a un entero
                
                        vehiculoNom = 'Hiboy S2 Pro'
            
                        txt = f'Transaccion exitosa. Usted rento un {vehiculoNom} del {fechaSalida.get()} al {fechaLlegada.get()}. Favor de recoger el vehiculo en la sucursal {sucursalSeleccionada.get()}'
                        messagebox.showinfo("Transaccion exitosa", txt)
                    except ValueError:
                        messagebox.showerror("Error", "El CVV debe contener solo números")
                        return
        else:
            messagebox.showerror("Error", "No puede rentar ahora porque el coche no esta disponible. Por favor haga una reservación.")
        
    def reservar ():
        if not (fechaSalida.get() and fechaLlegada.get() and titularTarjeta.get() and numTarjeta.get() and expiTarjeta.get() and cvv.get()):
                messagebox.showerror("Error", "Todos los campos son obligatorios")
                return  
        else: 
            if sucursalSeleccionada.get() == 'Seleccione una sucursal':
                messagebox.showerror("Error", "Por favor seleccione una sucursal")
                return
            else:
                # Validación de que CVV sea un número
                try:
                    cvv_value = int(cvv.get())  # Intenta convertir el CVV a un entero
                
                    vehiculoNom = 'Hiboy S2 Pro'
            
                    txt = f'Transaccion exitosa. Usted rento un {vehiculoNom} del {fechaSalida.get()} al {fechaLlegada.get()}. Favor de recoger el vehiculo en la sucursal {sucursalSeleccionada.get()}'
                    messagebox.showinfo("Transaccion exitosa", txt)
                except ValueError:
                    messagebox.showerror("Error", "El CVV debe contener solo números")
                    return
    
    rentarbnt = Button(topVehiculo,text='  Rentar  ',font=('Arial',10),command=rentar,bg='pink')
    rentarbnt.place(x=100,y=550)
    
    reservarbnt = Button(topVehiculo,text='  Reservar  ',font=('Arial',10),bg='pink',command=reservar)
    reservarbnt.place(x=250,y=550)
    
    fNODisponibleslbl = Label(topVehiculo,text='Fechas NO disponibles:',font=('Arial',12))
    fNODisponibleslbl.place(x=430,y=250)
    
    fndLbx = Listbox(topVehiculo,width=24,font=('Arial',10))
    fndLbx.insert(0,'13/12/2024 - 26/12/2024')
    fndLbx.insert(1,'03/01/2025 - 07/01/2025')
    fndLbx.place(x=430,y=285)
    
    sucursalSbx = Spinbox(topVehiculo,font=('Arial',12),values=('Seleccione una sucursal','Zapopan','Guadalajara','Tonala'), textvariable=sucursalSeleccionada)
    sucursalSbx.place(x=430,y=490)
    
    topVehiculo.mainloop()