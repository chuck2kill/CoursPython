# programme 1 page 45
# ce programme sert à créer une liste à partir de 2 autres listes
# en alternant les termes de chaque liste

# déclaration des variables
t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 
      'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
t3 = []
c = 0                                                                   # simple variable de compteur

# boucle pour parcourir les 2 listes
while c < len(t1):
    t3.append(t2[c])                                                    # on ajoute le terme de t2
    t3.append(t1[c])                                                    # on ajoute le terme de t1
    c = c + 1

#affichage du résultat
print(t3)