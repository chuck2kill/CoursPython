# programme 8.30 page 101

"""Programme avec des balles qui rebondissent les unes sur les autres
et sur les parois"""

# import de modules
from tkinter import *

# définiton des fonctions
def move():
    "Fonction qui gère le déplacement de la balle"
    global x, y, dx, dv, flag
    i = 0
    while i < 3:
        if x[i] > 390 or x[i] < 10:           # si la balle touche un côté
            dx[i] = -dx[i]
        x[i] = x[i] + dx[i]
        y[i] = y[i] + dv[i]
        if y[i] > 240:
            y[i] = 240
            dv[i] = -dv[i]
        if y[i] < 10:
            dv[i] = -dv[i]
        i += 1
    # bouvelle position de la balle
    can.coords(balle1, x[0] - taille, y[0] - taille, x[0] + taille, y[0] + taille)
    can.coords(balle2, x[1] - taille, y[1] - taille, x[1] + taille, y[1] + taille)
    can.coords(balle3, x[2] - taille, y[2] - taille, x[2] + taille, y[2] + taille)
    if flag > 0:
        fen.after(50, move)

def start():
    "Focntion de démarrage"
    global flag
    flag = flag + 1
    if flag == 1:
        move()

def stop():
    "Fonction d'arrêt de la balle"
    global flag
    flag = 0

# ========== Programme principal ========== #

# déclaration des variables
flag = 0
x = [10, 50, 100]
y = [10, 100, 50]
dx = [6, 6, 6]
dv = [5, 5, 5]
taille = 10
clic, score = 0, 0

# création de la fenêtre, de la balle et des boutons
fen = Tk()
fen.title('Chutes et rebonds')
can = Canvas(fen, width=400, height=250, bg='white')
can.pack()
balle1 = can.create_oval(x[0] - taille, y[0] - taille, x[0] + taille, y[0] + taille, fill='red')
balle2 = can.create_oval(x[1] - taille, y[1] - taille, x[1] + taille, y[1] + taille, fill='blue')
balle3 = can.create_oval(x[2] - taille, y[2] - taille, x[2] + taille, y[2] + taille, fill='green')
Button(fen, text='Start', command=start).pack(side=LEFT, padx=10)
Button(fen, text='Stop', command=stop).pack(side=LEFT)
Button(fen, text='Quitter', command=fen.quit).pack(side=RIGHT, padx=10)

# réceptionnaire d'événements (boucle principale)
fen.mainloop()
