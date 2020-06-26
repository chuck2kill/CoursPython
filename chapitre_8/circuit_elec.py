# programme 9 page 98

""" Ce programme montre un circuit électrique simple dans un canevas
(générateur, interrupteur, resistance).

La fenêtre doit être pourvue de champs d'entrée pour modifier les valeurs.

Le circuit doit être fonctionnel grâce à un interrupteur.
Des étiquettes doivent afficher en permanence les tension et
intensités résultant des choix faits par l'utilisateur."""

# import de modules
from tkinter import *
from math import *

# définition de fonction
def calcul():
    # on efface les 2 champs qui reçoivent les calculs
    tension.delete(0, END)
    intensite.delete(0, END)
    # on effectue les calculs
    t = sqrt(int(puissance.get()) * int(resistance.get()))
    i = sqrt(int(puissance.get()) / int(resistance.get()))
    # on insert le résultat des calculs dans les bons champs
    tension.insert(0, t)
    intensite.insert(0, i)

# ---------- Programme principal ----------

# création de la fenêtre
fen = Tk()
fen.title('Schéma simplifé de circuit électrique')

# création des graphismes
can = Canvas(fen, width=500, height=350, bg='light yellow')
can.grid(row=0, column=0, columnspan=4)
# création de la résistance
can.create_rectangle(200, 100, 250, 120, fill='light grey')
can.create_line(210, 100, 210, 120, fill='green')
can.create_line(220, 100, 220, 120, fill='red')
can.create_line(230, 100, 230, 120, fill='blue')
can.create_line(235, 100, 235, 120, fill='yellow')
# création de la pile
can.create_rectangle(50, 250, 150, 280, fill='light grey')
can.create_text(100, 265, text='PILE')
# création de l'interrupteur
can.create_rectangle(320, 200, 380, 230, fill='light grey')
can.create_text(350, 215, text='ON/OFF')
# création des lignes entre les objets
can.create_line(100, 110, 200, 110)
can.create_line(250, 110, 350, 110)
can.create_line(100, 110, 100, 250)
can.create_line(350, 110, 350, 200)
can.create_line(100, 280, 100, 300)
can.create_line(350, 230, 350, 300)
can.create_line(100, 300, 350, 300)

# création des libellés
Label(fen, text='Résistance').grid(row=1, column=0, sticky=E)
Label(fen, text='Puissance').grid(row=2, column=0, sticky=E)
Label(fen, text='Tension').grid(row=3, column=0, sticky=E)
Label(fen, text='Intensité').grid(row=4, column=0, sticky=E)
Label(fen, text='Ω(Ohm)').grid(row=1, column=2, sticky=W)
Label(fen, text='W(Watt)').grid(row=2, column=2, sticky=W)
Label(fen, text='V(Volt)').grid(row=3, column=2, sticky=W)
Label(fen, text='A(Ampère)').grid(row=4, column=2, sticky=W)

# création des champs
resistance = Entry(fen, bg='light grey')
puissance = Entry(fen, bg='light grey')
tension = Entry(fen, bg='light grey')
intensite = Entry(fen, bg='light grey')
resistance.grid(row=1, column=1, padx=10, pady=10, sticky=W)
puissance.grid(row=2, column=1, padx=10, pady=10, sticky=W)
tension.grid(row=3, column=1, padx=10, pady=10, sticky=W)
intensite.grid(row=4, column=1, padx=10, pady=10, sticky=W)

# insertion de texte
can.create_text(250, 20, text='Veuillez entrer une valeur de résistance et de puissance, puis appuyez sur "Allumer"')

# création des bouttons
Button(fen, text='Allumer', command=calcul).grid(row=3, column=3, sticky=E, padx=10, pady=10)
Button(fen, text='Quitter', command=fen.quit).grid(row=4, column=3, sticky=E, padx=10, pady=10)

# boucle d'événements
fen.mainloop()
