__author__ = 'doshest'
print((lambda x:x*2)(3))
g = lambda x:x
print(g('test1'))

g1 = lambda x,y=10:x+y
print(g1(1))
print(g1(1,100))

dic ={'a':31,'bc':55,'c':20,'ab':74}
dict = sorted(dic.items(),key=lambda b:b[1],reverse=True)
print(dict)
a = [5,7,6,3,4,1,2]
b = sorted(a,reverse=True)
print(a)
print(b)