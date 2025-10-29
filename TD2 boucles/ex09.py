import random

x = int(random.randint(1, 1000))
num = int(input("enter un number entre 1-1000:"))
essai = 0
while(essai < 8 and x != num):
    if(x < num):
        print("le nombre est grand try again")
    if(x > num):
        print("le nombre est petit try again")
    essai +=1
    num = int(input("nouvel essai :"))

if(essai == 8):
    print("the number was " + x + "try play again!")
else : 
    print("BRAVO u tried " + essai + "times")
#print(type(x))  