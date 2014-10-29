Un script python qui permet de récupérer certaines informations sur le cavalier (dans un jeu d'échec).
Il dispose de plusieurs fonctions :
	- positionsPossibles(position): Renvoie toutes les positions accessibles depuis une case en un mouvement;
	- accessibleEnNCoups(position_depart, position_arrivee, nbreDeCoups): vérifie si on peut se déplacer de position_depart à position_arrivée en nbreDeCoups coups;
	- nbreMiniCoups(position_depart, position_arrivee): Renvoie le nombre minimum de coups pour aller d'une case à une autre;
	- listeDeplacements(position_depart, position_arrivee, nbreCoups, tableauSortie, tableauTmp): Renvoie tous les déplacements possibles pour aller d'une case à une autre en nbreCoups coups dans le tableau tableauSortie (notez que les deux tableaux tableauSortie et tableauTmp doivent être vides sous peine de causer bugs en tous genres)
	- deplacementLePlusCourt(pos_dep, pos_arr): Renvoie TOUS les chemins les plus courts pour aller d'une position à une autre.

Notez que les positions doivent s'exprimer sous la forme d'une liste de deux éléments, dont le premier sera l'abscisse et le second l'ordonnée. La numérotation commence à 1 et se termine à 8.
