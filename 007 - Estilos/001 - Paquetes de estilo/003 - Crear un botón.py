import tkinter as tk
from tkinter import ttk

raiz = tk.Tk()

estilo = ttk.Style()
print(estilo.theme_names())

tk.Button(raiz,text="Esto es un botón tk").pack(padx=25,pady=25)
ttk.Button(raiz,text="Esto es un botón ttk").pack(padx=25,pady=25)


raiz.mainloop()
