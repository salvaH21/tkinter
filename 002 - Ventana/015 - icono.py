import tkinter as tk

raiz = tk.Tk()
raiz.title("Aprendiendo tkinter")

anchuraventana = 400
alturaventana = 400

anchurapantalla =raiz.winfo_screenwidth()
alturapantalla = raiz.winfo_screenheight()

esquinax = int(anchurapantalla/2 - anchuraventana/2)
esquinay = int(alturapantalla/2 - alturaventana/2)

raiz.geometry(str(anchuraventana)+"x"+str(alturaventana)+"+"+str(esquinax)+"+"+str(esquinay))
raiz.resizable(False,False)

#raiz.attributes("-alpha",0.5)
#raiz.attributes("-fullscreen",True)
#raiz.attributes("-toolwindow",False)
raiz.attributes("-topmost",100)
raiz.iconbitmap("icono.ico")
print(raiz.attributes())
raiz.mainloop()
