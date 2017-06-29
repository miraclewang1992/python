__author__ = 'doshest'
list1 = [1,2,3]
print(list1[-1])
list1.reverse()
print(list1)

try:
    print([12,1,2,1].index(0))
except Exception:
    print('exception')

for index,val in enumerate(list1):
    print(index,val)
b=[1]
if not b:
    print('list is empty')
else:
    print('list is not empty')

list_a = [1,2,3,4]
list_b = [5,6,5]
list_a.append(list_b)
print(list_a)
list_a.extend(list_b)
print(list_a)