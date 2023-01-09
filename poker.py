from src.combinaisongagnante import détermination_du_vainqueur
from src.fin_de_petite_partie import mise_a_niveau_argent
from src.pourmel import détermination_premier_dealer
from src.pourmel import détermination_dealer
from src.pourmel import tour_de_jeu
from src.miseEnPlace import Partie
from src.fin_de_petite_partie import gagnants_finaux
import time


def main():
    choix_du_programe_status = False

    while choix_du_programe_status:
        choix_du_programe = input("Voulez-vous lancer le jeu avec l'interface graphique ? (Y/N) ")
        if choix_du_programe == "Y":
            choix_du_programe_status = True
            return
        elif choix_du_programe == "N":
            choix_du_programe_status = True
            return
        choix_du_programe = ""

    partie = Partie()

    dealer = None
    partie_en_cours = True

    while partie_en_cours:
        # Commence un nouvel partie de jeu
        partie.remise_à_zéro()

        if dealer == None :
            dealer = détermination_premier_dealer(partie.nombre_de_joueurs)
        else:
            dealer = détermination_dealer(dealer)
        print(f"Les mains des joueurs sont : {partie.mains}")
        #print(f"Les cartes du milieu sont : {partie.cartes_du_milieu}")
        present, partie.mises = tour_de_jeu(partie.nombre_de_joueurs, partie.mises, partie.argent, partie.mise_verif, dealer, partie.cartes_du_milieu)
        joueurs_gagnants = détermination_du_vainqueur(present, partie.cartes_du_milieu, partie.mains)
        partie.argent = mise_a_niveau_argent(joueurs_gagnants, partie.argent, partie.mises)
        print(partie.argent)
        partie_en_cours = True if input("Voulez vous continuer : oui ou non") == 'oui' else False
    print(f"Le joueur gagnant est : {gagnants_finaux(partie.argent)}")


if __name__ == "main" :
    main()
