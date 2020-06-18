# programme 6 page 56
# à partir d'une liste de chaines, on l'affiche
# avec le nombre de caractères correspondant à chaque chaine

# déclaration de la liste de départ
liste = ['Jean-Michel', 'Marc', 'Vanessa', 'Anne', 'Maximilien', 'Alexandre-Benoît', 'Louise']
i = 0

# on boucle sur la liste
while i < len(liste):
    print(liste[i], "contient", len(liste[i]), "caractères")    # on affiche la longueur de chaque
    i = i + 1                                                   # terme de la liste