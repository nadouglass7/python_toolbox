TheFile=open("/Users/nathanieldouglass/Desktop/WOF-Language/Countries/Original/WOF_Countries.geojson","r")                       #opens the Json file previously created in Pt. 1 of the script
TheOutput=open("/Users/nathanieldouglass/Desktop/Labels.geojson","w")                      #opens new .csv file to be writen

try:                                                               #try function to test for bugs
	TheJson=TheFile.read()                                              #creates a variable and assigns a read function to the Json file to read the contents
	#TheOutput.write("OID"+","+"Lat"+","+"Long"+","+"Name"+"\n")                     #Writes a header line for each row


	#print("OID"+","+"Lat"+",""Long"+","+"Name"+"\n")                               #prints header lines to test

###------------------Start Keys--------------------------------##  

	OIDKeyStart="(1:"                                     #key for locating characters before the occurance ID
	OIDKeyEnd=":"

	LatKeyStart="decimalLatitude\":\""                                  #Latitude key
	LatKeyEnd="\",\"geo"

	LongKeyStart="decimalLongitude\":\""                                #Longitude Key
	LongKeyEnd="\",\"common_name" 

	NameKeyStart="\"Observation\",\"name\":\""                          #Name Key
	NameKeyEnd="\",\"decimalLongitude"    


except Exception as TheException:                                 #If error occurs, messege will be displayed in Debug
	print("sorry, error occured while reading Json file"+"  "+format(TheException))


try:                                                              #try function to test index and parcing 

###------------------Start Index-------------------------------##
	OIDIndexStart=0                                                      #index value set to 0 for each key. This starts the loop for each find function                                      
	OIDIndexEnd=0                                                        #
	LatIndexStart=0                                                      #
	LatIndexEnd=0                                                        #
	LongIndexStart=0                                                     #
	LongIndexEnd=0                                                       #
	NameIndexStart=0                                                     #
	NameIndexEnd=0                                                       #    

	##-----------------Start Index Loop---------------------------##  
	while (OIDIndexStart!=-1) and (LatIndexEnd!=-1):                     #Start while loop if index starts with 0 
		OIDIndexStart=TheJson.find(OIDKeyStart,OIDIndexEnd)                       #Resets value of OID start index to a find function of the value of OID key and End index (these two lines help reset values after the first loop)
		OIDIndexEnd=TheJson.find(OIDKeyEnd,OIDIndexStart)                         #Resets value of End index to be a find function between End key and the new Start index

		LatIndexStart=TheJson.find(LatKeyStart,LatIndexEnd)                       #Reset Index for Latitude
		LatIndexEnd=TheJson.find(LatKeyEnd, LatIndexStart)

		LongIndexStart=TheJson.find(LongKeyStart,LongIndexEnd)                    #Reset Index for Longitude
		LongIndexEnd=TheJson.find(LongKeyEnd,LongIndexStart)

		NameIndexStart=TheJson.find(NameKeyStart,NameIndexEnd)                    #Reset Index for Name
		NameIndexEnd=TheJson.find(NameKeyEnd,NameIndexStart)        

		if (OIDIndexStart!=-1) and (LatIndexEnd!=-1):                             #If statement for Index
			#OIDIndexEnd=TheJson.find(OIDKeyEnd,OIDIndexStart+len(OIDKeyStart))          #Sets Index value to Start and end index plus length of the start key
			#LatIndexEnd=TheJson.find(LatKeyEnd,LatIndexStart+len(LatKeyStart))          #
			#LongIndexEnd=TheJson.find(LongKeyEnd,LongIndexStart+len(LongKeyStart))      #
			#NameIndexEnd=TheJson.find(NameKeyEnd,NameIndexStart+len(NameKeyStart))      #


			OID=TheJson[OIDIndexStart+len(OIDKeyStart):OIDIndexEnd]                     #OID value set to represent characters inbetween the start and end index
			Latitude=TheJson[LatIndexStart+len(LatKeyStart):LatIndexEnd]                #
			Longitude=TheJson[LongIndexStart+len(LongKeyStart):LongIndexEnd]            #
			Name=TheJson[NameIndexStart+len(NameKeyStart):NameIndexEnd]                 #

			TheOutput.write(OID+","+Latitude+","+Longitude+","+Name+"\n")                        #Writes each line of the the output .csv for values collected in the loop                
			print(OID+","+Latitude+","+Longitude+","+Name+"\n")                                  #prints results for testing


			## This causes the loop to start AFTER collected values
			OIDIndexStart=OIDIndexEnd+len(OIDKeyEnd)                                    #Resets value of start indexes to be after the last index and lenghth of end index key
			LatIndexStart=LatIndexEnd+len(LatKeyEnd)                                    #
			LongIndexStart=LongIndexEnd+len(LongKeyEnd)                                 #
			NameIndexStart=NameIndexEnd+len(NameKeyEnd)                                 #


except Exception as TheException:                                 #Exception function for if error occurs
	print("sorry, error occured"+format(TheException))

TheFile.close()                                          #Closes the file