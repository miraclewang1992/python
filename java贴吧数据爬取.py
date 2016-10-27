__author__ = 'doshest'
import  requests
from bs4 import BeautifulSoup
import  re
class Tool:
    #去除img标签,7位长空格
    removeImg = re.compile('<img.*?>| {7}|')
    #删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')
    #把换行的标签换为\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    #将表格制表<td>替换为\t
    replaceTD= re.compile('<td>')
    #把段落开头换为\n加空两格
    replacePara = re.compile('<p.*?>')
    #将换行符或双换行符替换为\n
    replaceBR = re.compile('<br><br>|<br>')
    #将其余标签剔除
    removeExtraTag = re.compile('<.*?>')
    def replace(self,x):
        x = re.sub(self.removeImg,"",x)
        x = re.sub(self.removeAddr,"",x)
        x = re.sub(self.replaceLine,"\n",x)
        x = re.sub(self.replaceTD,"\t",x)
        x = re.sub(self.replacePara,"\n    ",x)
        x = re.sub(self.replaceBR,"\n",x)
        x = re.sub(self.removeExtraTag,"",x)
        #strip()将前后多余内容删除
        return x.strip()

def get_java_tieba(url,name,key,value):
    result=requests.get(url);
    #print(result.text)
    soup=BeautifulSoup(result.text,'html.parser')
    values={}
    values[key]=value
    print(values)
    content=soup.find_all(name,attrs=values)
    tool = Tool()
    i=0
    for tmp in content:
        content[i]=tool.replace(tmp.text)
        i=i+1
    return content

url='http://tieba.baidu.com/f?kw=java&fr=ala0&tpl=5'
name='a'
key="class"
value="j_th_tit"
print(get_java_tieba(url,name,key,value))

