__author__ = 'doshest'
total=0
def getTotal(arg1,arg2):
    total=arg1+arg2
    return total
getTotal(10,100)
print(total)
list =[10,100,20]
def changelist(varlist):
    varlist[1]=15
changelist(list)
for tmp in list:
    print(tmp)
