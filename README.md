# poker

Ravayrol Mélie

Sterlin Valentine

Vignault Aurélie


Installation Pygame
------------

   pip3 install pygame


Help
----

If you are just getting started with pygame, you should be able to
get started fairly quickly.  Pygame comes with many tutorials and
introductions.  There is also full reference documentation for the
entire library. Browse the documentation on the `docs page`_. You
can also browse the documentation locally by running `python -m pygame.docs`
in your terminal. If the docs aren't found locally, it'll launch the online
website instead.

The online documentation stays up to date with the development version
of pygame on github.  This may be a bit newer than the version of pygame
you are using. To upgrade to the latest full release, run 
``pip install pygame --upgrade`` in your terminal.

Best of all, the examples directory has many playable small programs
which can get you started playing with the code right away.

Procédure à suivre 
-------------------

Mode d'emploi du poker :

- aller dans la branche ***Main_Final***
- ouvrir le fichier 'poker.py'
- importer les fichiers suivants qui continennent les fonctions appelées dans poker.py
  - combinaisongagnante.py
  - fin_de_petite_partie.py
  - graphique.py
  - miseEnplace.py
  - tourdejeu.py
- lancer le fichier 'poker.py'
- choisir si l'on souhaite une version avec interface graphique ou non (Y ou N)
- entrer le nombre de joueurs
- entrer la petite blinde
- A ce moment-là du jeu, l'interface graphique se lance mais la zone de dialogue reste le terminal.
- suivre les différentes indications du terminal : les réponses se font en toutes lettres (pour la formulation "s'aligner - checker", il suffit d'écrire "s'aligner")
- Pour terminer un tour, même si tout le monde s'est mis à la même mise, il faut que la première personne ayant misé cette mise s'aligne. 
- A la fin d'une petite partie (flop-turn-river), l'algorithme vous demande si vous voulez continuer pour un autre tour de 'flop-turn-river'.

PS : Nous avons fait le maximum sur l'interface graphique en utilisant pygame. C'est assez complexe d'intégrer une bibliothèque complète sur python, de la manipuler et de l'implémenter correctement avec le jeu. 
Cependant, c'était intéressant à faire car nous avons vraiment eu le sentiment de créer un jeu. 
Par manque de temps, nous avons donc créé un hybride interface graphique/terminal.

