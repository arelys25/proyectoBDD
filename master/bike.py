import tkinter as tk
from tkinter.font import BOLD
import util.generic as utl
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tktooltip import ToolTip

def infoPanelBk1 ():
    topVehiculo = Toplevel()
    topVehiculo.title('Electric Bike Information')
    topVehiculo.iconbitmap('./images/CarIcon.ico')
    topVehiculo.geometry('650x600')
    topVehiculo.config(bg='gray')
    utl.center_window(topVehiculo,650,600)
    topVehiculo.resizable(width=False, height=False)
    
    # Leer y cargar la imagen
    vehiculo = utl.read_Image('./images/bikes/Allant7.png',(200, 170))
    
    vehiculolbl = Label(topVehiculo, image=vehiculo, bd=0)
    vehiculolbl.place(x=40, y=55)  
    
    txtVehiculo1 = 'Trek Allant+7\nVelocidad máx: 32 km/h\nPeso máx: 136 kg\nAccesorio: Portaequipaje\nPeso: 23.5 kg\nTiempo de carga: 5 hrs\nPlegable: No\nVoltaje: 36 V\nSeguro: Sí\n$16 dls /hora'
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
                
                        vehiculoNom = 'Trek Allant+7'
                        
                        total = 250
                    
                        ans = messagebox.askquestion('Transacción',f'Su cuenta sería un total de {total} dólares.')
                        if ans == 'yes':
                            txt = f'Transacción exitosa. Usted rento un {vehiculoNom} del {fechaSalida.get()} al {fechaLlegada.get()}. Favor de recoger el vehiculo en la sucursal {sucursalSeleccionada.get()} 1 hora antes de su partida.'
                            messagebox.showinfo("Transaccion exitosa", txt)
                            
                             # Añadir fechas al Listbox de fechas no disponibles
                            fndLbx.insert(END, f'{fechaSalida.get()} - {fechaLlegada.get()}')
                        
                            # Limpiar los campos para una nueva reserva
                            fechaSalida.set('')
                            fechaLlegada.set('')
                            titularTarjeta.set('')
                            numTarjeta.set('')
                            expiTarjeta.set('')
                            cvv.set('')
                            sucursalSeleccionada.set('Seleccione una sucursal')
                        else:
                            messagebox.showerror("Error", "Hubo un error en la transacción, por favor intente otra vez.")
                        
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
                
                    vehiculoNom = 'Trek Allant+7'
            
                    total = 250
                    
                    ans = messagebox.askquestion('Transacción',f'Su cuenta sería un total de {total} dólares.')
                    if ans == 'yes':
                        txt = f'Transacción exitosa. Usted rento un {vehiculoNom} del {fechaSalida.get()} al {fechaLlegada.get()}. Favor de recoger el vehiculo en la sucursal {sucursalSeleccionada.get()} 1 hora antes de su partida.'
                        messagebox.showinfo("Transaccion exitosa", txt)
                        
                        # Añadir fechas al Listbox de fechas no disponibles
                        fndLbx.insert(END, f'{fechaSalida.get()} - {fechaLlegada.get()}')
                        
                        # Limpiar los campos para una nueva reserva
                        fechaSalida.set('')
                        fechaLlegada.set('')
                        titularTarjeta.set('')
                        numTarjeta.set('')
                        expiTarjeta.set('')
                        cvv.set('')
                        sucursalSeleccionada.set('Seleccione una sucursal')
                    else:
                        messagebox.showerror("Error", "Hubo un error en la transacción, por favor intente otra vez.")
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
def infoPanelBk2():
    topVehiculo = Toplevel()
    topVehiculo.title('Electric Bike Information')
    topVehiculo.iconbitmap('./images/CarIcon.ico')
    topVehiculo.geometry('650x600')
    topVehiculo.config(bg='gray')
    utl.center_window(topVehiculo,650,600)
    topVehiculo.resizable(width=False, height=False)
    
    # Leer y cargar la imagen
    vehiculo = utl.read_Image('./images/bikes/D11.png',(200, 170))
    
    vehiculolbl = Label(topVehiculo, image=vehiculo, bd=0)
    vehiculolbl.place(x=40, y=55)  
    
    txtVehiculo1 = 'Fiido D11\nVelocidad máx: 25 km/h\nPeso máx: 120 kg\nAccesorio: Portaequipaje\nPeso: 12.9 kg\nTiempo de carga: 5 hrs\nPlegable: Sí\nVoltaje: 36 V\nSeguro: Sí\n$8 dls /hora'
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
                
                        vehiculoNom = 'Fiido D11'
            
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
                
                    vehiculoNom = 'Fiido D11'
            
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
def infoPanelBk3():
    topVehiculo = Toplevel()
    topVehiculo.title('Electric Bike Information')
    topVehiculo.iconbitmap('./images/CarIcon.ico')
    topVehiculo.geometry('650x600')
    topVehiculo.config(bg='gray')
    utl.center_window(topVehiculo,650,600)
    topVehiculo.resizable(width=False, height=False)
    
    # Leer y cargar la imagen
    vehiculo = utl.read_Image('./images/bikes/ElectricCLine.png',(200, 170))
    
    vehiculolbl = Label(topVehiculo, image=vehiculo, bd=0)
    vehiculolbl.place(x=40, y=55)  
    
    txtVehiculo1 = 'Brompton Electric C Line\nVelocidad máx: 25 km/h\nPeso máx: 105 kg\nAccesorio: Bolsa de transporte\nPeso: 13.7 kg\nTiempo de carga: 4 hrs\nPlegable: Sí\nVoltaje: 36 V\nSeguro: Sí\n$12 dls /hora'
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
                
                        vehiculoNom = 'Brompton Electric C Line'
            
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
                
                    vehiculoNom = 'Brompton Electric C Line'
            
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
def infoPanelBk4():
    topVehiculo = Toplevel()
    topVehiculo.title('Electric Bike Information')
    topVehiculo.iconbitmap('./images/CarIcon.ico')
    topVehiculo.geometry('650x600')
    topVehiculo.config(bg='gray')
    utl.center_window(topVehiculo,650,600)
    topVehiculo.resizable(width=False, height=False)
    
    # Leer y cargar la imagen
    vehiculo = utl.read_Image('./images/bikes/HimoC26.png',(200, 170))
    
    vehiculolbl = Label(topVehiculo, image=vehiculo, bd=0)
    vehiculolbl.place(x=40, y=55)  
    
    txtVehiculo1 = 'Xiaomi Himo C26\nVelocidad máx: 25 km/h\nPeso máx: 100 kg\nAccesorio: Pantalla LCD\nPeso: 25 kg\nTiempo de carga: 6 hrs\nPlegable: No\nVoltaje: 48 V\nSeguro: Sí\n$6 dls /hora'
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
                
                        vehiculoNom = 'Xiaomi Himo C26'
            
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
                
                    vehiculoNom = 'Xiaomi Himo C26'
            
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
def infoPanelBk5():
    topVehiculo = Toplevel()
    topVehiculo.title('Electric Bike Information')
    topVehiculo.iconbitmap('./images/CarIcon.ico')
    topVehiculo.geometry('650x600')
    topVehiculo.config(bg='gray')
    utl.center_window(topVehiculo,650,600)
    topVehiculo.resizable(width=False, height=False)
    
    # Leer y cargar la imagen
    vehiculo = utl.read_Image('./images/bikes/PowerPlus.png',(200, 170))
    
    vehiculolbl = Label(topVehiculo, image=vehiculo, bd=0)
    vehiculolbl.place(x=40, y=55)  
    
    txtVehiculo1 = 'Ancheer Power Plus\nVelocidad máx: 25 km/h\nPeso máx: 120 kg\nAccesorio: Guardabarros\nPeso: 23 kg\nTiempo de carga: 6 hrs\nPlegable: Sí\nVoltaje: 36 V\nSeguro: Sí\n$7 dls /hora'
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
                
                        vehiculoNom = 'Ancheer Power Plus'
            
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
                
                    vehiculoNom = 'Ancheer Power Plus'
            
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
def infoPanelBk6():
    topVehiculo = Toplevel()
    topVehiculo.title('Electric Bike Information')
    topVehiculo.iconbitmap('./images/CarIcon.ico')
    topVehiculo.geometry('650x600')
    topVehiculo.config(bg='gray')
    utl.center_window(topVehiculo,650,600)
    topVehiculo.resizable(width=False, height=False)
    
    # Leer y cargar la imagen
    vehiculo = utl.read_Image('./images/bikes/Supercharger2.png',(200, 170))
    
    vehiculolbl = Label(topVehiculo, image=vehiculo, bd=0)
    vehiculolbl.place(x=40, y=55)  
    
    txtVehiculo1 = 'Riese & Müller Supercharger2\nVelocidad máx: 45 km/h\nPeso máx: 140 kg\nAccesorio: Pantalla Bosch Kiox\nPeso: 28 kg\nTiempo de carga: 6 hrs\nPlegable: Sí\nVoltaje: 36 V\nSeguro: Sí\n$20 dls /hora'
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
                
                        vehiculoNom = 'Riese & Müller Supercharger2'
            
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
                
                    vehiculoNom = 'Riese & Müller Supercharger2'
            
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
def infoPanelBk7():
    topVehiculo = Toplevel()
    topVehiculo.title('Electric Bike Information')
    topVehiculo.iconbitmap('./images/CarIcon.ico')
    topVehiculo.geometry('650x600')
    topVehiculo.config(bg='gray')
    utl.center_window(topVehiculo,650,600)
    topVehiculo.resizable(width=False, height=False)
    
    # Leer y cargar la imagen
    vehiculo = utl.read_Image('./images/bikes/TurboVadoSL40.png',(200, 170))
    
    vehiculolbl = Label(topVehiculo, image=vehiculo, bd=0)
    vehiculolbl.place(x=40, y=55)  
    
    txtVehiculo1 = 'Specialized Turbo Vado SL 4.0\nVelocidad máx: 45 km/h\nPeso máx: 120 kg\nAccesorio: Portaequipaje\nPeso: 14.9 kg\nTiempo de carga: 3 hrs\nPlegable: No\nVoltaje: 36 V\nSeguro: Sí\n$15 dls /hora'
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
                
                        vehiculoNom = 'Specialized Turbo Vado SL 4.0'
            
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
                
                    vehiculoNom = 'Specialized Turbo Vado SL 4.0'
            
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
def infoPanelBk8():
    topVehiculo = Toplevel()
    topVehiculo.title('Electric Bike Information')
    topVehiculo.iconbitmap('./images/CarIcon.ico')
    topVehiculo.geometry('650x600')
    topVehiculo.config(bg='gray')
    utl.center_window(topVehiculo,650,600)
    topVehiculo.resizable(width=False, height=False)
    
    # Leer y cargar la imagen
    vehiculo = utl.read_Image('./images/bikes/VanMoofS3.png',(200, 170))
    
    vehiculolbl = Label(topVehiculo, image=vehiculo, bd=0)
    vehiculolbl.place(x=40, y=55)  
    
    txtVehiculo1 = 'VanMoof S3\nVelocidad máx: 32 km/h\nPeso máx: 120 kg\nAccesorio: Bloqueo inteligente\nPeso: 19 kg\nTiempo de carga: 4 hrs\nPlegable: No\nVoltaje: 36 V\nSeguro: Sí\n$14 dls /hora'
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
                
                        vehiculoNom = 'VanMoof S3'
            
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
                
                    vehiculoNom = 'HVanMoof S3'
            
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