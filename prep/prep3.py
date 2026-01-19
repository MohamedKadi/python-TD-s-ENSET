

def estVide(P):
    if len(P) == 0: 
        return True
    return False

def PileVide():
    return []

def taillePile(P):
    return len(P)

def empiler(P,v):
    P.append(v)
    return P

def depiler(P):
    if(len(P) != 0):
        P.pop()
    return P
##########same for file
def defille(P):
    if(len(P) != 0):
        P.pop(0)
    return P
