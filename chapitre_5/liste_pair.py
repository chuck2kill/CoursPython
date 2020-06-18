# programme 4 page 45
# à partir d'une seule liste de nombres, on créé
# une liste pair et une liste impair

# déclaration des listes et du compteur
depart = [100, 54, 42, 87, 69, 81, 54, 56, 987, 842, 125, 21, 545, 632, 159 ,831, 1, 0]
pair, impair = [], []
i = 0

# boucle de traitement
while i < len(depart):
    if depart[i] % 2 == 0:
        pair.append(depart[i])
    else:
        impair.append(depart[i])
    i = i + 1

# affichage des 2 listes
print(pair, ",", impair)