#getting data 
#sudo pip install requests
from urllib2 import Request, urlopen
from urllib import urlencode, quote_plus
url = 'https://gw.its.yale.edu/soa-gateway/buildings/feed' 
queryParams = '?' + urlencode({ quote_plus('apikey') : 'l74b29a694df8f43de9df37c8b6554f0d8',quote_plus('type') : 'json' }) 
request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()
#print response_body[0]





#converting from json to python dictionary
import json
json1_data = json.loads(response_body)

#sudo pip install mysql-connector-python
#connecting to msql
import mysql.connector
from mysql.connector import errorcode


cnx = mysql.connector.connect(user='root', password='Shreya1997$')
cursor = cnx.cursor()
DB_NAME = 'dbfinalproj'
cursor.execute("use dbfinalproj")
#function to create database
#taken from https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-transaction.html
import csv
import os

data = json1_data["ServiceResponse"]["Buildings"]
for i in range(0, len(data)): 
	#print data[i], k 
	tempdict = {}
	for k in data[i]: 
		print data[i][k]
		if data[i][k] != []: 
			tempdict[k] = data[i][k].encode("utf-8")
		else: 
			tempdict[k] = []
	data[i] = tempdict
	#data[i] = {k = data[i][k].encode("utf-8") for k in data[i]}
keys = data[0].keys() #bad coding technique
#['Name','Hour','Time']
print keys
dirname = os.path.dirname(os.path.abspath("/Users/sanjeevd/Documents/introtodb/fproj/buildings.tsv")) #absolute path bad
#print os.path.abspath("."), dirname
tsvfilename = os.path.join(dirname, 'buildings.tsv')
with open(tsvfilename, 'wb') as output_file:
    dict_writer = csv.DictWriter(output_file, keys, delimiter='\t')
    dict_writer.writeheader()
    dict_writer.writerows(data)  




