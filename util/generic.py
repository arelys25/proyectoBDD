from PIL import ImageTk, Image

def read_Image(path, size):
    return ImageTk.PhotoImage(Image.open(path).resize(size, Image.LANCZOS))

#funcion para el centrado de la ventana
def center_window(window, appWidth, appHeight):
        screenWidth = window.winfo_screenwidth()
        screenHeight = window.winfo_screenheight()
        x = int((screenWidth/2) -  (appWidth /2))
        y = int((screenHeight/2) - (appHeight/2))
        return window.geometry(f"{appWidth}x{appHeight}+{x}+{y}")