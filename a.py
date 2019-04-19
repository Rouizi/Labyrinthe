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
            if len(direction) == 1:
                n = 1
                if direction == 'E':
                    x, y = 1, 0
                elif direction == 'O':
                    x, y = -1, 0
                elif direction == 'N':
                    x, y = 0, -1
                elif direction == 'S':
                    x, y = 0, 1
            if len(direction) == 2:
                n = int(direction[1])
                if direction[0] == 'E':
                    x, y = n, 0
                elif direction[0] == 'O':
                    x, y = -n, 0
                elif direction[0] == 'N':
                    x, y = 0, -n
                elif direction[0] == 'S':
                    x, y = 0, n
            line, column = position_robot(Labyrinthe, perso)
            if x == n:
                for i in range(1, n+1):
                    if Labyrinthe[line + y][column + i] == 'O':
                        print("Vous ne pouvez pas aller par là, il y'a un mur.")
                        continue
            if Labyrinthe[line + y][column + x] == '.' or \
               Labyrinthe[line + y][column + x] == ' ' or \
               Labyrinthe[line + y][column + x] == 'X' or \
               Labyrinthe[line + y][column + x] == 'U':
                Labyrinthe = labyrinthe_sans_perso(labyrinthe(carte), perso)
                Labyrinthe[line + y][column + x] = 'X'
                afficher_labyrinthe(Labyrinthe)
                if labyrinthe_sans_perso(labyrinthe(carte), perso)[line + y][column + x] == 'U':
                    print("BRAVO vous vaez gagnez !!!")
                    deplacement = False