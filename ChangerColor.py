from tkinter import*
import time
from tkinter import messagebox as MessageBox
from tkinter import colorchooser as ColorChooser

root = Tk()
root.geometry("340x150")
root.title("Changer Color")
ventana=Frame(root)
ventana.grid()

titulo=Label(ventana, text="Cambiar Color", font=("ROBOTO", 20), fg="#000000")
titulo.grid(row=1, column=4)


def verificar():
    respuesta = red.get() + green.get() + blue.get()
    print(respuesta)
    respuesta2=(len(respuesta))

    if (respuesta2==6):
        ventana.config(bg=("#"+ respuesta))
        root.config(bg=("#"+respuesta))
        colored.config(bg=("#"+ respuesta))
        colorgreen.config(bg=("#"+ respuesta))
        colorblue.config(bg=("#"+ respuesta))
        titulo.config(bg=("#"+respuesta))
        pass

    else:
          MessageBox.showwarning("Alerta", "Exceso de limite de caracteres")


#----------------#
red=StringVar()
green=StringVar()
blue=StringVar()
#----------------#


colored= Label(ventana, text="Red:       ", font="TimesNewRoman", fg="#0C0707")
colored.grid(row=5, column=3)
redTexto= Entry(ventana,textvariable=red)
redTexto.grid(row=5, column=4)

colorgreen= Label(ventana, text="Green:       ", font="TimesNewRoman",  fg="#0C0707")
colorgreen.grid(row=7, column=3)
greenTexto= Entry(ventana,textvariable=green)
greenTexto.grid(row=7, column=4)

colorblue= Label(ventana, text="Blue:       ", font="TimesNewRoman", fg="#0C0707")
colorblue.grid(row=10, column=3)
blueTexto= Entry(ventana,textvariable=blue)
blueTexto.grid(row=10, column=4)

#BOTON "CAMBIAR COLOR"
boton1=Button(ventana,text="Cambiar Color", fg="#000000", bg="#D4AADD", font=("Roboto", 10, "bold"), command=verificar)
boton1.grid(row=13, column=4)


root.mainloop()
