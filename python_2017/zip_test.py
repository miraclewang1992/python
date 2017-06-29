__author__ = 'doshest'
a ={'xiaming','hont','bb'}
b = {4,2,3}
for c,d in zip(a,b):
    print(c,d)
print(dict(zip(a,b)))
dic = dict(sorted(dict(zip(a,b)).items(),key=lambda d:d[1]))
print('-----------',dic)
print(dic.items())
e =['xiaming','hont','bb']
f =[1,2,3]

dic1= dict(zip(dic.values(),dic.keys()))
print(dic1)
for g,h in zip(e,f):
    print(g,h)

