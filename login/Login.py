from tkinter import messagebox
from master.masterPanel import MasterPanel
from login.login_designer import FormLoginDesigner
from db.conection import login  # Importa la función login desde connection.py
from registration.registroPanel import Registro

class FormLogin(FormLoginDesigner):

    def verify(self):
        user = self.user.get()  # Obtener el usuario desde el formulario
        password = self.password.get()  # Obtener la contraseña desde el formulario

        # Llamar a la función de login con los valores del formulario
        if login(user, password):
            self.window.destroy()  # Cerrar la ventana de login si es exitoso
            MasterPanel()  # Abrir el panel principal
            #FormLogin.destroy()
        else:
            messagebox.showerror(message="La contraseña o el usuario no son correctos", title="Error")

    def userRegister(self):
        Registro()  # Iniciar el registro de usuario

    def __init__(self):
        super().__init__()
