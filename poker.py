from src.miseEnPlace import Partie
from src.combinaisongagnante import détermination_du_vainqueur

def main():
    partie = Partie()
    print('début du jeu')
    détermination_du_vainqueur(partie.mains, partie.cartes_du_milieu)


main()