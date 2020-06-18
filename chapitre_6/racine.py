# programme 4 page 56
# on demande un chiffre à l'utilisateur
# soit on affiche la racine carrée
# soit on affiche un message pour dire
# que la racine carrée ne peut pas être calculée

# importation de module
from math import *

# on demande le chiffre
chiffre = int(input("Veuillez entrer un chiffre :"))

# condition pour choisir ce que l'on affiche
if chiffre <= 0:
    print("Impossible de calculer la racine carrée de", chiffre)
else:
    print("La racine carrée de", chiffre, "est", sqrt(chiffre))