

def possible(mot,lettres):

    for key in mot:
        if(key not in lettres):
            return False
        if lettres[key] > 0:
            lettres[key] -= 1
        else:
            return False
    return True

print(possible("maman",{'m':2,'n':1,'a':2,'t':1}))