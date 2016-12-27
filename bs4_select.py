__author__ = 'doshest'
import requests
from bs4 import BeautifulSoup
url='http://tieba.baidu.com/f?kw=java&fr=ala0&tpl=5'
result=requests.get(url)
text=result.text
#print(text)
soup=BeautifulSoup(result.text,'html.parser')
dic_a_title=soup.find_all(name='a',attrs={'class':'j_th_tit'})
array_link=[]
array_title=[]
dic_content={}
for link in dic_a_title:
    array_link.append(link.get('href'))

    array_title.append(link.get('title'))
print(array_link)
dic_content=dict(zip(array_link,array_title))
print(dic_content)
print(dic_a_title)
# url_tieba=soup.select('a.j_th_tit ')
# print(url_tieba)



