# programme 7 page 56
# l'utilisateur entre des notes dans une liste grâce à une boucle 
# la boucle s'arrête si une valeur négative est entrée
# à chaque fois qu'une note est entrée, on inscrit le nombre de notes entrées,
# la note la plus élevée, la plus basse et la moyenne

# declaration de variable
note, i = 0, 0
liste = list()

# boucle générale
while note >= 0:                                        # si la note n'est pas négative
    note = int(input("Veuillez entrer une note :"))
    if note <= 0:                                       # si la note est négative, on sort
        break                                           # du programme
    i = i + 1
    liste.append(note)                                  # on intègre la note à la liste
    # on affiche le nombre de notes, le max et le minimum
    print("Il y a", i, "note(s) entrée(s)")
    print("La note maximale est", max(liste))
    print("La note minimale est", min(liste))
    # variables pour calculer la moyenne
    j = 0
    somme = 0
    # calcul de la moyenne
    while j < i:
        somme = somme + liste[j]
        j = j + 1
    # on affiche la moyenne des notes
    print("La moyenne des notes est", somme / i)