import queryProcessor as qp

querySheet=open("/home/sis/python/templateQuery/query.txt","r")
query=querySheet.read()

dataSheet=open("/home/sis/python/templateQuery/data.txt","r")
data=dataSheet.read().split("\n")[:-1];

outputSheet=open("/home/sis/python/templateQuery/output.txt","a")

for dataSet in data:
	finalQuery=qp.processQuery(query,dataSet.split(','))
	outputSheet.write(finalQuery+"\n")
