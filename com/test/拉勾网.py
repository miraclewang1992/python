__author__ = 'doshest'
# from urllib import request, parse
# from bs4 import BeautifulSoup as BS
# import json
# import datetime
# import xlsxwriter
# def read_page(url, page_num, keyword):  # 模仿浏览器post需求信息，并读取返回后的页面信息
#     page_headers = {
#         'Host': 'www.lagou.com',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                       'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
#         'Connection': 'keep-alive'
#         }
#     if page_num == 1:
#         boo = 'true'
#     else:
#         boo = 'false'
#     page_data = parse.urlencode([   # 通过页面分析，发现浏览器提交的FormData包括以下参数
#         ('positionId', 999999),
#         ('pageSize', 500)
#         ])
#     req = request.Request(url, headers=page_headers)
#     page = request.urlopen(req, data=page_data.encode('utf-8')).read()
#     page = page.decode('utf-8')
#     return page
# print(read_page('http://www.lagou.com/interview/experience/byPosition.json',3,'java'))
#
import requests
# result=requests.get('http://www.lagou.com/zhaopin/Java/6/?filterOption=2','1','2')
# print(result.text)

data={
    'positionId':999999,
    'pageSize':500
}

result=requests.post('http://www.lagou.com/interview/experience/byPosition.json',data)
print(result.text)