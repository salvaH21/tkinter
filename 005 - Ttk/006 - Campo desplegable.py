import tkinter as tk
from tkinter import ttk

raiz = tk.Tk()

ttk.Combobox(raiz,values=['manzana','pera','plátano','sandía']).pack(padx=50,pady=50)

raiz.mainloop()
