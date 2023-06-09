import requests
import configparser
import zipfile
import os

# Récupération des variables placées sur config.txt
config = configparser.ConfigParser()
config.read('/usr/src/app/scripts/config.txt')
datalake = config.get('Paths', 'chemin_entree')

# On parcourt les URLs du fichier config.txt
for key in config['Downloads']:
    url = config['Downloads'][key]
    print(url)
    response = requests.get(url)
    
    # On télécharge dans le datalake
    with open(datalake + key, 'wb') as file:
        file.write(response.content)
    
    if key == "ensemble.zip":
        path_ensemble = datalake + key
        files_to_extract = ["donnees_communes.csv", "donnees_departements.csv", "donnees_regions.csv"]

        with zipfile.ZipFile(path_ensemble, "r") as zip_ref:
            for file in files_to_extract:
                zip_ref.extract(file, datalake)
                print("Fichier :",file,"écrasé")
        os.remove(path_ensemble)
    else:
        print("Fichier :",key,"écrasé")