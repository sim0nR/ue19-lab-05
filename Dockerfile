# Utiliser l'image officielle Python 3.13.0 comme base
FROM python:3.13.0

# Définir le répertoire de travail à l'intérieur du conteneur
WORKDIR /usr/src/app

# Copier les fichiers `app.py` et `requirements.txt` depuis le système hôte vers le répertoire de travail du conteneur
COPY app.py requirements.txt ./

# Installer les dépendances Python spécifiées dans `requirements.txt`
# L'option `--no-cache-dir` est utilisée pour éviter de stocker des fichiers temporaires inutiles, ce qui réduit la taille de l'image.
RUN pip install --no-cache-dir -r requirements.txt

# Définir la commande par défaut à exécuter lorsque le conteneur démarre
CMD ["python", "app.py"]