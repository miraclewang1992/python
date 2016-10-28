__author__ = 'doshest'
import sys
def vartuple(arg1,*var):
    print(arg1)
    print(var[0])
    for v in var:
        print(v)
#vartuple(11)
vartuple(1,12,3434,3223)
print (sys.path)