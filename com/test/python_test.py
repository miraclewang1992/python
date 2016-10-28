__author__ = 'doshest'
import json

import pymysql
var1='hello world'
print('var[0]',var1[0])
print('var[1,5]',var1[1:5])
print('已经更新的字符串',var1[:6]+'rubbooo')
print(var1.find('lo',0,var1.__len__()))
var2='1231'
print(var2.isdigit());
list1=['google1','google2','google3']
list2=[1,2,3,4]
list3=["a","b","c","d"]
print(list1[1])
print(list1[0:2])
print(list1[0:])
print(len(list1))
print(list1[-2:-1])

dict = {'name':'xiaoming','sex':'man'}

print(dict['name'])

print(dict.values())

class MyClass:
    def __init__(self):
        self.a=10
        self.b=20
myClass=MyClass()
myClassDict = myClass.__dict__

print(myClassDict)
myClassRebuild=json.dumps(myClassDict)
print(myClassRebuild)
print('-------------')

