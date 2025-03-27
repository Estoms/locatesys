import streamlit as st
import folium
from streamlit_folium import st_folium

# Fonction pour afficher la carte avec un marqueur
def show_map(lat, lon):
    m = folium.Map(location=[lat, lon], zoom_start=15)
    folium.Marker([lat, lon], popup="Position actuelle", tooltip="Vous êtes ici").add_to(m)
    return m

# Interface Streamlit
st.title("📍 Géolocalisation en Temps Réel")

# Section pour afficher les coordonnées récupérées par JavaScript
st.subheader("Coordonnées récupérées :")
latitude = st.text_input("Latitude", key="latitude")
longitude = st.text_input("Longitude", key="longitude")

# Affichage de la carte si les coordonnées sont disponibles
if latitude and longitude:
    try:
        lat, lon = float(latitude), float(longitude)
        st_folium(show_map(lat, lon), width=700, height=500)
    except ValueError:
        st.error("Coordonnées invalides.")

# Ajout du script JavaScript
st.markdown("""
<script>
function getLocation() {
    if ("geolocation" in navigator) {
        navigator.geolocation.getCurrentPosition(
            (position) => {
                document.getElementById("latitude").value = position.coords.latitude;
                document.getElementById("longitude").value = position.coords.longitude;
                document.getElementById("geo-form").submit();
            },
            (error) => {
                console.error("Erreur de géolocalisation :", error);
            }
        );
    } else {
        alert("Géolocalisation non supportée.");
    }
}
window.onload = getLocation;
</script>
""", unsafe_allow_html=True)
