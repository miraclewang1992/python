__author__ = 'doshest'
from bs4 import BeautifulSoup
import requests
import json

import urllib
header = {
    'Host':'youth.casicloud.com',
    'Origin':'http://youth.casicloud.com',
    'Content-Type': 'application/json; charset=UTF-8',  # 因为是ajax请求，格式为json，这个必须指定
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.87 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest',
    'Connection':'keep-alive',
    'Referer':'http://youth.casicloud.com/youthInno/common/listProject.do',
    'Accept':'application/json,text/javascript, */*; q=0.01',
    'Accept-Language':'zh-CN,zh;q=0.8'}
url = 'http://youth.casicloud.com/youthInno/common/listProject.json?pageNum=1'
data = {'proType':'11181039509240001','proStype':'11280855356090001'}
result = requests.post(url,data=json.dumps({}),headers=header)
# soup =BeautifulSoup(result.text,"html.parser");
# projects =soup.find_all(name="div",attrs='{class:t-Itemslistone}');
print(result.text,'message')
a=json.loads(result.text)

print(a['model']['pros'][1])
# for pro in  projects:
#     pass
#     print(pro)






