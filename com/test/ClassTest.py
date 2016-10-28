__author__ = 'doshest'
class people:

    def __init__(self,sex):
        self.sex=sex

class student(people):
    '''这是一个简单的例子'''
    i=123456;
    _classNum=0
    def __init__(self,age,name,sex,classNum):
        people.__init__(self,sex)
        self.age=age
        self.name=name
        self._classNum=classNum
    def stuPrint(self):
        print('this is a test')
x = student(18,"xiaoming","man",121)
x.stuPrint()
print(x.age)
print(x.sex)



