import tkinter as tk
from tkinter import ttk

raiz = tk.Tk()

arbol =ttk.Treeview(raiz,columns=('nombre','apellidos','email'))
arbol.heading("#0",text="Identificador")#heading es la cabecera de la tabla
arbol.heading("nombre",text="Nombre")
arbol.heading("apellidos",text="Apellidos")
arbol.heading("email",text="Correo electrónico")
arbol.pack(padx=50,pady=50)

raiz.mainloop()
