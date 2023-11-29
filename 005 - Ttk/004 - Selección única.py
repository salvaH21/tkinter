import tkinter as tk
from tkinter import ttk

raiz = tk.Tk()

ttk.Radiobutton(raiz,text="Esta es la opción 1").pack(padx=50,pady=50)
ttk.Radiobutton(raiz,text="Esta es la opción 2").pack(padx=50,pady=50)

raiz.mainloop()
