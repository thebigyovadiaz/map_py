# Import Library
import folium

# Create base map
map_geo = folium.Map(location=[37.296933, -121.9574983], zoom_start=8)

# Add Marker
folium.Marker(
    location=[37.4074687, -122.086669],
    popup="Google HQ",
    icon=folium.Icon(color='orange')
).add_to(map_geo)

# Save the map
map_geo.save("map2.html")