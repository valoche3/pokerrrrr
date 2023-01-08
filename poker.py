from src.miseEnPlace import Partie
from src.miseEnPlace import sous_Partie
from src.combinaisongagnante import détermination_du_vainqueur
from src.pourmel import tour_de_jeu
from src.pourmel import détermination_dealer
from src.pourmel import détermination_premier_dealer

def main():
    partie = Partie()
    continuer = 'oui'
    dealer = None
    while continuer == 'oui' :
        sous_partie = sous_Partie(partie.nombre_de_joueurs)
        print("Début du jeu")
        if dealer == None :
            dealer = détermination_premier_dealer(partie.nombre_de_joueurs)
        else:
            dealer = détermination_dealer(dealer)
        print(f"Les mains des joueurs sont : {sous_partie.mains}")
        print(f"Les cartes du milieu sont : {sous_partie.cartes_du_milieu}")
        present = tour_de_jeu(partie.nombre_de_joueurs, sous_partie.mises, partie.argent, sous_partie.mise_verif, dealer)
        détermination_du_vainqueur(present, sous_partie.cartes_du_milieu, sous_partie.mains)
        print("Fin du jeu")
        continuer = input()
        

main()
