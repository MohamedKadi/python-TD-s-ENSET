from collections import Counter

def occurrences(lettre, mot):
    occu = 0
    for key in mot:
        if key == lettre:
            occu += 1
    return occu

print(occurrences("b","bonjourb"))

def occurrences2(sequence):
    seq = {}
    for key in sequence:
        if key in seq:
            seq[key] += 1
        else:
            seq[key] = 1
    return seq

print(occurrences2("bonjour"))
