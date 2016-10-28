__author__ = 'doshest'
with open("text.txt","wt") as out_file:
    out_file.write("该文本写入到文件中\n看到我了吧！")
with open("text.txt","rt") as in_file:

    text=in_file.read()
print(text)

print(out_file.readable())
