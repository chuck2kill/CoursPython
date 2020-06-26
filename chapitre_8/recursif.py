from tkinter import *
from random import *
from math import *

# définition des gestionnaires
# d'événements :

def move():
    "déplacement de la balle"
    global x1, y1, t, x, y, r, flag
    t += 0.1
    x1, y1 = x + (r * cos(t)), y + (r * sin(t))
    
    can1.coords(oval1, x1, y1, x1 + 30, y1 + 30)
    if flag > 0:
        fen1.after(50, move)        # => boucler, après 50 milisecondes

def stop_it():
    "arrêt de l'animation"
    global flag
    flag = 0

def start_it():
    "démarrage de l'animation"
    global flag
    if flag == 0:                   # pour ne lancer qu'une seule boucle
        flag = 1
        move()

#========== Programme prinsipal ==========

# les variables suivantes seront utilisées de manière globale :
                    # coordonnées initiales
x, y = 125, 125
t, r = 0, 50       # 'pas' du déplacement
x1, y1 = x + (r * cos(t)), y + (sin(t))
flag = 0

# création du widget principal ("parent") :
fen1 = Tk()
fen1.title('Exercice d\'animation avec Tkinter')
# création des widgets enfants :
can1 = Canvas(fen1, bg='dark grey', height=250, width=250)
can1.pack(side=LEFT, padx=5, pady=5)
oval1 = can1.create_oval(x1, y1, x1 + 30, y1 + 30, width=2, fill='red')
bou1 = Button(fen1, text='Quitter', width=8, command=fen1.quit)
bou1.pack(side=BOTTOM)
bou2 = Button(fen1, text='Démarrer', width=8, command=start_it)
bou2.pack()
bou3 = Button(fen1, text='Arrêter', width=8, command=stop_it)
bou3.pack()

# démarrage du réceptionnaire d'événements (boucle principale) :
fen1.mainloop()
