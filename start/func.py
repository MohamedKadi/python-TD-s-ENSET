def add(x,y) :
    return x+y

def addv2(*args) :
    s = 0
    for x in args:
        s += x
    return s

def func(**args) :
    for c,v in args.items() :
        print(c,v)

print(func(nom="reda",age=22,taille=1.74))