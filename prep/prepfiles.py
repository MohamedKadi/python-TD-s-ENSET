

#readlines array of content \n
#readline only one line
#read show the text
# with open("file.txt","r") as f:
#     text = f.readline()
#     while(text != ""):
#         print(text)
#         text = f.readline()

#print(text)

arr = ["hello" , "mohamed", "cv", "bien"]
with open("file2.txt","w") as f:
    for animal in arr:
        f.write(str(animal) + " ")

#============================================ CSV (structuré)

import csv

with open("data.csv", newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

#dicts
f = open("data.csv","r")

lecteur = csv.DictReader(f,delimiter=";")
for ligne in lecteur:
    print(ligne)

#=========================================
f = open("demofile.txt","rb")
