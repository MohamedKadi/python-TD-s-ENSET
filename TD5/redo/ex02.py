
#pile is stack LIFO vs file queue FIFO

def PileVide():
    P = []
    return P

def EstVide(P):
    if P == None:
            return True
    return False

def Empiler(P, n):
     if P is None:
          return
     P.append(n)
     return P

def Depiler(P):
     if P is None:
          return
     P.pop()
     return P

def SommetPile(P):
     return P[-1]