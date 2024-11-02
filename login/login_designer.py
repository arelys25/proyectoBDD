import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD
#import util.generic as utl
from util import generic as utl

class FormLoginDesigner:

    def verify(self):
       pass
    
    def userRegister(self):
        pass

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Login")
        self.window.iconbitmap('./images/CarIcon.ico')
        
        self.window.geometry('800x500')
        self.window.config(bg='#F5F5F5')  # Fondo principal en tono claro
        self.window.resizable(width=0, height=0)
        utl.center_window(self.window, 800, 500)
        
        logo = utl.read_Image("./images/logo.png", (200, 200))
        
        # frame logo
        frame_logo = tk.Frame(self.window, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10, bg='#222831') 
        frame_logo.pack(side="left", expand=tk.NO, fill=tk.BOTH)
        label = tk.Label(frame_logo, image=logo, bg='#222831')
        label.place(x=0, y=0, relwidth=1, relheight=1)

        # frame_form
        frame_form = tk.Frame(self.window, bd=0, relief=tk.SOLID, bg='#F5F5F5')
        frame_form.pack(side="right", expand=tk.YES, fill=tk.BOTH)

        # frame_form_top
        frame_form_top = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='#F5F5F5')
        frame_form_top.pack(side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text="Inicio de sesión", font=('Arial', 28, BOLD), fg="#30475E", bg="#F5F5F5", pady=20)
        title.pack(expand=tk.YES, fill=tk.BOTH)
        
        # frame_form_fill
        frame_form_fill = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='#F5F5F5')
        frame_form_fill.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)
        
        # entry usuario
        etiqueta_user = tk.Label(frame_form_fill, text="Usuario", font=("Arial", 13), fg="#30475E", bg='#F5F5F5', anchor="w")
        etiqueta_user.pack(fill=tk.X, padx=20, pady=5)
        self.user = ttk.Entry(frame_form_fill, font=('Arial', 13), style="TEntry")
        self.user.pack(fill=tk.X, padx=20, pady=10)
        
        # entry contraseña
        etiqueta_password = tk.Label(frame_form_fill, text="Contraseña", font=("Arial", 13), fg="#30475E", bg='#F5F5F5', anchor="w")
        etiqueta_password.pack(fill=tk.X, padx=20, pady=5)
        self.password = ttk.Entry(frame_form_fill, font=('Arial', 13), style="TEntry")
        self.password.pack(fill=tk.X, padx=20, pady=10)
        self.password.config(show="*")

        # botón iniciar sesión
        loginButton = tk.Button(frame_form_fill, text="Iniciar Sesión", font=('Arial', 14, BOLD), bg='#30475E', bd=0, fg="#F5F5F5", command=self.verify, activebackground="#222831", activeforeground="#F5F5F5")
        loginButton.pack(fill=tk.X, padx=20, pady=20)
        loginButton.bind("<Return>", (lambda event: self.verify()))

        # botón registrar usuario
        registerButton = tk.Button(frame_form_fill, text="Registrar Usuario", font=('Arial', 13), bg='#F5F5F5', bd=1, fg="#30475E", command=self.userRegister, activebackground="#F5F5F5", activeforeground="#30475E", highlightbackground="#30475E")
        registerButton.pack(fill=tk.X, padx=20, pady=20)
        registerButton.bind("<Return>", (lambda event: self.userRegister()))
        
        self.window.mainloop()
