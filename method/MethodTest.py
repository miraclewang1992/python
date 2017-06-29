__author__ = 'doshest'
class methodTest:
    name='111'
    age=0
    def __init__(self,name,age):
        self.name =name
        self.age =age
    def normal_method(self):
        print('normal_method')
    @classmethod
    def class_method(cls):
        print(cls.name)
        print('class_method')

    @staticmethod
    def static_method():
        print('static_method')
t= methodTest('xiaoming',18)
t.class_method()