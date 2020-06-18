# programme 2 page 50
# permet de calculer le périmètre et l'aire d'un triangle
# dont l'utilisateur fournit les 3 cotés

#importation du module math
from math import *

# on demande les 3 cotés à l'utilisateur
cote1 = int(input("Entrez le 1er coté en cm: "))
cote2 = int(input("Entrez le 2e coté en cm: "))
cote3 = int(input("Entrez le 3e coté en cm: "))

# calculs
perimetre = cote1 + cote2 + cote3
d = perimetre / 2
aire = sqrt(d * (d - cote1) * (d - cote2) * (d - cote3))

# affichage du résultat
print("Ce triangle à un périmètre de", perimetre, "cm et une aire de", aire, "cm².")
input()