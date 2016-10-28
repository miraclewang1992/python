__author__ = 'doshest'
import  math
num= int(input("请输入一个数字"))
if(num>1):
    for tmp in range(2,num):
        if(num % tmp==0):
            print("{0}不是质数".format(num))
            break
    else:
        print("{0}是质数".format(num))


'''-------------------------'''
print('''---------------------''')

num1=int(input("请输入第二个数字"))
num2=int(input("请输入第三个数字"))
min1=min(num1,num2)
max2=max(num1,num2)
for tmp in range(min1,max2):
    if (tmp>1):
        for tmp2 in range(2,math.ceil(tmp/2)):
            print(tmp2)
            if(tmp%tmp2==0):
                break
        else:
            print("{0}是质数".format(tmp))


