__author__ = 'doshest'
import requests
from bs4 import BeautifulSoup
url ='http://bd.58.com/anguo/ershoufang/?huxingshi=3&huxingting=&huxingwei=&bunengdaikuan=0'
result = requests.get(url)
soup = BeautifulSoup(result.text,'html.parser')
html_tr = soup.find_all('td',attrs={'class':'t'})
for tr in html_tr:
    print(str(tr))
    break

    soup_a = BeautifulSoup(str(tr.a),'html.parser')
    if soup_a.a != None:
       print(soup_a.a['href'])
    soup_div =BeautifulSoup(str(tr),'html.parser')
    print(list(soup_div.td.children)[0])
    # if(list(soup_div.td.children)[5]!=None):
    #     print(list(soup_div.td.children)[5].string,'-------------')

