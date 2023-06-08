![Gif Back to the future](media/back-to-the-future.gif)
# Projet DataElec


## Sommaire
- Objectifs du projet
- Organisation
- Collecte : les sources​ et leur stockage
- Préparation : modélisation​ et traitement
- Analyse​ : visualisation​
- Optimisation



## Hum, intéressant... 
![Gif The office](media/gif-office-01.gif)



## Objectifs du projet


## Objectifs du projet
- Comprendre la consommation électrique en France : par type de clients, par région, par période (saisons, jours de semaine…)​


## Objectifs du projet
- Comprendre la consommation électrique en France : par type de clients, par région, par période (saisons, jours de semaine…)​
- Pour identifier les éléments qui influencent la consommation : météo, jours de semaine… (exemple : coefficient de sensibilité météo par région ou zone géographique plus petite pour identifier les priorités en terme d’isolation des bâtiments)



## Organisation
- Microsoft Teams (et OneDrive)
- Trello
- Github


### Github (évidemment)
![Github](media/capture-github.png)


### Microsoft Teams
Pour les échanges
![Teams pour échanger](media/capture-teams-publications.png)


Et les partages de fichiers (hors github)
![Teams pour le partage de fichiers](media/capture-teams-fichiers.png)


### Trello pour le suivi collaboratif des tâches
![Trello](media/capture-trello.png)



## Collecte
- Les sources
- Import et stockage des données


### Les sources
- Open Data Réseau Energies https://odre.opendatasoft.com/​
    - Réseaux Énergies réunit plusieurs acteurs de l'énergies (GRTgaz, RTE, Teréga...) dans une démarche de transparence et de pédagogie à l’égard des citoyens, des collectivités territoriales et des acteurs économiques...​
    - Données utilisées : Consommation, production par région, quotidien...​


### Les sources
- INSEE https://www.insee.fr/​
    - L'Insee est une direction générale du ministère de l’Économie et des Finances implantée dans l'ensemble du territoire français, indépendante dont l'objectif est la conception, la production et la diffusion des statistiques publiques.​
    - Données utilisées : Population et type de logements par région, départements, communes​


### Les sources
- Bulletin officiel de l'éducation nationale https://www.education.gouv.fr/​
    - Le Bulletin officiel de l'éducation nationale, de la jeunesse et des sports publie des actes administratifs : décrets, arrêtés, notes de service, etc. ​
    - Données utilisées : dates des vacances scolaires par zone 


### Les sources
![Tableau des champs par source de données](media/tableau-sources-donnees.png)


### Stockage des données
Le datalake dans un dossier local
![Datalake dans un dossier local](media/capture-dossier-datalake.png)


### Stockage des données
Le datalake dans un bucket Google Cloud
![Datalake dans un bucket Google Cloud](media/capture-bucket-datalake.png)



## Préparation
- Modélisation du warehouse
- Schématisation et traitement V1
- Schématisation et traitement V2


### Modélisation
![Modélisation du schéma de données attendu dans le warehouse](media/schema-donnees.png)


### Traitement V1
Schématisation
![Schéma de l'architecture des traitements de données](media/schema-architecture-v01.png)


### Traitement V1
Avec Talend (exemple 1)
![Exemple de job sur Talend 01](media/capture-talend-01.png)


### Traitement V1
Avec Talend (exemple 2)
![Exemple de job sur Talend 02](media/capture-talend-02.png)


### Traitement V1
Résultat dans MySQL Workbench
![BDD dans MySqL Workbench](media/capture-mysql-workbench.png)



## Data visualization
- Import des données
- Réalisation


### Importation des données
Dans Qlik
![Schéma des données après importation dans Qlik](media/capture-schema-donnees-qlik.png)


### Importation des données
Dans PowerBI
![Schéma des données après importation dans PowerBI](media/capture-schema-donnees-powerbi.png)



## Fin