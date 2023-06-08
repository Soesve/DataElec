FROM python:latest

RUN apt-get update && apt-get install -y nano

# Créer un répertoire de travail dans le conteneur
WORKDIR /usr/src/app

# Installer les dépendances Python à partir du fichier requirements.txt (si nécessaire)
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

# Exécuter le script Python au démarrage du conteneur
CMD [ "bash" ]
