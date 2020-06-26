# programme 8.27 page 101

"""Programme simulant une balle qui tombe
et qui rebondit selon les lois de
la gravité"""

# import de modules
from tkinter import *

# définition de fonction
def rebond():
    global x, y, yi, step
    y = y + step * 2
    can.coords(balle, x - 20, y - 20, x + 20, y + 20)
    if y < yi:
        fen.after(50, rebond)

#========== Programme principal ==========

# création de la fenêtre
fen = Tk()
fen.title('Balle rebondissante')

# variables globales
x, y, yi = 250, 100, 450
step = 10

# création du canevas
can = Canvas(fen, width=500, height=500, bg='light blue')
can.grid(row=0, column=0, rowspan=2)

# création des graphiques
sol = can.create_rectangle(0, 400, 500, 500, fill='light green', width=0)
soleil = can.create_oval(400, 20, 450, 70, fill='yellow', width=0)
balle = can.create_oval(x - 20, y - 20, x + 20, y + 20, fill='red', width=2)

# création des boutons
Button(fen, text='Quitter', command=fen.quit, width=10).grid(row=1, column=1, sticky=S)
Button(fen, text='Démarrage', command=rebond, width=10).grid(row=0, column=1, sticky=N)

# démarrage du réceptionnaire d'événements (boucle principale) :
fen.mainloop()