def grands(L,x) :
    result = filter(lambda y : y > x , L)
    return list(result)

res = grands([1,2,3,4,5],2)
print(res)

def petits(L,x) :
    result = filter(lambda y : y < x, L)
    return list(result)

res = petits([1,2,3,4,5],4)
print(res)

def median(L) :
    nbrsup = 0
    nbrinf = 0
    for x in L :
        nbrsup = len(grands(L,x))
        nbrinf = len(petits(L,x))
        if(nbrsup <= len(L)/2 and nbrinf <= len(L)/2) :
            return x    
    
L = [ 25 , 12 , 6 , 17, 3 , 10 , 20 , 12 , 15 , 38 ]
resu = median(L)
print(resu)
