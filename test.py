def labyrinthe(fichier):
    Labyrinthe = []
    with open(fichier, 'r') as une_carte:
        for line in une_carte:
            liste = line.strip()
            Labyrinthe.append(list(liste))
    return Labyrinthe

def afficher_labyrinthe(labyrinthe):
    for line in labyrinthe:
        print(''.join(line))

def choisir_direction():
    direction = input('Entrez une commande: N(Nord), S(Sud), E(Est), O(Ouest),' 
                           'Q(sauvegarder et quitter): ')
    if len(direction)>2 or direction == '' or direction == ' ' or direction == '  ':
        print("Vous n'avez pas saisi une réponse valide.")
        return choisir_direction()
    if len(direction) == 1:
        if not direction.isalpha():
            print("Vous n'avez pas saisi de lettre")
            return choisir_direction()
        else:
            direction = direction.upper()
            return direction
    if len(direction) == 2:
        if not direction[0].isalpha():
            print("Vous n'avez pas saisi de lettre")
            return choisir_direction()
        elif direction[1].isalpha():
            print("Vous n'avez pas saisi de lettre")
            return choisir_direction()
        else:
            direction = direction[0].upper() + direction[1]
            return direction


def position_robot(un_labyrinthe, wanted):
    for index_line, line in enumerate(un_labyrinthe):
        for index_column, column in enumerate(line):
            if column == wanted:
                l, c = index_line, index_column
    return l, c

def labyrinthe_sans_perso(un_labyrinthe, perso):
    for index_line, line in enumerate(un_labyrinthe):
        for index_column, column in enumerate(line):
            if column == perso:
                un_labyrinthe[index_line][index_column] = ' '
    return un_labyrinthe


continuer_partie = True

while continuer_partie:
    print("Labyrinthes existants :")
    print("  1 - facile.\n  2 - prison.")
    choix_labyrinthe = True
    while choix_labyrinthe:
        numero = input('Entrez un numéro de labyrinthe pour commencer à jouer : ')

        try:
            numero = int(numero)
        except ValueError:
            print("Vous n'avez pas saisi de nombre.")
            continue
        if numero == 1:
            carte = 'facile.txt'
        elif numero == 2:
            carte = 'prison.txt'
        Labyrinthe = labyrinthe(carte)
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
                    print("Vous ne pouvez pas faire ça, vous serez hors de la carte du jeux")
                    continue
                l = []
                for i in range(n + 1):
                    l.append(Labyrinthe[line][column + i])
                    if Labyrinthe[line][column + i] == 'O':
                        print("Vous ne pouvez pas aller par là, il y'a un mur.")
                        continue
                if 'O' not in l:
                    Labyrinthe = labyrinthe_sans_perso(labyrinthe(carte), perso)
                    Labyrinthe[line][column + n] = 'X'
                    afficher_labyrinthe(Labyrinthe)
                    if labyrinthe_sans_perso(labyrinthe(carte), perso)[line][column + n] == 'U':
                        print("BRAVO vous vaez gagnez !!!")
                        deplacement = False
            elif direction[0] == 'O':
                if n > column:
                    print("Vous ne pouvez pas faire ça, vous serez hors de la carte du jeux")
                    continue
                l = []
                for i in range(n + 1):
                    l.append(Labyrinthe[line][column - i])
                    if Labyrinthe[line][column - i] == 'O':
                        print("Vous ne pouvez pas aller par là, il y'a un mur.")
                        continue
                if 'O' not in l:
                    Labyrinthe = labyrinthe_sans_perso(labyrinthe(carte), perso)
                    Labyrinthe[line][column - n] = 'X'
                    afficher_labyrinthe(Labyrinthe)
                    if labyrinthe_sans_perso(labyrinthe(carte), perso)[line][column - n] == 'U':
                        print("BRAVO vous vaez gagnez !!!")
                        deplacement = False
            elif direction[0] == 'N':
                if n > line:
                    print("Vous ne pouvez pas faire ça, vous serez hors de la carte du jeux")
                    continue
                l = []
                for i in range(n + 1):
                    l.append(Labyrinthe[line - i][column])
                    if Labyrinthe[line - i][column] == 'O':
                        print("Vous ne pouvez pas aller par là, il y'a un mur.")
                        continue
                if 'O' not in l:
                    Labyrinthe = labyrinthe_sans_perso(labyrinthe(carte), perso)
                    Labyrinthe[line - n][column] = 'X'
                    afficher_labyrinthe(Labyrinthe)
                    if labyrinthe_sans_perso(labyrinthe(carte), perso)[line - n][column] == 'U':
                        print("BRAVO vous vaez gagnez !!!")
                        deplacement = False
            elif direction[0] == 'S':
                if n > len(Labyrinthe) - line - 1:
                    print("Vous ne pouvez pas faire ça, vous serez hors de la carte du jeux")
                    continue
                l = []
                for i in range(n+1):
                    l.append(Labyrinthe[line + i][column])
                    if Labyrinthe[line + i][column] == 'O':
                        print("Vous ne pouvez pas aller par là, il y'a un mur.")
                        continue
                if 'O' not in l:
                    Labyrinthe = labyrinthe_sans_perso(labyrinthe(carte), perso)
                    Labyrinthe[line + n][column] = 'X'
                    afficher_labyrinthe(Labyrinthe)
                    if labyrinthe_sans_perso(labyrinthe(carte), perso)[line + n][column] == 'U':
                        print("BRAVO vous vaez gagnez !!!")
                        deplacement = False




