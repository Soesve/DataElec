FROM python:latest

# Créer un répertoire de travail dans le conteneur
WORKDIR /usr/src/app

# Copier les fichiers de script Python dans le conteneur
COPY script*.py /usr/src/app/

# Installer les dépendances Python à partir du fichier requirements.txt (si nécessaire)
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

# Exécuter le script Python au démarrage du conteneur
CMD [ "python", "script.py" ]
