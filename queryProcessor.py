def processQuery(query,data):
	
	finalQuery=query
	for item in data:
		finalQuery=finalQuery.replace("?",item,1)
	return (finalQuery)