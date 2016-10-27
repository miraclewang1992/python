__author__ = 'doshest'
from functools import reduce
#python3中reduce函数要从functools中引入
def multipliers():
    return [lambda x : i * x for i in range(4)]

print( [m(2) for m in multipliers()])
'''
以上代码的输出是 [6, 6, 6, 6] （而不是 [0, 2, 4, 6]）。
这个的原因是 Python 的闭包的后期绑定导致的 late binding，这意味着在闭包中的变量是在内部函数被调用的时候被查找。
所以结果是，当任何 multipliers() 返回的函数被调用，在那时，i 的值是在它被调用时的周围作用域中查找，到那时，无论哪个返回的函数被调用，for 循环都已经完成了，i 最后的值是 3，
因此，每个返回的函数 multiplies 的值都是 3。因此一个等于 2 的值被传递进以上代码，它们将返回一个值 6 （比如： 3 x 2）。
（顺便说下，正如在 The Hitchhiker’s Guide to Python 中指出的，
这里有一点普遍的误解，是关于 lambda 表达式的一些东西。一个 lambda 表达式创建的函数不是特殊的，和使用一个普通的 def 创建的函数展示的表现是一样的。）
这里有两种方法解决这个问题。
最普遍的解决方案是创建一个闭包，通过使用默认参数立即绑定它的参数。例如：
def multipliers():
    return [lambda x, i=i : i * x for i in range(4)]
另外一个选择是，你可以使用 functools.partial 函数：
from functools import partial
from operator import mul
def multipliers():
    return [partial(mul, i) for i in range(4)]
'''

f = lambda x : 2 * x
print( f(3))

f = lambda x: x > 10
print(f(2))
print(f(12))

list = [1,2,3,4,5]
squaredList = map(lambda x: x*2, list)
list1=[item for item in squaredList]
print(list1)

list = [1,2,4,4,5,6,7,8,9,10]
newList = filter(lambda x: x % 2 == 0, list)
list2=[item for item in newList]
print(list2)

list = [1,2,3,4,5]
s = reduce(lambda x,y: x+y,  list)
print(s)

#去掉list中的重复元素
old_list = [1,1,1,3,4]
new_list = set(old_list)
print(new_list)

#翻转字符串
s = 'abcde'
ss = s[::-1]
print(ss)

#用两个元素之间有对应关系的list构造一个list
names=['jianpx','yue']
ages=[20,30]
dic_people=dict(zip(names,ages))
print(dic_people)

#将数量较多的字符串相连，如何效率较高，为什么
fruits = ['apple', 'banana','peach']
result = ''.join(fruits)
print(result)

x = 3
y = 2.15315315313532

# 打印数字的时候，经常要把数字转换为字符串
print("We have defined two numbers,")
print( "x = " + str(x))
print( "y = " + str(y))


list = [10,6,7,5,2,1,8,5,11]
s = reduce(lambda x,y: x if (x > y) else y, list)
print(s)




