# programme 8.29 page 101

"""Même jeu que jeu_balle1, mais à chaque fois qu'on clique sur la balle, celle-ci rétrécit"""

# import de modules
from tkinter import *

# définiton des fonctions
def move():
    "Fonction qui gère le déplacement de la balle"
    global x, y, dx, dv, flag, vit
    xp, yp = x, y
    if x > 375 or x < 25:           # si la balle touche un côté
        dx = -dx
    x = x + dx
    y = y + dv
    if y > 225:
        y = 225
        dv = -dv
    if y < 25:
        dv = -dv
    # bouvelle position de la balle
    can.coords(balle, x - taille, y - taille, x + taille, y + taille)
    if flag > 0:
        fen.after(vit, move)

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

def compte(event):
    "fonction de gestion du clic"
    global clic, score, dv, flag, vit
    if flag > 0:
        clic += 1
        if event.x < x + taille and event.x > x - taille and event.y < y + taille and event.y > y - taille:
            score += 1
            vit -= 5
        if clic >= 10:
            stop()
            scoreF = Label(fen, text='score = ' + str(score), font=50)
            scoreF.pack(side=TOP)

# ========== Programme principal ========== #

# déclaration des variables
x, y, vit, dx, dv, flag = 25, 25, 50, 6, 5, 0
taille = 25
clic, score = 0, 0

# création de la fenêtre, de la balle et des boutons
fen = Tk()
fen.title('Chutes et rebonds')
can = Canvas(fen, width=400, height=250, bg='white')
can.pack()
balle = can.create_oval(x - taille, y - taille, x + taille, y + taille, fill='red')
Button(fen, text='Start', command=start).pack(side=LEFT, padx=10)
Button(fen, text='Stop', command=stop).pack(side=LEFT)
Button(fen, text='Quitter', command=fen.quit).pack(side=RIGHT, padx=10)

# 2vénement de clic
can.bind('<Button-1>', compte)

# réceptionnaire d'événements (boucle principale)
fen.mainloop()
