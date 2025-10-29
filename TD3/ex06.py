def encrypteLettre(letter, cle) :
    if ord(letter) >= 97 and ord(letter) <= 122 :
        num = (ord(letter) - ord('a') + cle) % 26
        encode = chr(ord('a') + num)
    elif ord(letter) >= 65 and ord(letter) <= 90 :
        num = (ord(letter) - ord('A') + cle) % 26
        encode = chr(ord('A') + num)
    else :
        num = ord(letter)
        encode = chr(num)
    
    return encode

def encrypteMot(texteEnClair,cle) :
    result = ""
    for letter in texteEnClair :
        result += encrypteLettre(letter, cle)
    return result

print(encrypteMot("Toto va aux girafes avec des petites jambes.", 12))

def decrypteLettre(letter, cle) :
    if ord(letter) >= 97 and ord(letter) <= 122 :
        num = (ord(letter) - ord('a') - cle) % 26
        encode = chr(ord('a') + num)
    elif ord(letter) >= 65 and ord(letter) <= 90 :
        num = (ord(letter) - ord('A') - cle) % 26
        encode = chr(ord('A') + num)
    else :
        num = ord(letter)
        encode = chr(num)
    
    return encode

def decrypte(texteCache,cle) :
    result = ""
    for letter in texteCache :
        result += decrypteLettre(letter, cle)
    return result

print(decrypte("Fafa hm mgj sudmrqe mhqo pqe bqfufqe vmynqe.", 12))
