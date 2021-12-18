import folium  


points=[]
lat=[]
long=[]

print("Veuillez saisir 3 coordonnées géographiques :")

print("Latitudes :")
for j in range(3):
    lat.append(float(input()))

print("Longitudes :")
for j in range(3):
    long.append(float(input()))

print(lat)
#lat=[-7.9981267,36.692974,2.387625]
#long=[-34.9082027,3.001217,34.811026]

world = folium.Map(
    zoom_start=2,
    location=[13.133932434766733, 16.103938729508073])


for i in range(len(lat)):
    points.append([lat[i],long[i]]) 


folium.Polygon(locations=points, color='#FF0000', fill_color='blue', weight=5).add_to(world)
world
