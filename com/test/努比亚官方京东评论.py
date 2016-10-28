__author__ = 'doshest'
import requests
import json
def get_comments(url):
    result=requests.get('http://sclub.jd.com/comment/productPageComments.action?productId=3435053&score=0&sortType=3&page=6&pageSize=10&callback=fetchJSON_comment98vv1072')
    # print(result.text)
    length=int(len('fetchJSON_comment98vv1072('))
    # print(length)
    total_length=int(len(result.text))
    comments=result.text[length:-2]
    # print(comments)
    a=json.loads(comments)


    print(a['comments'])
get_comments('')

