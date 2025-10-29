def factorielle(n):
    if n <=1:
        return 1
    else:
        res=1
        for i in range(2,n+1):  
            res=res*i
        return res

def Empiler_Fat(n, P1):
    for i in range(n+1):
        P1.append(factorielle(i))
    return P1

def Empiler_Puiss(n,x,P2):
    for i in range(n+1):
        P2.append(x**i)
    return P2

def Empiler_Frac(P1 , P2):
    P3=[]
    for i in range(len(P1)):
        P3.append(P2[i]/P1[i])
    return P3

def Somme(n ,x):
    P1=[]
    P2=[]
    P1=Empiler_Fat(n , P1)
    P2=Empiler_Puiss(n , x , P2)
    P3=Empiler_Frac(P1 , P2)
    S=0
    print("Les éléments de la série sont :", P1)
    print("Les éléments de la série sont :", P2)
    print("Les éléments de la série sont :", P3)
    for i in range(len(P3)):
        S=S+P3[i]
    return S

Somme_result=Somme(2 , 2)
print("La somme de la série est :", Somme_result)