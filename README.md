# RandomPeopleAPI
## **Table des Matières**
1. [Description du Projet](#description-du-projet)  
2. [Installation et Exécution du Projet](#installation-et-exécution-du-projet) 
3. [Utilisation du Projet](#utilisation-du-projet)   
4. [Crédits](#crédits)  
5. [Licence](#licence) 

---

## Description du Projet
RandomPeopleAPI est une application Python qui récupère et affiche des informations sur des utilisateurs générés aléatoirement à l'aide de l'API publique **Random User Generator**. Cette application est idéale pour explorer des données simulées de personnes comme leur prénom, nom, âge, ville, et pays.
Le projet est conçu pour fonctionner facilement dans des environnements locaux ou via Docker, offrant flexibilité et simplicité d'exécution.  

---

## Installation et Exécution du Projet
Pour commencer, clonez ce dépôt sur votre machine locale :
1. **Cloner le dépôt :**
    ```sh
    git clone https://github.com/sim0nR/ue19-lab-05.git  
   cd ue19-lab-05
    ```

2. **Construire l'image Docker :**
Si vous souhaitez utiliser Docker pour exécuter le projet, construisez l'image Docker avec la commande suivante :
    ```sh
    docker build -t random-people-api .
    ```

3. **Exécuter le conteneur Docker :**
Une fois l'image construite, vous pouvez lancer le projet dans un conteneur Docker avec la commande :
    ```sh
    docker run --rm random-people-api
    ```
Le conteneur s'exécutera et interrogera l'API Random User Generator pour récupérer et afficher des informations aléatoires sur des utilisateurs.

---

## Utilisation du Projet
Une fois l'application en cours d'exécution, elle interrogera l'API Random User Generator pour récupérer des données aléatoires sur les utilisateurs.

Informations récupérées :
- Prénom
- Nom
- Âge
- Ville
- Pays

Par défaut, l'application récupère les informations de 10 utilisateurs. Vous pouvez modifier ce nombre en modifiant la variable suivante dans le fichier app.py :
```py
nombre_total = 10  # Modifiez cette valeur pour changer le nombre d'utilisateurs
```

---

## Crédits
Ce projet a été développé par [Simon Roÿen](https://github.com/sim0nR)

---

## Licence
Ce projet est sous licence libre. Vous êtes libre de l'utiliser, de le modifier et de le partager selon vos besoins, sans restriction particulière.