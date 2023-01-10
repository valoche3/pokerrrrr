from random import randint

Piques = ["Pique_As", "Pique_R", "Pique_D", "Pique_V", "Pique_10", "Pique_9", "Pique_8", "Pique_7", "Pique_6", "Pique_5", "Pique_4", "Pique_3", "Pique_2"]
Trèfles = ["Trèfle_As", "Trèfle_R", "Trèfle_D", "Trèfle_V", "Trèfle_10", "Trèfle_9", "Trèfle_8", "Trèfle_7", "Trèfle_6", "Trèfle_5", "Trèfle_4", "Trèfle_3", "Trèfle_2"]
Coeurs = ["Coeur_As", "Coeur_R", "Coeur_D", "Coeur_V", "Coeur_10", "Coeur_9", "Coeur_8", "Coeur_7", "Coeur_6", "Coeur_5", "Coeur_4", "Coeur_3", "Coeur_2"]
Carreaux = ["Carreau_As", "Carreau_R", "Carreau_D", "Carreau_V", "Carreau_10", "Carreau_9", "Carreau_8", "Carreau_7", "Carreau_6", "Carreau_5", "Carreau_4", "Carreau_3", "Carreau_2"]


def récupère_le_nombre_de_joueur():
    nombre_de_joueurs = 0

    while True:
        nombre_de_joueurs = int(input("Combien de joueurs ? > "))
        if nombre_de_joueurs <= 1 or nombre_de_joueurs > 10:
            print("Nombre de joueurs doit être compris entre 2 et 10 !")
        else:
            break

    return nombre_de_joueurs


def initialisation_de_dictionnaire(nombre_de_joueurs, valeur_par_défaut):
    dictionnaire = {}
    for i in range(0, nombre_de_joueurs):
        dictionnaire['j' + str(i)] = valeur_par_défaut

    return dictionnaire


def distribution_des_cartes_joueurs(nombre_de_joueurs):
    paquet_de_jeu = Piques + Trèfles + Coeurs + Carreaux
    mains = initialisation_de_dictionnaire(nombre_de_joueurs, 0)

    for i in mains:
            mains[i] = [0, 0]
            mains[i][0] = paquet_de_jeu.pop(randint(0, len(paquet_de_jeu) - 1))
            mains[i][1] = paquet_de_jeu.pop(randint(0, len(paquet_de_jeu) - 1))

    return mains, paquet_de_jeu


def distribution_cartes_du_milieu(paquet_de_jeu):
    cartes_du_milieu = [0, 0, 0, 0, 0]

    for i in range(len(cartes_du_milieu)):
        if i == 0 or i >= 3:
            paquet_de_jeu.pop(randint(0, len(paquet_de_jeu) - 1))
        cartes_du_milieu[i] = paquet_de_jeu.pop(randint(0, len(paquet_de_jeu) - 1))

    return cartes_du_milieu, paquet_de_jeu


class Partie:
    def __init__(self):
        self.nombre_de_joueurs = récupère_le_nombre_de_joueur()
        self.argent = self.argent = initialisation_de_dictionnaire(self.nombre_de_joueurs, 500)
        self.mains, self.paquet_de_jeu = distribution_des_cartes_joueurs(self.nombre_de_joueurs)
        self.mises = self.mises = initialisation_de_dictionnaire(self.nombre_de_joueurs, 0)
        self.cartes_du_milieu, self.paquet_de_jeu = distribution_cartes_du_milieu(self.paquet_de_jeu)
        self.mise_verif = initialisation_de_dictionnaire(self.nombre_de_joueurs, 0)


    def remise_à_zéro(self):
        self.mains, self.paquet_de_jeu = distribution_des_cartes_joueurs(self.nombre_de_joueurs)
        self.mises = initialisation_de_dictionnaire(self.nombre_de_joueurs, 0)
        self.cartes_du_milieu, self.paquet_de_jeu = distribution_cartes_du_milieu(self.paquet_de_jeu)
        self.mise_verif = initialisation_de_dictionnaire(self.nombre_de_joueurs, 0)
