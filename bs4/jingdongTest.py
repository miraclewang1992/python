__author__ = 'doshest'
import requests
from bs4 import BeautifulSoup
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="title1"><b>11The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
# url ='http://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&wq=%E6%89%8B%E6%9C%BA&pvid=eubw2nwi.0ehhb4'
# result = requests.get(url)
# html_doc=str(result.content,'utf-8')
soup=BeautifulSoup(html_doc,'html.parser')
phone_li = soup.find_all('a',attrs={'class':'sister'})
tag = soup.p
# for each_tag in tag:
#     print(each_tag.string)
#print(soup.prettify())
#print(soup.get_text())

for phone in phone_li:
    print(phone.text)
    href =phone.get('href')
    # content = phone.string
    # print(content)
    print(href)