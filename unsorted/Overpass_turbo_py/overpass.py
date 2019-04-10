import overpass
api = overpass.API("endpoint=https://overpass.myserver/interpreter")
response = api.Get('node["name"="Salt Lake City"]', responseformat="xml")

print [(feature['tags']['name'], feature['id']) for feature in response['elements']]
[(u'Salt Lake City', 150935219), (u'Salt Lake City', 585370637), (u'Salt Lake City', 1615721573)]
