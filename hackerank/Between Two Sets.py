

#sum = pgcd(4,6)
#pcm = ppcm(4,6)

a = [2,4]   #4,8,12,16... ppcm 4
b = [16,32,96] #2,4,8,16 pgcd 16
#4 8 16

a = [2,3]   
b = [2,4] 

def pgcd(a,b):
    mod = a%b
    while(mod != 0):
        a = b
        b = mod
        mod = a%b
    return b


def ppcm(a,b):
    mx = max(a,b)
    while(((mx%a)!= 0) or ((mx%b)!= 0)):
        mx +=1
    return mx
        
    
def getTotalX(a, b):
    lcm = a[0]
    for i in range(1,len(a)):
        lcm = ppcm(lcm,a[i])

    gcd = b[0]
    for i in range(1,len(b)):
        gcd = pgcd(gcd,b[i])
    result = 0
    temp = 0
    while(temp <= gcd):
        temp += lcm
        if gcd%temp == 0:
            print("resu " + str(temp))
            result += 1
    return result

print(getTotalX(a,b))
