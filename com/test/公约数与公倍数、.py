__author__ = 'doshest'
def maxCommon(a,b):
    while b: a,b=b,a%b
    return a
def minCommon(a,b):
    c=a*b
    while b:
        a,b=b,a%b
        print('a=',a,'b=',b)
    return c//a
print(maxCommon(31,21))
print(minCommon(31,21))