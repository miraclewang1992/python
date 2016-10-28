__author__ = 'doshest'
import  re
from collections import  Counter
def get_max_value(text):
    text =text.lower()
    result =re.findall('[a-zA-Z]',text)
    count=Counter(result)

    count_list=list(count.values())
    max_value=max(count_list)
    max_list=[]
    for k,v in count.items():
        if v==max_value:
            max_list.append(k)
    max_list=sorted(max_list)
    print(max_list[0])
get_max_value('aaaabbbbbc')
'''
精简方法
'''
import string
def get_max_value_better(text):
    text=text.lower();
    text.index('a')

    max_data=max(string.ascii_lowercase,key=text.count)
    min_data=min(string.ascii_lowercase,key=text.count)
    print(string.ascii_lowercase)
    print(text.count)
    print(max_data)
    print('min-data',min_data)

get_max_value_better('aaaaabbbbb')
