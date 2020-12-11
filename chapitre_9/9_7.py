# A partir de 2 fichiers existants, ce script
# va fabriquer un 3e fichier qui contiendra alternativement
# des éléments du 1er et du 2e
# Si les deux fichiers ne font pas la même taille,
# on remplira le 3e avec le surplus

fichierA = input("Entrez le chemin du premier fichier : ")
fichierB = input("Entrez le chemin du second fichier : ")

try:
    fa, fb = open(fichierA, 'r'), open(fichierB, 'r')
    fa.close()
    fb.close()
except:
    print("Veuillez entrer un nom de fichier valide...")
else:
    