__author__ = 'doshest'

def get_media(data):
    data=sorted(data)
    num=len(data)
    if num%2 ==0 :
        median=(data[num//2]+data[num//2]-1)/2
        print(median)
    if num%2 ==1 :
        median=data[num//2]
        print(median)
get_media([1,2,3,7,8])


'''
最佳方法
'''
def get_median_better(data):
    data=sorted(data)
    size=len(data)
    print( (data[size//2]+data[~size//2])/2)
get_median_better([1,2,3,7,8])


print(7.0//2)

