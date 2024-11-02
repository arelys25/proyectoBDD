import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD
import util.generic as utl

class RegistroDesigner:

    def register(self):  # Método abstracto
        pass

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Registro de Usuario")
        
        self.window.geometry('800x500')
        self.window.config(bg='#F5F5F5')  # Fondo principal en tono claro
        self.window.resizable(width=0, height=0)
        utl.center_window(self.window, 800, 500)
        
        # Frame para el logo
        frame_logo = tk.Frame(self.window, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10, bg='#222831') 
        frame_logo.pack(side="left", expand=tk.NO, fill=tk.BOTH)
        label = tk.Label(frame_logo, bg='#222831')
        label.place(x=0, y=0, relwidth=1, relheight=1)

        # Frame para el formulario
        frame_form = tk.Frame(self.window, bd=0, relief=tk.SOLID, bg='#F5F5F5')
        frame_form.pack(side="right", expand=tk.YES, fill=tk.BOTH)

        # Título del formulario
        frame_form_top = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='#F5F5F5')
        frame_form_top.pack(side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text="Registro de Usuario", font=('Arial', 28, BOLD), fg="#30475E", bg="#F5F5F5", pady=20)
        title.pack(expand=tk.YES, fill=tk.BOTH)

        # Frame para el formulario de entrada
        frame_form_fill = tk.Frame(frame_form, height=400, bd=0, relief=tk.SOLID, bg='#F5F5F5')
        frame_form_fill.pack(side="top", expand=tk.YES, fill=tk.BOTH, padx=20, pady=10)

        # Campos de entrada
        fields = [("Nombre", "username"), ("Correo Electrónico", "email"), ("Teléfono", "telefono"), ("Contraseña", "password")]
        for label_text, attr in fields:
            etiqueta = tk.Label(frame_form_fill, text=label_text, font=("Arial", 13), fg="#30475E", bg='#F5F5F5', anchor="w")
            etiqueta.pack(fill=tk.X, padx=20, pady=3)
            entry = ttk.Entry(frame_form_fill, font=('Arial', 13))
            entry.pack(fill=tk.X, padx=20, pady=8)
            if attr == "password":
                entry.config(show="*")
            setattr(self, attr, entry)

        # Botón para registrar
        registerButton = tk.Button(frame_form_fill, text="Registrar", font=('Arial', 14, BOLD), bg='#30475E', bd=0, fg="#F5F5F5", command=self.register, activebackground="#222831", activeforeground="#F5F5F5")
        registerButton.pack(fill=tk.X, padx=20, pady=15)
        registerButton.bind("<Return>", (lambda event: self.register()))

        self.window.mainloop()