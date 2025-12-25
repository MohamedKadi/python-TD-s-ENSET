import sqlite3



#1
def AccederBD(maBase):
    conn = sqlite3.connect(maBase)
    cursor = conn.cursor() 
    return conn, cursor

# 2
def CreerTable1(c):
    c.execute('''CREATE TABLE IF NOT EXISTS FILM (
                    idFilm INTEGER PRIMARY KEY,
                    titre TEXT NOT NULL,
                    realisateur TEXT,
                    annee INTEGER
                )''')

# 3
def CreerTable2(c):
    c.execute('''CREATE TABLE IF NOT EXISTS ACTEUR (
                    idActeur INTEGER PRIMARY KEY,
                    nom TEXT NOT NULL,
                    prenom TEXT NOT NULL
                )''')

# 4
def CreerTable3(c):
    c.execute('''CREATE TABLE IF NOT EXISTS FILMOGRAPHIE (
                    idActeur INTEGER,
                    idFilm INTEGER,
                    role TEXT,
                    salaire REAL,
                    PRIMARY KEY (idActeur, idFilm),
                    FOREIGN KEY (idActeur) REFERENCES ACTEUR(idActeur),
                    FOREIGN KEY (idFilm) REFERENCES FILM(idFilm)
                )''')

# 5
def rech_personne(c, nom, prenom):
    c.execute("SELECT * FROM ACTEUR WHERE nom=? AND prenom=?", (nom, prenom))
    resultat = c.fetchone()
    return resultat

# 6
def insert_acteur(c, id, nom, prenom):
    if not rech_personne(c, nom, prenom):
        c.execute("INSERT INTO ACTEUR (idActeur, nom, prenom) VALUES (?, ?, ?)", 
                  (id, nom, prenom))

# 7
def affiche_table(c, nomTable):
    c.execute(f"SELECT * FROM {nomTable}")
    lignes = c.fetchall()
    if lignes:
        for ligne in lignes:
            print(ligne)
    else:
        print(f"La table {nomTable} est vide.")

# 8
def affiche_film(c, id):
    c.execute("SELECT * FROM FILM WHERE idFilm=?", (id,))
    film = c.fetchone()
    if film:
        print(f"ID: {film[0]}, Titre: {film[1]}, Réalisateur: {film[2]}, Année: {film[3]}")
    else:
        print(f"Aucun film trouvé avec l'identifiant {id}")

# 9
def supr_film(c, id):
    c.execute("DELETE FROM FILMOGRAPHIE WHERE idFilm=?", (id,))
    c.execute("DELETE FROM FILM WHERE idFilm=?", (id,))
    print(f"Film avec l'identifiant {id} supprimé.")

# 10
def modif_FILMOGRAPHIE(c, id1, id2, val):
    c.execute("UPDATE FILMOGRAPHIE SET salaire=? WHERE idActeur=? AND idFilm=?", 
              (val, id1, id2))
    print(f"Salaire mis à jour pour l'acteur {id1} dans le film {id2}")

# 11
def Nbr_acteurs(c, nomFilm):
    c.execute('''SELECT COUNT(DISTINCT f.idActeur) 
                 FROM FILMOGRAPHIE f 
                 JOIN FILM fi ON f.idFilm = fi.idFilm 
                 WHERE fi.titre=?''', (nomFilm,))
    resultat = c.fetchone()
    return resultat[0]

# 12
def ActeursSansFilms(c):
    c.execute('''SELECT nom, prenom 
                 FROM ACTEUR 
                 WHERE idActeur NOT IN (SELECT DISTINCT idActeur FROM FILMOGRAPHIE)''')
    acteurs = c.fetchall()
    if acteurs:
        print("Acteurs sans films :")
        for acteur in acteurs:
            print(f"{acteur[1]} {acteur[0]}")
    else:
        print("Tous les acteurs ont joué dans au moins un film.")

# 13
def ActeursDebutants(c):
    c.execute('''SELECT a.nom, a.prenom, AVG(f.salaire) as moyenne_salaire
                 FROM ACTEUR a
                 JOIN FILMOGRAPHIE f ON a.idActeur = f.idActeur
                 GROUP BY a.idActeur, a.nom, a.prenom''')
    acteurs = c.fetchall()
    if acteurs:
        print("Acteurs avec moyenne des salaires :")
        for acteur in acteurs:
            print(f"{acteur[1]} {acteur[0]} - Moyenne: {acteur[2]:.2f}$")
    else:
        print("Aucun acteur trouvé.")

# 14
def ActeursMemeSalaire(c):
    c.execute('''SELECT DISTINCT a1.nom, a1.prenom, a2.nom, a2.prenom, f1.salaire
                 FROM FILMOGRAPHIE f1
                 JOIN FILMOGRAPHIE f2 ON f1.salaire = f2.salaire AND f1.idActeur < f2.idActeur
                 JOIN ACTEUR a1 ON f1.idActeur = a1.idActeur
                 JOIN ACTEUR a2 ON f2.idActeur = a2.idActeur
                 ORDER BY f1.salaire''')
    paires = c.fetchall()
    if paires:
        print("Paires d'acteurs avec le même salaire :")
        for paire in paires:
            print(f"{paire[1]} {paire[0]} et {paire[3]} {paire[2]} - Salaire: {paire[4]}$")
    else:
        print("Aucune paire trouvée.")

# 15
def SalaireDollarToDirham(c):
    taux_change = 9
    c.execute('''SELECT a.nom, a.prenom, f.salaire, fi.titre
                 FROM FILMOGRAPHIE f
                 JOIN ACTEUR a ON f.idActeur = a.idActeur
                 JOIN FILM fi ON f.idFilm = fi.idFilm''')
    salaires = c.fetchall()
    if salaires:
        print("Salaires en dirhams :")
        for sal in salaires:
            salaire_dh = sal[2] * taux_change
            print(f"{sal[1]} {sal[0]} dans '{sal[3]}': {salaire_dh:.2f} DH")
    else:
        print("Aucun salaire trouvé.")

# 16
def ValiderTrans(conn):
    conn.commit()
    print("Transactions validées.")

# 17
def TableToFile(Fich, c, nomTable):
    c.execute(f"SELECT * FROM {nomTable}")
    lignes = c.fetchall()
    with open(Fich, 'w', encoding='utf-8') as f:
        for ligne in lignes:
            f.write(str(ligne) + '\n')
    print(f"Table {nomTable} exportée vers {Fich}")

# 18
def FileToTable(Fich, c, nomTable):
    with open(Fich, 'r', encoding='utf-8') as f:
        lignes = f.readlines()
        for ligne in lignes:
            ligne = ligne.strip()
            if ligne:
                donnees = eval(ligne)
                placeholders = ','.join(['?'] * len(donnees))
                c.execute(f"INSERT INTO {nomTable} VALUES ({placeholders})", donnees)
    print(f"Données importées de {Fich} vers {nomTable}")

# 19
def FermerConnex(conn):
    conn.close()
    print("Connexion fermée.")


if __name__ == "__main__":
    maBase = 'cinema.sqlite'
    
    conn, c = AccederBD(maBase)
    
    CreerTable1(c)
    CreerTable2(c)
    CreerTable3(c)
    
    c.execute("INSERT OR IGNORE INTO FILM VALUES (1, 'Inception', 'Christopher Nolan', 2010)")
    c.execute("INSERT OR IGNORE INTO FILM VALUES (2, 'Titanic', 'James Cameron', 1997)")
    
    insert_acteur(c, 1, 'DiCaprio', 'Leonardo')
    insert_acteur(c, 2, 'Cotillard', 'Marion')
    
    c.execute("INSERT OR IGNORE INTO FILMOGRAPHIE VALUES (1, 1, 'Cobb', 20000000)")
    c.execute("INSERT OR IGNORE INTO FILMOGRAPHIE VALUES (2, 1, 'Mal', 10000000)")
    
    ValiderTrans(conn)
    
    print("\n=== Table FILM ===")
    affiche_table(c, 'FILM')
    
    print("\n=== Détails du film 1 ===")
    affiche_film(c, 1)
    
    print("\n=== Nombre d'acteurs dans Inception ===")
    print(f"Nombre: {Nbr_acteurs(c, 'Inception')}")
    
    FermerConnex(conn)
