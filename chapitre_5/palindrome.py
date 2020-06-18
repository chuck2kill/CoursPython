# programme 5 page 42
# programme visant à vérifier qu'une chaine de caractères est un palindrome

# déclaration des variables
mot = "s.o.s"
c = len(mot) - 1                # la variable 'c' est égale à la longueur de 'mot' - 1
inverse = mot[c]                # on créé la variable 'inverse' avec la valeur de la dernière lettre
i, t = 0, 0                     # de la variable 'mot'

c = c - 1                       # on décrémente 'c' de 1

# boucle inversée sur 'c' pour parcourir 'mot' à l'envers
while c >= 0:
    inverse = inverse + mot[c]  # on ajoute une lettre à chaque tour
    c = c - 1

# on teste pour voir si les deux variables sont égales
while i < len(mot):
    if mot[i] == inverse[i]:
        t = t +1                # on incrémente 't' si les 2 caractères sont identiques
    i = i + 1

# si t est égal à la longueur de 'mot', c'est un palindrome,
# sinon, ce n'en est pas un
if t == len(mot):
    print("C'est un palindrome")
else:
    print("Ce n'est pas un palindrome")