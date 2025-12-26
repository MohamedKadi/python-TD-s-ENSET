import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(page_title="Cinema Database", page_icon="🎬", layout="wide")

def AccederBD(maBase):
    conn = sqlite3.connect(maBase)
    c = conn.cursor()
    return conn, c

def CreerTable1(c):
    c.execute('''CREATE TABLE IF NOT EXISTS FILM (
        idFilm INTEGER PRIMARY KEY,
        titre TEXT NOT NULL,
        realisateur TEXT,
        annee INTEGER
    )''')

def CreerTable2(c):
    c.execute('''CREATE TABLE IF NOT EXISTS ACTEUR (
        idActeur INTEGER PRIMARY KEY,
        nom TEXT NOT NULL,
        prenom TEXT NOT NULL
    )''')

def CreerTable3(c):
    c.execute('''CREATE TABLE IF NOT EXISTS FILMOGRAPHIE (
        idActeur INTEGER,
        idFilm INTEGER,
        role TEXT,
        salaire REAL,
        FOREIGN KEY (idActeur) REFERENCES ACTEUR(idActeur),
        FOREIGN KEY (idFilm) REFERENCES FILM(idFilm),
        PRIMARY KEY (idActeur, idFilm)
    )''')

def rech_personne(c, nom, prenom):
    c.execute("SELECT * FROM ACTEUR WHERE nom=? AND prenom=?", (nom, prenom))
    return c.fetchone() is not None

def insert_acteur(c, id, nom, prenom):
    if not rech_personne(c, nom, prenom):
        c.execute("INSERT INTO ACTEUR VALUES (?, ?, ?)", (id, nom, prenom))
        return True
    return False

def affiche_table(c, nomTable):
    c.execute(f"SELECT * FROM {nomTable}")
    return c.fetchall()

def affiche_film(c, id):
    c.execute("SELECT * FROM FILM WHERE idFilm=?", (id,))
    return c.fetchone()

def supr_film(c, id):
    c.execute("DELETE FROM FILMOGRAPHIE WHERE idFilm=?", (id,))
    c.execute("DELETE FROM FILM WHERE idFilm=?", (id,))

def modif_FILMOGRAPHIE(c, id1, id2, val):
    c.execute("UPDATE FILMOGRAPHIE SET salaire=? WHERE idActeur=? AND idFilm=?", 
              (val, id1, id2))

def Nbr_acteurs(c, nomFilm):
    c.execute("""SELECT COUNT(*) FROM FILMOGRAPHIE f
                 JOIN FILM ON f.idFilm = FILM.idFilm
                 WHERE FILM.titre=?""", (nomFilm,))
    return c.fetchone()[0]

def ActeursSansFilms(c):
    c.execute("""SELECT nom, prenom FROM ACTEUR
                 WHERE idActeur NOT IN (SELECT idActeur FROM FILMOGRAPHIE)""")
    return c.fetchall()

def ActeursDebutants(c):
    c.execute("""SELECT A.nom, A.prenom, AVG(F.salaire) as moyenne
                 FROM ACTEUR A
                 JOIN FILMOGRAPHIE F ON A.idActeur = F.idActeur
                 GROUP BY A.idActeur, A.nom, A.prenom""")
    return c.fetchall()

def ActeursMemeSalaire(c):
    c.execute("""SELECT DISTINCT A1.nom, A1.prenom, A2.nom, A2.prenom, F1.salaire
                 FROM FILMOGRAPHIE F1
                 JOIN FILMOGRAPHIE F2 ON F1.salaire = F2.salaire AND F1.idActeur < F2.idActeur
                 JOIN ACTEUR A1 ON F1.idActeur = A1.idActeur
                 JOIN ACTEUR A2 ON F2.idActeur = A2.idActeur""")
    return c.fetchall()

def SalaireDollarToDirham(c):
    c.execute("""SELECT A.nom, A.prenom, F.salaire, F.salaire * 9 as salaire_dirham
                 FROM FILMOGRAPHIE F
                 JOIN ACTEUR A ON F.idActeur = A.idActeur""")
    return c.fetchall()

def ValiderTrans(conn):
    conn.commit()

def TableToFile(Fich, c, nomTable):
    c.execute(f"SELECT * FROM {nomTable}")
    rows = c.fetchall()
    with open(Fich, 'w', encoding='utf-8') as f:
        for row in rows:
            f.write(str(row) + '\n')

def FileToTable(Fich, c, nomTable):
    with open(Fich, 'r', encoding='utf-8') as f:
        for line in f:
            data = eval(line.strip())
            placeholders = ','.join(['?'] * len(data))
            c.execute(f"INSERT INTO {nomTable} VALUES ({placeholders})", data)

def FermerConnex(conn):
    conn.close()


st.title("🎬 Cinema Database Dashboard")
st.markdown("---")

maBase = 'cinema.sqlite'
conn, c = AccederBD(maBase)

CreerTable1(c)
CreerTable2(c)
CreerTable3(c)
ValiderTrans(conn)

menu = st.sidebar.selectbox(
    "Menu",
    ["📊 Tableau de bord", "🎥 Films", "👤 Acteurs", "📋 Filmographie", 
     "🔍 Recherches", "⚙️ Opérations"]
)

if menu == "📊 Tableau de bord":
    st.header("Tableau de bord")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        c.execute("SELECT COUNT(*) FROM FILM")
        nb_films = c.fetchone()[0]
        st.metric("Films", nb_films)
    
    with col2:
        c.execute("SELECT COUNT(*) FROM ACTEUR")
        nb_acteurs = c.fetchone()[0]
        st.metric("Acteurs", nb_acteurs)
    
    with col3:
        c.execute("SELECT COUNT(*) FROM FILMOGRAPHIE")
        nb_roles = c.fetchone()[0]
        st.metric("Rôles", nb_roles)
    
    st.subheader("Films récents")
    c.execute("SELECT * FROM FILM ORDER BY annee DESC LIMIT 5")
    films = c.fetchall()
    if films:
        df = pd.DataFrame(films, columns=['ID', 'Titre', 'Réalisateur', 'Année'])
        st.dataframe(df, use_container_width=True, hide_index=True)
    else:
        st.info("Aucun film dans la base de données")

elif menu == "🎥 Films":
    st.header("Gestion des Films")
    
    tab1, tab2, tab3 = st.tabs(["Liste", "Ajouter", "Supprimer"])
    
    with tab1:
        films = affiche_table(c, "FILM")
        if films:
            df = pd.DataFrame(films, columns=['ID', 'Titre', 'Réalisateur', 'Année'])
            st.dataframe(df, use_container_width=True, hide_index=True)
        else:
            st.info("Aucun film")
    
    with tab2:
        with st.form("add_film"):
            id_film = st.number_input("ID Film", min_value=1, step=1)
            titre = st.text_input("Titre")
            realisateur = st.text_input("Réalisateur")
            annee = st.number_input("Année", min_value=1900, max_value=2025, value=2024)
            
            submitted = st.form_submit_button("➕ Ajouter Film", use_container_width=True)
            
            if submitted:
                if not titre:
                    st.error("❌ Erreur: Le titre est obligatoire!")
                else:
                    try:
                        c.execute("INSERT INTO FILM VALUES (?, ?, ?, ?)", 
                                 (id_film, titre, realisateur, annee))
                        ValiderTrans(conn)
                        st.success(f"✅ Film '{titre}' ajouté avec succès!")
                        st.balloons()
                    except sqlite3.IntegrityError:
                        st.error(f"❌ Erreur: Un film avec l'ID {id_film} existe déjà!")
                    except Exception as e:
                        st.error(f"❌ Erreur lors de l'ajout: {e}")
    
    with tab3:
        films = affiche_table(c, "FILM")
        if films:
            film_options = {f"{f[0]} - {f[1]}": f[0] for f in films}
            film_select = st.selectbox("Choisir le film à supprimer", film_options.keys())
            
            if st.button("🗑️ Supprimer", type="primary", use_container_width=True):
                try:
                    id_supr = film_options[film_select]
                    supr_film(c, id_supr)
                    ValiderTrans(conn)
                    st.success(f"✅ Film supprimé avec succès!")
                    st.rerun()
                except Exception as e:
                    st.error(f"❌ Erreur lors de la suppression: {e}")
        else:
            st.info("Aucun film à supprimer")

elif menu == "👤 Acteurs":
    st.header("Gestion des Acteurs")
    
    tab1, tab2 = st.tabs(["Liste", "Ajouter"])
    
    with tab1:
        acteurs = affiche_table(c, "ACTEUR")
        if acteurs:
            num_cols = len(acteurs[0]) if acteurs else 0
            if num_cols == 3:
                df = pd.DataFrame(acteurs, columns=['ID', 'Nom', 'Prénom'])
            elif num_cols == 4:
                df = pd.DataFrame(acteurs, columns=['ID', 'Nom', 'Prénom', 'Extra'])
            else:
                df = pd.DataFrame(acteurs)
            st.dataframe(df, use_container_width=True, hide_index=True)
        else:
            st.info("Aucun acteur")
    
    with tab2:
        with st.form("add_acteur"):
            id_acteur = st.number_input("ID Acteur", min_value=1, step=1)
            nom = st.text_input("Nom")
            prenom = st.text_input("Prénom")
            
            submitted = st.form_submit_button("➕ Ajouter Acteur", use_container_width=True)
            
            if submitted:
                if not nom or not prenom:
                    st.error("❌ Erreur: Le nom et le prénom sont obligatoires!")
                else:
                    try:
                        if insert_acteur(c, id_acteur, nom, prenom):
                            ValiderTrans(conn)
                            st.success(f"✅ Acteur '{prenom} {nom}' ajouté avec succès!")
                            st.balloons()
                        else:
                            st.warning(f"⚠️ L'acteur '{prenom} {nom}' existe déjà dans la base!")
                    except sqlite3.IntegrityError:
                        st.error(f"❌ Erreur: Un acteur avec l'ID {id_acteur} existe déjà!")
                    except Exception as e:
                        st.error(f"❌ Erreur lors de l'ajout: {e}")

elif menu == "📋 Filmographie":
    st.header("Filmographie")
    
    tab1, tab2, tab3 = st.tabs(["Liste", "Ajouter", "Modifier Salaire"])
    
    with tab1:
        try:
            c.execute("""SELECT F.idActeur, A.nom, A.prenom, F.idFilm, 
                         FILM.titre, F.role, F.salaire
                         FROM FILMOGRAPHIE F
                         JOIN ACTEUR A ON F.idActeur = A.idActeur
                         JOIN FILM ON F.idFilm = FILM.idFilm""")
            filmo = c.fetchall()
            if filmo:
                df = pd.DataFrame(filmo, columns=['ID Acteur', 'Nom', 'Prénom', 
                                                  'ID Film', 'Film', 'Rôle', 'Salaire $'])
                st.dataframe(df, use_container_width=True, hide_index=True)
            else:
                st.info("Aucune filmographie")
        except Exception as e:
            st.error(f"Erreur: {e}")
    
    with tab2:
        acteurs = affiche_table(c, "ACTEUR")
        films = affiche_table(c, "FILM")
        
        if not acteurs or not films:
            st.warning("⚠️ Veuillez d'abord ajouter des acteurs et des films!")
        else:
            with st.form("add_filmo"):
                acteur_options = {f"{a[0]} - {a[2]} {a[1]}": a[0] for a in acteurs}
                film_options = {f"{f[0]} - {f[1]}": f[0] for f in films}
                
                acteur_select = st.selectbox("Choisir l'acteur", acteur_options.keys())
                film_select = st.selectbox("Choisir le film", film_options.keys())
                role = st.text_input("Rôle")
                salaire = st.number_input("Salaire ($)", min_value=0.0, step=1000.0)
                
                submitted = st.form_submit_button("➕ Ajouter Rôle", use_container_width=True)
                
                if submitted:
                    if not role:
                        st.error("❌ Erreur: Le rôle est obligatoire!")
                    else:
                        try:
                            id_act = acteur_options[acteur_select]
                            id_film = film_options[film_select]
                            c.execute("INSERT INTO FILMOGRAPHIE VALUES (?, ?, ?, ?)", 
                                     (id_act, id_film, role, salaire))
                            ValiderTrans(conn)
                            st.success(f"✅ Rôle ajouté avec succès!")
                            st.balloons()
                        except sqlite3.IntegrityError:
                            st.error("❌ Erreur: Cet acteur joue déjà dans ce film!")
                        except Exception as e:
                            st.error(f"❌ Erreur lors de l'ajout: {e}")
    
    with tab3:
        c.execute("""SELECT F.idActeur, A.nom, A.prenom, F.idFilm, FILM.titre, F.salaire
                     FROM FILMOGRAPHIE F
                     JOIN ACTEUR A ON F.idActeur = A.idActeur
                     JOIN FILM ON F.idFilm = FILM.idFilm""")
        filmographie = c.fetchall()
        
        if filmographie:
            filmo_options = {f"Acteur {f[0]} ({f[2]} {f[1]}) - Film {f[3]} ({f[4]}) - Salaire: ${f[5]}": 
                            (f[0], f[3]) for f in filmographie}
            
            filmo_select = st.selectbox("Choisir l'entrée à modifier", filmo_options.keys())
            nouveau_salaire = st.number_input("Nouveau Salaire ($)", min_value=0.0, step=1000.0)
            
            if st.button("💰 Modifier Salaire", type="primary", use_container_width=True):
                try:
                    id_act, id_film = filmo_options[filmo_select]
                    modif_FILMOGRAPHIE(c, id_act, id_film, nouveau_salaire)
                    ValiderTrans(conn)
                    st.success(f"✅ Salaire modifié avec succès à ${nouveau_salaire}!")
                    st.rerun()
                except Exception as e:
                    st.error(f"❌ Erreur lors de la modification: {e}")
        else:
            st.info("Aucune filmographie à modifier")

elif menu == "🔍 Recherches":
    st.header("Recherches et Analyses")
    
    option = st.selectbox(
        "Choisir une recherche",
        ["Nombre d'acteurs par film", "Acteurs sans films", 
         "Acteurs avec moyenne salaires", "Acteurs même salaire",
         "Salaires en Dirhams"]
    )
    
    if option == "Nombre d'acteurs par film":
        c.execute("SELECT titre FROM FILM")
        films = [f[0] for f in c.fetchall()]
        if films:
            film_choisi = st.selectbox("Choisir un film", films)
            if st.button("🔍 Rechercher", use_container_width=True):
                try:
                    nb = Nbr_acteurs(c, film_choisi)
                    st.success(f"✅ Nombre d'acteurs dans '{film_choisi}': **{nb}**")
                except Exception as e:
                    st.error(f"❌ Erreur: {e}")
        else:
            st.info("Aucun film dans la base")
    
    elif option == "Acteurs sans films":
        try:
            acteurs = ActeursSansFilms(c)
            if acteurs:
                df = pd.DataFrame(acteurs, columns=['Nom', 'Prénom'])
                st.dataframe(df, use_container_width=True, hide_index=True)
                st.info(f"Total: {len(acteurs)} acteur(s) sans film")
            else:
                st.success("✅ Tous les acteurs ont joué dans au moins un film!")
        except Exception as e:
            st.error(f"❌ Erreur: {e}")
    
    elif option == "Acteurs avec moyenne salaires":
        try:
            acteurs = ActeursDebutants(c)
            if acteurs:
                df = pd.DataFrame(acteurs, columns=['Nom', 'Prénom', 'Moyenne Salaire $'])
                df['Moyenne Salaire $'] = df['Moyenne Salaire $'].round(2)
                st.dataframe(df, use_container_width=True, hide_index=True)
            else:
                st.info("Aucune donnée disponible")
        except Exception as e:
            st.error(f"❌ Erreur: {e}")
    
    elif option == "Acteurs même salaire":
        try:
            paires = ActeursMemeSalaire(c)
            if paires:
                df = pd.DataFrame(paires, columns=['Nom 1', 'Prénom 1', 'Nom 2', 
                                                   'Prénom 2', 'Salaire $'])
                st.dataframe(df, use_container_width=True, hide_index=True)
                st.info(f"Total: {len(paires)} paire(s) trouvée(s)")
            else:
                st.info("Aucune paire d'acteurs avec le même salaire")
        except Exception as e:
            st.error(f"❌ Erreur: {e}")
    
    elif option == "Salaires en Dirhams":
        try:
            salaires = SalaireDollarToDirham(c)
            if salaires:
                df = pd.DataFrame(salaires, columns=['Nom', 'Prénom', 'Salaire $', 
                                                     'Salaire MAD'])
                df['Salaire MAD'] = df['Salaire MAD'].round(2)
                st.dataframe(df, use_container_width=True, hide_index=True)
            else:
                st.info("Aucune donnée disponible")
        except Exception as e:
            st.error(f"❌ Erreur: {e}")

elif menu == "⚙️ Opérations":
    st.header("Opérations sur la base")
    
    tab1, tab2 = st.tabs(["Exporter", "Importer"])
    
    with tab1:
        table_export = st.selectbox("Table à exporter", ["FILM", "ACTEUR", "FILMOGRAPHIE"])
        nom_fichier = st.text_input("Nom du fichier", value=f"{table_export.lower()}.txt")
        
        if st.button("📤 Exporter", use_container_width=True):
            try:
                TableToFile(nom_fichier, c, table_export)
                st.success(f"✅ Table {table_export} exportée vers {nom_fichier}")
            except Exception as e:
                st.error(f"❌ Erreur lors de l'export: {e}")
    
    with tab2:
        st.warning("⚠️ Format requis: chaque ligne doit être un tuple Python valide")
        table_import = st.selectbox("Table destination", 
                                    ["FILM", "ACTEUR", "FILMOGRAPHIE"], key="import")
        fichier_import = st.text_input("Nom du fichier à importer")
        
        if st.button("📥 Importer", use_container_width=True):
            try:
                FileToTable(fichier_import, c, table_import)
                ValiderTrans(conn)
                st.success(f"✅ Données importées dans {table_import}!")
                st.balloons()
            except FileNotFoundError:
                st.error(f"❌ Erreur: Le fichier '{fichier_import}' n'existe pas!")
            except Exception as e:
                st.error(f"❌ Erreur lors de l'import: {e}")

st.sidebar.markdown("---")
st.sidebar.info("🎬 Cinema Database v1.0")
st.sidebar.caption("Base de données: cinema.sqlite")