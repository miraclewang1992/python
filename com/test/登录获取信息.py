__author__ = 'doshest'
import requests
from bs4 import BeautifulSoup
p={'userName':'13520085340','passWord':'123456'}
def login(p):
    s=requests.session();
    s.post('http://www.yqscpt.com/cloud-platform-x3/common/csoet/user/booLogin.ht',data=p)
    r=s.get('http://www.yqscpt.com/cloud-platform-x3/common/csoet/home/page.ht')
    return r.text
def get_title(content,name,values):
    soup =BeautifulSoup(content,'html.parser')
    soup.find_all(name,attrs=values)



