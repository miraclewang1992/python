__author__ = 'doshest'
import  redis
conn =redis.Redis(host='127.0.0.1',port=6379,db=0)
conn.set('name','xiaohong')
print(conn.get('name'))
print(conn.keys())
