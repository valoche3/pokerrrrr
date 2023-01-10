from src.combinaisongagnante import détermination_du_vainqueur
from src.fin_de_petite_partie import mise_a_niveau_argent
from src.pourmel import détermination_premier_dealer
from src.fin_de_petite_partie import gagnants_finaux
from src.pourmel import détermination_dealer
from src.pourmel import tour_de_jeu
from src.graphique import Graphique
from src.miseEnPlace import Partie


def main():
    choix_du_programe_status = True

    while choix_du_programe_status:
        choix_du_programe = input("\nVoulez-vous lancer le jeu avec l'interface graphique ? (Y/N) ")
        if choix_du_programe.upper() == "Y" or choix_du_programe.upper() == "N":
            choix_du_programe_status = False
            mode_graphique = choix_du_programe == "Y"

            partie = Partie()
            graphique = Graphique(mode_graphique)

            dealer = None
            partie_en_cours = True

            while partie_en_cours:
                # Commence un nouvel partie de jeu
                partie.remise_à_zéro()

                if dealer == None :
                    dealer = détermination_premier_dealer(partie.nombre_de_joueurs)
                else:
                    dealer = détermination_dealer(dealer)

                print(f"\nLes mains des joueurs sont : {partie.mains}")
                graphique.affichage_des_cartes_joueurs(partie.mains, partie.argent)

                present, partie.mises = tour_de_jeu(graphique, partie.nombre_de_joueurs, partie.mises, partie.argent, partie.mise_verif, dealer, partie.cartes_du_milieu)
                joueurs_gagnants = détermination_du_vainqueur(present, partie.cartes_du_milieu, partie.mains)
                partie.argent = mise_a_niveau_argent(joueurs_gagnants, partie.argent, partie.mises)

                print(partie.argent)

                partie_en_cours = True if input("\nVoulez vous continuer (OUI ou NON) : ").upper == 'OUI' else False

            print(f"\nLe joueur gagnant est : {gagnants_finaux(partie.argent)}")

            return
        choix_du_programe = ""


if __name__ == "__main__" :
    main()
