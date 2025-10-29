import random

alpha = { "a" :1 , "b" :3 , "c" :3 , "d" :2 , "e" :1 , "f" :4 , "g" :2 , "h" :4 , "i" :1 , "j" :8 ,
             "k" :10 , "l" :1 , "m" :2 , "n" :1 , "o" :1 , "p" :3 , "q" :8 , "r" :1 , "s" :1 , "t" :1 ,
            "u" :1 , "v" :4 , "w" :10 , "x" :10 , "y" :10 , "z" :10}
keys_list = list(alpha.keys())
print(keys_list)
def pioche():
    randlettre = {}
    for i in range(7):
        random_integer = random.randint(0,25)
        random_integer2 = random.randint(0, 99)
        randlettre[keys_list[random_integer]] = random_integer2
    return randlettre

print(pioche())

