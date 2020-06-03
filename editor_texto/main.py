from tkinter import *

def salir():
    root.quit()

def nuevo():
    mensaje.set('Nuevo')

def abrir():
    mensaje.set('Abrir')

def guardar():
    mensaje.set('Guardar')

def guardar_como():
    mensaje.set('Guardar como...')

root = Tk()
root.title("Editor de texto")
root.iconbitmap('resources/favicon.ico')
menubar = Menu(root)
root.config(menu=menubar)

filemenu = Menu(menubar,tearoff=0)
filemenu.add_command(label="Nuevo",command=nuevo)
filemenu.add_command(label="Abrir",command=abrir)
filemenu.add_command(label="Guardar",command=guardar)
filemenu.add_command(label="Guardar como...",command=guardar_como)
filemenu.add_separator()
filemenu.add_command(label="Salir",command=salir)
menubar.add_cascade(label="Archivo",menu=filemenu)

text = Text(root)
text.config(bd=0,padx=4,pady=6,font=("Consolas",12))
text.pack()

mensaje = StringVar()
mensaje.set("Bienvenidos al editor de texto!")
monitor = Label(textvariable=mensaje,justify='left')
monitor.pack(side='left')

root.mainloop()