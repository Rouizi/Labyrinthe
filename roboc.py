# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

import os

os.chdir("C:/Python/Labyrinthe/roboc")

from carte import Carte

from labyrinthe import *

from Enregistrement import *

# On charge les cartes existantes

cartes = []

premier_passage = True

liste_controle = ["q", "n", "e", "s", "o"]

choix = 0

for nom_fichier in os.listdir("cartes"):  # nom_fichier contient les cartes

    if nom_fichier.endswith(".txt"):  # Si nom fichier se termine par ".txt"

        chemin = os.path.join("cartes", nom_fichier)  # Un nouveau chemin "cartes//facile.txt ou prison.txt"
        nom_carte = nom_fichier[:-3].lower()  # facile., prison. minuscule

        with open(chemin, "r") as fichier:  # On pointe directement l'intérieur des fichiers avec des cartes

            contenu = fichier.read()  # variable qui contient les cartes
            cartes.append(contenu)

with open("Partie", "rb") as fichier:
    unpickler = pickle.Unpickler(fichier)
    dictionnaire_partie = unpickler.load()  # On récupère le dictionnaire_partie qui est dans le dossier Partie

if not dictionnaire_partie:  # Si le dictionnaire est vide, on crée une nouvelle partie

    nom_partie = "Nouvelle Partie"

else:

    print("Il y a déjà des parties existantes : ")

    compteur_partie_existantes = 1  # Représente le chiffre avant la partie, exemple (1 -)
    indice_liste_partie = 0
    liste_partie = dictionnaire_partie.keys()  # liste_partie prend toutes les clés du dictionnaire_partie
    liste_partie = list(liste_partie)  # liste_partie devient une liste
    liste_partie.append("Nouvelle Partie")  # On ajoute nouvelle partie en dernier choix

    while compteur_partie_existantes <= len(liste_partie):
        print("{} - {}".format(compteur_partie_existantes,
                               liste_partie[indice_liste_partie]))  # On affiche les parties sous forme 1 - partie
        compteur_partie_existantes += 1
        indice_liste_partie += 1

    partie_recuperation = ""

    while not isinstance(partie_recuperation, int):

        partie_recuperation = input("Choisissez un numéro : ")

        try:

            partie_recuperation = int(partie_recuperation)

            if partie_recuperation > len(liste_partie) or partie_recuperation < 1:
                print("Vous avez saisi un mauvais numéro")
                partie_recuperation = str(partie_recuperation)

        except ValueError:

            print("Vous n'avez pas saisie un nombre")

    partie_recuperation -= 1  # On enlève 1 de partie récuparation pour pouvoir en faire un indice de liste_partie

    nom_partie = liste_partie[partie_recuperation]  # Partie est égal au nom de la partie

if nom_partie == "Nouvelle Partie":

    nom_partie = input("Choisissez le nom de votre partie : ")

    print("Labyrinthes existants :")

    print("1 - facile.")
    print("2 - facile_teste.")
    print("3 - prison.")

    while choix > len(cartes) or choix < 1:

        try:

            print("\n")
            choix = input("Entre un numéro de labyrinthe pour commencer à jouer : ")
            choix = int(choix)

        except ValueError:

            print("Vous n'avez pas rentré un chiffre")
            choix = 0

    print("\n")

    if choix == 1:
        print(cartes[0])
        objet_partie = Labyrinthe(cartes[0])
    elif choix == 2:
        print(cartes[1])
        objet_partie = Labyrinthe(cartes[1])
    elif choix == 3:
        print(cartes[2])
        objet_partie = Labyrinthe(cartes[2])

else:

    objet_partie = dictionnaire_partie[nom_partie]
    print("\n")
    print(objet_partie)

# On affiche les cartes existantes

print("\n")

while objet_partie.sortie not in objet_partie.liste_passage:

    controle = input("")
    objet_partie.commandes("f")

    if not controle:
        controle = "f"  # Si pas de controle, on oblige le joueur à mettre une lettre qui se trouve dans liste controle

    while controle[0].lower() not in liste_controle:
        print("\n")
        print("Vous ne pouvez pas utiliser cette commande")
        print("\n")
        print(objet_partie)
        controle = input("")
        if not controle:
            controle = "f"

    print("\n")

    if controle[0].lower() == "q":
        if len(controle) > 1:
            print("Vous ne pouvez pas utiliser cette commande")
            print("\n")
            print(objet_partie)
        else:
            objet_partie.commandes(controle)
            dictionnaire_partie[nom_partie] = objet_partie
            enregistrer("Partie", dictionnaire_partie)
            break

    elif len(controle) > 1:

        plusieurs_cases = controle[1:]  # On met dans une variable les chiffres qui viennent après la première lettre
        try:
            plusieurs_cases = int(plusieurs_cases)
        except ValueError:
            print("Vous ne pouvez pas utiliser cette commande")
            print("\n")
            print(objet_partie)
            print("\n")
            continue

        compteur_cases = 0

        while compteur_cases != plusieurs_cases:

            objet_partie.commandes(controle[0])
            print(objet_partie)
            print("\n")
            if objet_partie.sortie in objet_partie.liste_passage:
                break
            compteur_cases += 1

    else:

        objet_partie.commandes(controle)
        print(objet_partie)

    dictionnaire_partie[nom_partie] = objet_partie

    enregistrer("Partie", dictionnaire_partie)

os.system("pause")
