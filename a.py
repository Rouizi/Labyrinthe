def carte(fichier):
    with open(fichier, 'r') as une_carte:
        contenu = une_carte.read()
    return contenu

def labyrinthe(fichier):
    L = []
    for l in carte(fichier):
        L.append(l)
