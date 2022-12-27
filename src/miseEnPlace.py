from random import randint


Piques = ["Pi_As","Pi_R","Pi_D","Pi_V","Pi_10","Pi_9","Pi_8","Pi_7","Pi_6","Pi_5","Pi_4","Pi_3","Pi_2"] #cartes triées par ordre
Trèfles = ["Tr_As","Tr_R","Tr_D","Tr_V","Tr_10","Tr_9","Tr_8","Tr_7","Tr_6","Tr_5","Tr_4","Tr_3","Tr_2"]
Coeurs = ["Co_As","Co_R","Co_D","Co_V","Co_10","Co_9","Co_8","Co_7","Co_6","Co_5","Co_4","Co_3","Co_2"]
Carreaux = ["Ca_As","Ca_R","Ca_D","Ca_V","Ca_10","Ca_9","Ca_8","Ca_7","Ca_6","Ca_5","Ca_4","Ca_3","Ca_2"]


def recupere_le_nombre_de_joueur():
    nombre_de_joueurs = 0

    while True:
        nombre_de_joueurs = int(input("Combien de joueurs ? > "))
        if nombre_de_joueurs <= 1 or nombre_de_joueurs > 10 :
            print("Nombre de joueurs doit être compris entre 0 et 10 !")
        else:
            break

    return nombre_de_joueurs


def initalisation_de_dictionnaire(nombre_de_joueurs, valeur_par_défaut):
    dictionnaire = {}
    for i in range (0, nombre_de_joueurs):
        dictionnaire['j' + str(i)] = valeur_par_défaut

    return dictionnaire


def distribution_des_cartes(paquet_de_jeu, nombre_de_joueurs):
    mains = initalisation_de_dictionnaire(nombre_de_joueurs, 0)

    for i in mains :
        mains[i] = [0, 0]
        mains[i][0] = paquet_de_jeu.pop(randint(0, len(paquet_de_jeu)))
        mains[i][1]= paquet_de_jeu.pop(randint(0, len(paquet_de_jeu)))
    return mains


class Partie:
    def __init__ (self):
        self.nombre_de_joueurs = recupere_le_nombre_de_joueur()
        self.paquet_de_jeu = Piques + Trèfles + Coeurs + Carreaux
        self.mains = distribution_des_cartes(self.paquet_de_jeu, self.nombre_de_joueurs)
        self.mises = self.mises = initalisation_de_dictionnaire(self.nombre_de_joueurs, 0)
        self.argent = self.argent = initalisation_de_dictionnaire(self.nombre_de_joueurs, 500)
