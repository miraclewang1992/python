__author__ = 'doshest'
import random
foo = ['a','b','c','d']
print(''.join(random.choice('abcdef') for _ in range(6)))