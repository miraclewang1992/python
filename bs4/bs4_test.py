__author__ = 'doshest'
import requests
from bs4 import BeautifulSoup
html_test="""
<div>
    <p class='p1'>
        <a href='index1'>index1</a>
        <a href='index2'>index2</a>
        <a href='index3'>index3</a>
        <a href='index4'>index4</a>
        <a href='index5'>index5</a>
    </p>
    <p class='p2'>
        <a href='index1'>index1</a>
        <a href='index2'>index2</a>
        <a href='index3'>index3</a>
        <a href='index4'>index4</a>
        <a href='index5'>index5</a>
    </p>
    <p  class='p3'>
        <a href='index1'>index1</a>
        <a href='index2'>index2</a>
        <a href='index3'>index3</a>
        <a href='index4'>index4</a>
        <a href='index5'>index5</a>
    </p>
</div>
"""
soup = BeautifulSoup(html_test,'html.parser')
j=0
for tmp in soup.div.children:
    print('-------------',j)

    print(tmp)
    j=j+1
print(list(soup.div.children)[5])

