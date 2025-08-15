from tkinter import *
from tkinter import messagebox

ventana_principal = Tk()

ventana_principal.title("proyecto")

ventana_principal.geometry("500x500")

ventana_principal.resizable(0,0)

ventana_principal.config(bg="blue")



logo = PhotoImage(file="imagen.png")
lb_logo = Label(ventana_principal, image=logo, bg="blue")
lb_logo.place(x=250,y=60)

frame_1 = Button(ventana_principal)
frame_1.config(bg="black", width = 10 ,height = 2)
frame_1.place(x = 10 , y =10)



ventana_principal.mainloop()