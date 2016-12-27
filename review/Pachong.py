__author__ = 'doshest'
import requests
from bs4 import BeautifulSoup
csdn_text=requests.get("http://tieba.baidu.com/f?kw=java&fr=ala0&tpl=5").text
bs4_text=BeautifulSoup(csdn_text,"html.parser")
li_result=bs4_text.find_all(name='a',attrs={'class':'j_th_tit '})
#print(li_result)
list_href=[]
list_href_lambda=list(map(lambda x: x.get('href'),li_result))
print(list_href_lambda)
for href in li_result:
    list_href.append(href.get('href'))
print(list_href)

# make sure the development packages of libxml2 and libxslt are installed