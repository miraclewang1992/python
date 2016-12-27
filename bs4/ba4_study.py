__author__ = 'doshest'
from bs4 import BeautifulSoup
#html定义的可以为多个值，返回的是list
css_soup = BeautifulSoup('<p class ="body chekou"></p>','html.parser')
print(css_soup.p['class'])
#html定义的属性只能为一个值，返回的是string
id_soup =BeautifulSoup('<p id ="body chekou">1</p>','html.parser')
print(id_soup.p['id'])
#强tag换成字符串时，多值属性会合并成为一个值
rel_soup = BeautifulSoup('<p>back to the <a rel="index">homepage</a></p>','html.parser')
print(rel_soup.a['rel'])
rel_soup.a['rel']=['index','contents']
print(rel_soup.a['rel'])
print(rel_soup.a.string)

print(id_soup.p.string)

#注释及特殊字符串
markup ='<b><!--hey, buddy,want to buy a used parser?--></b>'
soup = BeautifulSoup(markup,'html.parser')
content =soup.b.string
print(type(content))
print(content)
print(soup.b.prettify())


html_doc = """
<html><head><title>The Dormouse's story</title></head>
<p class="title"><b>The Dormouse's story1<a href='index'>calss</a></b><b>The Dormouse's story2</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc,'html.parser')
p_tag = soup.p
print('-----',p_tag,'++++')
p_contents =p_tag.contents
print('----',p_contents[0].string,'---')
for tag in p_tag.children:
    print(tag.string,'=====')
for tag in p_tag.descendants:
    print(tag.string,'--descendants')
print('tanslate into list',list(p_tag.descendants))
print('num of list',len(list(p_tag.descendants)))
print(list(p_tag.descendants)[2].get('href'),'+++++++++')
#兄弟节点
sibling_soup=soup.p
print('next sibling=======',sibling_soup.next_sibling)
print('======================================')


