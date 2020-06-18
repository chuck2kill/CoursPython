# programme 4 page 50
# permet de récupérer les chiffres de l'utilisateur dans
# une liste, jusqu'à ce qu'il ne mette rien

# Déclaration de la liste
chiffre = 0
liste = []

# boucle globale
while chiffre != "":                                # si la valeur entrée n'est pas vide, on continue la boucle
    chiffre = input("Veuillez entrer une valeur:")
    if chiffre != "":                               # si la valeur entréé n'est pas vide, on l'ajoute à la liste
        liste.append(int(chiffre))

# on affiche le résultat
print(liste)