# Script permettant de créer et de relire un fichier texte
# le programme doit d'abord demander d'entrer le nom du fichier
# Ensuite, il propose au choix d'enregistrer du nouveau texte ou
# d'afficher le contenu

fichier = input("Entrez le chemin de votre fichier:")
action = input("Voulez vous écrire à la suite, ou simplement lire? : E/L")
if action == "E":
    phrase = input("Entrez votre phrase: ")
    try:
        f = open(fichier, 'w')
    except:
        print("Ce fichier n'éxiste pas")
    else:
        f.write(phrase)
        f.close()