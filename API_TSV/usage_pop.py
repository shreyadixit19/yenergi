import urllib2
from urllib2 import Request, urlopen
from urllib import urlencode, quote_plus
url = 'https://gw.its.yale.edu/soa-gateway/buildings/feed' 
queryParams = '?' + urlencode({ quote_plus('apikey') : 'l74b29a694df8f43de9df37c8b6554f0d8',quote_plus('type') : 'json' }) 
request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()
import json
json1_data = json.loads(response_body)
buildingsdata = json1_data["ServiceResponse"]["Buildings"]
data = []

for element in buildingsdata: 
	#print buildingsdata
	building = element["BUILDING"]
	print building
	#if building == "3742":
	#	continue
	#getting data 
	#sudo pip install requests
	
	url = 'https://gw.its.yale.edu/soa-gateway/energy/data' 
	queryParams = '?' + urlencode({ quote_plus('apikey') : 'l74b29a694df8f43de9df37c8b6554f0d8',quote_plus('buildingID') : building,quote_plus('rangeStart') : '1997-07-01',quote_plus('rangeEnd') : '2017-08-01',quote_plus('type') : 'xml' }) 
	request = Request(url + queryParams)
	request.get_method = lambda: 'GET'
	try: 
    		response = urllib2.urlopen(request)
	except urllib2.HTTPError, e:
    		print 'HTTPError ', building
		#checksLogger.error('HTTPError = ' + str(e.code))
		continue;
	except urllib2.URLError, e:
    		print 'URLError ', building
		#checksLogger.error('URLError = ' + str(e.reason))
		continue;
	except httplib.HTTPException, e:
		print 'HTTPException ', building
    		#checksLogger.error('HTTPException')
		continue;
	except Exception:
		print 'Exception ', building
    		import traceback
    		#checksLogger.error('generic exception: ' + traceback.format_exc())
		continue;
	
	response_body = response.read()
	import json


	#converting from html to dictionary
	#sudo pip install beautifulsoup4
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(response_body, "html.parser")
	for record in soup.find_all('record'):
		d = {}
		for child in record.children:
			#print child.name, child.contents[0]
			d[child.name.encode("utf-8")] = child.contents[0].encode("utf-8")
		data.append(d)
	print data 
	#break
	#print data



#converting dictionary to tsv
import os
import csv
keys = data[0].keys() #bad coding technique
#['Name','Hour','Time']
print keys
dirname = os.path.dirname(os.path.abspath("/Users/sanjeevd/Documents/introtodb/fproj/usage.tsv")) #absolute path bad
#print os.path.abspath("."), dirname
tsvfilename = os.path.join(dirname, 'usage.tsv')
with open(tsvfilename, 'wb') as output_file:
    dict_writer = csv.DictWriter(output_file, keys, delimiter='\t')
    dict_writer.writeheader()
    dict_writer.writerows(data)
