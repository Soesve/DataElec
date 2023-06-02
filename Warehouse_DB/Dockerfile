FROM postgres:latest

# Créer un répertoire de travail dans le conteneur
WORKDIR /usr/src/app

# Copier les scripts SQL dans le conteneur
COPY init.sql /docker-entrypoint-initdb.d/

# Exposer le port par défaut de Postgres
EXPOSE 5432

# Définir les variables d'environnement pour la configuration de la base de données
ENV POSTGRES_USER dataelec
ENV POSTGRES_PASSWORD jL2wtvNMa6Ttkd
ENV POSTGRES_DB dataelec

# Exécuter les commandes supplémentaires si nécessaire
# Par exemple, pour installer des extensions PostgreSQL :
# RUN apt-get update && apt-get install -y postgresql-contrib

# CMD et ENTRYPOINT sont déjà configurés dans l'image de base (postgres)

