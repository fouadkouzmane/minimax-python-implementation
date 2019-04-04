#the node's classes 
from random import randrange

#ordinary node  
class node : 
    def __init__(self):
        self.childs = []
        self.value = 0
    def __str__(self): 
        return "{}".format(self.value)
#leaf class 
class nodef : 
    def __init__(self):
        self.value = 0
    def __str__(self): 
        return "{}".format(self.value)

#MINIMAX-methods 

def makeTree(noder,nodex,nodey): #connecting the node with the childs

    noder.childs.append(nodex)
    noder.childs.append(nodey)
    
 
def minimax(node): #apply the minimax algorithm to a given tree (ref by the root node)
    v = MAX_VALUE(node)
    return v 

def MAX_VALUE(nodez): #returns the max value of a node 
    if isinstance(nodez,nodef) : return nodez.value #si on a une feuille retourne sa valeur 
    else :
        v = -10000 
        for object in nodez.childs : 
            v = max(v,MIN_VALUE(object))
            nodez.value = v
        return v 
        
def MIN_VALUE(nodez): #returns the min value of a node
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
makeTree(noder,node11,node12) #linking 
node21 = nodef()
node21.value=randrange(30) #random leaf value 
node22 = nodef()
node22.value=randrange(30) 
makeTree(node11,node21,node22) 
node23 = nodef()
node23.value=randrange(30)  
node24 = nodef()
node24.value=randrange(30)
makeTree(node12,node23,node24) 

#Printing the tree with the value of each node  

print("resultat : {}".format(minimax(noder)))
print('\n')
print("max :   {}     {}".format(node11,node12))
print('\n')
print("min : {}  {}  {}  {} ".format(node21,node22,node23,node24)) 