![Gif Back to the future](media/back-to-the-future.gif)
# Projet DataElec


## Sommaire
- Objectifs et organisation du projet
- Collecte des données (sources​, datalake)
- Préparation des données (modélisation​, traitement)
- Analyse​ : data visualisation​
- Pour aller plus loin



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
- Importation des données
- Dataviz


### Importation des données
Dans Qlik
![Schéma des données après importation dans Qlik](media/capture-schema-donnees-qlik.png)


### Importation des données
Dans PowerBI
![Schéma des données après importation dans PowerBI](media/capture-schema-donnees-powerbi.png)


### Dataviz
Première étape : faire un plan !
![Plan dataviz](media/capture-plan-dataviz.png)


### Dataviz
Dashboard - Qlik
![Dataviz Qlik - Ecran 01](media/capture-qlik-ecran-01.png)


### Dataviz
Dashboard - PowerBI
![Dataviz PowerBI - Ecran 01](media/capture-powerbi-ecran-01.png)


### Dataviz
Conso vs météo - Qlik
![Dataviz Qlik - Ecran 02](media/capture-qlik-ecran-02.png)


### Dataviz
Conso vs météo - PowerBI
![Dataviz PowerBI - Ecran 02](media/capture-powerbi-ecran-02.png)


### Dataviz
Conso vs jour de semaine - Qlik
![Dataviz Qlik - Ecran 03](media/capture-qlik-ecran-03.png)


### Dataviz
Conso vs jour de semaine - PowerBI
![Dataviz PowerBI - Ecran 01](media/capture-powerbi-ecran-03.png)


### Dataviz
Conso vs heure de la journée - Qlik
![Dataviz Qlik - Ecran 04](media/capture-qlik-ecran-04.png)


### Dataviz
Conso vs heure de la journée - PowerBI
![Dataviz PowerBI - Ecran 01](media/capture-powerbi-ecran-04.png)


### Dataviz
Conso vs type de client - Qlik
![Dataviz Qlik - Ecran 05](media/capture-qlik-ecran-05.png)


### Dataviz
Conso vs type de client - PowerBI
![Dataviz PowerBI - Ecran 01](media/capture-powerbi-ecran-05.png)


### Dataviz
Conso vs logements - Qlik
![Dataviz Qlik - Ecran 06](media/capture-qlik-ecran-06.png)


### Dataviz
Conso vs logements - PowerBI
![Dataviz PowerBI - Ecran 01](media/capture-powerbi-ecran-06.png)


### Dataviz
Production  - Qlik
![Dataviz Qlik - Ecran 07](media/capture-qlik-ecran-07.png)


### Dataviz
Production - PowerBI
![Dataviz PowerBI - Ecran 01](media/capture-powerbi-ecran-07.png)


### Dataviz
Imports/Exports - Qlik
![Dataviz Qlik - Ecran 08](media/capture-qlik-ecran-08.png)


### Dataviz
Imports/Exports - PowerBI
![Dataviz PowerBI - Ecran 01](media/capture-powerbi-ecran-08.png)



## Pour aller plus loin
- Retours d'expériences
- Pistes d'optimisation


### Retours d'expériences
- Utiliser tout de suite Docker + Github = 🫶
- Qlik vs PowerBI : 
    - Importation des données : avantage à PowerBI pour la configuration des clés (et clés secondaires)
    - Visuel cartes géographiques : avantage à Qlik pour la configuration du visuel
    - Visuel histogrammes : avantage à Qlik pour le choix manuel de l'ordre des données
    - Calcul de la corrélation : avantage à Qlik qui a une formule dédiée
    - ...


### Pour aller plus loin
Optimisations : 
- Conditionner le script d'import à la date de dernière mise à jour du fichier en ligne vs celui en local
- Utiliser le cloud (voir diapos suivantes)


### Pour aller plus loin
Utiliser Google Cloud : Stocker le datalake dans un bucket
![Datalake dans un bucket Google Cloud](media/capture-bucket-datalake.png)


### Pour aller plus loin
Utiliser Google Cloud : Faire le traitement via DataProc et BigQuery
![Datalake dans un bucket Google Cloud](media/capture-bucket-datalake.png)



![Gif Back to the future](media/back-to-the-future-on-schedule.gif)
## Fin