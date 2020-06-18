# programme 5 page 45
# création de deux listes à partir d'une liste de noms
# il y aura une liste avec les noms de - de 6 caractères, et 
# une autre liste avec les autres

# déclaration des listes et du compteur 'i'
noms = ['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Jean-pierre', 'Sandra']
plus6, moins6 = [], []
i = 0

# boucle de traitement
while i < len(noms):                # on parcourt la liste
    if len(noms[i]) < 6:            
        moins6.append(noms[i])
    else:
        plus6.append(noms[i])
    i = i + 1

# affichage des listes résultantes
print(plus6, moins6)