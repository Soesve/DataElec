import os
import psycopg2
import csv

# Chemin du dossier contenant les fichiers CSV
dossier_csv = '/warehouse_csv'

# Liste des fichiers CSV dans le dossier spécifié
fichiers_csv = [f for f in os.listdir(dossier_csv) if f.endswith('.csv')]

# Connexion à la base de données PostgreSQL
conSQL = psycopg2.connect(
    host="localhost",
    port="5432",
    dbname="dataelec",
    user="dataelec",
    password="jL2wtvNMa6Ttkd"
)

cur = conSQL.cursor()

# Vérifier si une table existe déjà dans la base de données
def table_exists(nom_table):
    cur.execute("SELECT EXISTS(SELECT 1 FROM information_schema.tables WHERE table_name = %s)", (nom_table,))
    return cur.fetchone()[0]

# Supprimer une table existante
def supprimer_table(nom_table):
    cur.execute(f"DROP TABLE IF EXISTS {nom_table}")
    print(f"L'ancienne table {nom_table} a été supprimée.")

# Parcours des fichiers CSV
for fichier_csv in fichiers_csv:
    chemin_fichier_csv = os.path.join(dossier_csv, fichier_csv)

    # Lecture du fichier CSV
    with open(chemin_fichier_csv, 'r') as file:
        # Obtenir les noms et les types des colonnes à partir du premier fichier CSV
        lecteur_csv = csv.reader(file)
        entetes = next(lecteur_csv)
        types_colonnes = ['TEXT'] * len(entetes)  # Par défaut, le type des colonnes est défini sur TEXT

        # Création du nom de la table basé sur le nom du fichier CSV
        nom_table = fichier_csv.replace('.csv', '')

        # Vérifier si la table existe déjà
        if table_exists(nom_table):
            # Supprimer l'ancienne table
            supprimer_table(nom_table)

        # Création de la table dans la base de données
        liste_colonnes = [f"{colonne} {type_colonne}" for colonne, type_colonne in zip(entetes, types_colonnes)]
        create_table_query = f"CREATE TABLE {nom_table} (id SERIAL PRIMARY KEY, {', '.join(liste_colonnes)})"
        cur.execute(create_table_query)
        print(f"La nouvelle table {nom_table} a été créée.")

        # Réinitialiser le curseur du fichier CSV
        file.seek(0)

        # Insertion des données du fichier CSV dans la table
        cur.copy_expert(f"COPY {nom_table} FROM STDIN WITH CSV HEADER", file)

        print(f"Le fichier {fichier_csv} a été inséré dans la table {nom_table}")

# Validation des modifications et fermeture de la connexion
conSQL.commit()
cur.close()
conSQL.close()