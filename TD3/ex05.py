def ispalindrom(text) :
    rev = text[::-1]
    if text == rev :
        return True
    return False

str = input("enter a string: ")
if(ispalindrom(str)) :
    print("is palindrom")
else :
    print("non palindrom")