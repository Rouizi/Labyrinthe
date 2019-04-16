def labyrinthe(fichier):
    Labyrinthe = []
    with open(fichier, 'r') as une_carte:
        for line in une_carte:
            liste = line.strip()
            Labyrinthe.append(list(liste))
    return Labyrinthe

def choisir_direction():
    direction = input('entrez une direction: n(nord), s(sud)'
                              'e(est), o(ouest): ').lower()
    if len(direction)>1 or not direction.isalpha():
        print("Vous n'avez pas saisi une lettre valide.")
        return choisir_direction()
    else:
        return direction

def position_robot(un_labyrinthe):
    for index_line, line in enumerate(un_labyrinthe):
        for index_column, column in enumerate(line):
            if column == 'X':
                l, c = index_line, index_column
    return l, c

def verification_direction(un_labyrinthe, line, column):
    if un_labyrinthe[line][column] == 'O':
        print("vous ne pouvez aller par là")
        return direction




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
            Labyrinthe = labyrinthe('facile.txt')
            for line in Labyrinthe:
                chaine = ''.join(line)
                print(chaine)
            direction = choisir_direction()
            if direction == 'e':
                line, column = position_robot(Labyrinthe)
                verification_deplaction(Labyrinthe, line, column-1)
            if direction == 'o':
                pass
            if direction == 'n':
                pass
            if direction == 's':
                pass


            break
        if numero == 2:
            Labyrinthe = labyrinthe('prison.txt')
            for line in Labyrinthe:
                chaine = ''.join(line)
                print(chaine)
            direction = choisir_direction()
            if direction == 'e':
                pass
            if direction == 'o':
                pass
            if direction == 'n':
                pass
            if direction == 's':
                pass
            break

