import streamlit as st  
import folium  
from streamlit.components.v1 import html  

st.title("📍 Géolocalisation en Temps Réel")  

# Injecter du JavaScript pour récupérer la position
js_code = """
<script>
navigator.geolocation.getCurrentPosition(
    (position) => {
        const lat = position.coords.latitude;
        const lon = position.coords.longitude;
        const accuracy = position.coords.accuracy;
        document.getElementById("geo-data").value = `${lat},${lon},${accuracy}`;
    },
    (error) => {
        console.error(error);
    }
);
</script>
"""

# Boîte cachée pour stocker les coordonnées récupérées en JS
st.write('<input type="hidden" id="geo-data">', unsafe_allow_html=True)
html(js_code)

# Lire les données de la boîte cachée
coords = st.text_input("Coordonnées GPS (Lat, Lon, Précision)", key="coords")

# Afficher la carte si les coordonnées sont disponibles
if coords:
    try:
        lat, lon, acc = map(float, coords.split(","))
        st.write(f"🌍 Position détectée : **{lat}, {lon}** (± {acc}m)")

        # Affichage de la carte avec Folium
        m = folium.Map(location=[lat, lon], zoom_start=15)
        folium.Marker([lat, lon], tooltip="Vous êtes ici").add_to(m)
        st.components.v1.html(m._repr_html_(), height=500)

    except Exception as e:
        st.error("Erreur de lecture des coordonnées !")