__author__ = 'doshest'
import  requests
from bs4 import BeautifulSoup
url ='http://inno.casicloud.com/innoCasicloud/common/showAllProjects.do?page=1'
result =requests.get(url)
soup = BeautifulSoup(result.text,'html.parser')
html_divs = soup.find_all('div',attrs={'class':'Tleftt'})
html_choose = soup.findChildren(name='div',attrs={'class':'Tchoose'})
for div in html_divs:
    pass
    #print(div.text.replace('\n',''))
for choose in html_choose:
    print(choose.text)