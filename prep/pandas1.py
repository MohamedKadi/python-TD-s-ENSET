

import pandas as pd
from functools import reduce
import numpy as np

data = {
    "id": [1, 2, 3, 4, 5, 6, 7, 8],
    "name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Helen"],
    "age": [25, 30, np.nan, 45, 22, 36, np.nan, 29],
    "country": ["USA", "Canada", "UK", "USA", "France", "Germany", "USA", "Canada"],
    "salary": [50000, 60000, 55000, np.nan, 48000, 72000, 51000, 59000],
    "department": ["IT", "HR", "IT", "Finance", "HR", "IT", "Finance", "HR"],
    "join_date": [
        "2019-01-15", "2020-06-01", "2018-09-23", "2017-03-10",
        "2021-11-05", "2016-07-18", "2019-12-01", "2022-02-14"
    ]
}



df = pd.DataFrame(data)

#Q1
print(df.head())
print("===============")
print(df.tail(3))
#Q2

print(df.dtypes)
print("====================")
df["join_date"] = df["join_date"].astype("datetime64[s]")
print("====================")
print(df.isnull().sum())
print(df.isnull().any())

df["age"].fillna(df["age"].mean(), inplace=True)
df["salary"].fillna(df["salary"].mean(),inplace=True)




print(df.query("country == 'USA' and salary >= 50000"))

print("=============================")
print(df.loc[df["country"] == "Canada"])
print(df.values)
print("===========================")
print(df.describe())

# data = {
#     'nom': ['Ali', 'Sara', 'Omar', 'Fatima', 'Hassan'],
#     'age': [22, 25, 23, 24, 22],
#     'ville': ['Tanger', 'Rabat', 'Tanger', 'Casablanca', 'Rabat'],
#     'note': [15, 18, 12, 16, 14]
# }

# df = pd.DataFrame(data)

# # Group by city and calculate average grade
# df["moy"] = df["note"].apply(lambda x : "Excellente" if x >=16 else ("T.Bien" if x >=14 else "bien"))
# print(df)

#ex
# Écrivez un programme Python complet qui :
# 1. Crée un dictionnaire contenant les notes de 5 étudiants (nom → liste de notes)
# 2. Calcule la moyenne de chaque étudiant
# 3. Affiche les étudiants ayant une moyenne supérieure à 12
# 4. Trouve et affiche le nom de l’étudiant ayant la meilleure moyenne
# Exemple de structure :
# 1 etudiants = {
# ’Ali’: [15, 16, 14],
# ’Sara’: [18, 17, 19],}


etudiants = { 'Ali': [15, 16, 14], 'Sara': [18, 17, 19], 'Omar': [12, 13, 11], 'Fatima': [14, 15, 13], 'Hassan': [10, 12, 9] }
moyennes = {}
for etu, notes in etudiants.items():
    moyennes[etu] = sum(notes)/len(notes)

for etu, moy in moyennes.items():
    if moy >= 12:
        print(etu)

best_student = max(moyennes)
print(best_student) 
print("Meilleure moyenne :", best_student, moyennes[best_student])

# df = pd.DataFrame(etudient).T
# df["moy"] = df.mean(axis=1)
# print(df)
# print(df.query("moy >= 12"))
# df_sorted_desc = df.sort_values(by="moy", ascending=False)

# print(df_sorted_desc.index[0])

# etudiant = {
#     'nom': 'Alami',
#     'prenom': 'Sara',
#     'age': 21,
#     'notes': [15, 17, 14, 16]
# }
# moy = reduce(lambda acc,x: acc+x ,etudiant["notes"])
# print(moy/len(etudiant["notes"]))


import pandas as pd

data = {
    'nom': ['Youssef', 'Imane', 'Karim', 'Nadia', 'Samir'],
    'departement': ['IT', 'Finance', 'IT', 'RH', 'Finance'],
    'age': [28, 34, 26, 29, 31],
    'salaire': [12000, 15000, 11000, 13000, 14000]
}

# df = pd.DataFrame(data)

# df.head(2)
# print(df.query("departement == 'IT'"))
# print(df.query("salaire >= 13000"))

# df["salaire"].mean()

# df["niveau"] = df["salaire"].apply(lambda x: "Senior" if x >= 14000 else( "Intermédiaire" if x >= 12000 else "Junior"))
# print("====")
# print(df.groupby("departement")["salaire"].count())

# print(df)