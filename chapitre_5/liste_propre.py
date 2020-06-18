# programme 2 page 45
# permet d'afficher de manière "propre"
# une liste composées de strings

# déclaration de la liste et d'un compteur
t1 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 
      'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
i = 0

# boucle de traitement
while i < len(t1):
    print(t1[i], end = " ")
    i = i + 1

# affichage
print()