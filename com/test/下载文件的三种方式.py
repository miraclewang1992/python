__author__ = 'doshest'


import requests
print("downloading with requests")
url = 'http://img.blog.csdn.net/20150815202621411'
r = requests.get(url)
code =open("test.png", "wb")
code.write(r.content)
code.close()