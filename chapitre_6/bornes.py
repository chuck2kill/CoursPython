# programme 1 page 55
# ce programme permet d'additionner les multiples de 3 et 5
# compris entre les bornes données par l'utilisateur

# on demande les bornes
a = int(input("Renseignez la borne basse :"))
b = int(input("Renseignez la borne haute :"))

# variable de calcul
resultat = 0

# boucle de traitement
while a < b:
    if a % 3 == 0 or a % 5 == 0:
        resultat = resultat + a
    a = a + 1

# affichage du résultat
print("Voici le résultat :", resultat)