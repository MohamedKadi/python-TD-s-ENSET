from sympy import *
#Question 1
#q1
x ,y= symbols("x,y") 
derivation = diff(x**3 - 6*x**2 + 5*x + 12, x)
print(derivation)
#q2
solutions = solve(derivation,x)
print(solutions)

#Question 2

print(simplify(sin(x)*cos(y) + cos(x)*sin(y)))
print(expand((2*x + 3)**4))

#Question 3
# Fonction à intégrer
f = sin(x)*cos(x)

# Calcul de l'intégrale indéfinie
integrale = integrate(f, (x, 0, pi/2))
print(integrale)

#Question 4
print(solveset(4*x + 7-3*(x-1),x))


#Question 5
expr = (exp(2*x) - 1) / x
limit_value = limit(expr, x, 0)
print(limit_value)


#Question 6
solutions = solve((2*x-3*y-5,-x+2*y+3),(x,y))
print(solutions[x])
print(solutions[y])

#Question 7
from sympy import symbols, Function, dsolve, Eq, Derivative

x = symbols('x')
y = Function('y')

diff_eq = Eq(Derivative(y(x), x) - y(x), x**2)

solution = dsolve(diff_eq, y(x))
print(solution)
