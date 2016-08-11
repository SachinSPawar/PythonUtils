import convertStringToBuilder as converter
rawQuery=open('rawQuery','r').read();

finalQuery=converter.parseToBuilder(rawQuery);

w=open('output.txt','w')

w.write(finalQuery);

print (finalQuery);
