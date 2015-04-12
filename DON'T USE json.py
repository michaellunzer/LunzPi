#!/usr/bin/python
import urllib
import json
url = "http://api.thingspeak.com/channels/15486/feed.json?key=1X5610SMHNUIF9XL"
response = urllib.urlopen(url)
data = json.loads(response.read())
print data
