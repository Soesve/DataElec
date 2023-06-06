import pandas as pd
import configparser

# Récupération des variables placées sur config.txt
config = configparser.ConfigParser()
config.read('config.txt')
chemin_entree = config.get('Paths', 'chemin_entree')
chemin_sortie = config.get('Paths', 'chemin_sortie')

print("\n *** Chargement des fichiers de consommation, production et import/export du Datalake vers Warehouse_CSV *** \n")

# Traitement vers consommation_quotidienne_brute_regionale.csv
# Chargement des fichiers depuis Datalake
df_in_conso_quot_brute_regionale = pd.read_csv(chemin_entree + 'consommation-quotidienne-brute-regionale.csv', usecols=['Date','Heure','Code INSEE région','Consommation brute électricité (MW) - RTE'], sep=';')

# Renommmage des colonnes
df_out_conso_quot_region = df_in_conso_quot_brute_regionale
df_out_conso_quot_region.columns = ['Date', 'Heure', 'Code_region', 'Conso_electrique_brute_MWh']

# Enregistrement du fichier dans Warehouse_CSV
df_out_conso_quot_region.to_csv(chemin_sortie + 'conso_quot_region.csv', index=False)

print("Traitement vers conso_quot_region.csv : OK")


# Traitement vers conso_annuelle_type_region.csv
# Chargement des fichiers depuis Datalake
dtype = {
    'Année': int,
    'Code Région': str,
    'Code Département': str,
    'Code Commune': str,
    'Consommation Agriculture (MWh)': float,
    'Nombre de points Agriculture': int,
    'Consommation Industrie (MWh)': float,
    'Nombre de points Industrie': int,
    'Consommation Tertiaire  (MWh)': float,
    'Nombre de points Tertiaire': int,
    'Consommation Résidentiel  (MWh)': float,
    'Nombre de points Résidentiel': int,
    'Consommation totale (MWh)': float
}
df_in_conso_annuelle_secteur = pd.read_csv(chemin_entree + 'conso-elec-gaz-annuelle-par-secteur-dactivite-agregee-commune.csv', usecols=dtype.keys(), dtype=dtype, sep=';')

# Renommmage des colonnes
df_out_conso_annuelle_type_region = df_in_conso_annuelle_secteur
df_out_conso_annuelle_type_region.columns = ['Annee', 'Code_region', 'Code_departement', 'Code_commune','Conso_agriculture_MWh', 'Nb_points_agriculture', 'Conso_industrie_MWh', 'Nb_points_industrie','Conso_tertiaire_MWh', 'Nb_points_tertiaire', 'Conso_residentiel_MWh', 'Nb_points_residentiel', 'Conso_totale_MWh']

# Enregistrement du fichier dans Warehouse_CSV
df_out_conso_annuelle_type_region.to_csv(chemin_sortie + 'conso_annuelle_type_region.csv', index=False)

print("Traitement vers conso_annuelle_type_region.csv : OK")



# Traitement vers temperature-quotidienne-regionale.csv
# Chargement des fichiers depuis Datalake
df_in_temp_quotidienne_regionale = pd.read_csv(chemin_entree + 'temperature-quotidienne-regionale.csv', usecols=['Date', 'Code INSEE région', 'TMin (°C)', 'TMax (°C)', 'TMoy (°C)'], sep=';')

# Renommmage des colonnes
df_out_temp_quot_region = df_in_temp_quotidienne_regionale
df_out_temp_quot_region.columns = ['Date', 'Code_region', 'TMin','TMax','TMoy']

# Enregistrement du fichier dans Warehouse_CSV
df_out_temp_quot_region.to_csv(chemin_sortie + 'temp_quot_region.csv', index=False)

print("Traitement vers temp_quot_region.csv : OK")



# Traitement vers import-exports.csv
# Chargement des fichiers depuis Datalake
df_in_import_exports_commerciaux = pd.read_csv(chemin_entree + 'imports-exports-commerciaux.csv', usecols=['Date', "Tranche horaire du programme d'échange", 'FR vers GB (MWh)', 'GB vers FR (MWh)', 'FR vers CWE (MWh)', 'CWE vers FR (MWh)', 'FR vers CH (MWh)', 'CH vers FR (MWh)', 'FR vers IT (MWh)', 'IT vers FR (MWh)', 'FR vers ES (MWh)', 'ES vers FR (MWh)', 'Export France (MWh)', 'Import France (MWh)'], sep=';')

# Agrégation par date
df_out_imports_exports = df_in_import_exports_commerciaux.groupby('Date').sum()
df_out_imports_exports = df_out_imports_exports.reset_index()
df_out_imports_exports = df_out_imports_exports.drop("Tranche horaire du programme d'échange", axis=1)

# Renommmage des colonnes
df_out_imports_exports.columns = ['Date', 'FR_vers_GB__MWh', 'GB_vers_FR__MWh', 'FR_vers_CWE__MWh', 'CWE_vers_FR__MWh', 'FR_vers_CH__MWh', 'CH_vers_FR__MWh', 'FR_vers_IT__MWh','IT_vers_FR__MWh', 'FR_vers_ES__MWh','ES_vers_FR__MWh', 'Export_France__MWh', 'Import_France__MWh']

# Enregistrement du fichier dans Warehouse_CSV
df_out_imports_exports.to_csv(chemin_sortie + 'exports_imports.csv', index=False)

print("Traitement vers imports_exports.csv : OK")



# Traitement vers temperature-quotidienne-regionale.csv
# Chargement des fichiers depuis Datalake
df_in_injections_regionales_quotidiennes = pd.read_csv(chemin_entree + 'injections-regionales-quotidiennes-consolidees-rpt.csv', usecols=['Date', 'Code INSEE région', 'Filière', 'Energie journalière (MWh)'], sep=';')

# Renommmage des colonnes
df_out_injection_quot_region = df_in_injections_regionales_quotidiennes
df_out_injection_quot_region.columns = ['Date', 'Code_region', 'Filiere', 'Injection_quot']

# Enregistrement du fichier dans Warehouse_CSV
df_out_injection_quot_region.to_csv(chemin_sortie + 'injection_quot_region.csv', index=False)

print("Traitement vers injection_quot_region.csv : OK")



print("\n *** Fin du chargement des fichiers du Datalake vers Warehouse_CSV *** \n")