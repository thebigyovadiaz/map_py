# Import Library
import folium
import pandas as pd

# Load data
data = pd.read_csv("Volcanoes_USA.txt")
lat = data['LAT']
lon = data['LON']
elevation = data['ELEV']


# Function to change colors
def color_change(elev):
    if elev < 1000:
        return 'green'
    elif 1000 <= elev < 3000:
        return 'orange'
    else:
        return 'red'


# Create base map
mapG = folium.Map(
    location=[37.296933, -121.9574983],
    zoom_start=5,
    tiles="Mapbox bright"
)

# Plot Markers
for lat, lon, elevation in zip(lat, lon, elevation):
    folium.Marker(
        location=[lat, lon],
        popup=str(elevation)+" m",
        icon=folium.Icon(color=color_change(elevation))
    ).add_to(mapG)

# Save the map
mapG.save("map5.html")
