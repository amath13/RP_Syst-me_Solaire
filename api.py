import requests
import json

# Définition de l'URL de l'API
url = "https://api.le-systeme-solaire.net/rest/bodies/?data&exclude&order&page&rowData"

# Les données à envoyer avec la requête (vide dans ce cas)
payload = {}

# Les en-têtes HTTP à inclure dans la requête (vide dans ce cas)
headers = {}

# Envoi de la requête GET à l'URL spécifiée
response = requests.request("GET", url, headers=headers, data=payload)

# Vérification du code de statut de la réponse
if response.status_code == 200:
    # Conversion de la réponse en format JSON
    json_data = response.json()

    # Enregistrement des données JSON dans un fichier
    with open("solar_system_data.json", "w") as json_file:
        json.dump(json_data, json_file, indent=4)

    print("Les données JSON ont été enregistrées avec succès dans le fichier 'solar_system_data.json'.")
else:
    print("La requête a échoué avec le code de statut :", response.status_code)
