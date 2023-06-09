import os
import requests
import configparser

# Récupération des variables placées sur config.txt
config = configparser.ConfigParser()
config.read('config.txt')
datalake = config.get('Paths', 'chemin_entree')

# URL du fichier à télécharger
url = "https://odre.opendatasoft.com/api/explore/v2.1/catalog/datasets/consommation-quotidienne-brute-regionale/exports/csv?lang=fr&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B"

# Nom du fichier téléchargé
file_name = "consommation-quotidienne-brute-regionale.csv"

# Vérification de la dernière version déjà téléchargée
last_downloaded_file = os.path.join(datalake, file_name)
last_modified = None

if os.path.exists(last_downloaded_file):
    last_modified = os.path.getmtime(last_downloaded_file)

# Téléchargement du fichier
response = requests.get(url)
if response.status_code == 200:
    remote_modified = response.headers.get('last-modified')
    remote_modified_timestamp = None

    if remote_modified:
        remote_modified_timestamp = response.headers.get('last-modified')

    if not last_modified or (remote_modified_timestamp and remote_modified_timestamp > last_modified):
        with open(last_downloaded_file, 'wb') as file:
            file.write(response.content)
        print("Le fichier a été téléchargé avec succès.")
    else:
        print("La dernière version du fichier est déjà téléchargée.")
else:
    print("Échec du téléchargement du fichier.")