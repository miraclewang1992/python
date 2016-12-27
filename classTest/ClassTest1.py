__author__ = 'doshest'
import copy
# def foo(x):
#     print('executing foo(%s)'%(x))
class A(object):
    def foo(self,x):
        print('executing foo(%s,%s)'%(self,x))
    @classmethod
    def class_foo(cls,x):
        print('executing foo(%s,%s)'%(cls,x))
    @staticmethod
    def static_foo(x):
        print('executing foo(%s)'%(x))
a =A()

A.class_foo(1)
A.static_foo(2)


def print_everything(*args):
    for count ,thing in enumerate(args):
        print('{0}.{1}'.format(count,thing))
print_everything('apple','banana','cabbage')
def table_things(**kwargs):
    for name,value in kwargs.items():
        print('{0}.{1}'.format(name,value))
table_things(name='jackson',age=12)

a = [1,2,3,4,['a','b']]
b = a
c = copy.copy(a)
d = copy.deepcopy(a)
a.append(5)
a[4].append('c')
print(a)
print(b)
print(c)
print(d)

