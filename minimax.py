#the node's classes 
from random import randrange

#la classe d'un noeud ordinaire 
class node : 
    def __init__(self):
        self.childs = []
        self.value = 0
    def __str__(self): 
        return "{}".format(self.value)
#la classe d'un noeud feuille 
class nodef : 
    def __init__(self):
        self.value = 0
    def __str__(self): 
        return "{}".format(self.value)

#MINIMAX-methods 

#methode qui qui fait le lien entre un noeud et ses fils 
def makeTree(noder,nodex,nodey):
    noder.childs.append(nodex)
    noder.childs.append(nodey)
    
#methode de l'algorithme 
def minimax(node):
    v = MAX_VALUE(node)
    return v 

def MAX_VALUE(nodez):
    if isinstance(nodez,nodef) : return nodez.value #si on a une feuille retourne sa valeur 
    else :
        v = -10000 
        for object in nodez.childs : 
            v = max(v,MIN_VALUE(object))
            nodez.value = v
        return v 
        
def MIN_VALUE(nodez):
    if isinstance(nodez,nodef) : return nodez.value #si on a une feuille retourne sa valeur
    else :
        v = 10000
        for object in nodez.childs : 
            v = min(v,MAX_VALUE(object))
            nodez.value = v
        return v 

#test-section 

noder = node()
node11 = node()
node12 = node()
makeTree(noder,node11,node12) #faire la liasion
node21 = nodef()
node21.value=randrange(30) #aulieu des fonctions heuristiques 
node22 = nodef()
node22.value=randrange(30) #aulieu des fonctions heuristiques 
makeTree(node11,node21,node22) #faire la liasion
node23 = nodef()
node23.value=randrange(30) #aulieu des fonctions heuristiques 
node24 = nodef()
node24.value=randrange(30)#aulieu des fonctions heuristiques 
makeTree(node12,node23,node24) #faire la liasion

#affichage de l'arbre avec le poids de chaque noued après l'application de minimax 

print("resultat : {}".format(minimax(noder)))
print('\n')
print("max :   {}     {}".format(node11,node12))
print('\n')
print("min : {}  {}  {}  {} ".format(node21,node22,node23,node24)) 