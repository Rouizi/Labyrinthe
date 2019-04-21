from function import *

continuer_partie = True

while continuer_partie:
    print("Labyrinthes existants :")
    for i, nom_fichier in enumerate(os.listdir("cartes")):
        if nom_fichier.endswith(".txt"):
            print(f"  {i + 1} - {nom_fichier[:-4]}")
        if nom_fichier == 'labyrinthe':
            print(f"  {i + 1} - continuer partie")

    choix_labyrinthe = True

    while choix_labyrinthe:
        numero = input('Entrez un numéro de labyrinthe pour commencer à jouer : ')

        try:
            numero = int(numero)
            D = {}
            for i, nom_fichier in enumerate(os.listdir("cartes")):
                if nom_fichier.endswith(".txt"):
                    chemin = os.path.join("cartes", nom_fichier)
                    D[i + 1] = chemin
                if "labyrinthe" in os.listdir("cartes"):
                    if numero > len(D) + 1:
                        print("Vous avez entrée un numéro invalide")
                        continue
                else:
                    if numero > len(D):
                        print("Vous avez entrée un numéro invalide")
                        continue
            if numero <= 0:
                print("Vous avez entrée un numéro invalide")
                continue
        except ValueError:
            print("Vous n'avez pas saisi de nombre")
            continue

        if numero in D.keys():
            carte = D[numero]
            Labyrinthe = labyrinthe(carte)
        else:
            with open(os.getcwd() +'\\cartes\\labyrinthe', 'rb') as fichier:
                mon_depickler = pickle.Unpickler(fichier)
                Labyrinthe = mon_depickler.load()
                carte = 'cartes\\facile.txt'

        afficher_labyrinthe(Labyrinthe)
        deplacement = True
        while deplacement:
            direction = choisir_direction()
            perso = 'X'
            line, column = position_robot(Labyrinthe, perso)
            if len(direction) == 1:
                n = 1
            if len(direction) == 2:
                n = int(direction[1])
            if direction[0] == 'E':
                if n > len(Labyrinthe[line]) - column - 1:
                    print("Vous ne pouvez pas faire ça")
                    continue
                liste_du_parcour = []
                for i in range(n + 1):
                    liste_du_parcour.append(Labyrinthe[line][column + i])
                if 'O' in liste_du_parcour:
                    print("Vous ne pouvez pas faire ça, il y'a un mur")
                    continue
                else:
                    Labyrinthe = labyrinthe_sans_perso(labyrinthe(carte), perso)
                    Labyrinthe[line][column + n] = 'X'
                    afficher_labyrinthe(Labyrinthe)
                    if labyrinthe_sans_perso(labyrinthe(carte), perso)[line][column + n] == 'U':
                        print("BRAVO vous vaez gagnez !!!")
                        deplacement = False
                        choix_labyrinthe = False
                        continuer_partie = False
            elif direction[0] == 'O':
                if n > column:
                    print("Vous ne pouvez pas faire")
                    continue
                liste_du_parcour = []
                for i in range(n + 1):
                    liste_du_parcour.append(Labyrinthe[line][column - i])
                if 'O' in liste_du_parcour:
                    print("Vous ne pouvez pas faire ça, il y'a un mur")
                    continue
                else:
                    Labyrinthe = labyrinthe_sans_perso(labyrinthe(carte), perso)
                    Labyrinthe[line][column - n] = 'X'
                    afficher_labyrinthe(Labyrinthe)
                    if labyrinthe_sans_perso(labyrinthe(carte), perso)[line][column - n] == 'U':
                        print("BRAVO vous vaez gagnez !!!")
                        deplacement = False
                        choix_labyrinthe = False
                        continuer_partie = False
            elif direction[0] == 'N':
                if n > line:
                    print("Vous ne pouvez pas faire ça")
                    continue
                liste_du_parcour = []
                for i in range(n + 1):
                    liste_du_parcour.append(Labyrinthe[line - i][column])
                if 'O' in liste_du_parcour:
                    print("Vous ne pouvez pas faire ça, il y'a un mur.")
                    continue
                else:
                    Labyrinthe = labyrinthe_sans_perso(labyrinthe(carte), perso)
                    Labyrinthe[line - n][column] = 'X'
                    afficher_labyrinthe(Labyrinthe)
                    if labyrinthe_sans_perso(labyrinthe(carte), perso)[line - n][column] == 'U':
                        print("BRAVO vous vaez gagnez !!!")
                        deplacement = False
                        choix_labyrinthe = False
                        continuer_partie = False
            elif direction[0] == 'S':
                if n > len(Labyrinthe) - line - 1:
                    print("Vous ne pouvez pas faire ça")
                    continue
                liste_du_parcour = []
                for i in range(n+1):
                    liste_du_parcour.append(Labyrinthe[line + i][column])
                if 'O' in liste_du_parcour:
                    print("Vous ne pouvez pas faire ça, il y'a un mur")
                    continue
                else:
                    Labyrinthe = labyrinthe_sans_perso(labyrinthe(carte), perso)
                    Labyrinthe[line + n][column] = 'X'
                    afficher_labyrinthe(Labyrinthe)
                    if labyrinthe_sans_perso(labyrinthe(carte), perso)[line + n][column] == 'U':
                        print("BRAVO vous vaez gagnez !!!")
                        deplacement = False
                        choix_labyrinthe = False
                        continuer_partie = False
            elif len(direction) == 2 and direction[0] == 'Q':
                print("Vous n'avez pas saisi une commande valide")
            elif len(direction) == 1 and direction == "Q":
                print("Vous avez sauvegarder et quitter la partie")
                enregistrer_partie(Labyrinthe)
                deplacement = False
                choix_labyrinthe = False
                continuer_partie = False



