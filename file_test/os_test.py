__author__ = 'doshest'
import  os
tt=os.walk('D:\\python3')
file=open('test.txt','a',encoding='utf-8')
print(tt)
for i in tt:
    #print(i)
    for ii in i[2]:

       print("文件的路径是",i[0]+ii)
       file.write(i[0]+ii+'\n')
file.flush()
file.close()

