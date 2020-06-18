# programme 3 page 50
# permet de calculer la période d'un pendule simple
# de longueur donnée

# import du module math
from math import *

# on demande la longueur du pendule
longueur = int(input("Donnez la longueur du pendule en cm: "))

# calcul de la période
periode = (2 * pi) * sqrt(longueur / 2)

# affichage de la réponse
print("La période du pendule est égale à", periode)
input()