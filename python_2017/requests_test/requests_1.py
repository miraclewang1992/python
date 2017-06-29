__author__ = 'doshest'
import  requests;
import  json
from bs4 import BeautifulSoup
url = 'http://youth.casicloud.com/youthInno/common/all/listProject.json?pageNum=1';
headers={
    'Content-Type':'application/json',
   'Accept':'application/json, text/javascript, */*; q=0.01'
}
json_val ={'proType': '11181039509240001'}
result = requests.post(url,data=json.dumps(json_val),headers=headers)
print( result.text)
json_result= json.loads(result.text)
print(json_result['model']['pros'][0]['proId'])

