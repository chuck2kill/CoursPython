# programme 4 page 42
# programme visant à recopier une chaine de caractères
# dans une nouvelle variable, mais en inversant
# l'ordre de la chaine de départ

# déclaration des variables
mot = "facilement"
c = len(mot) - 1                # la variable 'c' est égale à la longueur de 'mot' - 1
inverse = mot[c]                # on créé la variable 'inverse' avec la valeur de la dernière lettre
                                # de la variable 'mot'

c = c - 1                       # on décrémente 'c' de 1

# boucle inversée sur 'c' pour parcourir 'mot' à l'envers
while c >= 0:
    inverse = inverse + mot[c]  # on ajoute une lettre à chaque tour
    c = c - 1

# affichage du résultat
print(inverse)