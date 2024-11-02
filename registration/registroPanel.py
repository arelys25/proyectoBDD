from tkinter import messagebox
from master.masterPanel import MasterPanel
from db.conection import registrarUsuario  # Importa la función login desde connection.py
from registration.registro_designer import RegistroDesigner

class Registro(RegistroDesigner):
    def register(self):
        username = self.username.get()  # Obtener el usuario desde el formulario
        email = self.email.get()
        tel = self.telefono.get()
        password = self.password.get()  # Obtener la contraseña desde el formulario
        tipeUser = 'particular'
        if registrarUsuario(username, email, tel, password, tipeUser):
            self.window.destroy()  # Cerrar la ventana de login si es exitoso
            MasterPanel()  # Abrir el panel principal
        else:
            messagebox.showerror(message="La contraseña o el usuario no son correctos", title="Error")

    
    def __init__(self):
        super().__init__()
