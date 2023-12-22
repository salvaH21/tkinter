import tkinter as tk
from tkinter import ttk

def seleccionaElemento(event):
    seleccionado = arbol.focus()
    print(seleccionado)
    valores = arbol.item(seleccionado,'values')
    print(valores)
    

raiz = tk.Tk()

arbol =ttk.Treeview(raiz,columns=('nombre','apellidos','email'))
arbol.heading("#0",text="Identificador")#heading es la cabecera de la tabla
arbol.heading("nombre",text="Nombre")
arbol.heading("apellidos",text="Apellidos")
arbol.heading("email",text="Correo electrónico")

arbol.insert('','0','elemento1',text="Cliente 1",values=("Salva","Olivares Martínez","salva@gmail.com"))
arbol.insert('','1','elemento2',text="Cliente 2",values=("Marisa","Moya Cano","marisa@gmail.com"))

arbol.pack(padx=50,pady=50)

arbol.bind('<<TreeviewSelect>>',seleccionaElemento)

raiz.mainloop()
