__author__ = 'doshest'
fo = open("test.txt", "r+",encoding='utf-8')
print("文件名为: ", fo.name)
line =fo.readline()
print(line)
# 截取10个字节
#fo.truncate()
fo.write('\naaaaaaaaaa')
str = fo.readlines()
print( "读取数据---: %s" % (str))

# 关闭文件
fo.close()