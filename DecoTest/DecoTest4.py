__author__ = 'doshest'
def deco(arg):
    def _deco(func):
        def __deco():
            print('before the function ',arg)
            func()
            print('the function is stopped')
        return __deco
    return _deco
@deco('test')
def myfunc():
    print('the function is called')
myfunc()