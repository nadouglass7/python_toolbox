#!/usr/bin/env python
import overpy
import geojson
#from geojson import Feature, FeatureCollection, MultiLineString




'''
#---------------------------------#
#        SETUP FILE PATHS
#---------------------------------# 
'''

# output = sys.argv[2]
output = '/Users/nathanieldouglass/python_toolbox/overpass_turbo/output_test/test_line.geojson'

'''
#---------------------------------#
#        SETUP QUERY
#---------------------------------# 
'''


api = overpy.Overpass()

# fetch all ways and nodes
result = api.query("""
    way(44.05488903183197,-123.04877674613975,44.059356678965194,-123.04099084654963) ["highway"];
    (._;>;);
    out body;
    """)




'''
#---------------------------------#
#        WRITE TO FILE
#---------------------------------# 
'''

features = []
for way in result.ways:
    name = way.tags.get("name", "n/a")
    print("Name: %s" % way.tags.get("name", "n/a"))
    
    highway = way.tags.get("highway", "n/a")
    print("  Highway: %s" % way.tags.get("highway", "n/a"))
    print("  Nodes:")
    
    f = []
    #map nodes for each feature
    for node in way.nodes:
        lat = float(node.lat)
        lon = float(node.lon)
        coords = [lat, lon]
        print("    Lat: %f, Lon: %f" % (lat, lon))
        # print("    Lat: " + lat + ", Lon: " + lon)
        #f.append(eval('(' + str(lat) + ',' + str(lon) + ')'))
        f.append(coords)
    print(f)

    features.append(
        geojson.Feature(
            geometry = geojson.MultiLineString(((f))),
            properties = { #leave blank to have striped geojson
                'name': name,
                'highway': highway
            }
        )
    )
    
print(features)

collection = geojson.FeatureCollection(features)

type = '''
       "type": "FeatureCollection",
       "name": "Lines" 
'''

with open(output, "w") as f:
    # f.write('%s' % collection))
    geojson.dump(collection, f)
f.close()