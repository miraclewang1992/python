__author__ = 'doshest'
__author__ = 'doshest'
import requests
from urllib import request
from bs4 import BeautifulSoup
p={'username':'manager','password':'Yanshangbei2017'}
# http://cxcyds.zgqncyxd.cn/ym/forms?level=-1&group=-1&jie=0&p=2    704
# http://cxcyds.zgqncyxd.cn/ym/forms?level=-1&group=-1&jie=-1&p=2   695
def gerDescribe(result,r):
    soup = BeautifulSoup(result,'html.parser');
    table_list = soup.find_all(name='table',attrs={"class":"table"})
    for tmp in table_list:
        a_list = soup.find_all(name="a",attrs={"target":"_blank"})
        for a in a_list:
            get_url('http://cxcyds.zgqncyxd.cn'+a['href'],r)

def login(p):
    s=requests.session();
    s.post('http://cxcyds.zgqncyxd.cn/ym/login',data=p)
    for i in range(704):
        r=s.get('http://cxcyds.zgqncyxd.cn/ym/forms?level=-1&group=-1&jie=0&p='+str(i))
        gerDescribe(r.text,s)
    for k in range(695):
        r=s.get('http://cxcyds.zgqncyxd.cn/ym/forms?level=-1&group=-1&jie=-1&p='+str(k))
        gerDescribe(r.text,s)
def downloadFile(url,r,id,name):
    url ='http://cxcyds.zgqncyxd.cn'+url
    result =r.get(url)
    r = r.get(url)
    path = "d://test/"+id+'/'
    mkdir(path)
    with open(path+name, "wb") as code:
         code.write(r.content)
         code.close()

def get_title(content,name,values):
    soup =BeautifulSoup(content,'html.parser')
    soup.find_all(name,attrs=values)

def get_url(url,r):
    result = r.get(url)
    id = getId(url)
    soup = BeautifulSoup(result.text,'html.parser');
    a_list = soup.find_all(name="li",attrs={'class':'list-group-item'})
    if(a_list!=None):
        for a_l in a_list:
            if a_l.a !=None :
                print(a_l.a['href'])
                print(a_l.a.text)
                downloadFile(a_l.a['href'],r,id,a_l.a.text)

def getId(s):
    rx =s.rindex('/');

    return s[rx+1:len(s)]

def mkdir(path):
    # 引入模块
    import os
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")
    isExists=os.path.exists(path)

    # 判断结果
    if not isExists:
        os.makedirs(path)
        print( path+' 创建成功')
        return True
    else:

        print (path+' 目录已存在')
        return False


login(p)

