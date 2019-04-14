def carte(document):
    with open(document, 'r') as fichier:
        contenu = fichier.read()
    return contenu

continuer_partie = True

while continuer_partie:
    print("Labyrinthes existants :")
    print("  1 - facile.\n  2 - prison.")

    while True:
        numero = input('Entrez un numéro de labyrinthe pour commencer à jouer : ')

        try:
            numero = int(numero)
        except ValueError:
            print("vous n'avez pas saisi de nombre.")
        if numero == 1:
            print(carte('facile.txt'))
            break
        if numero == 2:
            pass
            break

