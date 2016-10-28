__author__ = 'doshest'
import sys
list=['22','4343','ad',1235545]
itr =iter(list)
while True:
    try:
        print(next(itr),end=',')
    except StopIteration:
        sys.exit()