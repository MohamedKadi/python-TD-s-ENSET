ozone = float(input("entrez la concentration"))

if ozone >= 220:
    niveau = 3
elif ozone >= 180:
    niveau = 2
elif ozone >= 140:
    niveau = 1
else:
    niveau = 0

print(f"niveau de pollution {niveau}")
