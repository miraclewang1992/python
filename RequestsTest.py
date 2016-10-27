__author__ = 'doshest'
import requests
s=requests.session()
p={'userName':'13520085340','passWord':'123456'}
s.post('http://www.yqscpt.com/cloud-platform-x3/common/csoet/user/booLogin.ht',data=p)
r=s.get('http://www.yqscpt.com/cloud-platform-x3/common/csoet/home/page.ht')

# p={'userName':'13520085340','passWord':'123456'}
# r=requests.post('http://www.yqscpt.com/cloud-platform-x3/common/csoet/user/booLogin.ht',data=p)



print(r.text)