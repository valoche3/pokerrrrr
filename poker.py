from src.miseEnPlace import Partie
from src.combinaisongagnante import détermination_du_vainqueur
import src.tour_de_jeu

def main():
    partie = Partie()
    print("Début du jeu")
    print(f"Les mains des joueurs sont : {partie.mains}")
    print(f"Les cartes du milieu sont : {partie.cartes_du_milieu}")
    détermination_du_vainqueur(partie.mains, partie.cartes_du_milieu)
    print("Fin du jeu")


main()
