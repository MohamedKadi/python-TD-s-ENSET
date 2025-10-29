

n = input("entrer un entier naturel: ")
n = eval(n)
u = 0
for k in range(0,n+1):
    u = u + k**3
    print(u)

print("le resultat est: ", u)