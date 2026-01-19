from sympy import *


#expand factor simplify solveset (une equ solutions en form ensemble) solve (solutions eq ou system en form list) 
# A.subs(x,5) kt3wd x b 5 A.subs([(x,2),(y,3)])

#derivation diff(exp,x)
#integral integrate(exp,x)

x = symbols("x")

expre = (x+2)**2

print(expand(expre))

expr = x**2 + 5*x + 6
new_ = factor(expr)
print(new_)


print(solveset(expre,x, domain=S.Reals))

print(solve(expre,x))

print(expre.subs(x,1))


#============================================================"""probabilite random module"
import random
x = random.random()        # [0,1[

x = random.uniform(5, 10)  #[a, b]
print(x)

x = random.randint(1, 6)   #[a, b]
print(x)

x = random.randrange(1, 6, 2)   #[a, b] + steps
print(x)

L=[1,2,3,4,5,6,7,8,9]
print("=======================")
print(random.choice(L)) #khtar 3adad random f list
random.shuffle(L) 
print(L)
print(random.sample(L,3)) #sample takes 3 random values in the list and put them in the list
print(L)


#============================================================"""matplotlib module"
import matplotlib.pyplot as plt
import numpy as np

plt.axis([0,10,0,10])
plt.grid()
x = np.linspace(1,10,50)
y = x**2
plt.plot(x,y)
plt.show()