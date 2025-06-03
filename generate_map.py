import folium
from folium.plugins import MarkerCluster
import json
import os

def load_properties(json_file="properties.json"):
    with open(json_file, "r") as f:
        return json.load(f)

def update_map_from_data(properties, output_file="docs/index.html"):
    if not properties:
        print("No properties found.")
        return

    m = folium.Map(location=[38.0, -97.0], zoom_start=4)
    cluster = MarkerCluster().add_to(m)

    for prop in properties:
        popup = f"""
        <b>Property:</b> {prop['name']}<br>
        <b>Address:</b> {prop['address']}<br>
        <b>Owner:</b> {prop['owner']}<br>
        <b>Acquired:</b> {prop['date']}
        """
        folium.Marker(
            location=[prop['latitude'], prop['longitude']],
            popup=popup
        ).add_to(cluster)

    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    m.save(output_file)
    print(f"Map updated at: {output_file}")

if __name__ == "__main__":
    properties = load_properties()
    update_map_from_data(properties)
