# Projet DataElec


## Sommaire
- Objectifs du projet
- Collecte : les sources​ et leur stockage
- Préparation : modélisation​ et traitement
- Analyse​ : visualisation​
- Optimisation



## Objectifs du projet


## Objectifs du projet
- Comprendre la consommation électrique en France : par type de clients, par région, par période (saisons, jours de semaine…)​


## Objectifs du projet
- Comprendre la consommation électrique en France : par type de clients, par région, par période (saisons, jours de semaine…)​
- Pour identifier les éléments qui influencent la consommation : météo, jours de semaine… (exemple : coefficient de sensibilité météo par région ou zone géographique plus petite pour identifier les priorités en terme d’isolation des bâtiments)



## Collecte


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
![Tableau des champs par source de données](media/capture-dossier-datalake.png)


### Stockage des données
Le datalake dans un bucket Google Cloud
![Tableau des champs par source de données](media/capture-bucket-datalake.png)



## Préparation


### Modélisation
![Tableau des champs par source de données](media/schema-donnees.png)
