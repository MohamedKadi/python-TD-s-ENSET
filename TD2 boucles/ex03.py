

x = input("un entier")
sum = 0
for k in range(0,x+1):
    sum = sum + k * x**k

print("the answer is: " + sum)