__author__ = 'doshest'
def div1(x,y):
    print("%s/%s = %s" % (x, y, x/y))

def div2(x,y):
    print("%s//%s = %s" % (x, y, x//y))
div1(5,2)
div1(5.,2)
div2(5,2)
div2(5.,2.)

'''
在 Python 3 中，期望的输出是：

5/2 = 2.5
5.0/2 = 2.5
5//2 = 2
5.0//2.0 = 2.0
在 Python 2 中，尽管如此，以上代码的输出将是：

5/2 = 2
5.0/2 = 2.5
5//2 = 2
5.0//2.0 = 2.0
'''