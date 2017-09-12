__author__ = 'doshest'
import  operator
dic_test ={
    'name':'xiaoming',
    'age':None
}
print(dic_test.get('age'))
print(dic_test['name'],'============')
print(dic_test)

for name,value in dic_test.items():
    print(name,value)
x = {1:1,2:3,2:2,3:2}
sorted_x =sorted(x.items(),key=operator.itemgetter(1))
print(sorted_x)


for tmp in range(1,1):
    print(tmp)