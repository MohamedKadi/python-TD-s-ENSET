def Occur(Text,lettre) :
    sum = 0
    for x in Text :
        if x == lettre :
            sum += 1
    return sum

def RecursiviteOccur(Text, lettre) : 
    if Text == None :
        return 0
    if Text[0] == lettre:
        return 1 + RecursiviteOccur(Text[1:],lettre)
    else:
         return RecursiviteOccur(Text[1:],lettre)


text = "L"
lettre = ""
sum = Occur(text,lettre)
print(sum)