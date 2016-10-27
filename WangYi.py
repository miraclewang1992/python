__author__ = 'doshest'
import requests
import urllib
'''
r = requests.get('http://music.163.com/#/playlist?id=474564716')
print(r.status_code)

r.json()
print(r.json())
print(r.text)
arr = r.json()['result']['tracks']
for i in range(10):
     name=str(i+1)+' '+arr[i][name]+'.mp3'
     link=arr[i]['mpaUrl']
     #urllib.request.urlretrieve(link,'网易云音乐\\'+name)
     print(name+'下载完成')
'''

r = requests.get('http://music.163.com/api/playlist/detail?id=3779629')
print(r.text)
arr = r.json()['result']['tracks'] # 共有100首歌

for i in range(100):
    name = str(i+1) + ' ' + arr[i]['name'] + '.mp3'
    link = arr[i]['mp3Url']
    print(link)
    urllib.request.urlretrieve(link, '网易云音乐\\' + name)
#urllib.request.urlretrieve('http://221.12.58.114:8666/file/4da99418ffab6a5d949d56f1cd02b8a4?sdk_id=258&task_id=2658094855345012910&business_id=4097&bkt=p3-00006b0826e827e425ec99798d22297cf8f8&xcode=054ecb29220d5153c14aadc354d88514721402e9e89d076b9717ec4418c70769&fid=639943504-250528-1120110477002242&time=1477038770&sign=FDTAXGERLBH-DCb740ccc5511e5e8fedcff06b081203-yLDYR4F4hYJg7kX9aXoZUSw9LeI%3D&to=sd&fm=Yan,B,U,nc&sta_dx=216363904&sta_cs=34782&sta_ft=mp4&sta_ct=5&sta_mt=5&fm2=Yangquan,B,U,nc&newver=1&newfm=1&secfm=1&flow_ver=3&pkey=00006b0826e827e425ec99798d22297cf8f8&sl=74383438&expires=8h&rt=pr&r=278146365&mlogid=6834681016931031478&vuk=639943504&vbdid=1993803560&fin=EP07.mp4&fn=EP07.mp4&slt=pm&uta=0&rtype=1&iv=0&isw=0&dp-logid=6834681016931031478&dp-callid=0.1.1&sdk_id=258&csl=176&csign=uzKSHmq%2B4Wt3YeYWyPnnAdRvOWs%3D', '网易云音乐\\' + 'shipin.mp4')


