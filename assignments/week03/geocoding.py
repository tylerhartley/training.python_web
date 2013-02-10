import urllib
import urllib2
from pprint import pprint
import json 

base = 'http://maps.googleapis.com/maps/api/geocode/json'
addr = '1325 4th Ave, Seattle, WA 98101'
data = {'address': addr, 'sensor': 'false' }

query = urllib.urlencode(data)
print data
print json.dumps(data)
res = urllib2.urlopen('?'.join([base, query]))
response = json.load(res)
pprint(response)