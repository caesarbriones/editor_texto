from tkinter import *
from tkinter import filedialog as FileDialog

ruta = ""

def salir():
    root.quit()

def nuevo():
    global ruta 
    ruta = ""
    text.delete(1.0,"end"
                )
    mensaje.set('Nuevo')

def abrir():
    global ruta
    ruta = FileDialog.askopenfilename(title="Selecciona un archivo de texto",
                                      initialdir="/")
    archivo = open(ruta,'r')
    contenido = archivo.read()
    text.delete(1.0,"end")
    text.insert('insert',contenido)
    archivo.close()
    root.title(ruta+" - Mi editor")
    
    mensaje.set('Abrir')

def guardar():
    mensaje.set('Guardar')
    
    if ruta !="":
        contenido = text.get(1.0,"end-1c")
        archivo = open(ruta,"w+")
        archivo.write(contenido)
        archivo.close()
        mensaje.set('Archivo guardado con exito')
    else:
        guardar_como()
    

def guardar_como():
    global ruta
    mensaje.set('Guardar como...')
    archivo = FileDialog.asksaveasfile(title="Guardar fichero",mode="w",defaultextension =".txt")
    
    if archivo is not None:
        ruta = archivo.name
        contenido = text.get(1.0,"end-1c")
        mensaje.set('Archivo guardado con exito')
    else:
        mensaje.set("Guardado cancelado")
        
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