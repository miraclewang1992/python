__author__ = 'doshest'

def deco(func):
    print('the function is called')
    func()
    print('the function is stopped')
    return func
@deco
def myFunc():
    print('the function is running')

myFunc()