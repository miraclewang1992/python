__author__ = 'doshest'
import requests
from bs4 import BeautifulSoup
proxies = {
  "http": "http://61.157.198.66:8080"
}
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36', 'Connection':'keep-alive'}
result = requests.get("http://tieba.baidu.com/f?kw=java&fr=ala0&tpl=5" , proxies=proxies,headers= headers)
soup = BeautifulSoup(result.text,'html.parser');
div_list = soup.find_all("div",attrs={'class':'threadlist_title'})
for div in div_list:
    soup_a = div.find('a')
    print(soup_a['href'])
    print(div.text)