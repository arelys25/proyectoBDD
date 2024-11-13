import mysql.connector
from mysql.connector import Error
import hashlib
from master.masterPanel import MasterPanel


# Función para hacer hash de la contraseña
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Función para conectarse a la base de datos
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='HP-LAP-ARELY25',
            database='emobility',
            user='root',
            password='Daniarely3',  # Cambia a 'password_db' si es necesario
            charset='utf8mb4',
            collation='utf8mb4_general_ci',
            port = 3305
        )
        if connection.is_connected():
            print("Conexión a la base de datos exitosa")
        return connection
    except Error as e:
        print(f"Error al conectarse a la base de datos: {e}")
        return None
    
#insertar usuario inicial    

def insert_initial_user():
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            # Inserta en la tabla usuarios
            cursor.execute("""
                INSERT INTO usuarios (Nombre, Email, telefono, TipoUsuario, FechaRegistro)
                VALUES ('Admin', 'admin@example.com', '1234567890', 'particular', NOW())
            """)
            user_id = cursor.lastrowid  # Obtener el ID del nuevo usuario
            # Inserta en la tabla login
            hashed_password = hash_password("1234")  # Hasheando la contraseña
            cursor.execute("""
                INSERT INTO login (usuario_ID, username, password, status)
                VALUES (%s, %s, %s, %s)
            """, (user_id, 'admin@example.com', hashed_password, 'exitoso'))
            connection.commit()  # Guardar los cambios
            print("Usuario inicial insertado exitosamente.")
        except Error as e:
            print(f"Error al insertar el usuario: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

def registrarUsuario(username, email,  tel, password, tipe_user):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            query ="""INSERT INTO usuarios (Nombre, Email, telefono, TipoUsuario, FechaRegistro)
                VALUES (%s, %s, %s, %s, NOW()) """
            cursor.execute(query,(username, email, tel, tipe_user))
            user_id = cursor.lastrowid

            #hashear contrasena
            hashed_password = hash_password(password)
            #insertar el login asociado en la tabla login
            query_login = """
                INSERT INTO login (usuario_ID, username, password, status)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query_login,(user_id,email,hashed_password, 'particular'))
            connection.commit()
            print("usuario registrado exitosamente")
            return True #indica que el registro fue exitoso
        except Error as e:
            print(f"Error al registrar el usuario: {e}")
            return False #indica que hubo un error en el registro
        finally:
            if(connection.is_connected()):
                cursor.close()
                connection.close()


# Función para registrar el intento de inicio de sesión
def log_login_attempt(usuario_id, username, password, status):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = """
            SELECT u.ID, l.password FROM login l
            JOIN usuarios u ON l.usuario_ID = u.ID
            WHERE u.Email = %s OR u.Nombre = %s
            """

            cursor.execute(query, (usuario_id, username, password, status))
            connection.commit()
            print(f"Intento de login registrado con estado: {status}")
        except Error as e:
            print(f"Error al registrar el intento de login: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

# Función para verificar usuario y contraseña
def login(username, password):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            query = """
                SELECT u.ID, l.password FROM login l
                JOIN usuarios u ON l.usuario_ID = u.ID
                WHERE u.Email = %s OR u.Nombre = %s
                """
            cursor.execute(query, (username, username))
            user = cursor.fetchone()

            if user:
                hashed_password = hash_password(password)
                # Si la contraseña coincide, el login es exitoso
                if hashed_password == user['password']:
                    print("Inicio de sesión exitoso")
                    log_login_attempt(user['ID'], username, hashed_password, 'exitoso')
                    
                    MasterPanel()
                    return True  # Retorna True si el inicio de sesión es exitoso
                else:
                    print("Contraseña incorrecta")
                    log_login_attempt(user['ID'], username, hashed_password, 'fallido')
                    return False  # Retorna False si la contraseña es incorrecta
            else:
                print("Usuario no encontrado")
                return False  # Retorna False si no se encuentra el usuario
        except Error as e:
            print(f"Error al consultar la base de datos {e}")
            return False  # Retorna False en caso de error
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()



