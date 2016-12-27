__author__ = 'doshest'
L = [(lambda x: x**2),
    (lambda x: x**3),
    (lambda x: x**4)]
print (L[0](2),L[1](2),L[2](2))
print('----------')
D = {'f1':(lambda: 2+3),
    'f2':(lambda: 2*3),
    'f3':(lambda: 2**3)}
print (D['f1'](),D['f2'](),D['f3']())
list_i=[]
for i in (x**2 for x in range(5)):
    list_i.append(i)
print(list_i)

sq=map( lambda x: x*x, [y for y in range(10)] )

for sq_one in sq:
    print(sq_one)

list_lambda=list(map(lambda x : x*2,range(1,10)))

print(list_lambda)

