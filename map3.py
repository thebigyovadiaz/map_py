# Import Library
import folium

# Create base map
mapG = folium.Map(location=[37.296933, -121.9574983], zoom_start=8)

# Add Multiple Marker
for coordinates in [[37.2074687, -122.086669], [37.8199286, -122.4804438]]:
    folium.Marker(
        location=coordinates,
        icon=folium.Icon(color='purple')
    ).add_to(mapG)

# Save the map
mapG.save("map1.html")
