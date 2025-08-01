from tkinter import *

# -----------------------------------------
# Ventana principa
# ------------------------------------------

ventana_principal = Tk()
ventana_principal.title("Bandera de Noruega - Samyr Alejandro Archila Guiza")
ventana_principal.geometry("800x500")
ventana_principal.resizable(0, 0)
ventana_principal.config(bg="white")

# -----------------------------------------
# Fondo rojo
# -----------------------------------------
fondo_rojo = Frame(ventana_principal, bg="red", width=780, height=480)
fondo_rojo.place(x=10, y=10)

# -----------------------------------------
# Cruz blanca vertical
# -----------------------------------------
cruz_blanca_vertical = Frame(ventana_principal, bg="white", width=60, height=480)
cruz_blanca_vertical.place(x=220, y=10)

# -----------------------------------------
# Cruz blanca horizontal
# -----------------------------------------
cruz_blanca_horizontal = Frame(ventana_principal, bg="white", width=780, height=60)
cruz_blanca_horizontal.place(x=10, y=180)

# -----------------------------------------
# Cruz azul vertical (dentro de la blanca)
# -----------------------------------------
cruz_azul_vertical = Frame(ventana_principal, bg="blue", width=30, height=480)
cruz_azul_vertical.place(x=235, y=10)

# -----------------------------------------
# 
# -----------------------------------------
cruz_azul_horizontal = Frame(ventana_principal, bg="blue", width=780, height=30)
cruz_azul_horizontal.place(x=10, y=195)

# Método principal
ventana_principal.mainloop()
