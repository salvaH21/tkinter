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
raiz.mainloop()
