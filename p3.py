# save-webpage.py

import urllib.request, urllib.error, urllib.parse

url = 'https://s3.amazonaws.com/tcmg476/http_access_log'

response = urllib.request.urlopen(url)
webContent = response.read().decode('UTF-8')

f = open('access.log', 'w')
f.write(webContent)
f.close