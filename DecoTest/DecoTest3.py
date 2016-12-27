__author__ = 'doshest'
def deco(func):
    def _def(*args,**kwargs):
        for count,thing in enumerate(args):
            print(count,thing,'参数')

        for name,value in kwargs.items():
            print(name,value,'不定参数')
        ret = func(*args,**kwargs)
        print(func.__name__)
        return ret
    return _def
@deco
def myfunc(a,b):
    print('myfunc(%s,%s)'%(a,b))
    return a+b
result=myfunc(1,2)
print(result)