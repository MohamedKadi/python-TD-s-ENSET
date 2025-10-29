import csv

# 1️ Import CSV
def importer_csv(fichier):
    table = []
    with open(fichier, newline='', encoding='utf-8-sig') as f:
        lecteur = csv.DictReader(f, delimiter=',')
        new_fieldnames = []
        for fn in lecteur.fieldnames:
            if fn is None:
                new_fieldnames.append(fn)
            else:
                new_fieldnames.append(fn.strip())
        lecteur.fieldnames = new_fieldnames

        for ligne in lecteur:
            clean = {}
            for k, v in ligne.items():
                if k is None:
                    continue
                key = k.strip()
                val = v.strip() if isinstance(v, str) else v
                clean[key] = val
            if 'score_1' in clean and clean['score_1'] != '':
                clean['score_1'] = int(clean['score_1'])
            else:
                clean['score_1'] = 0
            if 'score_2' in clean and clean['score_2'] != '':
                clean['score_2'] = int(clean['score_2'])
            else:
                clean['score_2'] = 0

            table.append(clean)
    return table


# 2️ Selections 
def moins_300_score1(table):
    result = []
    for i in range(len(table)):
        if table[i]['score_1'] < 300:
            result.append(table[i])
    return result

def filles(table):
    result = []
    for i in range(len(table)):
        if table[i]['genre'].upper() == 'F':
            result.append(table[i])
    return result

def email_example_com(table):
    result = []
    for i in range(len(table)):
        email = table[i]['email']
        if len(email) >= 12 and email[-12:] == '@example.com':
            result.append(table[i])
    return result

# 3️ Projections
def meilleurs_scores(table, score_col):
    scores = []
    for i in range(len(table)):
        scores.append({'nom': table[i]['nom'], 'score': table[i][score_col]})
    
    n = len(scores)
    for i in range(n):
        for j in range(0, n-i-1):
            if scores[j]['score'] > scores[j+1]['score']:
                temp = scores[j]
                scores[j] = scores[j+1]
                scores[j+1] = temp
    return scores

def score_moyen(table, score_col):
    total = 0
    for i in range(len(table)):
        total += table[i][score_col]
    if len(table) == 0:
        return 0
    return total / len(table)

def toutes_adresses(table):
    result = []
    for i in range(len(table)):
        result.append(table[i]['email'])
    return result

def pires_joueurs(table, score_col, n=10):
    copie = []
    for i in range(len(table)):
        copie.append(table[i])
    
    for i in range(len(copie)):
        for j in range(0, len(copie)-i-1):
            if copie[j][score_col] > copie[j+1][score_col]:
                temp = copie[j]
                copie[j] = copie[j+1]
                copie[j+1] = temp
    
    result = []
    for i in range(min(n, len(copie))):
        result.append(copie[i]['email'])
    return result

def supprimer_doublons(emails):
    result = []
    for i in range(len(emails)):
        duplicate = False
        for j in range(len(result)):
            if emails[i] == result[j]:
                duplicate = True
                break
        if not duplicate:
            result.append(emails[i])
    return result

utilisateurs = importer_csv("utilisateurs.csv")
    
print("Joueurs avec score_1 < 300 :")
for u in moins_300_score1(utilisateurs):
    print(u['nom'], u['score_1'])
    
print("\nJoueuses :")
for u in filles(utilisateurs):
    print(u['nom'], u['genre'])
    
print("\nEmails @example.com :")
for u in email_example_com(utilisateurs):
    print(u['email'])
    
print("\nMeilleurs scores score_1 :")
scores1 = meilleurs_scores(utilisateurs, 'score_1')
for s in scores1:
    print(s['nom'], s['score'])
    
print("\nScore moyen score_1 :", score_moyen(utilisateurs, 'score_1'))
print("Score moyen score_2 :", score_moyen(utilisateurs, 'score_2'))
    
print("\n10 pires joueurs score_1 :")
for e in pires_joueurs(utilisateurs, 'score_1'):
    print(e)
    
print("\nToutes les adresses sans doublons :")
for e in supprimer_doublons(toutes_adresses(utilisateurs)):
    print(e)