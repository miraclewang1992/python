__author__ = 'doshest'
import requests
import json
from bs4 import BeautifulSoup
url = 'https://search.jd.com/Search?keyword=%E5%8D%8E%E4%B8%BA&enc=utf-8'
result = requests.get(url)
html_doc = str(result.content,'utf-8')
soup = BeautifulSoup(html_doc,'html.parser')
ul_lis = soup.find_all('li',attrs={'class':'gl-item'})
for li in ul_lis:
    if(li.i != None):
        print(li.i.string)
    if(li.font != None):
        print(li.font.string)
        #print(li.text.replace('\n',''))
    print(li.text.replace('\n',''))

    print('---------------')
#print(html_doc)
#print(soup.get_text)