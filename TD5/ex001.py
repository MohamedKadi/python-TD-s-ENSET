
def fact(n):
    if( n <= 1):
        return 1
    return n * fact(n-1)

def Empiler_Fat(n, P1):
    for i in range(n+1):
        P1.append(fact(i))
    return P1


def Empiler_Puiss(n,x,P2):
    for i in range(n+1):
        P2.append(x**i)
    return P2

def Empiler_Frac(P1 , P2):
    P3 = []
    for i in range(len(P1)):
        P3.append(P2[i]/P1[i])
    return P3

def Somme(n ,x):
    sum = 0
    p1=[]
    p1=Empiler_Fat(n, p1)
    p2=[]
    p2=Empiler_Puiss(n,x,p2)
    P3 = Empiler_Frac(p1 , p2)
    for elemnt in P3:
        sum += elemnt
    return sum

Somme_result=Somme(2 , 2)
print("La somme de la série est :", Somme_result)