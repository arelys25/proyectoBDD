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

def infoPanelBk1 ():
    topVehiculo = Toplevel()
    topVehiculo.title('Electric Bike Information')
    topVehiculo.iconbitmap('./images/CarIcon.ico')
    topVehiculo.geometry('700x650')
    topVehiculo.config(bg='gray')
    utl.center_window(topVehiculo,700,650)
    topVehiculo.resizable(width=False, height=False)
    
    # Leer y cargar la imagen
    vehiculo = utl.read_Image('./images/bikes/Allant7.png',(200, 170))
    
    vehiculolbl = Label(topVehiculo, image=vehiculo, bd=0)
    vehiculolbl.place(x=40, y=55)  
    
    txtVehiculo1 = 'Trek Allant+7\nVelocidad máx: 32 km/h\nPeso máx: 136 kg\nAccesorio: Portaequipaje\nPeso: 23.5 kg\nTiempo de carga: 5 hrs\nPlegable: No\nVoltaje: 36 V\nSeguro: Sí\n$16 dls /dia'
    infoVehiculo = Label(topVehiculo,wraplength=800,text=txtVehiculo1,fg='#011736',font=('Arial', 12),anchor='w',justify='left',bg='gray')
    infoVehiculo.place(x=270,y=40)
    
    tipo = 'bike'
    bikeID = 7
    
    
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
    disponibilidad = operations.verificar_disponibilidad_vehiculo(vehiculo=tipo, id_tipo=bikeID, fecha_salida=fecha_salida, fecha_llegada=fecha_llegada)
    
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
                    disponibilidad = operations.verificar_disponibilidad_vehiculo(vehiculo=tipo, id_tipo=bikeID, fecha_salida=fecha_salida, fecha_llegada=fecha_llegada)
                    if not disponibilidad:
                        messagebox.showerror("Error", "El vehículo no está disponible en las fechas seleccionadas.")
                        return
                    
                    dias = (fecha_llegada - fecha_salida).days
                    if dias <= 0:
                        messagebox.showerror("Error", "Las fechas de alquiler no son válidas.")
                        return
                
                    vehiculoNom = 'Trek Allant+7'
                    
                    costoDia = 16
                    
                    monto = (dias + 1) * costoDia
                                     
                    
                    
                    ans = messagebox.askquestion('Transacción',f'Su cuenta sería un total de {monto} dólares.')
                    if ans == 'yes':
                        sucursal_id = getSucursalID(sucursal= sucursalSeleccionada.get())
                        txt = f'Transacción exitosa. Usted rentó un {vehiculoNom} del {fechaSalida.get()} al {fechaLlegada.get()}. Favor de recoger el vehiculo en la sucursal {sucursalSeleccionada.get()} 1 dia antes de su partida. diario: 4:00 am - 23:59 pm.'
                        operations.reservarDB(vehiculo= tipo,id_tipo= bikeID,sucursal_id= sucursal_id,fechaRenta= salida,fechaDevolucion= llegada,monto= monto)
                        messagebox.showinfo("Transaccion exitosa", txt)
                        
                        if opcion.get() == 1:  # Guardar tarjeta
                            operations.insertTarjeta(nomTitular=titularTarjeta.get(), numTarjeta=numTarjeta.get(), cvv=cvv.get(), expiracion=fecha_caducidad)
                                
                            
                        # Añadir fechas al Listbox de fechas no disponibles
                        fndLbx.delete(0, tk.END)
                        fechas = operations.obtener_fechas_reservadas(vehiculo= tipo,id_tipo= bikeID)
                        
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
    
    fechas = operations.obtener_fechas_reservadas(vehiculo= tipo,id_tipo= bikeID)
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
def infoPanelBk2():
    topVehiculo = Toplevel()
    topVehiculo.title('Electric Bike Information')
    topVehiculo.iconbitmap('./images/CarIcon.ico')
    topVehiculo.geometry('700x650')
    topVehiculo.config(bg='gray')
    utl.center_window(topVehiculo,700,650)
    topVehiculo.resizable(width=False, height=False)
    
    # Leer y cargar la imagen
    vehiculo = utl.read_Image('./images/bikes/D11.png',(200, 170)) 
    vehiculolbl = Label(topVehiculo, image=vehiculo, bd=0)
    vehiculolbl.place(x=40, y=55)
    txtVehiculo1 = 'Fiido D11\nVelocidad máx: 25 km/h\nPeso máx: 120 kg\nAccesorio: Portaequipaje\nPeso: 12.9 kg\nTiempo de carga: 5 hrs\nPlegable: Sí\nVoltaje: 36 V\nSeguro: Sí\n$8 dls /hora'
    infoVehiculo = Label(topVehiculo,wraplength=800,text=txtVehiculo1,font=('Arial', 12),anchor='w',justify='left',bg='gray')
    infoVehiculo.place(x=270,y=40)
    
    tipo = 'bike'
    bikeID = 8
    
    
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
    disponibilidad = operations.verificar_disponibilidad_vehiculo(vehiculo=tipo, id_tipo=bikeID, fecha_salida=fecha_salida, fecha_llegada=fecha_llegada)
    
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
                    disponibilidad = operations.verificar_disponibilidad_vehiculo(vehiculo=tipo, id_tipo=bikeID, fecha_salida=fecha_salida, fecha_llegada=fecha_llegada)
                    if not disponibilidad:
                        messagebox.showerror("Error", "El vehículo no está disponible en las fechas seleccionadas.")
                        return
                    
                    dias = (fecha_llegada - fecha_salida).days
                    if dias <= 0:
                        messagebox.showerror("Error", "Las fechas de alquiler no son válidas.")
                        return
                
                    vehiculoNom = 'Fiido D11'
                    costoDia = 16 
                    
                    monto = (dias + 1) * costoDia
                                     
                    
                    
                    ans = messagebox.askquestion('Transacción',f'Su cuenta sería un total de {monto} dólares.')
                    if ans == 'yes':
                        sucursal_id = getSucursalID(sucursal= sucursalSeleccionada.get())
                        txt = f'Transacción exitosa. Usted rentó un {vehiculoNom} del {fechaSalida.get()} al {fechaLlegada.get()}. Favor de recoger el vehiculo en la sucursal {sucursalSeleccionada.get()} 1 dia antes de su partida. diario: 4:00 am - 23:59 pm.'
                        operations.reservarDB(vehiculo= tipo,id_tipo= bikeID,sucursal_id= sucursal_id,fechaRenta= salida,fechaDevolucion= llegada,monto= monto)
                        messagebox.showinfo("Transaccion exitosa", txt)
                        
                        if opcion.get() == 1:  # Guardar tarjeta
                            operations.insertTarjeta(nomTitular=titularTarjeta.get(), numTarjeta=numTarjeta.get(), cvv=cvv.get(), expiracion=fecha_caducidad)
                                
                            
                        # Añadir fechas al Listbox de fechas no disponibles
                        fndLbx.delete(0, tk.END)
                        fechas = operations.obtener_fechas_reservadas(vehiculo= tipo,id_tipo= bikeID)
                        
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
    
    fechas = operations.obtener_fechas_reservadas(vehiculo= tipo,id_tipo= bikeID)
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
def infoPanelBk3():
    topVehiculo = Toplevel()
    topVehiculo.title('Electric Bike Information')
    topVehiculo.iconbitmap('./images/CarIcon.ico')
    topVehiculo.geometry('700x650')
    topVehiculo.config(bg='gray')
    utl.center_window(topVehiculo,700,650)
    topVehiculo.resizable(width=False, height=False)
    
    # Leer y cargar la imagen
    vehiculo = utl.read_Image('./images/bikes/ElectricCLine.png',(200, 170))
    vehiculolbl = Label(topVehiculo, image=vehiculo, bd=0)
    vehiculolbl.place(x=40, y=55) 
    txtVehiculo1 = 'Brompton Electric C Line\nVelocidad máx: 25 km/h\nPeso máx: 105 kg\nAccesorio: Bolsa de transporte\nPeso: 13.7 kg\nTiempo de carga: 4 hrs\nPlegable: Sí\nVoltaje: 36 V\nSeguro: Sí\n$12 dls /dia'
    infoVehiculo = Label(topVehiculo,wraplength=800,text=txtVehiculo1,font=('Arial', 12),anchor='w',justify='left',bg='gray')
    infoVehiculo.place(x=270,y=40)
    
    tipo = 'bike'
    bikeID = 1
    
    
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
    disponibilidad = operations.verificar_disponibilidad_vehiculo(vehiculo=tipo, id_tipo=bikeID, fecha_salida=fecha_salida, fecha_llegada=fecha_llegada)
    
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
                    disponibilidad = operations.verificar_disponibilidad_vehiculo(vehiculo=tipo, id_tipo=bikeID, fecha_salida=fecha_salida, fecha_llegada=fecha_llegada)
                    if not disponibilidad:
                        messagebox.showerror("Error", "El vehículo no está disponible en las fechas seleccionadas.")
                        return
                    
                    dias = (fecha_llegada - fecha_salida).days
                    if dias <= 0:
                        messagebox.showerror("Error", "Las fechas de alquiler no son válidas.")
                        return
                
                    vehiculoNom = 'Brompton Electric C Line'
                    costoDia = 12
                    
                    monto = (dias + 1) * costoDia
                                     
                    
                    
                    ans = messagebox.askquestion('Transacción',f'Su cuenta sería un total de {monto} dólares.')
                    if ans == 'yes':
                        sucursal_id = getSucursalID(sucursal= sucursalSeleccionada.get())
                        txt = f'Transacción exitosa. Usted rentó un {vehiculoNom} del {fechaSalida.get()} al {fechaLlegada.get()}. Favor de recoger el vehiculo en la sucursal {sucursalSeleccionada.get()} 1 dia antes de su partida. diario: 4:00 am - 23:59 pm.'
                        operations.reservarDB(vehiculo= tipo,id_tipo= bikeID,sucursal_id= sucursal_id,fechaRenta= salida,fechaDevolucion= llegada,monto= monto)
                        messagebox.showinfo("Transaccion exitosa", txt)
                        
                        if opcion.get() == 1:  # Guardar tarjeta
                            operations.insertTarjeta(nomTitular=titularTarjeta.get(), numTarjeta=numTarjeta.get(), cvv=cvv.get(), expiracion=fecha_caducidad)
                                
                            
                        # Añadir fechas al Listbox de fechas no disponibles
                        fndLbx.delete(0, tk.END)
                        fechas = operations.obtener_fechas_reservadas(vehiculo= tipo,id_tipo= bikeID)
                        
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
    
    fechas = operations.obtener_fechas_reservadas(vehiculo= tipo,id_tipo= bikeID)
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
def infoPanelBk4():
    topVehiculo = Toplevel()
    topVehiculo.title('Electric Bike Information')
    topVehiculo.iconbitmap('./images/CarIcon.ico')
    topVehiculo.geometry('700x650')
    topVehiculo.config(bg='gray')
    utl.center_window(topVehiculo,700,650)
    topVehiculo.resizable(width=False, height=False)
    
    # Leer y cargar la imagen
    vehiculo = utl.read_Image('./images/bikes/HimoC26.png',(200, 170))
    vehiculolbl = Label(topVehiculo, image=vehiculo, bd=0)
    vehiculolbl.place(x=40, y=55)
    txtVehiculo1 = 'Xiaomi Himo C26\nVelocidad máx: 25 km/h\nPeso máx: 100 kg\nAccesorio: Pantalla LCD\nPeso: 25 kg\nTiempo de carga: 6 hrs\nPlegable: No\nVoltaje: 48 V\nSeguro: Sí\n$6 dls /dia'
    infoVehiculo = Label(topVehiculo,wraplength=800,text=txtVehiculo1,font=('Arial', 12),anchor='w',justify='left',bg='gray')
    infoVehiculo.place(x=270,y=40)
    
    tipo = 'bike'
    bikeID = 3
    
    
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
    disponibilidad = operations.verificar_disponibilidad_vehiculo(vehiculo=tipo, id_tipo=bikeID, fecha_salida=fecha_salida, fecha_llegada=fecha_llegada)
    
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
                    disponibilidad = operations.verificar_disponibilidad_vehiculo(vehiculo=tipo, id_tipo=bikeID, fecha_salida=fecha_salida, fecha_llegada=fecha_llegada)
                    if not disponibilidad:
                        messagebox.showerror("Error", "El vehículo no está disponible en las fechas seleccionadas.")
                        return
                    
                    dias = (fecha_llegada - fecha_salida).days
                    if dias <= 0:
                        messagebox.showerror("Error", "Las fechas de alquiler no son válidas.")
                        return
                
                    vehiculoNom = 'Xiaomi Himo C26'
                    costoDia = 6
                    
                    monto = (dias + 1) * costoDia
                                     
                    
                    
                    ans = messagebox.askquestion('Transacción',f'Su cuenta sería un total de {monto} dólares.')
                    if ans == 'yes':
                        sucursal_id = getSucursalID(sucursal= sucursalSeleccionada.get())
                        txt = f'Transacción exitosa. Usted rentó un {vehiculoNom} del {fechaSalida.get()} al {fechaLlegada.get()}. Favor de recoger el vehiculo en la sucursal {sucursalSeleccionada.get()} 1 dia antes de su partida. diario: 4:00 am - 23:59 pm.'
                        operations.reservarDB(vehiculo= tipo,id_tipo= bikeID,sucursal_id= sucursal_id,fechaRenta= salida,fechaDevolucion= llegada,monto= monto)
                        messagebox.showinfo("Transaccion exitosa", txt)
                        
                        if opcion.get() == 1:  # Guardar tarjeta
                            operations.insertTarjeta(nomTitular=titularTarjeta.get(), numTarjeta=numTarjeta.get(), cvv=cvv.get(), expiracion=fecha_caducidad)
                                
                            
                        # Añadir fechas al Listbox de fechas no disponibles
                        fndLbx.delete(0, tk.END)
                        fechas = operations.obtener_fechas_reservadas(vehiculo= tipo,id_tipo= bikeID)
                        
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
    
    fechas = operations.obtener_fechas_reservadas(vehiculo= tipo,id_tipo= bikeID)
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
def infoPanelBk5():
    topVehiculo = Toplevel()
    topVehiculo.title('Electric Bike Information')
    topVehiculo.iconbitmap('./images/CarIcon.ico')
    topVehiculo.geometry('700x650')
    topVehiculo.config(bg='gray')
    utl.center_window(topVehiculo,700,650)
    topVehiculo.resizable(width=False, height=False)
    
    # Leer y cargar la imagen
    vehiculo = utl.read_Image('./images/bikes/PowerPlus.png',(200, 170))
    vehiculolbl = Label(topVehiculo, image=vehiculo, bd=0)
    vehiculolbl.place(x=40, y=55)
    txtVehiculo1 = 'Ancheer Power Plus\nVelocidad máx: 25 km/h\nPeso máx: 120 kg\nAccesorio: Guardabarros\nPeso: 23 kg\nTiempo de carga: 6 hrs\nPlegable: Sí\nVoltaje: 36 V\nSeguro: Sí\n$7 dls /dia'
    infoVehiculo = Label(topVehiculo,wraplength=800,text=txtVehiculo1,font=('Arial', 12),anchor='w',justify='left',bg='gray')
    infoVehiculo.place(x=270,y=40)
    
    tipo = 'bike'
    bikeID = 4
    
    
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
    disponibilidad = operations.verificar_disponibilidad_vehiculo(vehiculo=tipo, id_tipo=bikeID, fecha_salida=fecha_salida, fecha_llegada=fecha_llegada)
    
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
                    disponibilidad = operations.verificar_disponibilidad_vehiculo(vehiculo=tipo, id_tipo=bikeID, fecha_salida=fecha_salida, fecha_llegada=fecha_llegada)
                    if not disponibilidad:
                        messagebox.showerror("Error", "El vehículo no está disponible en las fechas seleccionadas.")
                        return
                    
                    dias = (fecha_llegada - fecha_salida).days
                    if dias <= 0:
                        messagebox.showerror("Error", "Las fechas de alquiler no son válidas.")
                        return
                
                    vehiculoNom = 'Ancheer Power Plus'
                    costoDia = 7 
                    
                    monto = (dias + 1) * costoDia
                                     
                    
                    
                    ans = messagebox.askquestion('Transacción',f'Su cuenta sería un total de {monto} dólares.')
                    if ans == 'yes':
                        sucursal_id = getSucursalID(sucursal= sucursalSeleccionada.get())
                        txt = f'Transacción exitosa. Usted rentó un {vehiculoNom} del {fechaSalida.get()} al {fechaLlegada.get()}. Favor de recoger el vehiculo en la sucursal {sucursalSeleccionada.get()} 1 dia antes de su partida. diario: 4:00 am - 23:59 pm.'
                        operations.reservarDB(vehiculo= tipo,id_tipo= bikeID,sucursal_id= sucursal_id,fechaRenta= salida,fechaDevolucion= llegada,monto= monto)
                        messagebox.showinfo("Transaccion exitosa", txt)
                        
                        if opcion.get() == 1:  # Guardar tarjeta
                            operations.insertTarjeta(nomTitular=titularTarjeta.get(), numTarjeta=numTarjeta.get(), cvv=cvv.get(), expiracion=fecha_caducidad)
                                
                            
                        # Añadir fechas al Listbox de fechas no disponibles
                        fndLbx.delete(0, tk.END)
                        fechas = operations.obtener_fechas_reservadas(vehiculo= tipo,id_tipo= bikeID)
                        
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
    
    fechas = operations.obtener_fechas_reservadas(vehiculo= tipo,id_tipo= bikeID)
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
def infoPanelBk6():
    topVehiculo = Toplevel()
    topVehiculo.title('Electric Bike Information')
    topVehiculo.iconbitmap('./images/CarIcon.ico')
    topVehiculo.geometry('700x650')
    topVehiculo.config(bg='gray')
    utl.center_window(topVehiculo,700,650)
    topVehiculo.resizable(width=False, height=False)
    
    # Leer y cargar la imagen
    vehiculo = utl.read_Image('./images/bikes/Supercharger2.png',(200, 170)) 
    vehiculolbl = Label(topVehiculo, image=vehiculo, bd=0)
    vehiculolbl.place(x=40, y=55)
    txtVehiculo1 = 'Riese & Müller Supercharger2\nVelocidad máx: 45 km/h\nPeso máx: 140 kg\nAccesorio: Pantalla Bosch Kiox\nPeso: 28 kg\nTiempo de carga: 6 hrs\nPlegable: Sí\nVoltaje: 36 V\nSeguro: Sí\n$20 dls /dia'
    infoVehiculo = Label(topVehiculo,wraplength=800,text=txtVehiculo1,font=('Arial', 12),anchor='w',justify='left',bg='gray')
    infoVehiculo.place(x=270,y=40)
    
    tipo = 'bike'
    bikeID = 5
    
    
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
    disponibilidad = operations.verificar_disponibilidad_vehiculo(vehiculo=tipo, id_tipo=bikeID, fecha_salida=fecha_salida, fecha_llegada=fecha_llegada)
    
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
                    disponibilidad = operations.verificar_disponibilidad_vehiculo(vehiculo=tipo, id_tipo=bikeID, fecha_salida=fecha_salida, fecha_llegada=fecha_llegada)
                    if not disponibilidad:
                        messagebox.showerror("Error", "El vehículo no está disponible en las fechas seleccionadas.")
                        return
                    
                    dias = (fecha_llegada - fecha_salida).days
                    if dias <= 0:
                        messagebox.showerror("Error", "Las fechas de alquiler no son válidas.")
                        return
                
                    vehiculoNom = 'Riese & Müller Supercharger2'
                    costoDia = 20 
                    
                    monto = (dias + 1) * costoDia
                                     
                    
                    
                    ans = messagebox.askquestion('Transacción',f'Su cuenta sería un total de {monto} dólares.')
                    if ans == 'yes':
                        sucursal_id = getSucursalID(sucursal= sucursalSeleccionada.get())
                        txt = f'Transacción exitosa. Usted rentó un {vehiculoNom} del {fechaSalida.get()} al {fechaLlegada.get()}. Favor de recoger el vehiculo en la sucursal {sucursalSeleccionada.get()} 1 dia antes de su partida. diario: 4:00 am - 23:59 pm.'
                        operations.reservarDB(vehiculo= tipo,id_tipo= bikeID,sucursal_id= sucursal_id,fechaRenta= salida,fechaDevolucion= llegada,monto= monto)
                        messagebox.showinfo("Transaccion exitosa", txt)
                        
                        if opcion.get() == 1:  # Guardar tarjeta
                            operations.insertTarjeta(nomTitular=titularTarjeta.get(), numTarjeta=numTarjeta.get(), cvv=cvv.get(), expiracion=fecha_caducidad)
                                
                            
                        # Añadir fechas al Listbox de fechas no disponibles
                        fndLbx.delete(0, tk.END)
                        fechas = operations.obtener_fechas_reservadas(vehiculo= tipo,id_tipo= bikeID)
                        
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
    
    fechas = operations.obtener_fechas_reservadas(vehiculo= tipo,id_tipo= bikeID)
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
def infoPanelBk7():
    topVehiculo = Toplevel()
    topVehiculo.title('Electric Bike Information')
    topVehiculo.iconbitmap('./images/CarIcon.ico')
    topVehiculo.geometry('700x650')
    topVehiculo.config(bg='gray')
    utl.center_window(topVehiculo,700,650)
    topVehiculo.resizable(width=False, height=False)
    
    # Leer y cargar la imagen
    vehiculo = utl.read_Image('./images/bikes/TurboVadoSL40.png',(200, 170))
    vehiculolbl = Label(topVehiculo, image=vehiculo, bd=0)
    vehiculolbl.place(x=40, y=55) 
    txtVehiculo1 = 'Specialized Turbo Vado SL 4.0\nVelocidad máx: 45 km/h\nPeso máx: 120 kg\nAccesorio: Portaequipaje\nPeso: 14.9 kg\nTiempo de carga: 3 hrs\nPlegable: No\nVoltaje: 36 V\nSeguro: Sí\n$15 dls /dia'
    infoVehiculo = Label(topVehiculo,wraplength=800,text=txtVehiculo1,font=('Arial', 12),anchor='w',justify='left',bg='gray')
    infoVehiculo.place(x=270,y=40)
    
    tipo = 'bike'
    bikeID = 2
    
    
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
    disponibilidad = operations.verificar_disponibilidad_vehiculo(vehiculo=tipo, id_tipo=bikeID, fecha_salida=fecha_salida, fecha_llegada=fecha_llegada)
    
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
                    disponibilidad = operations.verificar_disponibilidad_vehiculo(vehiculo=tipo, id_tipo=bikeID, fecha_salida=fecha_salida, fecha_llegada=fecha_llegada)
                    if not disponibilidad:
                        messagebox.showerror("Error", "El vehículo no está disponible en las fechas seleccionadas.")
                        return
                    
                    dias = (fecha_llegada - fecha_salida).days
                    if dias <= 0:
                        messagebox.showerror("Error", "Las fechas de alquiler no son válidas.")
                        return
                
                    vehiculoNom = 'Specialized Turbo Vado SL 4.0'
                    costoDia = 15 
                    
                    monto = (dias + 1) * costoDia
                                     
                    
                    
                    ans = messagebox.askquestion('Transacción',f'Su cuenta sería un total de {monto} dólares.')
                    if ans == 'yes':
                        sucursal_id = getSucursalID(sucursal= sucursalSeleccionada.get())
                        txt = f'Transacción exitosa. Usted rentó un {vehiculoNom} del {fechaSalida.get()} al {fechaLlegada.get()}. Favor de recoger el vehiculo en la sucursal {sucursalSeleccionada.get()} 1 dia antes de su partida. diario: 4:00 am - 23:59 pm.'
                        operations.reservarDB(vehiculo= tipo,id_tipo= bikeID,sucursal_id= sucursal_id,fechaRenta= salida,fechaDevolucion= llegada,monto= monto)
                        messagebox.showinfo("Transaccion exitosa", txt)
                        
                        if opcion.get() == 1:  # Guardar tarjeta
                            operations.insertTarjeta(nomTitular=titularTarjeta.get(), numTarjeta=numTarjeta.get(), cvv=cvv.get(), expiracion=fecha_caducidad)
                                
                            
                        # Añadir fechas al Listbox de fechas no disponibles
                        fndLbx.delete(0, tk.END)
                        fechas = operations.obtener_fechas_reservadas(vehiculo= tipo,id_tipo= bikeID)
                        
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
    
    fechas = operations.obtener_fechas_reservadas(vehiculo= tipo,id_tipo= bikeID)
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
def infoPanelBk8():
    topVehiculo = Toplevel()
    topVehiculo.title('Electric Bike Information')
    topVehiculo.iconbitmap('./images/CarIcon.ico')
    topVehiculo.geometry('700x650')
    topVehiculo.config(bg='gray')
    utl.center_window(topVehiculo,700,650)
    topVehiculo.resizable(width=False, height=False)
    
    # Leer y cargar la imagen
    vehiculo = utl.read_Image('./images/bikes/VanMoofS3.png',(200, 170))
    vehiculolbl = Label(topVehiculo, image=vehiculo, bd=0)
    vehiculolbl.place(x=40, y=55) 
    txtVehiculo1 = 'VanMoof S3\nVelocidad máx: 32 km/h\nPeso máx: 120 kg\nAccesorio: Bloqueo inteligente\nPeso: 19 kg\nTiempo de carga: 4 hrs\nPlegable: No\nVoltaje: 36 V\nSeguro: Sí\n$14 dls /dia'
    infoVehiculo = Label(topVehiculo,wraplength=800,text=txtVehiculo1,font=('Arial', 12),anchor='w',justify='left',bg='gray')
    infoVehiculo.place(x=270,y=40)
    
    tipo = 'bike'
    bikeID = 6
    
    
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
    disponibilidad = operations.verificar_disponibilidad_vehiculo(vehiculo=tipo, id_tipo=bikeID, fecha_salida=fecha_salida, fecha_llegada=fecha_llegada)
    
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
                    disponibilidad = operations.verificar_disponibilidad_vehiculo(vehiculo=tipo, id_tipo=bikeID, fecha_salida=fecha_salida, fecha_llegada=fecha_llegada)
                    if not disponibilidad:
                        messagebox.showerror("Error", "El vehículo no está disponible en las fechas seleccionadas.")
                        return
                    
                    dias = (fecha_llegada - fecha_salida).days
                    if dias <= 0:
                        messagebox.showerror("Error", "Las fechas de alquiler no son válidas.")
                        return
                
                    vehiculoNom = 'VanMoof S3'
                    costoDia = 14
                    
                    monto = (dias + 1) * costoDia
                                     
                    
                    
                    ans = messagebox.askquestion('Transacción',f'Su cuenta sería un total de {monto} dólares.')
                    if ans == 'yes':
                        sucursal_id = getSucursalID(sucursal= sucursalSeleccionada.get())
                        txt = f'Transacción exitosa. Usted rentó un {vehiculoNom} del {fechaSalida.get()} al {fechaLlegada.get()}. Favor de recoger el vehiculo en la sucursal {sucursalSeleccionada.get()} 1 dia antes de su partida. diario: 4:00 am - 23:59 pm.'
                        operations.reservarDB(vehiculo= tipo,id_tipo= bikeID,sucursal_id= sucursal_id,fechaRenta= salida,fechaDevolucion= llegada,monto= monto)
                        messagebox.showinfo("Transaccion exitosa", txt)
                        
                        if opcion.get() == 1:  # Guardar tarjeta
                            operations.insertTarjeta(nomTitular=titularTarjeta.get(), numTarjeta=numTarjeta.get(), cvv=cvv.get(), expiracion=fecha_caducidad)
                                
                            
                        # Añadir fechas al Listbox de fechas no disponibles
                        fndLbx.delete(0, tk.END)
                        fechas = operations.obtener_fechas_reservadas(vehiculo= tipo,id_tipo= bikeID)
                        
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
    
    fechas = operations.obtener_fechas_reservadas(vehiculo= tipo,id_tipo= bikeID)
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