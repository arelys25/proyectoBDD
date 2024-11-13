import mysql.connector
from mysql.connector import Error
import hashlib
from tkinter import messagebox


def encrypt_password(password):
    # Aquí puedes usar el algoritmo de hash que uses, por ejemplo SHA256
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

# Función para conectarse a la base de datos
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='HP-LAP-ARELY25',
            database='emobility',
            user='root',
            password='Daniarely3',
            charset='utf8mb4',
            collation='utf8mb4_general_ci',
            port = 3305
        )
        if connection.is_connected():
            print("Conexión a la base de datos exitosa")
        return connection
    except Error as e:
        print(f"Error al conectarse a la base de datos: conection {e}")
        return None
    
# Función para verificar usuario y contraseña
def loginForId(username, password):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            query = """
                SELECT u.ID 
                FROM login l
                JOIN usuarios u ON l.usuario_ID = u.ID
                WHERE u.Email = %s AND l.password = %s
                """
            cursor.execute(query, (username, encrypt_password(password)))

            result = cursor.fetchone()
    
            if result:
                user_id = result['ID']  # Obtén el ID del usuario
                print("ID del usuario:", user_id)
                return user_id
            else:
                print("Usuario o contraseña incorrectos")
                return None
        except Error as e:
            print(f"Error al consultar la base de datos loginForID {e}")
            return False
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                
# conseguir id del vehiculo con el id_tipo
# Función para verificar usuario y contraseña
def searchIDCoche(id_coche):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            query = """
                SELECT ID
                FROM vehiculos
                WHERE id_coche = %s;
                """
            cursor.execute(query, (id_coche,))

            result = cursor.fetchone()
    
            if result:
                vehiculo_id = result['ID']  # Obtén el ID del usuario
                print("ID vehiculo del carro:", vehiculo_id)
                return vehiculo_id
            else:
                print("id_coche incorrecto")
                return None
        except Error as e:
            print(f"Error al consultar la base de datos search coche{e}")
            return False
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                
def searchIDBike(id_bike):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            query = """
                SELECT ID
                FROM vehiculos
                WHERE id_bike = %s;
                """
            cursor.execute(query, (id_bike,))

            result = cursor.fetchone()
    
            if result:
                vehiculo_id = result['ID']  # Obtén el ID del usuario
                print("ID vehiculo de la bicicleta:", vehiculo_id)
                return vehiculo_id
            else:
                print("id incorrecto")
                return None
        except Error as e:
            print(f"Error al consultar la base de datos search bike {e}")
            return False
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                
def searchIDScooter(id_scooter):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            query = """
                SELECT ID
                FROM vehiculos
                WHERE id_scooter = %s;
                """
            cursor.execute(query, (id_scooter,))

            result = cursor.fetchone()
    
            if result:
                vehiculo_id = result['ID']  # Obtén el ID del usuario
                print("ID vehiculo del scooter:", vehiculo_id)
                return vehiculo_id
            else:
                print("id incorrecto")
                return None
        except Error as e:
            print(f"Error al consultar la base de datos search scooter {e}")
            return False
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

# reservar un vehiculo
def reservarDB(vehiculo,id_tipo,sucursal_id,fechaRenta,fechaDevolucion,monto):
    # usuario, id_vehiculo, fechaSalida, fechaLlegada
    connection = create_connection()
    if connection:
        try:
            userNow = 'donova@example.com'
            pswdNow = '1234'
            user_id = loginForId(userNow, pswdNow)
            if user_id:
                print("Usuario autenticado con ID:", user_id)
                
                if vehiculo == 'coche':
                    id_vehiculo =searchIDCoche(id_tipo)
                elif vehiculo == 'bike':
                    id_vehiculo = searchIDBike(id_tipo)
                elif vehiculo == 'scooter':
                    id_vehiculo = searchIDScooter(id_tipo)
                else:
                    print('Vehiculo no valido')
                    return False
                
                # Verificar disponibilidad utilizando la función ya existente
                if not verificar_disponibilidad_vehiculo(vehiculo, id_tipo, fechaRenta, fechaDevolucion):
                    return False  # Si el vehículo no está disponible, salir de la función
                
                cursor = connection.cursor(dictionary=True)
                
                connection.start_transaction()

                # Primera consulta: Insertar en la tabla de reservas
                query_reserva = """
                    INSERT INTO reservas (Usuario_ID, Vehiculo_ID, EstadoReserva, sucursalID, fechaSalida, fechaLlegada, dias)
                    VALUES (%s, %s, 'confirmada', %s, %s, %s, DATEDIFF(%s, %s));
                """
                cursor.execute(query_reserva, (user_id, id_vehiculo, sucursal_id, fechaRenta, fechaDevolucion, fechaDevolucion, fechaRenta))

                # Obtener el ID de la nueva reserva
                cursor.execute("SELECT LAST_INSERT_ID()")
                nueva_reserva_id = cursor.fetchone()['LAST_INSERT_ID()']
                
                # Segunda consulta: Insertar en la tabla de pagos
                query_pago = """
                    INSERT INTO pago (monto, fechaPago, reserva_ID)
                    VALUES (%s, NOW(), %s);
                """
                cursor.execute(query_pago, (monto, nueva_reserva_id))

                # Confirmar la transacción
                connection.commit()
                print("Reserva realizada exitosamente")
                
            else:
                print("Fallo en la autenticación")
                return False
            
            
        except Error as e:
            print(f"Error al consultar la base de datos reservar {e}")
            return False  # Retorna False en caso de error
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                
def obtener_fechas_reservadas(vehiculo,id_tipo):
    connection = create_connection()
    if connection:
        try:
            fechas_reservadas = []
            if vehiculo == 'coche':
                id_vehiculo =searchIDCoche(id_tipo)
            elif vehiculo == 'bike':
                id_vehiculo = searchIDBike(id_tipo)
            elif vehiculo == 'scooter':
                id_vehiculo = searchIDScooter(id_tipo)
            else:
                print('Vehiculo no valido')
                return False
            cursor = connection.cursor(dictionary=True)
            query = """
                SELECT fechaSalida, fechaLlegada 
                FROM reservas 
                WHERE Vehiculo_ID = %s
                AND fechaLlegada >= CURRENT_DATE
            """
            cursor.execute(query, (id_vehiculo,))
            reservas = cursor.fetchall()
            
            for reserva in reservas:
                fecha_salida = reserva['fechaSalida']
                fecha_llegada = reserva['fechaLlegada']
                fechas_reservadas.append(f"{fecha_salida} a {fecha_llegada}")

        except Error as e:
            print(f"Error al consultar la base de datos fechas reservadas: {e}")
        
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                
    return fechas_reservadas

def verificar_disponibilidad_vehiculo(vehiculo,id_tipo,fecha_salida, fecha_llegada):
    # Crear conexión a la base de datos
    connection = create_connection()
    if connection:
        try:
            if vehiculo == 'coche':
                id_vehiculo =searchIDCoche(id_tipo)
            elif vehiculo == 'bike':
                id_vehiculo = searchIDBike(id_tipo)
            elif vehiculo == 'scooter':
                id_vehiculo = searchIDScooter(id_tipo)
            else:
                print('Vehiculo no valido')
                return False
            cursor = connection.cursor(dictionary=True)
            query_reservas = """
                SELECT * FROM reservas 
                WHERE Vehiculo_ID = %s 
                AND ((fechaSalida BETWEEN %s AND %s) OR (fechaLlegada BETWEEN %s AND %s))
            """
            cursor.execute(query_reservas, (id_vehiculo, fecha_salida, fecha_llegada, fecha_salida, fecha_llegada))
            reservas_existentes = cursor.fetchall()

            if reservas_existentes:
                print(f"El vehículo con ID {id_vehiculo} está reservado en las fechas seleccionadas.")
                return False
            else:
                print(f"El vehículo con ID {id_vehiculo} está disponible para las fechas seleccionadas.")
                return True
                
        except Error as e:
            print(f"Error al consultar la disponibilidad del vehículo: {e}")
            return False
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    else:
        print("Error en la conexión a la base de datos")
        return False
    
def insertTarjeta(nomTitular, numTarjeta, cvv, expiracion):
    # usuario, id_vehiculo, fechaSalida, fechaLlegada
    connection = create_connection()
    if connection:
        try:
            userNow = 'donova@example.com'
            pswdNow = '1234'
            user_id = loginForId(userNow, pswdNow)
            if user_id:
                cursor = connection.cursor()

                # Validar si la tarjeta ya existe
                query_check_tarjeta = "SELECT COUNT(*) FROM tarjeta WHERE numTarjeta = %s"
                cursor.execute(query_check_tarjeta, (numTarjeta,))
                (count,) = cursor.fetchone()

                if count > 0:
                    print("Esta tarjeta ya está registrada.")
                    return False
                
                
                # Consulta SQL para insertar datos en la tabla tarjetas
                query_insert_tarjeta = """
                INSERT INTO tarjeta (nomTitular, numTarjeta, cvv, expiracion)
                VALUES (%s, %s, %s, %s)
                """
        
                # Datos de la tarjeta a insertar
                datos_tarjeta = (nomTitular, numTarjeta, cvv, expiracion)
        
                # Ejecutar la consulta para insertar la tarjeta
                cursor.execute(query_insert_tarjeta, datos_tarjeta)
        
                # Obtener el ID de la tarjeta recién insertada
                tarjeta_id = cursor.lastrowid

                # Consulta SQL para actualizar la tabla usuarios con el ID de la tarjeta
                query_update_usuario = """
                UPDATE usuarios
                SET tarjeta_ID = %s
                WHERE ID = %s
                """
        
                # Ejecutar la consulta para actualizar el usuario con el ID de la tarjeta
                cursor.execute(query_update_usuario, (tarjeta_id, user_id))

                # Confirmar la transacción
                connection.commit()
                print("Guardado de tarjeta realizado exitosamente")
                
            else:
                print("Fallo en la autenticación")
                return False
            
            
        except Error as e:
            print(f"Error al consultar la base de datos reservar {e}")
            return False  # Retorna False en caso de error
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()