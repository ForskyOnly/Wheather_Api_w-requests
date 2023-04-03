# Projet : Découverte de la librairie requests
Version 1.0

## Contexte du projet

Vous êtes des data scientists juniors qui cherchent à se familiariser avec la manipulation des API et la récupération de données en ligne. Vous devez commencer par découvrir les différents types de requêtes HTTP (GET, POST, etc.) et monter en compétences sur la librairie Requests en travaillant sur un notebook. Votre objectif est d'interagir avec l'API OpenWeatherMap pour récupérer et analyser les données météorologiques.

Récupérer les informations suivantes et stocker les dans un DataFrame (pandas) pour 20 villes françaises :

- Température actuelle
- Température ressentie
- Température minimale et maximale
- Pression atmosphérique
- Humidité
- Vitesse du vent
- Direction du vent
- Lever du soleil (Attention à bien convertir en information compréhensible pour un humain)
- Coucher du soleil (Attention à bien convertir en information compréhensible pour un humain)


Vous devez récupérer les informations actuelles. Les informations seront d'abord stockés dans un DataFrame et ensuite vous exporterez ce dataframe dans un fichier csv.

## Description du Projet

Ce projet a été réalisé lors de la formation Dev IA Microsoft by Simplon HDF.

Ce projet utilise l'API OpenWeatherMap pour récupérer les informations météorologiques des 20 plus grandes villes de France. Il comprend également une visualisation de ces informations à l'aide de la bibliothèque Folium et une interface Web construite avec Streamlit.

## Fonctionnalités

1. Récupération des informations météorologiques des 20 plus grandes villes de France
2. Sauvegarde des données dans un fichier CSV
3. Stockage des données dans une base de données SQLite
4. Affichage des informations météorologiques sur une carte interactive avec des popups

## Installation

1. Clonez ce dépôt.
2. Installez les dépendances avec `pip install `.
3. Créez un fichier `.env` à la racine du projet et ajoutez-y votre clé d'API OpenWeatherMap sous la forme `API_KEY=votre_clé_d'api`.

## Utilisation

1. Exécutez le fichier `meteo_france.ipynb` pour récupérer les informations météorologiques et les stocker dans un fichier CSV et une base de données SQLite.
2. Exécutez `streamlit run meteo_app.py` pour lancer l'interface Web Streamlit et visualiser les informations météorologiques sur une carte interactive.

## Bibliothèques utilisées

- requests
- pandas
- sqlite3
- dotenv
- streamlit
- folium
- streamlit-folium
- datetime

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.
