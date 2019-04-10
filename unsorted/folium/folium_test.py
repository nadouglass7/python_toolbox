import folium

a_map = folium.Map(location=[45.5236, -122.6750], tiles='Mapzen Refill',
           zoom_start=13)
a_map.save('a_map.html')