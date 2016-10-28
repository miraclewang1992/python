__author__ = 'doshest'
string='abc'
def fun1(string):
    all_string='ddd'.join(string)
    return all_string
print(fun1(string))

string1 = ['abc','b','c','d','e','f','g']

def fun(string):
    all_string = ''.join(string)
    return all_string
print(fun(string1))