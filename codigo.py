from tkinter import *
from tkinter import messagebox

ventana_principal = Tk()

ventana_principal.title("proyecto")

ventana_principal.geometry("500x500")

ventana_principal.resizable(0,0)

ventana_principal.config(bg="black")

def nacimiento():
    global toplevel_nacimiento
    toplevel_nacimiento = Toplevel()
    toplevel_nacimiento.title("nacimiento")
    toplevel_nacimiento.resizable(False, False)
    toplevel_nacimiento.geometry("450x300")
    toplevel_nacimiento.config(bg="grey")

    frame_nacimiento=Frame(toplevel_nacimiento)
    frame_nacimiento.config(bg="grey", width=450, height=400)
    frame_nacimiento.place(x=0,y=0)

    titulo = Label(frame_nacimiento, text="naci en el hospital de san gil un martes santo")
    titulo.config(bg = "grey",fg="black", font=("Helvetica", 15))
    titulo.place(x=10,y=10)

    titulo = Label(frame_nacimiento, text="y la hora de mi nacimiento fue a las 11:40 am ")
    titulo.config(bg = "grey",fg="white", font=("Helvetica", 15))
    titulo.place(x=10,y=50)

    titulo = Label(frame_nacimiento, text="el 30/03/2010 ")
    titulo.config(bg = "grey",fg="white", font=("Helvetica", 15))
    titulo.place(x=10,y=100)

def familia():
    global toplevel_familia
    toplevel_familia = Toplevel()
    toplevel_familia.title("familia")
    toplevel_familia.resizable(False, False)
    toplevel_familia.geometry("450x380")
    toplevel_familia.config(bg="grey")

    frame_familia=Frame(toplevel_familia)
    frame_familia.config(bg="grey", width=450, height=400)
    frame_familia.place(x=0,y=0)

    titulo = Label(frame_familia, text="Sonia Patricia Cala Lesmes")
    titulo.config(bg = "grey",fg="black", font=("Helvetica", 15))
    titulo.place(x=10,y=10)

    titulo = Label(frame_familia, text="Aldemar Santana Acosta")
    titulo.config(bg = "grey",fg="white", font=("Helvetica", 15))
    titulo.place(x=10,y=50)

    titulo = Label(frame_familia, text="Joan David Becerra Cala")
    titulo.config(bg = "grey",fg="green", font=("Helvetica", 15))
    titulo.place(x=10,y=100)


def educacion():
    global toplevel_educacion
    toplevel_educacion = Toplevel()
    toplevel_educacion.title("educacion")
    toplevel_educacion.resizable(False, False)
    toplevel_educacion.geometry("500x380")
    toplevel_educacion.config(bg="grey")

    frame_educacion=Frame(toplevel_educacion)
    frame_educacion.config(bg="grey", width=450, height=400)
    frame_educacion.place(x=0,y=0)

    titulo = Label(frame_educacion, text="primer y tercer grado estuve en la presentacion")
    titulo.config(bg = "grey",fg="black", font=("Helvetica", 15))
    titulo.place(x=10,y=10)

    titulo = Label(frame_educacion, text="los demas grados fueron en el guanenta")
    titulo.config(bg = "grey",fg="white", font=("Helvetica", 15))
    titulo.place(x=10,y=50)

def amigos():
    global toplevel_amigos
    toplevel_amigos = Toplevel()
    toplevel_amigos.title("amigos")
    toplevel_amigos.resizable(False, False)
    toplevel_amigos.geometry("450x380")
    toplevel_amigos.config(bg="grey")

    frame_amigos=Frame(toplevel_amigos)
    frame_amigos.config(bg="grey", width=450, height=400)
    frame_amigos.place(x=0,y=0)

    titulo = Label(frame_amigos, text="David Santiago Macias Maldonado")
    titulo.config(bg = "grey",fg="black", font=("Helvetica", 15))
    titulo.place(x=10,y=10)

    titulo = Label(frame_amigos, text="Oscar Eduardo Sanchez Payares")
    titulo.config(bg = "grey",fg="white", font=("Helvetica", 15))
    titulo.place(x=10,y=50)


def hoobies():
    global toplevel_hoobies
    toplevel_hoobies = Toplevel()
    toplevel_hoobies.title("hoobies")
    toplevel_hoobies.resizable(False, False)
    toplevel_hoobies.geometry("450x380")
    toplevel_hoobies.config(bg="grey")

    frame_hoobies=Frame(toplevel_hoobies)
    frame_hoobies.config(bg="grey", width=450, height=400)
    frame_hoobies.place(x=0,y=0)

    titulo = Label(frame_hoobies, text="videojuegos")
    titulo.config(bg = "grey",fg="black", font=("Helvetica", 15))
    titulo.place(x=10,y=10)

    titulo = Label(frame_hoobies, text="jugar futboll")
    titulo.config(bg = "grey",fg="white", font=("Helvetica", 15))
    titulo.place(x=10,y=50)

    titulo = Label(frame_hoobies, text="dormir")
    titulo.config(bg = "grey",fg="white", font=("Helvetica", 15))
    titulo.place(x=10,y=100)

def horario():
    global toplevel_horario
    toplevel_horario = Toplevel()
    toplevel_horario.title("horario")
    toplevel_horario.resizable(False, False)
    toplevel_horario.geometry("450x380")
    toplevel_horario.config(bg="grey")

    frame_horario=Frame(toplevel_horario)
    frame_horario.config(bg="grey", width=450, height=400)
    frame_horario.place(x=0,y=0)

    titulo = Label(frame_horario, text="levantarme a las 7am,desayunar,hacer tareas")
    titulo.config(bg = "grey",fg="black", font=("Helvetica", 15))
    titulo.place(x=10,y=10)

    titulo = Label(frame_horario, text="estar preparado para ir al colegio")
    titulo.config(bg = "grey",fg="white", font=("Helvetica", 15))
    titulo.place(x=10,y=50)

    titulo = Label(frame_horario, text="estar en el colegio hasta las 6pm")
    titulo.config(bg = "grey",fg="white", font=("Helvetica", 15))
    titulo.place(x=10,y=100)


def preparacionicfes():
    global toplevel_preparacionicfes
    toplevel_preparacionicfes = Toplevel()
    toplevel_preparacionicfes.title("preparacionicfes")
    toplevel_preparacionicfes.resizable(False, False)
    toplevel_preparacionicfes.geometry("450x380")
    toplevel_preparacionicfes.config(bg="grey")

    frame_preparacionicfes=Frame(toplevel_preparacionicfes)
    frame_preparacionicfes.config(bg="grey", width=450, height=400)
    frame_preparacionicfes.place(x=0,y=0)

    titulo = Label(frame_preparacionicfes, text="estudiar con algunos archivos de informacion")
    titulo.config(bg = "grey",fg="black", font=("Helvetica", 15))
    titulo.place(x=10,y=10)

    titulo = Label(frame_preparacionicfes, text=" de anteriores icfes que tengo en una memoria")
    titulo.config(bg = "grey",fg="white", font=("Helvetica", 15))
    titulo.place(x=10,y=50)

def proyectodevida():
    global toplevel_proyectodevida
    toplevel_proyectodevida = Toplevel()
    toplevel_proyectodevida.title("proyectodevida")
    toplevel_proyectodevida.resizable(False, False)
    toplevel_proyectodevida.geometry("450x380")
    toplevel_proyectodevida.config(bg="grey")

    frame_proyectodevida=Frame(toplevel_proyectodevida)
    frame_proyectodevida.config(bg="grey", width=450, height=400)
    frame_proyectodevida.place(x=0,y=0)

    titulo = Label(frame_proyectodevida, text=" se policia o ir a la marina")
    titulo.config(bg = "grey",fg="white", font=("Helvetica", 15))
    titulo.place(x=10,y=50)

logo = PhotoImage(file="img/imagen.png")
lb_logo = Label(ventana_principal, image=logo, bg="blue")
lb_logo.place(x=250,y=60)

frame_1 = Button(ventana_principal)
frame_1.config(bg="white", text="nacimiento", width = 10 ,height = 2, command=nacimiento)
frame_1.place(x = 10 , y =10)

frame_1 = Button(ventana_principal)
frame_1.config(bg="red", text="familia", width = 10 ,height = 2, command=familia)
frame_1.place(x = 10 , y =70)

frame_1 = Button(ventana_principal)
frame_1.config(bg="green", text="educacion", width = 10 ,height = 2, command=educacion)
frame_1.place(x = 10 , y =130)

frame_1 = Button(ventana_principal)
frame_1.config(bg="orange", text="amigos", width = 10 ,height = 2, command=amigos)
frame_1.place(x = 10 , y =190)

frame_1 = Button(ventana_principal)
frame_1.config(bg="blue", text="hoobies", width = 10 ,height = 2, command=hoobies)
frame_1.place(x = 10 , y =250)

frame_1 = Button(ventana_principal)
frame_1.config(bg="brown", text="horario", width = 10 ,height = 2, command=horario)
frame_1.place(x = 10 , y =310)

frame_1 = Button(ventana_principal)
frame_1.config(bg="grey", text="preparacion icfes", width = 10 ,height = 2, command=preparacionicfes)
frame_1.place(x = 10 , y =370)

frame_1 = Button(ventana_principal)
frame_1.config(bg="pink", text="proyecto de vida", width = 10 ,height = 2, command=proyectodevida)
frame_1.place(x = 10 , y =430)

titulo = Label(ventana_principal, text="Juan Fernando Santana cala")
titulo.config(bg = "red",fg="white", font=("Arial", 15))
titulo.place(x=220,y=280)

ventana_principal.mainloop()