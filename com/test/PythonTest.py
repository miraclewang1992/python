__author__ = 'doshest'
import http.client
import json
conn = http.client.HTTPConnection("m.weather.com.cn")
conn.request("GET","/data/101110100.html")
weather=conn.getresponse()
info=weather.read()
print(info)
weatherinfo = json.loads(info)
print( weatherinfo['weatherinfo']['city'])
conn.close()