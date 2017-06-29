__author__ = 'doshest'
list_a = [1,2,3]
list_b = [2,5,7]
#并集
list_c = [result  for result  in list_a if result  in list_b ]
print(list_c)
#差集
list_d = [result  for result  in list_a if result not in list_b]

list_e = [resultb for resultb in list_b if resultb not in list_a ]

list_d.extend(list_e)
print(list_d)

list_c.extend(list_d)
list_c.sort(reverse=True)
print(list_c)