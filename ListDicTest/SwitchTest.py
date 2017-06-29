__author__ = 'doshest'
def switch(x):
    return {
        1:2,
        3:4
    }.get(x,9)

print(switch(3))