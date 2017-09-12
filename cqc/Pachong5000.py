__author__ = 'doshest'
import xlrd
import requests

p={'username':'manager','password':'Yanshangbei2017'}
def read_excel_xlrd(s):
    '''Read Excel with xlrd'''
    #file
    TC_workbook=xlrd.open_workbook("pros.xlsx")
    # all_sheets_list=TC_workbook.sheet_names()
    first_sheet=TC_workbook.sheet_by_index(0)
    # second_sheet=TC_workbook.sheet_by_name("Sheet2")
    # print("Second sheet Rows:",second_sheet.nrows)
    for row in range(2900,3000):
            id = str(int(first_sheet.cell(row,0).value))
            name = first_sheet.cell(row,1).value
            url = first_sheet.cell(row,2).value
            print("row,id,name,url",row,id,name,url)
            if url !=None:
                downloadFile(url,s,id,name)

def downloadFile(url,s,id,name):
    r = s.get(url)
    path = "d://4950/"+id+'/'
    mkdir(path)
    with open(path+name, "wb") as code:
         code.write(r.content)
         code.close()

def login(p):
    s=requests.session();
    s.post('http://cxcyds.zgqncyxd.cn/ym/login',data=p)
    read_excel_xlrd(s)


def mkdir(path):
    # 引入模块
    import os
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")
    isExists=os.path.exists(path)
    # 判断结果
    if not isExists:
        os.makedirs(path)
        print( path+' 创建成功')
        return True
    else:
        print (path+' 目录已存在')
        return False
if __name__=="__main__":
    login(p)