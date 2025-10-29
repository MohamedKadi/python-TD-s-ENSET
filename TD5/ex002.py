

#q3
def PileVide():
    return []

def EstVide(P):
    if len(P) == 0:
        return True
    return False

def Empiler(P,n):
    P.append(n)
    return P

def Depiler(P):
    if EstVide(P):
        print("erreur: pile est vide")
        return 
    return P.pop()

def SommetPile(P):
    return P[-1]

#q4
def EstChiffre(c):
    if c >= '0' or c <= '9' :
        return 1
    return 0

#q5
def Convertir(c):
    return int(c)

#q6
def Evaluer(expression):
    op = ['+','-','*','/']
    nums = expression.split()
    P=[]
    for element in nums:
        if(element not in op):
            Empiler(P,element)
        else:
            if len(P) < 2:
                print(P)
                print("erreur")
                return
            else:
                p2 = Convertir(Depiler(P))
                p1 = Convertir(Depiler(P))
                if element == "+":
                    P = Empiler(P,p1 + p2)  
                if element == "-":
                    P = Empiler(P,p1 - p2)  
                if element == "*":
                    P = Empiler(P,p1 * p2)  
                if element == "/":
                    P = Empiler(P,p1 / p2)  
                
    return SommetPile(P)

print(Evaluer("3 28 + 7 /"))

#q7
def EvaluerTexte(Fsrc, Fdest):
    ff = open(Fsrc, "r", encoding="utf-8")
    contenu = ff.read()
    ff.close()
    resultat = Evaluer(contenu)
    f = open(Fdest, "w", encoding="utf-8")
    f.write(str(resultat))
    f.close()

EvaluerTexte("./src.txt","./dest.txt")

