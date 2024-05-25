# import tkinter as tk
# from tkinter import Label
# from PIL import Image, ImageTk
# import customtkinter as ctk

# app = ctk.CTk()
# app.geometry("900x700")
# app.title("Mi Proyecto")

# label_font = ("Georgia", 40, "bold")
# label = ctk.CTkLabel(app, text="Bievenido a Bluesky Airlines",
#                       font=label_font, text_color="blue")
# label.pack(pady=20)
# imagen = Image.open("PROYECTO/Programacion/avioncito.jpg")
# imagen = imagen.resize((800, 600))
# imagen_tk = ImageTk.PhotoImage(imagen)
# label = tk.Label(image=imagen_tk)
# label.pack()
# def ventana_dos():
#     ventana_dos = tk.Toplevel(root)
#     ventana_dos.title("Realizar compra de ticket")
#     label = tk.label(ventana_dos, text="Realiza Compra de tu ticket")
#     label.pack()
# root = tk.Tk()
# root.title("Ventana Principal")
# label_font = ("Georgia", 40, "bold")
# label = ctk.CTkLabel(root, text = "Reserva tu ticket",
#                      font=label_font, text_color="blue")
# label.pack()
# def boton_presionado():
#     ctk.messagebox.showinfo("Mensaje", "¡Botón presionado!")
# width = 50
# boton = tk.Button(app, text="Click para Continuar",width=width,bg="blue", fg="white",font=("Helvetica", 16, "italic"), command=ventana_dos)
# boton.pack(pady=30)





    





# app.mainloop()

import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk
import customtkinter as ctk

# Crear la ventana principal de la aplicación usando customtkinter
app = ctk.CTk()
app.geometry("900x700")
app.title("Mi Proyecto")

# Configurar la etiqueta de bienvenida
label_font = ("Georgia", 40, "bold")
label = ctk.CTkLabel(app, text="Bienvenido a Bluesky Airlines", font=label_font, text_color="blue")
label.pack(pady=20)

# Cargar y mostrar la imagen
imagen = Image.open("airplane-flying-vector-icon.jpg")
imagen = imagen.resize((800, 600))
imagen_tk = ImageTk.PhotoImage(imagen)
label_imagen = tk.Label(app, image=imagen_tk)
label_imagen.pack()

# Función para abrir una nueva ventana
def ventana_dos():
    nueva_ventana = tk.Toplevel(app)
    nueva_ventana.title("Realizar compra de ticket")
    label = tk.Label(nueva_ventana, text="Realiza Compra de tu ticket", font=("Georgia", 20, "bold"))
    label.pack(pady=20)
    nueva_ventana.geometry("900x700")
# Crear un botón que abre la nueva ventana al ser presionado
boton = tk.Button(app, text="Click para Continuar", width=20, bg="blue", fg="white", font=("Helvetica", 16, "italic"), command=ventana_dos)
boton.pack(pady=30)

# Ejecutar el loop principal de la aplicación
app.mainloop()



