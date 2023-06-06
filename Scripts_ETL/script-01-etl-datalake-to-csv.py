import pandas as pd

chemin_entree = '/Users/jeremy/Documents/1. Projets/Project DataElec/Datalake/'
chemin_sortie = '/Users/jeremy/Documents/1. Projets/Project DataElec/Warehouse_CSV/'



print("\n *** Chargement des fichiers du Datalake vers Warehouse_CSV *** \n")



# Traitement vers codes_region.csv
# Chargement des fichiers depuis Datalake
df_in_donnees_regions = pd.read_csv(chemin_entree + 'donnees_regions.csv', usecols=['CODREG','REG','PTOT'], sep=';')
df_in_regions_zones_scolaires = pd.read_csv(chemin_entree + 'regions-zones-scolaires.csv', usecols=['CODREG','ZONE'], sep=';')

# Fusion des fichiers via variable CODREG
df_out_codes_region = pd.merge(df_in_donnees_regions, df_in_regions_zones_scolaires, on='CODREG')

# Renommmage des colonnes
df_out_codes_region.columns = ['ID_code_region', 'Nom_region', 'Population_region', 'Zone_vacances']

# Enregistrement du fichier dans Warehouse_CSV
df_out_codes_region.to_csv(chemin_sortie + 'codes_region.csv', index=False)

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
df_out_codes_departements.to_csv(chemin_sortie + 'codes_departement.csv', index=False)

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
df_out_codes_commune.to_csv(chemin_sortie + 'codes_commune.csv', index=False)

print("Traitement vers codes_commune : OK")



# Traitement vers calendrier_vacances_scolaires.csv
# Chargement des fichiers depuis Datalake
df_in_calendrier_vacances = pd.read_excel(chemin_entree + 'calendrier-vacances.xlsx', "Feuil1", index_col=None, na_values=["NA"])
df_out_calendrier_vacances = df_in_calendrier_vacances

# Ajout colonne Semaine ou Week-end
df_out_calendrier_vacances.loc[(df_out_calendrier_vacances.Jour == "Samedi") | (df_out_calendrier_vacances.Jour == "Dimanche"), "Semaine"] = "Week-end"
df_out_calendrier_vacances.loc[~((df_out_calendrier_vacances.Jour == "Samedi") | (df_out_calendrier_vacances.Jour == "Dimanche")), "Semaine"] = "Semaine"

# Enregistrement du fichier dans Warehouse_CSV
df_out_calendrier_vacances.to_csv(chemin_sortie + 'calendrier_vacances_scolaires.csv', index=False)

print("Traitement vers calendrier_vacances_scolaires : OK")



print("\n *** Fin du chargement des fichiers du Datalake vers Warehouse_CSV *** \n")
