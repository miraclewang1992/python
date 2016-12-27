__author__ = 'doshest'
def deco(func):
    def _deco(a,b):
        print('the function is called',a,b)
        ret = func(a,b+1)
        print('the function is stopped',ret)
        return ret
    return _deco
@deco
def myfunc(a,b):
    print('myfunc(%s,%s) is called'%(a,b))
    return a+b
myfunc(1,2)
