__author__ = 'doshest'
class Parent(object):
    x=1
class Child1(Parent):
    pass
class Child2(Parent):
    pass
print(Parent.x,Child1.x,Child2.x)
Child1.x=2
print(Parent.x,Child1.x,Child2.x)
Parent.x=3
print(Parent.x,Child1.x,Child2.x)
'''
这个答案的关键是，在 Python 中，类变量在内部是作为字典处理的。如果一个变量的名字没有在当前类的字典中发现，
将搜索祖先类（比如父类）直到被引用的变量名被找到（如果这个被引用的变量名既没有在自己所在的类又没有在祖先类中找到，会引发一个AttributeError 异常 ）。

因此，在父类中设置 x = 1 会使得类变量 X 在引用该类和其任何子类中的值为 1。这就是因为第一个 print 语句的输出是 1 1 1。

随后，如果任何它的子类重写了该值（例如，我们执行语句 Child1.x = 2），
然后，该值仅仅在子类中被改变。这就是为什么第二个print 语句的输出是 1 2 1。

最后，如果该值在父类中被改变（例如，我们执行语句 Parent.x = 3），
这个改变会影响到任何未重写该值的子类当中的值（在这个示例中被影响的子类是 Child2）。这就是为什么第三个 print 输出是 3 2 3。
'''
