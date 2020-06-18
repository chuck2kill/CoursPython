# programme 3 page 42
# sert à insérer une chaine dans une nouvelle variable en 
# insérant une * entre chaque caractère

chaine = "Salut les musclés"    # première chaine
star = "*"                      # caractère à insérer
chaine2 = chaine[0]             # seconde chaine 
compte = 1                      # simple compteur que l'on va incrémenter

# boucle sur la première chaine de caractère
while compte < len(chaine):
    chaine2 = chaine2 + star + chaine[compte]           # onajoute à la chaine 2 une étoile et le 
    compte = compte + 1                                 # caractère suivant de la première chaine

# affichage du résultat
print(chaine2)