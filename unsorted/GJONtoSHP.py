import urllib, geojson, gdal, subprocess
File = '/Users/nathanieldouglass/Desktop/WOF-Language/Countries/Original/WOF_Countries.geojson'
#File = '/Users/nathanieldouglass/Desktop/ne_countries/Countries.geojson'
response = open(File, "r")
data = geojson.loads(response.read())

with open('data.geojson', 'w') as f:
	geojson.dump(data, f)

args = ['ogr2ogr', '-f', 'ESRI Shapefile', 'destination_data.shp', 'data.geojson']
data.geojson.close()
subprocess.Popen(args)