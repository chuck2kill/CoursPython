# programme 3 page 45
# nous allons chercher la plus grande valeur
# d'une liste, puis l'afficher

# déclaration de la liste, d'une variable de résultat et d'un compteur
val = [ 100, 54, 42, 87, 69, 81, 54, 56, 987, 842, 125, 21, 545, 632, 159 ,1000]
resultat = 0
i = 0

# boucle de traitement
while i < len(val):
    if val[i] > resultat:               # si la valeur de val[i] est plus grande que la valeur de
        resultat = val[i]               # resultat, on change resultat
    i = i + 1

# affichage du résultat
print("La plus grande valeur est", resultat)