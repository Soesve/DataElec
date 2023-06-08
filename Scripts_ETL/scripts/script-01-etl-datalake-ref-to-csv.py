import pandas as pd
import zipfile
import os
import configparser

# Récupération des variables placées sur config.txt
config = configparser.ConfigParser()
config.read('config.txt')
chemin_entree = config.get('Paths', 'chemin_entree')
chemin_sortie = config.get('Paths', 'chemin_sortie')


print("\n *** Chargement des fichiers de référence du Datalake vers Warehouse_CSV *** \n")



# Traitement vers codes_region.csv
# Chargement des fichiers depuis Datalake
df_in_donnees_regions = pd.read_csv(chemin_entree + 'donnees_regions.csv', usecols=['CODREG','REG','PTOT'], sep=';')
df_in_regions_zones_scolaires = pd.read_csv(chemin_entree + 'regions-zones-scolaires.csv', usecols=['CODREG','ZONE'], sep=';')

# Fusion des fichiers via variable CODREG
df_out_codes_region = pd.merge(df_in_donnees_regions, df_in_regions_zones_scolaires, on='CODREG')

# Renommmage des colonnes
df_out_codes_region.columns = ['ID_code_region', 'Nom_region', 'Population_region', 'Zone_vacances']

# Enregistrement du fichier dans Warehouse_CSV
df_out_codes_region.to_csv(chemin_sortie + 'codes_region.csv', sep=';', index=False)

print("Traitement vers codes_region : OK")



# Traitement vers codes_departement.csv
# Chargement des fichiers depuis Datalake
df_in_donnees_departements = pd.read_csv(chemin_entree + 'donnees_departements.csv', usecols=['CODREG','CODDEP','DEP','PTOT'], sep=';')

# Renommmage des colonnes
df_out_codes_departements = df_in_donnees_departements
df_out_codes_departements.columns = ['Code_region', 'ID_code_departement', 'Nom_departement', 'Population_departement']

# Réorganiser les colonnes dans le DataFrame
df_out_codes_departements = df_out_codes_departements.reindex(columns=['ID_code_departement', 'Nom_departement', 'Population_departement', 'Code_region'])

# Enregistrement du fichier dans Warehouse_CSV
df_out_codes_departements.to_csv(chemin_sortie + 'codes_departement.csv', sep=';', index=False)

print("Traitement vers codes_departement : OK")



# Traitement vers codes_commune.csv
# Chargement des fichiers depuis Datalake
df_in_donnees_communes = pd.read_csv(chemin_entree + 'donnees_communes.csv', usecols=['CODDEP','Code commune','COM','PTOT'], sep=';')

# Renommmage des colonnes
df_out_codes_commune = df_in_donnees_communes
df_out_codes_commune.columns = ['Code_departement', 'ID_code_commune', 'Nom_commune', 'Population_commune']

# Réorganiser les colonnes dans le DataFrame
df_out_codes_commune = df_out_codes_commune.reindex(columns=['ID_code_commune', 'Nom_commune', 'Population_commune', 'Code_departement'])

# Enregistrement du fichier dans Warehouse_CSV
df_out_codes_commune.to_csv(chemin_sortie + 'codes_commune.csv', sep=';', index=False)

print("Traitement vers codes_commune : OK")



# Traitement vers calendrier_vacances_scolaires.csv
# Chargement des fichiers depuis Datalake
df_in_calendrier_vacances = pd.read_excel(chemin_entree + 'calendrier-vacances.xlsx', "Feuil1", index_col=None, na_values=["NA"])
df_out_calendrier_vacances = df_in_calendrier_vacances

# Ajout colonne Semaine ou Week-end
df_out_calendrier_vacances.loc[(df_out_calendrier_vacances.Jour == "Samedi") | (df_out_calendrier_vacances.Jour == "Dimanche"), "Semaine"] = "Week-end"
df_out_calendrier_vacances.loc[~((df_out_calendrier_vacances.Jour == "Samedi") | (df_out_calendrier_vacances.Jour == "Dimanche")), "Semaine"] = "Semaine"

# Enregistrement du fichier dans Warehouse_CSV
df_out_calendrier_vacances.to_csv(chemin_sortie + 'calendrier_vacances_scolaires.csv', sep=';', index=False)

print("Traitement vers calendrier_vacances_scolaires : OK")



# Traitement vers surf_logement_commune.csv et type_logement_commune.csv
# Décompression de la source
with zipfile.ZipFile(chemin_entree + 'RP2019_LOGEMT_csv.zip', 'r') as zip_ref:
    zip_ref.extractall(chemin_entree + 'tmp')

# Chargement de la source dans un dataframe
df_in_donnees_logements = pd.read_csv(chemin_entree + 'tmp/FD_LOGEMT_2019.csv', usecols=['COMMUNE','SURF','TYPL'], sep=';', dtype={'COMMUNE': str})

# Aggrégation par surface de logement
df_out_surf_logement = pd.crosstab(index=df_in_donnees_logements['COMMUNE'], columns=df_in_donnees_logements['SURF'], rownames=['COMMUNE'])
df_out_surf_logement = df_out_surf_logement.reset_index()

# Aggrégation par type de logement
df_out_type_logement = pd.crosstab(index=df_in_donnees_logements['COMMUNE'], columns=df_in_donnees_logements['TYPL'], rownames=['COMMUNE'])
df_out_type_logement = df_out_type_logement.reset_index()
df_out_type_logement["type_autres"] = df_out_type_logement[[3, 4, 5, 6]].sum(axis=1)
df_out_type_logement = df_out_type_logement.drop([3, 4, 5, 6], axis=1)

# Renommage des colonnes
df_out_surf_logement.columns = ['Code_commune','surf_moins_30','surf_30_40','surf_40_60','surf_60_80','surf_80_100','surf_100_120','surf_plus_120','surf_hors_res_principale']
df_out_type_logement.columns = ['Code_commune','type_maison','type_appartement','type_autres']

# Enregistrement des fichiers dans Warehouse_CSV
df_out_surf_logement.to_csv(chemin_sortie + 'surf_logement_commune.csv', sep=';', index=False)
df_out_type_logement.to_csv(chemin_sortie + 'type_logement_commune.csv', sep=';', index=False)

# Suppression du dossier temporaire
dossier_a_supprimer = chemin_entree + "tmp"
os.system(f"sudo chmod -R 777 {dossier_a_supprimer}")
os.system(f"rm -rf {dossier_a_supprimer}")

print("Traitement vers surf_logement_commune.csv et type_logement_commune.csv : OK")

print("\n *** Fin du chargement des fichiers du Datalake vers Warehouse_CSV *** \n")
