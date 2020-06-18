# programme 3 page 56
# l'utilisateur rentre trois longueurs
# on vérifie s'il est possible de construire un triangle
# si c'est possible, on dit quel type de triangle c'est

# on demande les longueurs
a = int(input("Entrez la première longueur :"))
b = int(input("Entrez la deuxième longueur :"))
c = int(input("Entrez la troisième longueur :"))

# variables de tests
t1, t2, t3 = True, True, True

# on cherche le plus grand coté puis on calcule 'reste' pour vérifier pythagore :
# a² + b² = c²
maxi = a
reste = b**2 + c**2
if maxi < b:
    maxi = b
    reste = a**2 + c**2
if maxi < c:
    maxi = c
    reste = a**2 + b**2

# on effectue les calculs
if a + b < c:
    t1 = False
if a + c < b:
    t2 = False
if b + c < a:
    t3 = False

# on affiche le type de triangle, s'il est valide
if t1 and t2 and t3:
    if a == b and a == c:                           # si tous les cotés sont égaux
        print("C'est un triangle équilatéral")
    elif maxi**2 == reste:                          # sinon si pythagore est vérifié
        print("C'est un triangle rectangle")
    elif a == b or a == c or b == c:                # sinon si 2 cotés sont égaux
        print("C'est un triangle isocèle")
    else:                                           # sinon c'est un triangle quelconque
        print("c'est un triangle quelconque")
else:                                               # sinon ce n'est pas un triangle
    print("Ces valeurs ne permettent pas de construire un triangle")
input()