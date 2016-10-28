__author__ = 'doshest'
import pymysql
import pickle
import redis
class user:
    def __init__(self,id,username,password):
        self.id=id
        self.username=username
        self.password=password

try:

  r=redis.Redis(host='127.0.0.1',port=6379,db=1)
#获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
  conn=pymysql.connect(host='localhost',user='database',passwd='root',db='lesson',port=3306,charset='utf8')
  cur=conn.cursor()#获取一个游标
  cur.execute('select * from user limit 10')
  data=cur.fetchall()
  for d in data :
    #注意int类型需要使用str函数转义
   print("ID: "+str(d[0])+'  名字： '+d[1])
   u =user(d[0],d[1],d[2])
   r.set(d[0],u.password)
  cur.close()#关闭游标
  conn.close()#释放数据库资源
except  Exception :print("发生异常")





