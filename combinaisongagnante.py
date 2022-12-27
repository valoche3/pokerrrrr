import random
Piques= ["Pi_As","Pi_R","Pi_D","Pi_V","Pi_10","Pi_9","Pi_8","Pi_7","Pi_6","Pi_5","Pi_4","Pi_3","Pi_2"] #cartes triées par ordre
Trèfles=["Tr_As","Tr_R","Tr_D","Tr_V","Tr_10","Tr_9","Tr_8","Tr_7","Tr_6","Tr_5","Tr_4","Tr_3","Tr_2"]
Coeurs=["Co_As","Co_R","Co_D","Co_V","Co_10","Co_9","Co_8","Co_7","Co_6","Co_5","Co_4","Co_3","Co_2"]
Carreaux=["Ca_As","Ca_R","Ca_D","Ca_V","Ca_10","Ca_9","Ca_8","Ca_7","Ca_6","Ca_5","Ca_4","Ca_3","Ca_2"]
paquet= Piques + Trèfles + Coeurs + Carreaux
nombre_de_joueurs= int(input("Combien de joueurs?"))
cartes=[]
paquet3=list(paquet)
for i in range (0,5):
    m=random.randint(0,len(paquet3))
    cartes.append(paquet3[paquet3.pop(m)])
mains={}
#création du dictionnaire des c
for i in range (0,nombre_de_joueurs):
    mains['j'+str(i)]=0

#création du dictionnaire des mises
argent={}
for i in range (0, nombre_de_joueurs):
    argent['j'+str(i)]=500

mise={}
for i in range (0,nombre_de_joueurs):
    mise['j'+str(i)]=0

#distribution:
def distribution(nombre_de_joueurs):
    paquet2=list(paquet)
    #joueurs=[]
    for i in mains :
        mains[i]=[0,0]
        n1 = random.randint(0,len(paquet2))
        mains[i][0]=paquet2.pop(n1)
        n2 = random.randint(0,len(paquet2))
        mains[i][1]= paquet2.pop(n2)
    print(mains)

distribution(2)

#fonction qui trie par chiffres+couleurs et par chiffres
res=[]
tri_chiffre=[]
tri_chiffres_couleurs=[]
for j in joueurs: 
    tot = cartes + joueurs[j]
    for k in range(0,len(paquet)):
        if paquet[k]== tot[0] or paquet[k]== tot[1] or paquet[k]== tot[2] or paquet[k]== tot[3]or paquet[k]== tot[4]:
            tri_chiffres_couleurs.append(paquet[k])
    for p in tot:
        if 'R' in p:
            tri_chiffre.append(p)
        if 'D' in p:
            tri_chiffre.append(p)
        if 'V' in p:
            tri_chiffre.append(p)
        if '10' in p:
            tri_chiffre.append(p)
        if '9' in p:
            tri_chiffre.append(p)
        if '8' in p:
            tri_chiffre.append(p)
        if '7' in p:
            tri_chiffre.append(p)
        if '6' in p:
            tri_chiffre.append(p)
        if '5' in p:
            tri_chiffre.append(p)
        if '4' in p:
            tri_chiffre.append(p)
        if '3' in p:
            tri_chiffre.append(p)
        if '2' in p:
            tri_chiffre.append(p)

#Compter le nombre de chaque couleur
compteur_pique=0
compteur_trèfle=0
compteur_coeur=0
compteur_carreau=0
val=[0,0,0,0,0,0,0,0,0,0,0,0]
for j in tot:
    while 'Pi' in j:
        compteur_pique += 1
    while 'Tr' in j:
        compteur_trèfle += 1
    while 'Co' in j:
        compteur_coeur += 1
    while 'Ca' in j:
        compteur_carreau +=1
for k in tot: 
    if 'R' in p:
            val[0]+=1
    if 'D' in p:
            val[1]+=1
    if 'V' in p:
            val[2]+=1
    if '10' in p:
            val[3]+=1
    if '9' in p:
            val[4]+=1
    if '8' in p:
            val[5]+=1
    if '7' in p:
            val[6]+=1
    if '6' in p:
            val[7]+=1
    if '5' in p:
            val[8]+=1
    if '4' in p:
            val[9]+=1
    if '3' in p:
            val[10]+=1
    if '2' in p:
            val[11]+=1

if compteur_pique >= 5 or compteur_trèfle>= 5 or compteur_carreau>=5 or compteur_coeur>= 5:
    #le test pour quinte flush royal
    if Piques[0,4] in tri_chiffres_couleurs or Trèfles[0,4] in tri_chiffres_couleurs or Carreaux[0,4] in tri_chiffres_couleurs or Coeurs[0,4] in tri_chiffres_couleurs:
        test_gain[j][0]= 10
        test_gain[j][1]=0
        break
     
    #faire le test pour quinte flush


if 4 in val:
    #on a un carré
    test_gain[j][0]=8
    test_gain[j][1]=val.index(4)
    break
# on compte le nombre de 3 dans val
nb_3=0
for a in val:
    if a ==3:
        nb_3+=1
if ( 2 in val and 5 in val) or (2 in val and 3 in val) or (2 in val and 4 in val) or ( 3 in val and 4 in val) or nb_3==2:
    #on a un full
    test_gain[j][0]=7
    k=0
    for i in range (len(val)-1,0)
        while k!=-1:
        if val[i]==5 or val[i]==4 or val[i]==3:
            k=-1
            test_gain[j][1]= i

if compteur_pique >= 5 or compteur_trèfle>= 5 or compteur_carreau>=5 or compteur_coeur>= 5:
    #on a une couleur
    test_gain[j][0]=6
    for i in tri_chiffre:
        

#test suite quinte

if 3 in val or 4 in val:
    #on a un brelan
    test_gain[j][0]=4

#on compte le nombre de 2 dans val
nb_2=0
for i in val:
    if i==2:
        nb_2+=1
if nb_2>=2:
    #on a deux paires
    test_gain[j][0]=3

if 2 in val :
    #on a une paire
    test_gain[j][0]=2


