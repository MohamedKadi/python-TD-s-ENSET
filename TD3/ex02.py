#['ad', 'ae', 'bd', 'be', 'cd', 'ce']

str1 = "abc"
str2 = "de"

newstr = []
for x in str1 :
    for y in str2 :
        newstr.append(x + y)
    

print(newstr)