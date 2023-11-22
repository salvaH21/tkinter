import tkinter as tk

raiz = tk.Tk()

def saluda():
    print("Has pulado el botón, eh?")

tk.Button(raiz,text="Hola mundo desde tkinter",command=saluda).pack(padx=50,pady=50)

raiz.mainloop()
