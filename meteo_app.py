import streamlit as st
import requests
from datetime import datetime
import os
from dotenv import load_dotenv
from streamlit_folium import folium_static
import folium

load_dotenv()

api_key = os.getenv("API_KEY")
url = "https://api.openweathermap.org/data/2.5/weather"
villes = ["Paris", "Marseille", "Lyon", "Toulouse", "Nice", "Nantes", "Montpellier", "Strasbourg", "Bordeaux", "Lille", "Rennes", "Reims", "Le Havre", "Saint-Étienne", "Toulon", "Grenoble", "Dijon", "Angers", "Nîmes", "Villeurbanne"]

def get_meteo_france(ville : str)-> dict:
    """
        Récupère les informations météorologiques pour une ville donnée en utilisant l'API OpenWeatherMap.
        Args:
            ville (str): Nom de la ville pour laquelle récupérer les informations météorologiques.
        Returns:
            dict: Un dictionnaire contenant les informations météorologiques pour la ville donnée.
    """
    params = {
        "q": ville + ",FR",
        "appid": api_key,
        "units": "metric", 
        "lang": "fr"
    }
    
    reponse = requests.get(url, params=params)
    if reponse.status_code == 200:
        rep_json = reponse.json()
        meteo_france = {
            "Ville": ville,
            "Température actuelle C°": rep_json["main"]["temp"],
            "Température ressentie C°": rep_json["main"]["feels_like"],
            "Température minimale C°": rep_json["main"]["temp_min"],
            "Température maximale C°": rep_json["main"]["temp_max"],
            "Pression atmosphérique": rep_json["main"]["pressure"],
            "Humidité": rep_json["main"]["humidity"],
            "Vitesse du vent km/h": rep_json["wind"]["speed"],
            "Direction du vent en ° ": rep_json["wind"]["deg"],
            "Lever du soleil": datetime.fromtimestamp(rep_json["sys"]["sunrise"]).strftime('%Y-%m-%d %H:%M:%S'),
            "Coucher du soleil": datetime.fromtimestamp(rep_json["sys"]["sunset"]).strftime('%Y-%m-%d %H:%M:%S'),
            "Latitude": None,
            "Longitude": None
        }
        if "coord" in rep_json:
            meteo_france["Latitude"] = rep_json["coord"]["lat"]
            meteo_france["Longitude"] = rep_json["coord"]["lon"]
        return meteo_france
    else:
        print(reponse.status_code)

def infos_villes(villes: list) -> list:
    """
        Récupère les informations de base (nom, latitude et longitude) pour une liste de villes en utilisant la fonction get_meteo_france.
        Args:
            villes (list): Liste des noms de villes pour lesquelles récupérer les informations.
        Returns:
            list: Une liste de dictionnaires contenant les informations de base pour chaque ville.
    """
    infos = []
    for ville in villes:
        mf = get_meteo_france(ville)
        infos.append({
            "name": mf["Ville"],
            "latitude": mf["Latitude"],
            "longitude": mf["Longitude"]
        })
    return infos

def generer_popup(meteo_popup : dict) -> str:
    """
        Génère le contenu HTML d'un popup pour afficher les informations météorologiques d'une ville.
        Args:
            meteo_popup (dict): Un dictionnaire contenant les informations météorologiques d'une ville.
        Returns:
            str: Une chaîne de caractères HTML formatée avec les informations météorologiques de la ville.
    """
    contenu = f"""
    <b>{meteo_popup['Ville']}</b><br>
    Température actuelle: {meteo_popup['Température actuelle C°']}°C<br>
    Température ressentie: {meteo_popup['Température ressentie C°']}°C<br>
    Température minimale: {meteo_popup['Température minimale C°']}°C<br>
    Température maximale: {meteo_popup['Température maximale C°']}°C<br>
    Pression atmosphérique: {meteo_popup['Pression atmosphérique']}hPa<br>
    Humidité: {meteo_popup['Humidité']}%<br>
    Vitesse du vent: {meteo_popup['Vitesse du vent km/h']}km/h<br>
    Direction du vent: {meteo_popup['Direction du vent en ° ']}°<br>
    Lever du soleil: {meteo_popup['Lever du soleil']}<br>
    Coucher du soleil: {meteo_popup['Coucher du soleil']}<br>
    """
    return contenu

ville_selectionnee = st.sidebar.selectbox("Sélectionnez une ville en France", villes)
meteo_france = get_meteo_france(ville_selectionnee)

st.write(f"### La Méteo à {meteo_france['Ville']} :")
st.write(f"Température actuelle: {meteo_france['Température actuelle C°']}°C")
st.write(f"Température ressentie: {meteo_france['Température ressentie C°']}°C")
st.write(f"Température minimale: {meteo_france['Température minimale C°']}°C")
st.write(f"Température maximale: {meteo_france['Température maximale C°']}°C")
st.write(f"Pression atmosphérique: {meteo_france['Pression atmosphérique']}hPa")
st.write(f"Humidité: {meteo_france['Humidité']}%")
st.write(f"Vitesse du vent: {meteo_france['Vitesse du vent km/h']}km/h")
st.write(f"Direction du vent: {meteo_france['Direction du vent en ° ']}", "°")
st.write(f"Lever du soleil: {meteo_france['Lever du soleil']}")
st.write(f"Coucher du soleil: {meteo_france['Coucher du soleil']}")

infos = infos_villes(villes) 

st.sidebar.markdown("### Couches de la carte")
infos_des_villes = st.sidebar.checkbox("Afficher des villes", True)

map = folium.Map(location=[46.227638, 2.213749], zoom_start=6)

if infos_villes:
    for info in infos:
        meteo_popup = get_meteo_france(info["name"])
        folium.Marker(
            [info["latitude"], info["longitude"]],
            popup=folium.Popup(generer_popup(meteo_popup), max_width=300)
        ).add_to(map)

folium_static(map)
