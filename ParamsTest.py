__author__ = 'doshest'
#-*- coding:utf-8 -*-
import requests
import pickle
url = 'http://www.baidu.com'
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get(url, params=payload)


s='abc中国'
t=pickle.dumps(s);
print(t)
ss =pickle.loads(t)
print( ss)