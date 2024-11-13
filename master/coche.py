import tkinter as tk
from tkinter.font import BOLD
import util.generic as utl
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tktooltip import ToolTip
from db import operations
from datetime import datetime
import re

def getSucursalID (sucursal):
    if sucursal == 'Guadalajara':
        return 1
    elif sucursal == 'Zapopan':
        return 2
    elif sucursal == 'Tonala':
        return 3
    else:
        return False

def infoPanelCar1 ():
    topVehiculo = Toplevel()
    topVehiculo.title('Electric Cars Information')
    topVehiculo.iconbitmap('./images/CarIcon.ico')
    topVehiculo.geometry('700x650')
    topVehiculo.config(bg='gray')
    utl.center_window(topVehiculo,700,650)
    topVehiculo.resizable(width=False, height=False)
    
    vehiculo = utl.read_Image('./images/cars/ChevroletBoltEV.png', (200, 170))
    
    vehiculolbl = Label(topVehiculo, image=vehiculo, bd=0)
    vehiculolbl.place(x=40, y=55)  
    
    txtVehiculo1 = 'Chevrolet Bolt EV\nCapacidad: 5 personas\nMaletero: 381 lts\nAutonomia: 416 km\nPotencia: 200hp\nVelocidad máxima: 150km/h\nTiempo de carga: 9 hrs (cargador nivel 2),\n1 hora (carga rápida)\nSeguro: Sí\n$90 dls /day'
    infoVehiculo = Label(topVehiculo,wraplength=800,text=txtVehiculo1,font=('Arial', 12),anchor='w',justify='left',bg='gray',fg='#011736')
    infoVehiculo.place(x=270,y=40)
    
    tipo = 'coche'
    cocheID = 16
    
    
    fechaSalida = StringVar()
    fechaLlegada = StringVar()
    titularTarjeta = StringVar()
    numTarjeta = StringVar()
    expiTarjeta = StringVar()
    cvv = StringVar()
    sucursalSeleccionada = StringVar()
    opcion = IntVar()
    
    # Obtener fechas de salida y llegada
    fecha_salida = fechaSalida.get()
    fecha_llegada = fechaLlegada.get()

    # Verificar disponibilidad
    disponibilidad = operations.verificar_disponibilidad_vehiculo(vehiculo=tipo, id_tipo=cocheID, fecha_salida=fecha_salida, fecha_llegada=fecha_llegada)
    
    if disponibilidad:
        estado = 'DISPONIBLE'
    else:
        estado = 'EN MANTENIMIENTO'
    
    estadolbl = Label(topVehiculo,text='Estado: '+estado,fg='#011736',font=('Arial', 12,BOLD),bg='gray')
    estadolbl.place(x=30,y=20)
    
        
    fechaSalidalbl = Label(topVehiculo,font=('Arial', 12),fg='#011736',text='Fecha de renta (yyyy-mm-dd): ',bg='gray')
    fechaSalidalbl.place(x=40,y=250) 
    fSalida = Entry(topVehiculo,font=('Arial', 11),textvariable=fechaSalida,bd=2)
    fSalida.place(x=270,y=250)
    
    fechaLlegadalbl = Label(topVehiculo,font=('Arial', 12),fg='#011736',text='Fecha devolución (yyyy-mm-dd): ',bg='gray')
    fechaLlegadalbl.place(x=40,y=300) 
    fLlegada = Entry(topVehiculo,font=('Arial', 11),textvariable=fechaLlegada,bd=2)
    fLlegada.place(x=270,y=300)   
    
    titularTarjetalbl = Label(topVehiculo,font=('Arial', 12),fg='#011736',text='Titular de la tarjeta: ',bg='gray')
    titularTarjetalbl.place(x=112,y=350) 
    titularTarjetaEny = Entry(topVehiculo,font=('Arial', 11),textvariable=titularTarjeta,bd=2)
    titularTarjetaEny.place(x=270,y=350)
    
    numTarjetalbl = Label(topVehiculo,font=('Arial', 12),fg='#011736',text='Numero de tarjeta: ',bg='gray')
    numTarjetalbl.place(x=112,y=400) 
    numTarjetaEny = Entry(topVehiculo,font=('Arial', 11),textvariable=numTarjeta,bd=2)
    numTarjetaEny.place(x=270,y=400)
    
    expiTarjetalbl = Label(topVehiculo,font=('Arial', 12),fg='#011736',text='Fecha de expiracion (mm-yy): ',bg='gray')
    expiTarjetalbl.place(x=40,y=450) 
    expiTarjetaEny = Entry(topVehiculo,font=('Arial', 11),textvariable=expiTarjeta,bd=2)
    expiTarjetaEny.place(x=270,y=450)
    
    cvvlbl = Label(topVehiculo,font=('Arial', 12),fg='#011736',text='CVV: ',bg='gray')
    cvvlbl.place(x=208,y=500) 
    cvvEny = Entry(topVehiculo,font=('Arial', 11),textvariable=cvv,bd=2)
    cvvEny.place(x=270,y=500)
        
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
                    numTarjeta_value = int(numTarjeta.get())
                    
                    if not re.match(r'^\d{16}$', numTarjeta.get()):
                        messagebox.showerror("Error", "El número de tarjeta debe tener 16 dígitos.")
                        return
                    if not re.match(r'^\d{3}$', cvv.get()):
                        messagebox.showerror("Error", "El CVV debe tener 3 dígitos.")
                        return
                    
                    # Validación de la fecha de expiración de la tarjeta
                    try:
                        formato_fechatj = "%m-%y"
                        fecha_caducidad = datetime.strptime(expiTarjeta.get(), formato_fechatj)
                    except ValueError:
                        messagebox.showerror("Error", "Formato de fecha incorrecto. Usa el formato mm-yy")
                        return
                    
                    # Validación de fechas de renta
                    formato_fecha = "%Y-%m-%d"
                    salida = fechaSalida.get()
                    llegada = fechaLlegada.get()
        
                    try:
                        fecha_salida = datetime.strptime(salida, formato_fecha)
                        fecha_llegada = datetime.strptime(llegada, formato_fecha)
            
                        if fecha_salida >= fecha_llegada:
                            messagebox.showerror("Error", "La fecha de renta debe ser anterior a la fecha de devolución.")
                            return
                        
                        if fecha_llegada < datetime.today():
                            messagebox.showerror("Error", "La fecha de llegada no puede ser una fecha pasada.")
                            return
                    except ValueError:
                        messagebox.showerror("Error", "Formato de fecha incorrecto. Usa el formato yyyy-mm-dd.")
                        return
                    
                    # Verificar la disponibilidad del vehículo
                    disponibilidad = operations.verificar_disponibilidad_vehiculo(vehiculo=tipo, id_tipo=cocheID, fecha_salida=fecha_salida, fecha_llegada=fecha_llegada)
                    if not disponibilidad:
                        messagebox.showerror("Error", "El vehículo no está disponible en las fechas seleccionadas.")
                        return
                    
                    dias = (fecha_llegada - fecha_salida).days
                    if dias <= 0:
                        messagebox.showerror("Error", "Las fechas de alquiler no son válidas.")
                        return
                
                    vehiculoNom = 'Chevrolet Bolt EV'
                    costoDia = 90 
                    
                    monto = (dias + 1) * costoDia
                                     
                    
                    
                    ans = messagebox.askquestion('Transacción',f'Su cuenta sería un total de {monto} dólares.')
                    if ans == 'yes':
                        sucursal_id = getSucursalID(sucursal= sucursalSeleccionada.get())
                        txt = f'Transacción exitosa. Usted rentó un {vehiculoNom} del {fechaSalida.get()} al {fechaLlegada.get()}. Favor de recoger el vehiculo en la sucursal {sucursalSeleccionada.get()} 1 dia antes de su partida. diario: 4:00 am - 23:59 pm.'
                        operations.reservarDB(vehiculo= tipo,id_tipo= cocheID,sucursal_id= sucursal_id,fechaRenta= salida,fechaDevolucion= llegada,monto= monto)
                        messagebox.showinfo("Transaccion exitosa", txt)
                        
                        if opcion.get() == 1:  # Guardar tarjeta
                            operations.insertTarjeta(nomTitular=titularTarjeta.get(), numTarjeta=numTarjeta.get(), cvv=cvv.get(), expiracion=fecha_caducidad)
                                
                            
                        # Añadir fechas al Listbox de fechas no disponibles
                        fndLbx.delete(0, tk.END)
                        fechas = operations.obtener_fechas_reservadas(vehiculo= tipo,id_tipo= cocheID)
                        
                        if fechas:
                            for fecha in fechas:
                                fndLbx.insert(tk.END, fecha)
                                
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
                    messagebox.showerror("Error", "El CVV y el numero de tarjeta deben contener solo números")
                    return
    
    reservarbnt = Button(topVehiculo,text='    Reservar    ',font=('Arial',12),bg='#C9C0D9',command=reservar)
    reservarbnt.place(x=285,y=565)
    
    fNODisponibleslbl = Label(topVehiculo,text='Fechas NO disponibles:',font=('Arial',12),bg='gray')
    fNODisponibleslbl.place(x=480,y=250)
    
    fechas = operations.obtener_fechas_reservadas(vehiculo= tipo,id_tipo= cocheID)
    fndLbx = Listbox(topVehiculo,width=24,font=('Arial',10))
    fndLbx.place(x=480,y=285)
    if fechas:
        for fecha in fechas:
            fndLbx.insert(tk.END, fecha)
    
    guardarTarjeta = Radiobutton(topVehiculo,font=('Arial', 12,BOLD),fg='#011736',text='Guardar tarjeta',value=1,variable=opcion,bg='gray')
    guardarTarjeta.place(x=40,y=550)
    
    noGuardarTarjeta = Radiobutton(topVehiculo,font=('Arial', 12,BOLD),fg='#011736',text='No guardar tarjeta',value=2,variable=opcion,bg='gray')
    noGuardarTarjeta.place(x=40,y=600)
    
    sucursalSbx = Spinbox(topVehiculo,font=('Arial',12),values=('Seleccione una sucursal','Zapopan','Guadalajara','Tonala'), textvariable=sucursalSeleccionada)
    sucursalSbx.place(x=480,y=490)
    
    topVehiculo.mainloop()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def infoPanelCar2():
    topVehiculo = Toplevel()
    topVehiculo.title('Electric Cars Information')
    topVehiculo.iconbitmap('./images/CarIcon.ico')
    topVehiculo.geometry('700x650')
    topVehiculo.config(bg='gray')
    utl.center_window(topVehiculo,700,650)
    topVehiculo.resizable(width=False, height=False)
    
    vehiculo = utl.read_Image('./images/cars/KiaSoulEV.png',(200, 170))
    
    vehiculolbl = Label(topVehiculo, image=vehiculo, bd=0)
    vehiculolbl.place(x=40, y=55)  
    
    txtVehiculo1 = 'KiaSoulEV\nCapacidad: 5 personas\nMaletero: 315 lts\nAutonomia: 383 km\nPotencia: 201 hp\nVelocidad máxima: 167 km/h\nTiempo de carga: 9 hrs (cargador nivel 2),\n1 hora (carga rápida)\nSeguro: Sí\n$65 dls /day'
    infoVehiculo = Label(topVehiculo,wraplength=800,text=txtVehiculo1,font=('Arial', 12),anchor='w',justify='left',bg='gray',fg='#011736')
    infoVehiculo.place(x=270,y=40)
    
    tipo = 'coche'
    cocheID = 15
    
    
    fechaSalida = StringVar()
    fechaLlegada = StringVar()
    titularTarjeta = StringVar()
    numTarjeta = StringVar()
    expiTarjeta = StringVar()
    cvv = StringVar()
    sucursalSeleccionada = StringVar()
    opcion = IntVar()
    
    # Obtener fechas de salida y llegada
    fecha_salida = fechaSalida.get()
    fecha_llegada = fechaLlegada.get()

    # Verificar disponibilidad
    disponibilidad = operations.verificar_disponibilidad_vehiculo(vehiculo=tipo, id_tipo=cocheID, fecha_salida=fecha_salida, fecha_llegada=fecha_llegada)
    
    if disponibilidad:
        estado = 'DISPONIBLE'
    else:
        estado = 'EN MANTENIMIENTO'
    
    estadolbl = Label(topVehiculo,text='Estado: '+estado,fg='#011736',font=('Arial', 12,BOLD),bg='gray')
    estadolbl.place(x=30,y=20)
    
        
    fechaSalidalbl = Label(topVehiculo,font=('Arial', 12),fg='#011736',text='Fecha de renta (yyyy-mm-dd): ',bg='gray')
    fechaSalidalbl.place(x=40,y=250) 
    fSalida = Entry(topVehiculo,font=('Arial', 11),textvariable=fechaSalida,bd=2)
    fSalida.place(x=270,y=250)
    
    fechaLlegadalbl = Label(topVehiculo,font=('Arial', 12),fg='#011736',text='Fecha devolución (yyyy-mm-dd): ',bg='gray')
    fechaLlegadalbl.place(x=40,y=300) 
    fLlegada = Entry(topVehiculo,font=('Arial', 11),textvariable=fechaLlegada,bd=2)
    fLlegada.place(x=270,y=300)   
    
    titularTarjetalbl = Label(topVehiculo,font=('Arial', 12),fg='#011736',text='Titular de la tarjeta: ',bg='gray')
    titularTarjetalbl.place(x=112,y=350) 
    titularTarjetaEny = Entry(topVehiculo,font=('Arial', 11),textvariable=titularTarjeta,bd=2)
    titularTarjetaEny.place(x=270,y=350)
    
    numTarjetalbl = Label(topVehiculo,font=('Arial', 12),fg='#011736',text='Numero de tarjeta: ',bg='gray')
    numTarjetalbl.place(x=112,y=400) 
    numTarjetaEny = Entry(topVehiculo,font=('Arial', 11),textvariable=numTarjeta,bd=2)
    numTarjetaEny.place(x=270,y=400)
    
    expiTarjetalbl = Label(topVehiculo,font=('Arial', 12),fg='#011736',text='Fecha de expiracion (mm-yy): ',bg='gray')
    expiTarjetalbl.place(x=40,y=450) 
    expiTarjetaEny = Entry(topVehiculo,font=('Arial', 11),textvariable=expiTarjeta,bd=2)
    expiTarjetaEny.place(x=270,y=450)
    
    cvvlbl = Label(topVehiculo,font=('Arial', 12),fg='#011736',text='CVV: ',bg='gray')
    cvvlbl.place(x=208,y=500) 
    cvvEny = Entry(topVehiculo,font=('Arial', 11),textvariable=cvv,bd=2)
    cvvEny.place(x=270,y=500)
        
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
                    numTarjeta_value = int(numTarjeta.get())
                    
                    if not re.match(r'^\d{16}$', numTarjeta.get()):
                        messagebox.showerror("Error", "El número de tarjeta debe tener 16 dígitos.")
                        return
                    if not re.match(r'^\d{3}$', cvv.get()):
                        messagebox.showerror("Error", "El CVV debe tener 3 dígitos.")
                        return
                    
                    # Validación de la fecha de expiración de la tarjeta
                    try:
                        formato_fechatj = "%m-%y"
                        fecha_caducidad = datetime.strptime(expiTarjeta.get(), formato_fechatj)
                    except ValueError:
                        messagebox.showerror("Error", "Formato de fecha incorrecto. Usa el formato mm-yy")
                        return
                    
                    # Validación de fechas de renta
                    formato_fecha = "%Y-%m-%d"
                    salida = fechaSalida.get()
                    llegada = fechaLlegada.get()
        
                    try:
                        fecha_salida = datetime.strptime(salida, formato_fecha)
                        fecha_llegada = datetime.strptime(llegada, formato_fecha)
            
                        if fecha_salida >= fecha_llegada:
                            messagebox.showerror("Error", "La fecha de renta debe ser anterior a la fecha de devolución.")
                            return
                        
                        if fecha_llegada < datetime.today():
                            messagebox.showerror("Error", "La fecha de llegada no puede ser una fecha pasada.")
                            return
                    except ValueError:
                        messagebox.showerror("Error", "Formato de fecha incorrecto. Usa el formato yyyy-mm-dd.")
                        return
                    
                    # Verificar la disponibilidad del vehículo
                    disponibilidad = operations.verificar_disponibilidad_vehiculo(vehiculo=tipo, id_tipo=cocheID, fecha_salida=fecha_salida, fecha_llegada=fecha_llegada)
                    if not disponibilidad:
                        messagebox.showerror("Error", "El vehículo no está disponible en las fechas seleccionadas.")
                        return
                    
                    dias = (fecha_llegada - fecha_salida).days
                    if dias <= 0:
                        messagebox.showerror("Error", "Las fechas de alquiler no son válidas.")
                        return
                
                    vehiculoNom = 'Kia Soul EV'
                    costoDia = 65 
                    
                    monto = (dias + 1) * costoDia
                                     
                    
                    
                    ans = messagebox.askquestion('Transacción',f'Su cuenta sería un total de {monto} dólares.')
                    if ans == 'yes':
                        sucursal_id = getSucursalID(sucursal= sucursalSeleccionada.get())
                        txt = f'Transacción exitosa. Usted rentó un {vehiculoNom} del {fechaSalida.get()} al {fechaLlegada.get()}. Favor de recoger el vehiculo en la sucursal {sucursalSeleccionada.get()} 1 dia antes de su partida. diario: 4:00 am - 23:59 pm.'
                        operations.reservarDB(vehiculo= tipo,id_tipo= cocheID,sucursal_id= sucursal_id,fechaRenta= salida,fechaDevolucion= llegada,monto= monto)
                        messagebox.showinfo("Transaccion exitosa", txt)
                        
                        if opcion.get() == 1:  # Guardar tarjeta
                            operations.insertTarjeta(nomTitular=titularTarjeta.get(), numTarjeta=numTarjeta.get(), cvv=cvv.get(), expiracion=fecha_caducidad)
                                
                            
                        # Añadir fechas al Listbox de fechas no disponibles
                        fndLbx.delete(0, tk.END)
                        fechas = operations.obtener_fechas_reservadas(vehiculo= tipo,id_tipo= cocheID)
                        
                        if fechas:
                            for fecha in fechas:
                                fndLbx.insert(tk.END, fecha)
                                
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
                    messagebox.showerror("Error", "El CVV y el numero de tarjeta deben contener solo números")
                    return
    
    reservarbnt = Button(topVehiculo,text='    Reservar    ',font=('Arial',12),bg='#C9C0D9',command=reservar)
    reservarbnt.place(x=285,y=565)
    
    fNODisponibleslbl = Label(topVehiculo,text='Fechas NO disponibles:',font=('Arial',12),bg='gray')
    fNODisponibleslbl.place(x=480,y=250)
    
    fechas = operations.obtener_fechas_reservadas(vehiculo= tipo,id_tipo= cocheID)
    fndLbx = Listbox(topVehiculo,width=24,font=('Arial',10))
    fndLbx.place(x=480,y=285)
    if fechas:
        for fecha in fechas:
            fndLbx.insert(tk.END, fecha)
    
    guardarTarjeta = Radiobutton(topVehiculo,font=('Arial', 12,BOLD),fg='#011736',text='Guardar tarjeta',value=1,variable=opcion,bg='gray')
    guardarTarjeta.place(x=40,y=550)
    
    noGuardarTarjeta = Radiobutton(topVehiculo,font=('Arial', 12,BOLD),fg='#011736',text='No guardar tarjeta',value=2,variable=opcion,bg='gray')
    noGuardarTarjeta.place(x=40,y=600)
    
    sucursalSbx = Spinbox(topVehiculo,font=('Arial',12),values=('Seleccione una sucursal','Zapopan','Guadalajara','Tonala'), textvariable=sucursalSeleccionada)
    sucursalSbx.place(x=480,y=490)
    
    topVehiculo.mainloop()
    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def infoPanelCar3():
    topVehiculo = Toplevel()
    topVehiculo.title('Electric Cars Information')
    topVehiculo.iconbitmap('./images/CarIcon.ico')
    topVehiculo.geometry('700x650')
    topVehiculo.config(bg='gray')
    utl.center_window(topVehiculo,700,650)
    topVehiculo.resizable(width=False, height=False)
    
    vehiculo = utl.read_Image('./images/cars/MazdaMX-30.png',(200, 170))
    
    vehiculolbl = Label(topVehiculo, image=vehiculo, bd=0)
    vehiculolbl.place(x=40, y=55)  
    
    txtVehiculo1 = 'Mazda MX-30\nCapacidad: 5 personas\nMaletero: 366 lts\nAutonomia: 161 km\nPotencia: 143 hp\nVelocidad máxima: 140 km/h\nTiempo de carga: 5 hrs (cargador nivel 2),\n36 min (carga rápida)\nSeguro: Sí\n$120 dls /day'
    infoVehiculo = Label(topVehiculo,wraplength=800,text=txtVehiculo1,font=('Arial', 12),anchor='w',justify='left',bg='gray',fg='#011736')
    infoVehiculo.place(x=270,y=40)
    
    tipo = 'coche'
    cocheID = 14
    
    
    fechaSalida = StringVar()
    fechaLlegada = StringVar()
    titularTarjeta = StringVar()
    numTarjeta = StringVar()
    expiTarjeta = StringVar()
    cvv = StringVar()
    sucursalSeleccionada = StringVar()
    opcion = IntVar()
    
    # Obtener fechas de salida y llegada
    fecha_salida = fechaSalida.get()
    fecha_llegada = fechaLlegada.get()

    # Verificar disponibilidad
    disponibilidad = operations.verificar_disponibilidad_vehiculo(vehiculo=tipo, id_tipo=cocheID, fecha_salida=fecha_salida, fecha_llegada=fecha_llegada)
    
    if disponibilidad:
        estado = 'DISPONIBLE'
    else:
        estado = 'EN MANTENIMIENTO'
    
    estadolbl = Label(topVehiculo,text='Estado: '+estado,fg='#011736',font=('Arial', 12,BOLD),bg='gray')
    estadolbl.place(x=30,y=20)
    
        
    fechaSalidalbl = Label(topVehiculo,font=('Arial', 12),fg='#011736',text='Fecha de renta (yyyy-mm-dd): ',bg='gray')
    fechaSalidalbl.place(x=40,y=250) 
    fSalida = Entry(topVehiculo,font=('Arial', 11),textvariable=fechaSalida,bd=2)
    fSalida.place(x=270,y=250)
    
    fechaLlegadalbl = Label(topVehiculo,font=('Arial', 12),fg='#011736',text='Fecha devolución (yyyy-mm-dd): ',bg='gray')
    fechaLlegadalbl.place(x=40,y=300) 
    fLlegada = Entry(topVehiculo,font=('Arial', 11),textvariable=fechaLlegada,bd=2)
    fLlegada.place(x=270,y=300)   
    
    titularTarjetalbl = Label(topVehiculo,font=('Arial', 12),fg='#011736',text='Titular de la tarjeta: ',bg='gray')
    titularTarjetalbl.place(x=112,y=350) 
    titularTarjetaEny = Entry(topVehiculo,font=('Arial', 11),textvariable=titularTarjeta,bd=2)
    titularTarjetaEny.place(x=270,y=350)
    
    numTarjetalbl = Label(topVehiculo,font=('Arial', 12),fg='#011736',text='Numero de tarjeta: ',bg='gray')
    numTarjetalbl.place(x=112,y=400) 
    numTarjetaEny = Entry(topVehiculo,font=('Arial', 11),textvariable=numTarjeta,bd=2)
    numTarjetaEny.place(x=270,y=400)
    
    expiTarjetalbl = Label(topVehiculo,font=('Arial', 12),fg='#011736',text='Fecha de expiracion (mm-yy): ',bg='gray')
    expiTarjetalbl.place(x=40,y=450) 
    expiTarjetaEny = Entry(topVehiculo,font=('Arial', 11),textvariable=expiTarjeta,bd=2)
    expiTarjetaEny.place(x=270,y=450)
    
    cvvlbl = Label(topVehiculo,font=('Arial', 12),fg='#011736',text='CVV: ',bg='gray')
    cvvlbl.place(x=208,y=500) 
    cvvEny = Entry(topVehiculo,font=('Arial', 11),textvariable=cvv,bd=2)
    cvvEny.place(x=270,y=500)
        
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
                    numTarjeta_value = int(numTarjeta.get())
                    
                    if not re.match(r'^\d{16}$', numTarjeta.get()):
                        messagebox.showerror("Error", "El número de tarjeta debe tener 16 dígitos.")
                        return
                    if not re.match(r'^\d{3}$', cvv.get()):
                        messagebox.showerror("Error", "El CVV debe tener 3 dígitos.")
                        return
                    
                    # Validación de la fecha de expiración de la tarjeta
                    try:
                        formato_fechatj = "%m-%y"
                        fecha_caducidad = datetime.strptime(expiTarjeta.get(), formato_fechatj)
                    except ValueError:
                        messagebox.showerror("Error", "Formato de fecha incorrecto. Usa el formato mm-yy")
                        return
                    
                    # Validación de fechas de renta
                    formato_fecha = "%Y-%m-%d"
                    salida = fechaSalida.get()
                    llegada = fechaLlegada.get()
        
                    try:
                        fecha_salida = datetime.strptime(salida, formato_fecha)
                        fecha_llegada = datetime.strptime(llegada, formato_fecha)
            
                        if fecha_salida >= fecha_llegada:
                            messagebox.showerror("Error", "La fecha de renta debe ser anterior a la fecha de devolución.")
                            return
                        
                        if fecha_llegada < datetime.today():
                            messagebox.showerror("Error", "La fecha de llegada no puede ser una fecha pasada.")
                            return
                    except ValueError:
                        messagebox.showerror("Error", "Formato de fecha incorrecto. Usa el formato yyyy-mm-dd.")
                        return
                    
                    # Verificar la disponibilidad del vehículo
                    disponibilidad = operations.verificar_disponibilidad_vehiculo(vehiculo=tipo, id_tipo=cocheID, fecha_salida=fecha_salida, fecha_llegada=fecha_llegada)
                    if not disponibilidad:
                        messagebox.showerror("Error", "El vehículo no está disponible en las fechas seleccionadas.")
                        return
                    
                    dias = (fecha_llegada - fecha_salida).days
                    if dias <= 0:
                        messagebox.showerror("Error", "Las fechas de alquiler no son válidas.")
                        return
                
                    vehiculoNom = 'Mazda MX-30'
                    costoDia = 120 
                    
                    monto = (dias + 1) * costoDia
                                     
                    
                    
                    ans = messagebox.askquestion('Transacción',f'Su cuenta sería un total de {monto} dólares.')
                    if ans == 'yes':
                        sucursal_id = getSucursalID(sucursal= sucursalSeleccionada.get())
                        txt = f'Transacción exitosa. Usted rentó un {vehiculoNom} del {fechaSalida.get()} al {fechaLlegada.get()}. Favor de recoger el vehiculo en la sucursal {sucursalSeleccionada.get()} 1 dia antes de su partida. diario: 4:00 am - 23:59 pm.'
                        operations.reservarDB(vehiculo= tipo,id_tipo= cocheID,sucursal_id= sucursal_id,fechaRenta= salida,fechaDevolucion= llegada,monto= monto)
                        messagebox.showinfo("Transaccion exitosa", txt)
                        
                        if opcion.get() == 1:  # Guardar tarjeta
                            operations.insertTarjeta(nomTitular=titularTarjeta.get(), numTarjeta=numTarjeta.get(), cvv=cvv.get(), expiracion=fecha_caducidad)
                                
                            
                        # Añadir fechas al Listbox de fechas no disponibles
                        fndLbx.delete(0, tk.END)
                        fechas = operations.obtener_fechas_reservadas(vehiculo= tipo,id_tipo= cocheID)
                        
                        if fechas:
                            for fecha in fechas:
                                fndLbx.insert(tk.END, fecha)
                                
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
                    messagebox.showerror("Error", "El CVV y el numero de tarjeta deben contener solo números")
                    return
    
    reservarbnt = Button(topVehiculo,text='    Reservar    ',font=('Arial',12),bg='#C9C0D9',command=reservar)
    reservarbnt.place(x=285,y=565)
    
    fNODisponibleslbl = Label(topVehiculo,text='Fechas NO disponibles:',font=('Arial',12),bg='gray')
    fNODisponibleslbl.place(x=480,y=250)
    
    fechas = operations.obtener_fechas_reservadas(vehiculo= tipo,id_tipo= cocheID)
    fndLbx = Listbox(topVehiculo,width=24,font=('Arial',10))
    fndLbx.place(x=480,y=285)
    if fechas:
        for fecha in fechas:
            fndLbx.insert(tk.END, fecha)
    
    guardarTarjeta = Radiobutton(topVehiculo,font=('Arial', 12,BOLD),fg='#011736',text='Guardar tarjeta',value=1,variable=opcion,bg='gray')
    guardarTarjeta.place(x=40,y=550)
    
    noGuardarTarjeta = Radiobutton(topVehiculo,font=('Arial', 12,BOLD),fg='#011736',text='No guardar tarjeta',value=2,variable=opcion,bg='gray')
    noGuardarTarjeta.place(x=40,y=600)
    
    sucursalSbx = Spinbox(topVehiculo,font=('Arial',12),values=('Seleccione una sucursal','Zapopan','Guadalajara','Tonala'), textvariable=sucursalSeleccionada)
    sucursalSbx.place(x=480,y=490)
    
    topVehiculo.mainloop()
    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def infoPanelCar4():
    topVehiculo = Toplevel()
    topVehiculo.title('Electric Cars Information')
    topVehiculo.iconbitmap('./images/CarIcon.ico')
    topVehiculo.geometry('700x650')
    topVehiculo.config(bg='gray')
    utl.center_window(topVehiculo,700,650)
    topVehiculo.resizable(width=False, height=False)
    
    vehiculo = utl.read_Image('./images/cars/NissanLeaf.png',(200, 170))
    
    vehiculolbl = Label(topVehiculo, image=vehiculo, bd=0)
    vehiculolbl.place(x=40, y=55)  
    
    txtVehiculo1 = 'Nissan Leaf\nCapacidad: 5 personas\nMaletero: 435 lts\nAutonomia: 240 km\nPotencia: 147 hp\nVelocidad máxima: 144 km/h\nTiempo de carga: 7.5 hrs (cargador nivel 2)\nSeguro: Sí\n$85 dls /day'
    infoVehiculo = Label(topVehiculo,wraplength=800,text=txtVehiculo1,font=('Arial', 12),anchor='w',justify='left',bg='gray',fg='#011736')
    infoVehiculo.place(x=270,y=40)
    
    tipo = 'coche'
    cocheID = 13
    
    
    fechaSalida = StringVar()
    fechaLlegada = StringVar()
    titularTarjeta = StringVar()
    numTarjeta = StringVar()
    expiTarjeta = StringVar()
    cvv = StringVar()
    sucursalSeleccionada = StringVar()
    opcion = IntVar()
    
    # Obtener fechas de salida y llegada
    fecha_salida = fechaSalida.get()
    fecha_llegada = fechaLlegada.get()

    # Verificar disponibilidad
    disponibilidad = operations.verificar_disponibilidad_vehiculo(vehiculo=tipo, id_tipo=cocheID, fecha_salida=fecha_salida, fecha_llegada=fecha_llegada)
    
    if disponibilidad:
        estado = 'DISPONIBLE'
    else:
        estado = 'EN MANTENIMIENTO'
    
    estadolbl = Label(topVehiculo,text='Estado: '+estado,fg='#011736',font=('Arial', 12,BOLD),bg='gray')
    estadolbl.place(x=30,y=20)
    
        
    fechaSalidalbl = Label(topVehiculo,font=('Arial', 12),fg='#011736',text='Fecha de renta (yyyy-mm-dd): ',bg='gray')
    fechaSalidalbl.place(x=40,y=250) 
    fSalida = Entry(topVehiculo,font=('Arial', 11),textvariable=fechaSalida,bd=2)
    fSalida.place(x=270,y=250)
    
    fechaLlegadalbl = Label(topVehiculo,font=('Arial', 12),fg='#011736',text='Fecha devolución (yyyy-mm-dd): ',bg='gray')
    fechaLlegadalbl.place(x=40,y=300) 
    fLlegada = Entry(topVehiculo,font=('Arial', 11),textvariable=fechaLlegada,bd=2)
    fLlegada.place(x=270,y=300)   
    
    titularTarjetalbl = Label(topVehiculo,font=('Arial', 12),fg='#011736',text='Titular de la tarjeta: ',bg='gray')
    titularTarjetalbl.place(x=112,y=350) 
    titularTarjetaEny = Entry(topVehiculo,font=('Arial', 11),textvariable=titularTarjeta,bd=2)
    titularTarjetaEny.place(x=270,y=350)
    
    numTarjetalbl = Label(topVehiculo,font=('Arial', 12),fg='#011736',text='Numero de tarjeta: ',bg='gray')
    numTarjetalbl.place(x=112,y=400) 
    numTarjetaEny = Entry(topVehiculo,font=('Arial', 11),textvariable=numTarjeta,bd=2)
    numTarjetaEny.place(x=270,y=400)
    
    expiTarjetalbl = Label(topVehiculo,font=('Arial', 12),fg='#011736',text='Fecha de expiracion (mm-yy): ',bg='gray')
    expiTarjetalbl.place(x=40,y=450) 
    expiTarjetaEny = Entry(topVehiculo,font=('Arial', 11),textvariable=expiTarjeta,bd=2)
    expiTarjetaEny.place(x=270,y=450)
    
    cvvlbl = Label(topVehiculo,font=('Arial', 12),fg='#011736',text='CVV: ',bg='gray')
    cvvlbl.place(x=208,y=500) 
    cvvEny = Entry(topVehiculo,font=('Arial', 11),textvariable=cvv,bd=2)
    cvvEny.place(x=270,y=500)
        
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
                    numTarjeta_value = int(numTarjeta.get())
                    
                    if not re.match(r'^\d{16}$', numTarjeta.get()):
                        messagebox.showerror("Error", "El número de tarjeta debe tener 16 dígitos.")
                        return
                    if not re.match(r'^\d{3}$', cvv.get()):
                        messagebox.showerror("Error", "El CVV debe tener 3 dígitos.")
                        return
                    
                    # Validación de la fecha de expiración de la tarjeta
                    try:
                        formato_fechatj = "%m-%y"
                        fecha_caducidad = datetime.strptime(expiTarjeta.get(), formato_fechatj)
                    except ValueError:
                        messagebox.showerror("Error", "Formato de fecha incorrecto. Usa el formato mm-yy")
                        return
                    
                    # Validación de fechas de renta
                    formato_fecha = "%Y-%m-%d"
                    salida = fechaSalida.get()
                    llegada = fechaLlegada.get()
        
                    try:
                        fecha_salida = datetime.strptime(salida, formato_fecha)
                        fecha_llegada = datetime.strptime(llegada, formato_fecha)
            
                        if fecha_salida >= fecha_llegada:
                            messagebox.showerror("Error", "La fecha de renta debe ser anterior a la fecha de devolución.")
                            return
                        
                        if fecha_llegada < datetime.today():
                            messagebox.showerror("Error", "La fecha de llegada no puede ser una fecha pasada.")
                            return
                    except ValueError:
                        messagebox.showerror("Error", "Formato de fecha incorrecto. Usa el formato yyyy-mm-dd.")
                        return
                    
                    # Verificar la disponibilidad del vehículo
                    disponibilidad = operations.verificar_disponibilidad_vehiculo(vehiculo=tipo, id_tipo=cocheID, fecha_salida=fecha_salida, fecha_llegada=fecha_llegada)
                    if not disponibilidad:
                        messagebox.showerror("Error", "El vehículo no está disponible en las fechas seleccionadas.")
                        return
                    
                    dias = (fecha_llegada - fecha_salida).days
                    if dias <= 0:
                        messagebox.showerror("Error", "Las fechas de alquiler no son válidas.")
                        return
                
                    vehiculoNom = 'Nissan Leaf'
                    costoDia = 85
                    
                    monto = (dias + 1) * costoDia
                                     
                    
                    
                    ans = messagebox.askquestion('Transacción',f'Su cuenta sería un total de {monto} dólares.')
                    if ans == 'yes':
                        sucursal_id = getSucursalID(sucursal= sucursalSeleccionada.get())
                        txt = f'Transacción exitosa. Usted rentó un {vehiculoNom} del {fechaSalida.get()} al {fechaLlegada.get()}. Favor de recoger el vehiculo en la sucursal {sucursalSeleccionada.get()} 1 dia antes de su partida. diario: 4:00 am - 23:59 pm.'
                        operations.reservarDB(vehiculo= tipo,id_tipo= cocheID,sucursal_id= sucursal_id,fechaRenta= salida,fechaDevolucion= llegada,monto= monto)
                        messagebox.showinfo("Transaccion exitosa", txt)
                        
                        if opcion.get() == 1:  # Guardar tarjeta
                            operations.insertTarjeta(nomTitular=titularTarjeta.get(), numTarjeta=numTarjeta.get(), cvv=cvv.get(), expiracion=fecha_caducidad)
                                
                            
                        # Añadir fechas al Listbox de fechas no disponibles
                        fndLbx.delete(0, tk.END)
                        fechas = operations.obtener_fechas_reservadas(vehiculo= tipo,id_tipo= cocheID)
                        
                        if fechas:
                            for fecha in fechas:
                                fndLbx.insert(tk.END, fecha)
                                
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
                    messagebox.showerror("Error", "El CVV y el numero de tarjeta deben contener solo números")
                    return
    
    reservarbnt = Button(topVehiculo,text='    Reservar    ',font=('Arial',12),bg='#C9C0D9',command=reservar)
    reservarbnt.place(x=285,y=565)
    
    fNODisponibleslbl = Label(topVehiculo,text='Fechas NO disponibles:',font=('Arial',12),bg='gray')
    fNODisponibleslbl.place(x=480,y=250)
    
    fechas = operations.obtener_fechas_reservadas(vehiculo= tipo,id_tipo= cocheID)
    fndLbx = Listbox(topVehiculo,width=24,font=('Arial',10))
    fndLbx.place(x=480,y=285)
    if fechas:
        for fecha in fechas:
            fndLbx.insert(tk.END, fecha)
    
    guardarTarjeta = Radiobutton(topVehiculo,font=('Arial', 12,BOLD),fg='#011736',text='Guardar tarjeta',value=1,variable=opcion,bg='gray')
    guardarTarjeta.place(x=40,y=550)
    
    noGuardarTarjeta = Radiobutton(topVehiculo,font=('Arial', 12,BOLD),fg='#011736',text='No guardar tarjeta',value=2,variable=opcion,bg='gray')
    noGuardarTarjeta.place(x=40,y=600)
    
    sucursalSbx = Spinbox(topVehiculo,font=('Arial',12),values=('Seleccione una sucursal','Zapopan','Guadalajara','Tonala'), textvariable=sucursalSeleccionada)
    sucursalSbx.place(x=480,y=490)
    
    topVehiculo.mainloop()
    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def infoPanelCar5():
    topVehiculo = Toplevel()
    topVehiculo.title('Electric Cars Information')
    topVehiculo.iconbitmap('./images/CarIcon.ico')
    topVehiculo.geometry('700x650')
    topVehiculo.config(bg='gray')
    utl.center_window(topVehiculo,700,650)
    topVehiculo.resizable(width=False, height=False)
    
    vehiculo = utl.read_Image('./images/cars/TeslaModel3LongRangeAWD.png',(200, 170))
    
    vehiculolbl = Label(topVehiculo, image=vehiculo, bd=0)
    vehiculolbl.place(x=40, y=55)  
    
    txtVehiculo1 = 'Tesla Model 3 Long Range AWD\nCapacidad: 5 personas\nMaletero: 425 lts\nAutonomia: 576 km\nPotencia: 346 hp\nVelocidad máxima: 233 km/h\nTiempo de carga: 8 hrs (cargador nivel 2),\n15 min (carga rápida)\nSeguro: Sí\n$130 dls /day'
    infoVehiculo = Label(topVehiculo,wraplength=800,text=txtVehiculo1,font=('Arial', 12),anchor='w',justify='left',bg='gray',fg='#011736')
    infoVehiculo.place(x=270,y=40)
    
    tipo = 'coche'
    cocheID = 12
    
    
    fechaSalida = StringVar()
    fechaLlegada = StringVar()
    titularTarjeta = StringVar()
    numTarjeta = StringVar()
    expiTarjeta = StringVar()
    cvv = StringVar()
    sucursalSeleccionada = StringVar()
    opcion = IntVar()
    
    # Obtener fechas de salida y llegada
    fecha_salida = fechaSalida.get()
    fecha_llegada = fechaLlegada.get()

    # Verificar disponibilidad
    disponibilidad = operations.verificar_disponibilidad_vehiculo(vehiculo=tipo, id_tipo=cocheID, fecha_salida=fecha_salida, fecha_llegada=fecha_llegada)
    
    if disponibilidad:
        estado = 'DISPONIBLE'
    else:
        estado = 'EN MANTENIMIENTO'
    
    estadolbl = Label(topVehiculo,text='Estado: '+estado,fg='#011736',font=('Arial', 12,BOLD),bg='gray')
    estadolbl.place(x=30,y=20)
    
        
    fechaSalidalbl = Label(topVehiculo,font=('Arial', 12),fg='#011736',text='Fecha de renta (yyyy-mm-dd): ',bg='gray')
    fechaSalidalbl.place(x=40,y=250) 
    fSalida = Entry(topVehiculo,font=('Arial', 11),textvariable=fechaSalida,bd=2)
    fSalida.place(x=270,y=250)
    
    fechaLlegadalbl = Label(topVehiculo,font=('Arial', 12),fg='#011736',text='Fecha devolución (yyyy-mm-dd): ',bg='gray')
    fechaLlegadalbl.place(x=40,y=300) 
    fLlegada = Entry(topVehiculo,font=('Arial', 11),textvariable=fechaLlegada,bd=2)
    fLlegada.place(x=270,y=300)   
    
    titularTarjetalbl = Label(topVehiculo,font=('Arial', 12),fg='#011736',text='Titular de la tarjeta: ',bg='gray')
    titularTarjetalbl.place(x=112,y=350) 
    titularTarjetaEny = Entry(topVehiculo,font=('Arial', 11),textvariable=titularTarjeta,bd=2)
    titularTarjetaEny.place(x=270,y=350)
    
    numTarjetalbl = Label(topVehiculo,font=('Arial', 12),fg='#011736',text='Numero de tarjeta: ',bg='gray')
    numTarjetalbl.place(x=112,y=400) 
    numTarjetaEny = Entry(topVehiculo,font=('Arial', 11),textvariable=numTarjeta,bd=2)
    numTarjetaEny.place(x=270,y=400)
    
    expiTarjetalbl = Label(topVehiculo,font=('Arial', 12),fg='#011736',text='Fecha de expiracion (mm-yy): ',bg='gray')
    expiTarjetalbl.place(x=40,y=450) 
    expiTarjetaEny = Entry(topVehiculo,font=('Arial', 11),textvariable=expiTarjeta,bd=2)
    expiTarjetaEny.place(x=270,y=450)
    
    cvvlbl = Label(topVehiculo,font=('Arial', 12),fg='#011736',text='CVV: ',bg='gray')
    cvvlbl.place(x=208,y=500) 
    cvvEny = Entry(topVehiculo,font=('Arial', 11),textvariable=cvv,bd=2)
    cvvEny.place(x=270,y=500)
        
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
                    numTarjeta_value = int(numTarjeta.get())
                    
                    if not re.match(r'^\d{16}$', numTarjeta.get()):
                        messagebox.showerror("Error", "El número de tarjeta debe tener 16 dígitos.")
                        return
                    if not re.match(r'^\d{3}$', cvv.get()):
                        messagebox.showerror("Error", "El CVV debe tener 3 dígitos.")
                        return
                    
                    # Validación de la fecha de expiración de la tarjeta
                    try:
                        formato_fechatj = "%m-%y"
                        fecha_caducidad = datetime.strptime(expiTarjeta.get(), formato_fechatj)
                    except ValueError:
                        messagebox.showerror("Error", "Formato de fecha incorrecto. Usa el formato mm-yy")
                        return
                    
                    # Validación de fechas de renta
                    formato_fecha = "%Y-%m-%d"
                    salida = fechaSalida.get()
                    llegada = fechaLlegada.get()
        
                    try:
                        fecha_salida = datetime.strptime(salida, formato_fecha)
                        fecha_llegada = datetime.strptime(llegada, formato_fecha)
            
                        if fecha_salida >= fecha_llegada:
                            messagebox.showerror("Error", "La fecha de renta debe ser anterior a la fecha de devolución.")
                            return
                        
                        if fecha_llegada < datetime.today():
                            messagebox.showerror("Error", "La fecha de llegada no puede ser una fecha pasada.")
                            return
                    except ValueError:
                        messagebox.showerror("Error", "Formato de fecha incorrecto. Usa el formato yyyy-mm-dd.")
                        return
                    
                    # Verificar la disponibilidad del vehículo
                    disponibilidad = operations.verificar_disponibilidad_vehiculo(vehiculo=tipo, id_tipo=cocheID, fecha_salida=fecha_salida, fecha_llegada=fecha_llegada)
                    if not disponibilidad:
                        messagebox.showerror("Error", "El vehículo no está disponible en las fechas seleccionadas.")
                        return
                    
                    dias = (fecha_llegada - fecha_salida).days
                    if dias <= 0:
                        messagebox.showerror("Error", "Las fechas de alquiler no son válidas.")
                        return
                
                    vehiculoNom = 'Tesla Model 3 Long Range AWD'
                    costoDia = 130
                    
                    monto = (dias + 1) * costoDia
                                     
                    
                    
                    ans = messagebox.askquestion('Transacción',f'Su cuenta sería un total de {monto} dólares.')
                    if ans == 'yes':
                        sucursal_id = getSucursalID(sucursal= sucursalSeleccionada.get())
                        txt = f'Transacción exitosa. Usted rentó un {vehiculoNom} del {fechaSalida.get()} al {fechaLlegada.get()}. Favor de recoger el vehiculo en la sucursal {sucursalSeleccionada.get()} 1 dia antes de su partida. diario: 4:00 am - 23:59 pm.'
                        operations.reservarDB(vehiculo= tipo,id_tipo= cocheID,sucursal_id= sucursal_id,fechaRenta= salida,fechaDevolucion= llegada,monto= monto)
                        messagebox.showinfo("Transaccion exitosa", txt)
                        
                        if opcion.get() == 1:  # Guardar tarjeta
                            operations.insertTarjeta(nomTitular=titularTarjeta.get(), numTarjeta=numTarjeta.get(), cvv=cvv.get(), expiracion=fecha_caducidad)
                                
                            
                        # Añadir fechas al Listbox de fechas no disponibles
                        fndLbx.delete(0, tk.END)
                        fechas = operations.obtener_fechas_reservadas(vehiculo= tipo,id_tipo= cocheID)
                        
                        if fechas:
                            for fecha in fechas:
                                fndLbx.insert(tk.END, fecha)
                                
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
                    messagebox.showerror("Error", "El CVV y el numero de tarjeta deben contener solo números")
                    return
    
    reservarbnt = Button(topVehiculo,text='    Reservar    ',font=('Arial',12),bg='#C9C0D9',command=reservar)
    reservarbnt.place(x=285,y=565)
    
    fNODisponibleslbl = Label(topVehiculo,text='Fechas NO disponibles:',font=('Arial',12),bg='gray')
    fNODisponibleslbl.place(x=480,y=250)
    
    fechas = operations.obtener_fechas_reservadas(vehiculo= tipo,id_tipo= cocheID)
    fndLbx = Listbox(topVehiculo,width=24,font=('Arial',10))
    fndLbx.place(x=480,y=285)
    if fechas:
        for fecha in fechas:
            fndLbx.insert(tk.END, fecha)
    
    guardarTarjeta = Radiobutton(topVehiculo,font=('Arial', 12,BOLD),fg='#011736',text='Guardar tarjeta',value=1,variable=opcion,bg='gray')
    guardarTarjeta.place(x=40,y=550)
    
    noGuardarTarjeta = Radiobutton(topVehiculo,font=('Arial', 12,BOLD),fg='#011736',text='No guardar tarjeta',value=2,variable=opcion,bg='gray')
    noGuardarTarjeta.place(x=40,y=600)
    
    sucursalSbx = Spinbox(topVehiculo,font=('Arial',12),values=('Seleccione una sucursal','Zapopan','Guadalajara','Tonala'), textvariable=sucursalSeleccionada)
    sucursalSbx.place(x=480,y=490)
    
    topVehiculo.mainloop()
    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def infoPanelCar6():
    topVehiculo = Toplevel()
    topVehiculo.title('Electric Cars Information')
    topVehiculo.iconbitmap('./images/CarIcon.ico')
    topVehiculo.geometry('700x650')
    topVehiculo.config(bg='gray')
    utl.center_window(topVehiculo,700,650)
    topVehiculo.resizable(width=False, height=False)
    
    vehiculo = utl.read_Image('./images/cars/VolkswagenID4.png',(200, 170))
    
    vehiculolbl = Label(topVehiculo, image=vehiculo, bd=0)
    vehiculolbl.place(x=40, y=55)  
    
    txtVehiculo1 = 'Volkswagen ID.4\nCapacidad: 5 personas\nMaletero: 543 lts\nAutonomia: 418 km\nPotencia: 201hp\nVelocidad máxima: 150km/h\nTiempo de carga: 7.5 hrs (cargador nivel 2),\n38 min (carga rápida)\nSeguro: Sí\n$125 dls /day'
    infoVehiculo = Label(topVehiculo,wraplength=800,text=txtVehiculo1,font=('Arial', 12),anchor='w',justify='left',bg='gray',fg='#011736')
    infoVehiculo.place(x=270,y=40)
    
    tipo = 'coche'
    cocheID = 11
    
    
    fechaSalida = StringVar()
    fechaLlegada = StringVar()
    titularTarjeta = StringVar()
    numTarjeta = StringVar()
    expiTarjeta = StringVar()
    cvv = StringVar()
    sucursalSeleccionada = StringVar()
    opcion = IntVar()
    
    # Obtener fechas de salida y llegada
    fecha_salida = fechaSalida.get()
    fecha_llegada = fechaLlegada.get()

    # Verificar disponibilidad
    disponibilidad = operations.verificar_disponibilidad_vehiculo(vehiculo=tipo, id_tipo=cocheID, fecha_salida=fecha_salida, fecha_llegada=fecha_llegada)
    
    if disponibilidad:
        estado = 'DISPONIBLE'
    else:
        estado = 'EN MANTENIMIENTO'
    
    estadolbl = Label(topVehiculo,text='Estado: '+estado,fg='#011736',font=('Arial', 12,BOLD),bg='gray')
    estadolbl.place(x=30,y=20)
    
        
    fechaSalidalbl = Label(topVehiculo,font=('Arial', 12),fg='#011736',text='Fecha de renta (yyyy-mm-dd): ',bg='gray')
    fechaSalidalbl.place(x=40,y=250) 
    fSalida = Entry(topVehiculo,font=('Arial', 11),textvariable=fechaSalida,bd=2)
    fSalida.place(x=270,y=250)
    
    fechaLlegadalbl = Label(topVehiculo,font=('Arial', 12),fg='#011736',text='Fecha devolución (yyyy-mm-dd): ',bg='gray')
    fechaLlegadalbl.place(x=40,y=300) 
    fLlegada = Entry(topVehiculo,font=('Arial', 11),textvariable=fechaLlegada,bd=2)
    fLlegada.place(x=270,y=300)   
    
    titularTarjetalbl = Label(topVehiculo,font=('Arial', 12),fg='#011736',text='Titular de la tarjeta: ',bg='gray')
    titularTarjetalbl.place(x=112,y=350) 
    titularTarjetaEny = Entry(topVehiculo,font=('Arial', 11),textvariable=titularTarjeta,bd=2)
    titularTarjetaEny.place(x=270,y=350)
    
    numTarjetalbl = Label(topVehiculo,font=('Arial', 12),fg='#011736',text='Numero de tarjeta: ',bg='gray')
    numTarjetalbl.place(x=112,y=400) 
    numTarjetaEny = Entry(topVehiculo,font=('Arial', 11),textvariable=numTarjeta,bd=2)
    numTarjetaEny.place(x=270,y=400)
    
    expiTarjetalbl = Label(topVehiculo,font=('Arial', 12),fg='#011736',text='Fecha de expiracion (mm-yy): ',bg='gray')
    expiTarjetalbl.place(x=40,y=450) 
    expiTarjetaEny = Entry(topVehiculo,font=('Arial', 11),textvariable=expiTarjeta,bd=2)
    expiTarjetaEny.place(x=270,y=450)
    
    cvvlbl = Label(topVehiculo,font=('Arial', 12),fg='#011736',text='CVV: ',bg='gray')
    cvvlbl.place(x=208,y=500) 
    cvvEny = Entry(topVehiculo,font=('Arial', 11),textvariable=cvv,bd=2)
    cvvEny.place(x=270,y=500)
        
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
                    numTarjeta_value = int(numTarjeta.get())
                    
                    if not re.match(r'^\d{16}$', numTarjeta.get()):
                        messagebox.showerror("Error", "El número de tarjeta debe tener 16 dígitos.")
                        return
                    if not re.match(r'^\d{3}$', cvv.get()):
                        messagebox.showerror("Error", "El CVV debe tener 3 dígitos.")
                        return
                    
                    # Validación de la fecha de expiración de la tarjeta
                    try:
                        formato_fechatj = "%m-%y"
                        fecha_caducidad = datetime.strptime(expiTarjeta.get(), formato_fechatj)
                    except ValueError:
                        messagebox.showerror("Error", "Formato de fecha incorrecto. Usa el formato mm-yy")
                        return
                    
                    # Validación de fechas de renta
                    formato_fecha = "%Y-%m-%d"
                    salida = fechaSalida.get()
                    llegada = fechaLlegada.get()
        
                    try:
                        fecha_salida = datetime.strptime(salida, formato_fecha)
                        fecha_llegada = datetime.strptime(llegada, formato_fecha)
            
                        if fecha_salida >= fecha_llegada:
                            messagebox.showerror("Error", "La fecha de renta debe ser anterior a la fecha de devolución.")
                            return
                        
                        if fecha_llegada < datetime.today():
                            messagebox.showerror("Error", "La fecha de llegada no puede ser una fecha pasada.")
                            return
                    except ValueError:
                        messagebox.showerror("Error", "Formato de fecha incorrecto. Usa el formato yyyy-mm-dd.")
                        return
                    
                    # Verificar la disponibilidad del vehículo
                    disponibilidad = operations.verificar_disponibilidad_vehiculo(vehiculo=tipo, id_tipo=cocheID, fecha_salida=fecha_salida, fecha_llegada=fecha_llegada)
                    if not disponibilidad:
                        messagebox.showerror("Error", "El vehículo no está disponible en las fechas seleccionadas.")
                        return
                    
                    dias = (fecha_llegada - fecha_salida).days
                    if dias <= 0:
                        messagebox.showerror("Error", "Las fechas de alquiler no son válidas.")
                        return
                
                    vehiculoNom = 'Volkswagen ID.4'
                    costoDia = 125 
                    
                    monto = (dias + 1) * costoDia
                                     
                    
                    
                    ans = messagebox.askquestion('Transacción',f'Su cuenta sería un total de {monto} dólares.')
                    if ans == 'yes':
                        sucursal_id = getSucursalID(sucursal= sucursalSeleccionada.get())
                        txt = f'Transacción exitosa. Usted rentó un {vehiculoNom} del {fechaSalida.get()} al {fechaLlegada.get()}. Favor de recoger el vehiculo en la sucursal {sucursalSeleccionada.get()} 1 dia antes de su partida. diario: 4:00 am - 23:59 pm.'
                        operations.reservarDB(vehiculo= tipo,id_tipo= cocheID,sucursal_id= sucursal_id,fechaRenta= salida,fechaDevolucion= llegada,monto= monto)
                        messagebox.showinfo("Transaccion exitosa", txt)
                        
                        if opcion.get() == 1:  # Guardar tarjeta
                            operations.insertTarjeta(nomTitular=titularTarjeta.get(), numTarjeta=numTarjeta.get(), cvv=cvv.get(), expiracion=fecha_caducidad)
                                
                            
                        # Añadir fechas al Listbox de fechas no disponibles
                        fndLbx.delete(0, tk.END)
                        fechas = operations.obtener_fechas_reservadas(vehiculo= tipo,id_tipo= cocheID)
                        
                        if fechas:
                            for fecha in fechas:
                                fndLbx.insert(tk.END, fecha)
                                
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
                    messagebox.showerror("Error", "El CVV y el numero de tarjeta deben contener solo números")
                    return
    
    reservarbnt = Button(topVehiculo,text='    Reservar    ',font=('Arial',12),bg='#C9C0D9',command=reservar)
    reservarbnt.place(x=285,y=565)
    
    fNODisponibleslbl = Label(topVehiculo,text='Fechas NO disponibles:',font=('Arial',12),bg='gray')
    fNODisponibleslbl.place(x=480,y=250)
    
    fechas = operations.obtener_fechas_reservadas(vehiculo= tipo,id_tipo= cocheID)
    fndLbx = Listbox(topVehiculo,width=24,font=('Arial',10))
    fndLbx.place(x=480,y=285)
    if fechas:
        for fecha in fechas:
            fndLbx.insert(tk.END, fecha)
    
    guardarTarjeta = Radiobutton(topVehiculo,font=('Arial', 12,BOLD),fg='#011736',text='Guardar tarjeta',value=1,variable=opcion,bg='gray')
    guardarTarjeta.place(x=40,y=550)
    
    noGuardarTarjeta = Radiobutton(topVehiculo,font=('Arial', 12,BOLD),fg='#011736',text='No guardar tarjeta',value=2,variable=opcion,bg='gray')
    noGuardarTarjeta.place(x=40,y=600)
    
    sucursalSbx = Spinbox(topVehiculo,font=('Arial',12),values=('Seleccione una sucursal','Zapopan','Guadalajara','Tonala'), textvariable=sucursalSeleccionada)
    sucursalSbx.place(x=480,y=490)
    
    topVehiculo.mainloop()
    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def infoPanelCar7():
    topVehiculo = Toplevel()
    topVehiculo.title('Electric Cars Information')
    topVehiculo.iconbitmap('./images/CarIcon.ico')
    topVehiculo.geometry('700x650')
    topVehiculo.config(bg='gray')
    utl.center_window(topVehiculo,700,650)
    topVehiculo.resizable(width=False, height=False)
    
    vehiculo = utl.read_Image('./images/cars/TeslaModel3StandardRangePlus.png',(200, 170))
    
    vehiculolbl = Label(topVehiculo, image=vehiculo, bd=0)
    vehiculolbl.place(x=40, y=55)  
    
    txtVehiculo1 = 'Tesla Model 3 Standard Range Plus\nCapacidad: 5 personas\nMaletero: 425 lts\nAutonomia: 438 km\nPotencia: 283 hp\nVelocidad máxima: 225 km/h\nTiempo de carga: 9 hrs (cargador nivel 2),\n15 min (carga rápida)\nSeguro: Sí\n$128 dls /day'
    infoVehiculo = Label(topVehiculo,wraplength=800,text=txtVehiculo1,font=('Arial', 12),anchor='w',justify='left',bg='gray',fg='#011736')
    infoVehiculo.place(x=270,y=40)
    
    tipo = 'coche'
    cocheID = 10
    
    
    fechaSalida = StringVar()
    fechaLlegada = StringVar()
    titularTarjeta = StringVar()
    numTarjeta = StringVar()
    expiTarjeta = StringVar()
    cvv = StringVar()
    sucursalSeleccionada = StringVar()
    opcion = IntVar()
    
    # Obtener fechas de salida y llegada
    fecha_salida = fechaSalida.get()
    fecha_llegada = fechaLlegada.get()

    # Verificar disponibilidad
    disponibilidad = operations.verificar_disponibilidad_vehiculo(vehiculo=tipo, id_tipo=cocheID, fecha_salida=fecha_salida, fecha_llegada=fecha_llegada)
    
    if disponibilidad:
        estado = 'DISPONIBLE'
    else:
        estado = 'EN MANTENIMIENTO'
    
    estadolbl = Label(topVehiculo,text='Estado: '+estado,fg='#011736',font=('Arial', 12,BOLD),bg='gray')
    estadolbl.place(x=30,y=20)
    
        
    fechaSalidalbl = Label(topVehiculo,font=('Arial', 12),fg='#011736',text='Fecha de renta (yyyy-mm-dd): ',bg='gray')
    fechaSalidalbl.place(x=40,y=250) 
    fSalida = Entry(topVehiculo,font=('Arial', 11),textvariable=fechaSalida,bd=2)
    fSalida.place(x=270,y=250)
    
    fechaLlegadalbl = Label(topVehiculo,font=('Arial', 12),fg='#011736',text='Fecha devolución (yyyy-mm-dd): ',bg='gray')
    fechaLlegadalbl.place(x=40,y=300) 
    fLlegada = Entry(topVehiculo,font=('Arial', 11),textvariable=fechaLlegada,bd=2)
    fLlegada.place(x=270,y=300)   
    
    titularTarjetalbl = Label(topVehiculo,font=('Arial', 12),fg='#011736',text='Titular de la tarjeta: ',bg='gray')
    titularTarjetalbl.place(x=112,y=350) 
    titularTarjetaEny = Entry(topVehiculo,font=('Arial', 11),textvariable=titularTarjeta,bd=2)
    titularTarjetaEny.place(x=270,y=350)
    
    numTarjetalbl = Label(topVehiculo,font=('Arial', 12),fg='#011736',text='Numero de tarjeta: ',bg='gray')
    numTarjetalbl.place(x=112,y=400) 
    numTarjetaEny = Entry(topVehiculo,font=('Arial', 11),textvariable=numTarjeta,bd=2)
    numTarjetaEny.place(x=270,y=400)
    
    expiTarjetalbl = Label(topVehiculo,font=('Arial', 12),fg='#011736',text='Fecha de expiracion (mm-yy): ',bg='gray')
    expiTarjetalbl.place(x=40,y=450) 
    expiTarjetaEny = Entry(topVehiculo,font=('Arial', 11),textvariable=expiTarjeta,bd=2)
    expiTarjetaEny.place(x=270,y=450)
    
    cvvlbl = Label(topVehiculo,font=('Arial', 12),fg='#011736',text='CVV: ',bg='gray')
    cvvlbl.place(x=208,y=500) 
    cvvEny = Entry(topVehiculo,font=('Arial', 11),textvariable=cvv,bd=2)
    cvvEny.place(x=270,y=500)
        
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
                    numTarjeta_value = int(numTarjeta.get())
                    
                    if not re.match(r'^\d{16}$', numTarjeta.get()):
                        messagebox.showerror("Error", "El número de tarjeta debe tener 16 dígitos.")
                        return
                    if not re.match(r'^\d{3}$', cvv.get()):
                        messagebox.showerror("Error", "El CVV debe tener 3 dígitos.")
                        return
                    
                    # Validación de la fecha de expiración de la tarjeta
                    try:
                        formato_fechatj = "%m-%y"
                        fecha_caducidad = datetime.strptime(expiTarjeta.get(), formato_fechatj)
                    except ValueError:
                        messagebox.showerror("Error", "Formato de fecha incorrecto. Usa el formato mm-yy")
                        return
                    
                    # Validación de fechas de renta
                    formato_fecha = "%Y-%m-%d"
                    salida = fechaSalida.get()
                    llegada = fechaLlegada.get()
        
                    try:
                        fecha_salida = datetime.strptime(salida, formato_fecha)
                        fecha_llegada = datetime.strptime(llegada, formato_fecha)
            
                        if fecha_salida >= fecha_llegada:
                            messagebox.showerror("Error", "La fecha de renta debe ser anterior a la fecha de devolución.")
                            return
                        
                        if fecha_llegada < datetime.today():
                            messagebox.showerror("Error", "La fecha de llegada no puede ser una fecha pasada.")
                            return
                    except ValueError:
                        messagebox.showerror("Error", "Formato de fecha incorrecto. Usa el formato yyyy-mm-dd.")
                        return
                    
                    # Verificar la disponibilidad del vehículo
                    disponibilidad = operations.verificar_disponibilidad_vehiculo(vehiculo=tipo, id_tipo=cocheID, fecha_salida=fecha_salida, fecha_llegada=fecha_llegada)
                    if not disponibilidad:
                        messagebox.showerror("Error", "El vehículo no está disponible en las fechas seleccionadas.")
                        return
                    
                    dias = (fecha_llegada - fecha_salida).days
                    if dias <= 0:
                        messagebox.showerror("Error", "Las fechas de alquiler no son válidas.")
                        return
                
                    vehiculoNom = 'Tesla Model 3 Standard Range Plus'
                    costoDia = 128
                    
                    monto = (dias + 1) * costoDia
                                     
                    
                    
                    ans = messagebox.askquestion('Transacción',f'Su cuenta sería un total de {monto} dólares.')
                    if ans == 'yes':
                        sucursal_id = getSucursalID(sucursal= sucursalSeleccionada.get())
                        txt = f'Transacción exitosa. Usted rentó un {vehiculoNom} del {fechaSalida.get()} al {fechaLlegada.get()}. Favor de recoger el vehiculo en la sucursal {sucursalSeleccionada.get()} 1 dia antes de su partida. diario: 4:00 am - 23:59 pm.'
                        operations.reservarDB(vehiculo= tipo,id_tipo= cocheID,sucursal_id= sucursal_id,fechaRenta= salida,fechaDevolucion= llegada,monto= monto)
                        messagebox.showinfo("Transaccion exitosa", txt)
                        
                        if opcion.get() == 1:  # Guardar tarjeta
                            operations.insertTarjeta(nomTitular=titularTarjeta.get(), numTarjeta=numTarjeta.get(), cvv=cvv.get(), expiracion=fecha_caducidad)
                                
                            
                        # Añadir fechas al Listbox de fechas no disponibles
                        fndLbx.delete(0, tk.END)
                        fechas = operations.obtener_fechas_reservadas(vehiculo= tipo,id_tipo= cocheID)
                        
                        if fechas:
                            for fecha in fechas:
                                fndLbx.insert(tk.END, fecha)
                                
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
                    messagebox.showerror("Error", "El CVV y el numero de tarjeta deben contener solo números")
                    return
    
    reservarbnt = Button(topVehiculo,text='    Reservar    ',font=('Arial',12),bg='#C9C0D9',command=reservar)
    reservarbnt.place(x=285,y=565)
    
    fNODisponibleslbl = Label(topVehiculo,text='Fechas NO disponibles:',font=('Arial',12),bg='gray')
    fNODisponibleslbl.place(x=480,y=250)
    
    fechas = operations.obtener_fechas_reservadas(vehiculo= tipo,id_tipo= cocheID)
    fndLbx = Listbox(topVehiculo,width=24,font=('Arial',10))
    fndLbx.place(x=480,y=285)
    if fechas:
        for fecha in fechas:
            fndLbx.insert(tk.END, fecha)
    
    guardarTarjeta = Radiobutton(topVehiculo,font=('Arial', 12,BOLD),fg='#011736',text='Guardar tarjeta',value=1,variable=opcion,bg='gray')
    guardarTarjeta.place(x=40,y=550)
    
    noGuardarTarjeta = Radiobutton(topVehiculo,font=('Arial', 12,BOLD),fg='#011736',text='No guardar tarjeta',value=2,variable=opcion,bg='gray')
    noGuardarTarjeta.place(x=40,y=600)
    
    sucursalSbx = Spinbox(topVehiculo,font=('Arial',12),values=('Seleccione una sucursal','Zapopan','Guadalajara','Tonala'), textvariable=sucursalSeleccionada)
    sucursalSbx.place(x=480,y=490)
    
    topVehiculo.mainloop()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def infoPanelCar8():
    topVehiculo = Toplevel()
    topVehiculo.title('Electric Cars Information')
    topVehiculo.iconbitmap('./images/CarIcon.ico')
    topVehiculo.geometry('700x650')
    topVehiculo.config(bg='gray')
    utl.center_window(topVehiculo,700,650)
    topVehiculo.resizable(width=False, height=False)
    
    vehiculo = utl.read_Image('./images/cars/RenaultZoe.png',(200, 170))
    
    vehiculolbl = Label(topVehiculo, image=vehiculo, bd=0)
    vehiculolbl.place(x=40, y=55)  
    
    txtVehiculo1 = 'Renault Zoe\nCapacidad: 5 personas\nMaletero: 338 lts\nAutonomia: 395 km\nPotencia: 135 hp\nVelocidad máxima: 140 km/h\nTiempo de carga: 8 hrs (cargador nivel 2),\n1 hora (carga rápida)\nSeguro: Sí\n$45 dls /day'
    infoVehiculo = Label(topVehiculo,wraplength=800,text=txtVehiculo1,font=('Arial', 12),anchor='w',justify='left',bg='gray',fg='#011736')
    infoVehiculo.place(x=270,y=40)
    
    tipo = 'coche'
    cocheID = 9
    
    
    fechaSalida = StringVar()
    fechaLlegada = StringVar()
    titularTarjeta = StringVar()
    numTarjeta = StringVar()
    expiTarjeta = StringVar()
    cvv = StringVar()
    sucursalSeleccionada = StringVar()
    opcion = IntVar()
    
    # Obtener fechas de salida y llegada
    fecha_salida = fechaSalida.get()
    fecha_llegada = fechaLlegada.get()

    # Verificar disponibilidad
    disponibilidad = operations.verificar_disponibilidad_vehiculo(vehiculo=tipo, id_tipo=cocheID, fecha_salida=fecha_salida, fecha_llegada=fecha_llegada)
    
    if disponibilidad:
        estado = 'DISPONIBLE'
    else:
        estado = 'EN MANTENIMIENTO'
    
    estadolbl = Label(topVehiculo,text='Estado: '+estado,fg='#011736',font=('Arial', 12,BOLD),bg='gray')
    estadolbl.place(x=30,y=20)
    
        
    fechaSalidalbl = Label(topVehiculo,font=('Arial', 12),fg='#011736',text='Fecha de renta (yyyy-mm-dd): ',bg='gray')
    fechaSalidalbl.place(x=40,y=250) 
    fSalida = Entry(topVehiculo,font=('Arial', 11),textvariable=fechaSalida,bd=2)
    fSalida.place(x=270,y=250)
    
    fechaLlegadalbl = Label(topVehiculo,font=('Arial', 12),fg='#011736',text='Fecha devolución (yyyy-mm-dd): ',bg='gray')
    fechaLlegadalbl.place(x=40,y=300) 
    fLlegada = Entry(topVehiculo,font=('Arial', 11),textvariable=fechaLlegada,bd=2)
    fLlegada.place(x=270,y=300)   
    
    titularTarjetalbl = Label(topVehiculo,font=('Arial', 12),fg='#011736',text='Titular de la tarjeta: ',bg='gray')
    titularTarjetalbl.place(x=112,y=350) 
    titularTarjetaEny = Entry(topVehiculo,font=('Arial', 11),textvariable=titularTarjeta,bd=2)
    titularTarjetaEny.place(x=270,y=350)
    
    numTarjetalbl = Label(topVehiculo,font=('Arial', 12),fg='#011736',text='Numero de tarjeta: ',bg='gray')
    numTarjetalbl.place(x=112,y=400) 
    numTarjetaEny = Entry(topVehiculo,font=('Arial', 11),textvariable=numTarjeta,bd=2)
    numTarjetaEny.place(x=270,y=400)
    
    expiTarjetalbl = Label(topVehiculo,font=('Arial', 12),fg='#011736',text='Fecha de expiracion (mm-yy): ',bg='gray')
    expiTarjetalbl.place(x=40,y=450) 
    expiTarjetaEny = Entry(topVehiculo,font=('Arial', 11),textvariable=expiTarjeta,bd=2)
    expiTarjetaEny.place(x=270,y=450)
    
    cvvlbl = Label(topVehiculo,font=('Arial', 12),fg='#011736',text='CVV: ',bg='gray')
    cvvlbl.place(x=208,y=500) 
    cvvEny = Entry(topVehiculo,font=('Arial', 11),textvariable=cvv,bd=2)
    cvvEny.place(x=270,y=500)
        
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
                    numTarjeta_value = int(numTarjeta.get())
                    
                    if not re.match(r'^\d{16}$', numTarjeta.get()):
                        messagebox.showerror("Error", "El número de tarjeta debe tener 16 dígitos.")
                        return
                    if not re.match(r'^\d{3}$', cvv.get()):
                        messagebox.showerror("Error", "El CVV debe tener 3 dígitos.")
                        return
                    
                    # Validación de la fecha de expiración de la tarjeta
                    try:
                        formato_fechatj = "%m-%y"
                        fecha_caducidad = datetime.strptime(expiTarjeta.get(), formato_fechatj)
                    except ValueError:
                        messagebox.showerror("Error", "Formato de fecha incorrecto. Usa el formato mm-yy")
                        return
                    
                    # Validación de fechas de renta
                    formato_fecha = "%Y-%m-%d"
                    salida = fechaSalida.get()
                    llegada = fechaLlegada.get()
        
                    try:
                        fecha_salida = datetime.strptime(salida, formato_fecha)
                        fecha_llegada = datetime.strptime(llegada, formato_fecha)
            
                        if fecha_salida >= fecha_llegada:
                            messagebox.showerror("Error", "La fecha de renta debe ser anterior a la fecha de devolución.")
                            return
                        
                        if fecha_llegada < datetime.today():
                            messagebox.showerror("Error", "La fecha de llegada no puede ser una fecha pasada.")
                            return
                    except ValueError:
                        messagebox.showerror("Error", "Formato de fecha incorrecto. Usa el formato yyyy-mm-dd.")
                        return
                    
                    # Verificar la disponibilidad del vehículo
                    disponibilidad = operations.verificar_disponibilidad_vehiculo(vehiculo=tipo, id_tipo=cocheID, fecha_salida=fecha_salida, fecha_llegada=fecha_llegada)
                    if not disponibilidad:
                        messagebox.showerror("Error", "El vehículo no está disponible en las fechas seleccionadas.")
                        return
                    
                    dias = (fecha_llegada - fecha_salida).days
                    if dias <= 0:
                        messagebox.showerror("Error", "Las fechas de alquiler no son válidas.")
                        return
                
                    vehiculoNom = 'Renault Zoe'
                    costoDia = 45  
                    
                    monto = (dias + 1) * costoDia
                                     
                    
                    
                    ans = messagebox.askquestion('Transacción',f'Su cuenta sería un total de {monto} dólares.')
                    if ans == 'yes':
                        sucursal_id = getSucursalID(sucursal= sucursalSeleccionada.get())
                        txt = f'Transacción exitosa. Usted rentó un {vehiculoNom} del {fechaSalida.get()} al {fechaLlegada.get()}. Favor de recoger el vehiculo en la sucursal {sucursalSeleccionada.get()} 1 dia antes de su partida. diario: 4:00 am - 23:59 pm.'
                        operations.reservarDB(vehiculo= tipo,id_tipo= cocheID,sucursal_id= sucursal_id,fechaRenta= salida,fechaDevolucion= llegada,monto= monto)
                        messagebox.showinfo("Transaccion exitosa", txt)
                        
                        if opcion.get() == 1:  # Guardar tarjeta
                            operations.insertTarjeta(nomTitular=titularTarjeta.get(), numTarjeta=numTarjeta.get(), cvv=cvv.get(), expiracion=fecha_caducidad)
                                
                            
                        # Añadir fechas al Listbox de fechas no disponibles
                        fndLbx.delete(0, tk.END)
                        fechas = operations.obtener_fechas_reservadas(vehiculo= tipo,id_tipo= cocheID)
                        
                        if fechas:
                            for fecha in fechas:
                                fndLbx.insert(tk.END, fecha)
                                
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
                    messagebox.showerror("Error", "El CVV y el numero de tarjeta deben contener solo números")
                    return
    
    reservarbnt = Button(topVehiculo,text='    Reservar    ',font=('Arial',12),bg='#C9C0D9',command=reservar)
    reservarbnt.place(x=285,y=565)
    
    fNODisponibleslbl = Label(topVehiculo,text='Fechas NO disponibles:',font=('Arial',12),bg='gray')
    fNODisponibleslbl.place(x=480,y=250)
    
    fechas = operations.obtener_fechas_reservadas(vehiculo= tipo,id_tipo= cocheID)
    fndLbx = Listbox(topVehiculo,width=24,font=('Arial',10))
    fndLbx.place(x=480,y=285)
    if fechas:
        for fecha in fechas:
            fndLbx.insert(tk.END, fecha)
    
    guardarTarjeta = Radiobutton(topVehiculo,font=('Arial', 12,BOLD),fg='#011736',text='Guardar tarjeta',value=1,variable=opcion,bg='gray')
    guardarTarjeta.place(x=40,y=550)
    
    noGuardarTarjeta = Radiobutton(topVehiculo,font=('Arial', 12,BOLD),fg='#011736',text='No guardar tarjeta',value=2,variable=opcion,bg='gray')
    noGuardarTarjeta.place(x=40,y=600)
    
    sucursalSbx = Spinbox(topVehiculo,font=('Arial',12),values=('Seleccione una sucursal','Zapopan','Guadalajara','Tonala'), textvariable=sucursalSeleccionada)
    sucursalSbx.place(x=480,y=490)
    
    topVehiculo.mainloop()