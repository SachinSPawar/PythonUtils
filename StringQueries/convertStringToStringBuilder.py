import re
def parseToBuilder(queryString):

    finalQuery = 'StringBuilder query=new StringBuilder();'

    queryString=queryString.replace("query=","")
    queryString=queryString.replace("query+=","")
    queryParts = queryString.split(';')

    queryTokens = []

    for parts in queryParts:
        parts = re.sub(r"([\'][\"][+][a-zA-Z]*[+][\"][\'])", '?', parts )
        queryTokens.append(parts.split('+'))

    for tokens in queryTokens:
        for token in tokens:
            token=token.replace('\r',' ')
            token=token.replace('\n',' ')
            token=token.strip();
            finalQuery=finalQuery+"\n query.append( "+token+" );"
    return finalQuery;
