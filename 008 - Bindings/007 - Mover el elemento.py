import tkinter as tk

def pulsaTecla(evento):
    print("Has pulsado una tecla")
    print(evento.keysym)
    if evento.keysym == 'a':
        print("izquierda")
        lienzo.move(elemento,-10,0) # -10 pixeles en el eje x, y 0 en el eje y
    elif evento.keysym == 'd':
        print("derecha")
        lienzo.move(elemento,10,0) # 10 pixeles en el eje x, y 0 en el eje y
    elif evento.keysym == 'w':
        print("arriba")
        lienzo.move(elemento,0,-10) # -10 pixeles en el eje y, y 0 en el eje x
    elif evento.keysym == 's':
        print("abajo")
        lienzo.move(elemento,0,10) # 10 pixeles en el eje y, y 0 en el eje x
        

raiz = tk.Tk()
lienzo = tk.Canvas(raiz)
elemento = lienzo.create_oval(20,20,50,50,outline="red",width=2)
lienzo.pack(padx=50,pady=50)

raiz.bind('<Key>',pulsaTecla)
raiz.mainloop()
