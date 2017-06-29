__author__ = 'doshest'
a = 0
def change_global():
    global  a
    a=1
    return a
change_global()
print(a)