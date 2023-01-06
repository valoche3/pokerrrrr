from src.miseEnPlace import Partie
from src.miseEnPlace import sous_Partie
from src.combinaisongagnante import détermination_du_vainqueur

def main():
    partie = Partie()
    sous_partie = sous_Partie(partie.nombre_de_joueurs)
    print("Début du jeu")
    print(f"Les mains des joueurs sont : {partie.mains}")
    print(f"Les cartes du milieu sont : {partie.cartes_du_milieu}")
    détermination_du_vainqueur(partie.mains, partie.cartes_du_milieu)
    print("Fin du jeu")

main()
