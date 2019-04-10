with open(r'/Users/nathanieldouglass/Desktop/WOF-Language/Countries/Original/WOF_Countries.geojson', 'r') as infile, open(r'/Users/nathanieldouglass/Desktop/WOF-Language/Countries/Original/Countries_Test.geojson', 'w') as outfile:
		data = infile.read()
		data = data.replace("(1:", " ")
		data2 = data.replace(")", " ")
		outfile.write(data+data2)