############################################
# programme 2 page 56                      #
# permet d'afficher bonjour mr ou mme x    #
# en fonction de ce que l'utilisateur      #
# a entré                                  #
############################################

# on demande le nom et le sexe de l'utilisateur
nom = input("Veuillez entre votre nom :")
sexe = input("Veuillez entre votre sexe (M ou F) :")

# validité des conditions
if sexe == 'M':
    print("Cher monsieur", nom)
elif sexe == 'F':
    print("Chere mademoiselle", nom)
else:
    print("Vous devez entrez M ou F pour votre sexe")