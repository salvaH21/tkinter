import tkinter as tk
from tkinter import ttk

raiz = tk.Tk()

estilo = ttk.Style()
estilo.configure('TButton',padding=10,width=25,height=15)

ttk.Button(raiz,text="Pulsame si te atreves").pack(padx=25,pady=25)

raiz.mainloop()
