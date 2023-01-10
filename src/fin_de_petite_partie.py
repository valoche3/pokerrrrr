from src.miseEnPlace import distribution_des_cartes_joueurs

def mise_a_niveau_argent(joueurs_gagnants, dico_argent, dict_mises):
    argent_au_milieu = 0
    for joueur in dict_mises :
        argent_au_milieu += dict_mises[joueur]
        dico_argent[joueur] -= dict_mises[joueur]
    argent_gagné = argent_au_milieu / len(joueurs_gagnants)
    for joueur in joueurs_gagnants:
        dico_argent[joueur] += argent_gagné
    return dico_argent

def gagnants_finaux(dico_argent):
    maxi = max(dico_argent)
    gagnants = []
    for joueur in dico_argent :
        if dico_argent[joueur] == dico_argent[maxi] :
            gagnants.append(joueur)
    return gagnants
