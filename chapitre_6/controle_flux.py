# utilisation d'une liste et de branchements conditionnels

print("Ce script recherche le plus grand des trois nombres")
print("Veuillez entrer trois nombres séparés par des virgules : ")
ch = input()
# note : l'association des fonctions eval() et list() permet de convertir
# en liste toute chaine de valeurs séparées par des virgules :
nn = list(eval(ch))
max, index = nn[0], 'premier'
if nn[1] > max:                             # ne pas omettre le double point
    max = nn[1]
    index = 'second'
if nn[2] > max:
    max = nn[2]
    index = 'troisième'
print("Le plus grand de ces nombres est", max)
print("Ce nombre est le", index, "de votre liste.")
input()