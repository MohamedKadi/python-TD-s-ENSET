#Importer
#q1
import os

def copyfile():
    source = os.path.expanduser(r"C:\Users\moham\Downloads\utilisateurs.csv")
    destination = os.path.join(os.getcwd(), "utilisateurs.csv")

    os.rename(source, destination)
    print("File moved successfully!")
    return

#q2
import csv

def readingcsv():
    f = open("utilisateurs.csv")
    lecteur = csv.DictReader(f,delimiter=";")
    f.close
    arr= []
    for ligne in lecteur:
        arr.append(ligne)
    return arr
#q3
arrayofdicts = readingcsv()
######################################################################
#print(lecteur)
#Sélectionner
#1
def joueurs300score(arrayofdicts):
    joueurs = []
    for ligne in arrayofdicts:    
        raw = (list(ligne.values())[0])
        nom, genre, score1, score2, email = raw.split(",")
        if int(score1) >= 300:
            joueurs.append({nom, genre, score1, score2, email})
    return joueurs
#2
def joueursfills(arrayofdicts):
    joueurs = []
    for ligne in arrayofdicts:
        raw = list((ligne.values()))[0]
        nom, genre, score1, score2, email = raw.split(",")
        if genre == "F":
            joueurs.append({nom, genre, score1, score2, email})
    return joueurs
#3
def cherche_domaine(arrayofdicts, domaine):
    joueurs = []
    for ligne in arrayofdicts:
        raw = list((ligne.values()))[0]
        nom, genre, score1, score2, email = raw.split(",")
        if domaine in email:
            joueurs.append({nom, genre, score1, score2, email})
    return joueurs

#projection
#q1
parsed = []
for d in arrayofdicts:
    raw = list(d.values())[0]
    nom, genre, score1, score2, email = raw.split(",")
    parsed.append({
        "nom": nom,
        "genre": genre,
        "score_1": int(score1),
        "score_2": int(score2),
        "email": email
    })

"""
#a
sorted_by_score1 = sorted(parsed, key=lambda x: x["score_1"])
print(sorted_by_score1)

#b
sorted_by_score2 = sorted(parsed, key=lambda x: x["score_2"])
print(sorted_by_score2)
"""
#c
def moy1scores(arrayofplayers):
    sum1 = 0
    for ligne in arrayofplayers:
        sum1 += ligne["score_1"]
    return sum1/len(arrayofplayers)
def mo2scores(arrayofplayers):
    sum2 = 0
    for ligne in arrayofplayers:
        sum2 += ligne["score_2"]
    return sum2/len(arrayofplayers)

#q2
#a
def emails_players(arrayofplayers):
    emails = []
    for ligne in arrayofplayers:
        emails.append({"email": ligne["email"] })
    return emails
#b
def emails_mavJoueurs(arrayofplayers):
    sorted_by_score1 = sorted(arrayofplayers, key=lambda x: x["score_1"])
    i = 0
    arr= []
    while(i < 10):
        arr.append({"email":sorted_by_score1[i]["email"]})
        i+=1
    print(arr)

def emails_mavJoueurs2(arrayofplayers):
    sorted_by_score2 = sorted(arrayofplayers, key=lambda x: x["score_2"])
    i = 0
    arr= []
    while(i < 10):
        arr.append({"email":sorted_by_score2[i]["email"]})
        i+=1
    print(arr)

#emails_mavJoueurs(parsed)
#c
def effacer_doublent(arrayofplayers):
    array = []
    for ligne in arrayofplayers:
        if ligne["email"] not in array:
            array.append(ligne["email"])
    print(array)
    return array
effacer_doublent(parsed)