###########################################################################
# programme 1 page 56                                                     #
# programme permettant de déterminer si une année est bissextile          #
# elle est bissextile si l'année est un multiple de 4, mais               #
# pas si elle est un multiple de 100, sauf si c'est un multiple de 400    #
###########################################################################

# on demande une année
annee = int(input("Veuillez renseigner une année :"))

# conditions pour tester
# on affiche les résultats directement
if annee % 400 == 0:
    print("l'an", annee, "est une année bissextile")
elif annee % 100 == 0:
    print("l'an", annee, "n'est pas une année bissextile")
elif annee % 4 == 0:
    print("l'an", annee, "est une année bissextile")
else:
    print("l'an", annee, "n'est pas une année bissextile")