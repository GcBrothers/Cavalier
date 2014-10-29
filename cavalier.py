#!/usr/bin/python3.2
def addMam(tab1, tab2):
    """
    Additionne membre a membre deux tableaux (prévu pour 2 membres, mais marche avec tous tableaux de MEME dimension)
    """
    res = []
    for i in range(0,len(tab1)):
        res.append(tab1[i] + tab2[i])
    return res

def positionValide(position):
    """
    Teste si une position est valide ou non
    """
    if position[0] < 1 or position[1] < 1 or position[0] > 8 or position[1] > 8: #Si ça sort du cadre
        return False

    return True

def positionsPossibles(position_depart):
    """
    Renvoie toutes les positions d'arrivée possibles
    """
    poss = []
    tmp = []
    poss.append(addMam(position_depart, [2,1]))
    poss.append(addMam(position_depart, [1,2]))
    poss.append(addMam(position_depart, [-1,2]))
    poss.append(addMam(position_depart, [-2,1]))
    poss.append(addMam(position_depart, [-2,-1]))
    poss.append(addMam(position_depart, [-1,-2]))
    poss.append(addMam(position_depart, [1,-2]))
    poss.append(addMam(position_depart, [2,-1]))

    #for emt in poss: #Le remove stoppe la boucle ???
    #   if positionValide(emt) == False:
    #       poss.remove(emt)

    for emt in poss:
        if positionValide(emt):
            tmp.append(emt)
    
    return tmp

def accessibleEnNCoups(position_depart, position_arrivee, nbreCoups):
    """
    Précise si le déplacement d'une case à une autre est effectuable en nbreCoups coups
    """
    if nbreCoups > 1:
        for emt in positionsPossibles(position_depart):
            if accessibleEnNCoups(emt, position_arrivee, nbreCoups - 1):
               return True
        return False
    elif nbreCoups == 1:
        if position_arrivee in positionsPossibles(position_depart):
            return True
        return False
    elif nbreCoups == 0:
        if position_depart == position_arrivee:
            return True
        else:
            return False

def nbreMiniCoups(pos_dep, pos_arr):
    """
    Donne le nbre mini de déplacements qu'il faut pour aller d'une case à une autre (on supposera que c'est toujours possible)
    """
    i = 0
    while accessibleEnNCoups(pos_dep, pos_arr, i) == False:
        i += 1
    return i

#def listeDeplacements(pos_dep, pos_arr, nbreCoups, tableauArrivee,k): #Ne marchait pas
 #   if nbreCoups > 0:
  #      k[nbreCoups]=0        
   #     for emt in positionsPossibles(pos_dep):
#            if accessibleEnNCoups(emt, pos_arr, nbreCoups - 1):
#                tableauArrivee[k[nbreCoups + 1]].append(tableauArrivee[k[nbreCoups + 1]]+emt)
#                listeDeplacements(emt,pos_arr, nbreCoups -1, tableauArrivee,k)
#            k[nbreCoups] += 1
#    if nbreCoups == 0:
#        return tableauArrivee

def listeDeplacements(pos_dep, pos_arr, nbreCoups, tableauArrivee, tmp):
    """
    Renvoie toutes les déplacements possibles (dans tableauArrivée qui doit etre vide au début)
    pour aller d'une case à une autre en nbreCoups cous (notez que tmp doit lui aussi être vide au début)
    """
    if nbreCoups > 0:
        for emt in positionsPossibles(pos_dep)[:]:
            if accessibleEnNCoups(emt, pos_arr, nbreCoups-1):
                tmp.append(emt)
                #print("tmpAvant = %s"%(tmp))
                listeDeplacements(emt, pos_arr, nbreCoups-1,tableauArrivee, tmp)
                #print("tmpApres =  %s"%(tmp))
                tmp = tmp[:len(tmp)-(nbreCoups)]
    if nbreCoups == 0:
        tableauArrivee.append(tmp)
        tmp = []
        #print("Atteint, tmp = %s"%(tmp))

def deplacementLePlusCourt(pos_dep, pos_arr):
    """
    La fonction FINALE !
    """
    minCoup = nbreMiniCoups(pos_dep, pos_arr)
    res = []
    tmp = []
    listeDeplacements(pos_dep, pos_arr, minCoup, res, tmp)
    return res

def test():
    """
    Pour tester le déplacement offrant le plus de possibilités
    """
    tab = []
    caseDepArr = [1,2]
    for e in range(1,9):
        for i in range(1,9):
            tab.append([e,i])
    maxi = 0
    for e in tab:
        for i in tab:
            if len(deplacementLePlusCourt(e,i)) > maxi:
                maxi = len(deplacementLePlusCourt(e,i))
                caseDepArr[0]=e
                caseDepArr[1]=i
        print("%s done."%(e))
    print("Le nombre maximum de déplacements est de %s, il est effectué pour aller de %s à %s"%(maxi,caseDepArr[0],caseDepArr[1]))
