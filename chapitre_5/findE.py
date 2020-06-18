# programme 1 page 42
# ce script permet de déterminer si une chaine de 
# caractères contient la lettre 'e'

# déclaration des variables
chaine = "Égaliseur 4 bandes avec médiums paramétriques"
compteur, lettre = 0, 0

# boucle sur la taille de la chaine de caractères
while compteur < len(chaine):
    if chaine[compteur] == "e":         # si le caractère recherché est trouvé
        lettre = lettre + 1             # on incrémente le nombre d'occurences trouvées
    compteur = compteur + 1

# on affiche le résultat
print("cette chaine contient", lettre, "fois la lettre e")