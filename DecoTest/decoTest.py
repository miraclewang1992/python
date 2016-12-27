__author__ = 'doshest'
def deco(fun):
    def _deco():
        print('the function is called')
        fun()
        print('the function is stopped')
    return _deco
@deco
def test():
    print('is running')
test()