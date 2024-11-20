import requests


def obtenir_utilisateurs_aleatoires(total=1000):
    utilisateurs = []  # Liste pour stocker les utilisateurs récupérés
    taille_lot = 500  # Nombre maximal d'utilisateurs récupérables par requête
    url = "https://randomuser.me/api/"  # URL de l'API

    try:
        # Récupération des utilisateurs par lots
        for debut in range(0, total, taille_lot):
            taille_actuelle = min(taille_lot, total - debut)  # Taille du lot actuel
            # Effectuer une requête GET avec les paramètres nécessaires
            response = requests.get(url, params={"results": taille_actuelle, "nat": "fr"})
            response.raise_for_status()  # Génère une exception si la requête échoue
            donnees = response.json()  # Convertit la réponse en JSON

            # Extraire les informations des utilisateurs de la réponse
            for utilisateur in donnees['results']:
                prenom = utilisateur['name']['first']
                nom = utilisateur['name']['last']
                age = utilisateur['dob']['age']
                ville = utilisateur['location']['city']
                pays = utilisateur['location']['country']

                # Ajouter les informations formatées à la liste
                utilisateurs.append(
                    f"Prénom : {prenom}\nNom : {nom}\nÂge : {age}\nVille : {ville}\nPays : {pays}\n"
                )
        # Retourner les utilisateurs formatés sous forme de chaîne
        return "\n".join(utilisateurs)

    except requests.exceptions.RequestException as e:
        # Gestion des erreurs liées aux requêtes HTTP
        return f"Erreur lors de la récupération des utilisateurs : {e}"


if __name__ == "__main__":
    nombre_total = 10  # Nombre d'utilisateurs souhaités (modifiable)
    print(f"Récupération de {nombre_total} utilisateurs aléatoires...")
    utilisateurs = obtenir_utilisateurs_aleatoires(nombre_total)
    print(utilisateurs)
