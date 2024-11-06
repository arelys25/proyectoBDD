import tkinter as tk
from tkinter.font import BOLD
import util.generic as utl
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tktooltip import ToolTip

def infoPanelCar1 ():
    topVehiculo = Toplevel()
    topVehiculo.title('Electric Cars Information')
    topVehiculo.iconbitmap('./images/CarIcon.ico')
    topVehiculo.geometry('650x600')
    topVehiculo.config(bg='gray')
    utl.center_window(topVehiculo,650,600)
    topVehiculo.resizable(width=False, height=False)
    
    # Leer y cargar la imagen
    vehiculo = utl.read_Image('./images/cars/ChevroletBoltEV.png', (200, 170))
    
    vehiculolbl = Label(topVehiculo, image=vehiculo, bd=0)
    vehiculolbl.place(x=40, y=55)  
    
    txtVehiculo1 = 'Chevrolet Bolt EV\nCapacidad: 5 personas\nMaletero: 381 lts\nAutonomia: 416 km\nPotencia: 200hp\nVelocidad máxima: 150km/h\nTiempo de carga: 9 hrs (cargador nivel 2),\n1 hora (carga rápida)\nSeguro: Sí\n$90 dls /day'
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
                
                        vehiculoNom = 'Chevrolet Bolt EV'
            
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
                
                    vehiculoNom = 'Chevrolet Bolt EV'
            
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
def infoPanelCar2():
    topVehiculo = Toplevel()
    topVehiculo.title('Electric Cars Information')
    topVehiculo.iconbitmap('./images/CarIcon.ico')
    topVehiculo.geometry('650x600')
    topVehiculo.config(bg='gray')
    utl.center_window(topVehiculo,650,600)
    topVehiculo.resizable(width=False, height=False)
    
    # Leer y cargar la imagen
    vehiculo = utl.read_Image('./images/cars/KiaSoulEV.png',(200, 170))
    
    vehiculolbl = Label(topVehiculo, image=vehiculo, bd=0)
    vehiculolbl.place(x=40, y=55)  
    
    txtVehiculo1 = 'KiaSoulEV\nCapacidad: 5 personas\nMaletero: 315 lts\nAutonomia: 383 km\nPotencia: 201 hp\nVelocidad máxima: 167 km/h\nTiempo de carga: 9 hrs (cargador nivel 2),\n1 hora (carga rápida)\nSeguro: Sí\n$65 dls /day'
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
                
                        vehiculoNom = 'Kia Soul EV'
            
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
                
                    vehiculoNom = 'Kia Soul EV'
            
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
def infoPanelCar3():
    topVehiculo = Toplevel()
    topVehiculo.title('Electric Cars Information')
    topVehiculo.iconbitmap('./images/CarIcon.ico')
    topVehiculo.geometry('650x600')
    topVehiculo.config(bg='gray')
    utl.center_window(topVehiculo,650,600)
    topVehiculo.resizable(width=False, height=False)
    
    # Leer y cargar la imagen
    vehiculo = utl.read_Image('./images/cars/MazdaMX-30.png',(200, 170))
    
    vehiculolbl = Label(topVehiculo, image=vehiculo, bd=0)
    vehiculolbl.place(x=40, y=55)  
    
    txtVehiculo1 = 'Mazda MX-30\nCapacidad: 5 personas\nMaletero: 366 lts\nAutonomia: 161 km\nPotencia: 143 hp\nVelocidad máxima: 140 km/h\nTiempo de carga: 5 hrs (cargador nivel 2),\n36 min (carga rápida)\nSeguro: Sí\n$120 dls /day'
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
                
                        vehiculoNom = 'Mazda MX-30'
            
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
                
                    vehiculoNom = 'Mazda MX-30'
            
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
def infoPanelCar4():
    topVehiculo = Toplevel()
    topVehiculo.title('Electric Cars Information')
    topVehiculo.iconbitmap('./images/CarIcon.ico')
    topVehiculo.geometry('650x600')
    topVehiculo.config(bg='gray')
    utl.center_window(topVehiculo,650,600)
    topVehiculo.resizable(width=False, height=False)
    
    # Leer y cargar la imagen
    vehiculo = utl.read_Image('./images/cars/NissanLeaf.png',(200, 170))
    
    vehiculolbl = Label(topVehiculo, image=vehiculo, bd=0)
    vehiculolbl.place(x=40, y=55)  
    
    txtVehiculo1 = 'Nissan Leaf\nCapacidad: 5 personas\nMaletero: 435 lts\nAutonomia: 240 km\nPotencia: 147 hp\nVelocidad máxima: 144 km/h\nTiempo de carga: 7.5 hrs (cargador nivel 2)\nSeguro: Sí\n$85 dls /day'
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
                
                        vehiculoNom = 'Nissan Leaf'
            
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
                
                    vehiculoNom = 'Nissan Leaf'
            
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
def infoPanelCar5():
    topVehiculo = Toplevel()
    topVehiculo.title('Electric Cars Information')
    topVehiculo.iconbitmap('./images/CarIcon.ico')
    topVehiculo.geometry('650x600')
    topVehiculo.config(bg='gray')
    utl.center_window(topVehiculo,650,600)
    topVehiculo.resizable(width=False, height=False)
    
    # Leer y cargar la imagen
    vehiculo = utl.read_Image('./images/cars/TeslaModel3LongRangeAWD.png',(200, 170))
    
    vehiculolbl = Label(topVehiculo, image=vehiculo, bd=0)
    vehiculolbl.place(x=40, y=55)  
    
    txtVehiculo1 = 'Tesla Model 3 Long Range AWD\nCapacidad: 5 personas\nMaletero: 425 lts\nAutonomia: 576 km\nPotencia: 346 hp\nVelocidad máxima: 233 km/h\nTiempo de carga: 8 hrs (cargador nivel 2),\n15 min (carga rápida)\nSeguro: Sí\n$130 dls /day'
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
                
                        vehiculoNom = 'Tesla Model 3 Long Range AWD'
            
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
                
                    vehiculoNom = 'Tesla Model 3 Long Range AWD'
            
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
def infoPanelCar6():
    topVehiculo = Toplevel()
    topVehiculo.title('Electric Cars Information')
    topVehiculo.iconbitmap('./images/CarIcon.ico')
    topVehiculo.geometry('650x600')
    topVehiculo.config(bg='gray')
    utl.center_window(topVehiculo,650,600)
    topVehiculo.resizable(width=False, height=False)
    
    # Leer y cargar la imagen
    vehiculo = utl.read_Image('./images/cars/VolkswagenID4.png',(200, 170))
    
    vehiculolbl = Label(topVehiculo, image=vehiculo, bd=0)
    vehiculolbl.place(x=40, y=55)  
    
    txtVehiculo1 = 'Volkswagen ID.4\nCapacidad: 5 personas\nMaletero: 543 lts\nAutonomia: 418 km\nPotencia: 201hp\nVelocidad máxima: 150km/h\nTiempo de carga: 7.5 hrs (cargador nivel 2),\n38 min (carga rápida)\nSeguro: Sí\n$125 dls /day'
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
                
                        vehiculoNom = 'Volkswagen ID.4'
            
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
                
                    vehiculoNom = 'Volkswagen ID.4'
            
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
def infoPanelCar7():
    topVehiculo = Toplevel()
    topVehiculo.title('Electric Cars Information')
    topVehiculo.iconbitmap('./images/CarIcon.ico')
    topVehiculo.geometry('650x600')
    topVehiculo.config(bg='gray')
    utl.center_window(topVehiculo,650,600)
    topVehiculo.resizable(width=False, height=False)
    
    # Leer y cargar la imagen
    vehiculo = utl.read_Image('./images/cars/TeslaModel3StandardRangePlus.png',(200, 170))
    
    vehiculolbl = Label(topVehiculo, image=vehiculo, bd=0)
    vehiculolbl.place(x=40, y=55)  
    
    txtVehiculo1 = 'Tesla Model 3 Standard Range Plus\nCapacidad: 5 personas\nMaletero: 425 lts\nAutonomia: 438 km\nPotencia: 283 hp\nVelocidad máxima: 225 km/h\nTiempo de carga: 9 hrs (cargador nivel 2),\n15 min (carga rápida)\nSeguro: Sí\n$128 dls /day'
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
                
                        vehiculoNom = 'Tesla Model 3 Standard Range Plus'
            
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
                
                    vehiculoNom = 'Tesla Model 3 Standard Range Plus'
            
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
def infoPanelCar8():
    topVehiculo = Toplevel()
    topVehiculo.title('Electric Cars Information')
    topVehiculo.iconbitmap('./images/CarIcon.ico')
    topVehiculo.geometry('650x600')
    topVehiculo.config(bg='gray')
    utl.center_window(topVehiculo,650,600)
    topVehiculo.resizable(width=False, height=False)
    
    # Leer y cargar la imagen
    vehiculo = utl.read_Image('./images/cars/RenaultZoe.png',(200, 170))
    
    vehiculolbl = Label(topVehiculo, image=vehiculo, bd=0)
    vehiculolbl.place(x=40, y=55)  
    
    txtVehiculo1 = 'Renault Zoe\nCapacidad: 5 personas\nMaletero: 338 lts\nAutonomia: 395 km\nPotencia: 135 hp\nVelocidad máxima: 140 km/h\nTiempo de carga: 8 hrs (cargador nivel 2),\n1 hora (carga rápida)\nSeguro: Sí\n$45 dls /day'
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
                
                        vehiculoNom = 'Renault Zoe'
            
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
                
                    vehiculoNom = 'Renault Zoe'
            
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