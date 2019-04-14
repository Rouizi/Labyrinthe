nombre_mise = -1
while nombre_mise < 0 or nombre_mise > 49:
    nombre_mise = input("Tapez le nombre sur lequel vous voulez miser (entre 0 et 49) : ")
    # On convertit le nombre misé
    try:
        nombre_mise = int(nombre_mise)
    except ValueError:
        print("Vous n'avez pas saisi de nombre")
        nombre_mise = -1
        continue
    if nombre_mise < 0:
        print("Ce nombre est négatif")
    if nombre_mise > 49:
        print("Ce nombre est supérieur à 49")