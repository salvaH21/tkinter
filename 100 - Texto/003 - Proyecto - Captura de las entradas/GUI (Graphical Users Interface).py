import tkinter as tk

raiz = tk.Tk()

archivo = open("estructura.txt","r")
lineas = archivo.readlines()
for linea in lineas:
    elemento = linea.strip()
    if elemento == "entrada":
        tk.Entry(raiz).pack()
    elif elemento == "etiqueta":
        tk.Label(raiz,text="Esto es una etiqueta").pack()
    elif elemento == "boton":
        tk.Button(raiz,text="Pulsar").pack()

raiz.mainloop()
