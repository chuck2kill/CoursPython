# programme 3 page 98

""" Ce programme fait apparaître une fenêtre avec 2 champs
l'un indique la température en Celsius, et l'autre en Fahrenheit.
Lorsque l'on change une température, cela change l'autre et 
vice versa"""

# importation des modules
from tkinter import *

# définitions de fonctions
def convertFa(event):                       # conversion des celsius en fahrenheit
    fahrenheit.delete(0, END)               # on commence par effacer le contenu de la cellule
    f = (int(celsius.get()) * (9 / 5)) + 32 # on fait le calcul
    fahrenheit.insert(0, f)                 # et on l'affiche

def convertCe(event):                       # conversion de fahrenheit en celsius
    celsius.delete(0, END)                  # meme fonctionnement mais à l'inverse
    c = (int(fahrenheit.get()) - 32) * (5 / 9)
    celsius.insert(0, c)

# ---------- Programme principal ----------
fen = Tk()
fen.title('Conversion Celsius/Fahrenheit')
# Création des libellés
Label(fen, text='température en degrés Celsius').grid(row=0, column=0)
Label(fen, text='Température en degrés Fahrenheit').grid(row=1, column=0)
# Création des zones de textes
celsius = Entry(fen, fg='red')
celsius.grid(row=0, column=1)
celsius.bind("<Return>", convertFa)         # en appuyant sur entrée, on appelle la fonction
fahrenheit = Entry(fen, fg='green')
fahrenheit.grid(row=1, column=1)
fahrenheit.bind("<Return>", convertCe)      # en appuyant sur entrée, on appelle la fonction
# Création du bouton quitter
Button(fen, text='Quitter', command=fen.quit).grid(row=2, column=1, sticky=E)

# Activation de la boucle d'événements
fen.mainloop()
