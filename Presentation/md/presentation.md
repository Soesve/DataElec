![Gif Back to the future](media/back-to-the-future.gif)
# Projet DataElec


## Sommaire
- Objectifs et organisation du projet
- Collecte des données (sources​, datalake)
- Préparation des données (modélisation​, traitement)
- Analyse​ : data visualisation​
- Retours d'expériences



## Objectifs et <br/>organisation du projet
- Objectifs du projet
- Organisation du projet


### Objectifs du projet
- Analyser la consommation électrique en France pour identifier les éléments qui l'influencent : température, type de clients, région, saisonnalité (jours de semaine, vacances)...
- Cette étude permettrait de guider des choix politiques : 
    - Prévision de consommation électrique et ajustement de la production
    - Identification de zones géographiques particulièrement sensibles aux variations de température (prioriser l'investissement sur l'isolation thermique des bâtiments)
    - ...


### Organisation du projet
Github + Docker = ❤️
![Github](media/capture-github.png)


### Organisation du projet
Microsoft Teams pour les échanges...
![Teams pour échanger](media/capture-teams-publications.png)


### Organisation du projet
... et les partages de fichiers (hors github)
![Teams pour le partage de fichiers](media/capture-teams-fichiers.png)


### Organisation du projet 
Trello pour le suivi collaboratif des tâches
![Trello](media/capture-trello.png)



## Collecte des données<br/>(sources​, datalake)
- Sources
- Import et stockage vers le datalake


### Les sources
- Open Data Réseau Energies https://odre.opendatasoft.com/​
    - Réseaux Énergies réunit plusieurs acteurs de l'énergies (GRTgaz, RTE, Teréga...) dans une démarche de transparence et de pédagogie à l’égard des citoyens, des collectivités territoriales et des acteurs économiques...​
    - Données utilisées : Consommation et production par région, quotidien, annuel par type de client ou filière de production...​


### Les sources
- INSEE https://www.insee.fr/​
    - L'Insee est une direction générale du ministère de l’Économie et des Finances implantée dans l'ensemble du territoire français, indépendante dont l'objectif est la conception, la production et la diffusion des statistiques publiques.​
    - Données utilisées : Population et type de logements par région, départements, communes​


### Les sources
- Bulletin officiel de l'éducation nationale https://www.education.gouv.fr/​
    - Le Bulletin officiel de l'éducation nationale, de la jeunesse et des sports publie des actes administratifs : décrets, arrêtés, notes de service, etc. ​
    - Données utilisées : dates des vacances scolaires par zone 


### Les sources
Sélection des données à récupérer (sources, vocabulaire, type, mises à jour...)
![Tableau des champs par source de données](media/tableau-sources-donnees.png)


### Import et stockage vers le datalake
On ne va pas se mentir, au tout début, on a tout importé en téléchargeant manuellement chaque fichier... mais ce n'était pas idéal pour partager le projet ou mettre à jour les fichiers de consommation, production, de température...


![Gif Back to the future](media/back-to-the-future-this-is-it.gif)
<br/>Puis vint Docker...


### Import et stockage vers le datalake
Depuis un script Python qui télécharge dans un dossier Datalake (utilisé en volume docker)
![Datalake dans un dossier local](media/capture-flux-datalake.jpg)



## Préparation des données<br/>(modélisation​, traitement)
- Modélisation du warehouse
- Traitement initial (V1)
- Traitement optimisé (V2)


![Gif Back to the future](media/back-to-the-future-ready.gif)


### Modélisation du warehouse
![Modélisation du schéma de données attendu dans le warehouse](media/schema-donnees.png)


### Traitement initial (V1)
En utilisant Talend sur des dossiers locaux
![Schéma de l'architecture des traitements de données](media/schema-architecture-v01.jpg)


### Traitement initial (V1)
Exemple #1 d'un job Talend (jointure)
![Exemple de job sur Talend 01](media/capture-talend-02.png)


### Traitement initial (V1)
Exemple #2 d'un job Talend (dépivoter)
![Exemple de job sur Talend 02](media/capture-talend-01.png)


### Traitement initial (V1)
Résultat dans MySQL Workbench
![BDD dans MySqL Workbench](media/capture-mysql-workbench.png)


### Traitement initial (V1) 
Problématiques rencontrées avec ce traitement : 
- Partage et collaboration difficile : 
    - Export/import de jobs Talend
    - Pas d'utilisation de Github
- Configuration de Talend assez lourde au regard du type de traitement nécessaire


![Gif Back to the future](media/back-to-the-future-amazing.gif)
<br/>Puis vint Docker...


### Traitement optimisé (V2)
❤️ Python + Docker + Github ❤️
![Schéma de l'architecture du traitement optimisé v2](media/schema-architecture-v02.jpg)


### Traitement optimisé (V2)
Utilisation d'un fichier config.txt pour  y stocker les chemins des dossiers, les codes d'accès à la BDD...
![Import et jointure en python](media/code-configtxt.png)


### Traitement optimisé (V2)
Utilisation d'un fichier config.txt pour  y stocker les chemins des dossiers, les codes d'accès à la BDD...
![Import et jointure en python](media/code-import-configtxt.png)


### Traitement optimisé (V2)
L'exemple Talend #1 en Python
![Import et jointure en python](media/code-talend-01-en-python.png)


### Traitement optimisé (V2)
L'exemple Talend #2 en Python
![dépivotage en python](media/code-talend-02-en-python.png)



## Data visualization
- Import des données
- Réalisation


### Importation des données
Dans Qlik
![Schéma des données après importation dans Qlik](media/capture-schema-donnees-qlik.png)


### Importation des données
Dans PowerBI
![Schéma des données après importation dans PowerBI](media/capture-schema-donnees-powerbi.png)



## Retours d'expérience


### Stockage des données
Le datalake dans un bucket Google Cloud
![Datalake dans un bucket Google Cloud](media/capture-bucket-datalake.png)



![Gif Back to the future](media/back-to-the-future-on-schedule.gif)
## Fin