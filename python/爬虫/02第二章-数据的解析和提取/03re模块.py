
import re

# #findall 匹配字符串中所有符合正则的内容，返回列表（效率不高）
# lists = re.findall(r"\d+","我的电话号码是10086，10096")
# print(lists)

# # finditer 匹配字符串所有符合正则表达式的内容，返回迭代器（效率高）
# it = re.finditer(r"\d+","我的电话号码是10086，10096")
# print(it)
# for i in it:
#     print(i)
#     print(i.group()) #通过group函数拿到匹配的内容

# # search 找到一个结果就返回，返回的是match对象，拿数据要.group()函数
# s = re.search(r"\d+","我的电话号码是10086，10096")
# print(s.group())

# # match从头开始匹配,相当于r"^\d+"
# r = re.match(r"\d+","10086 10096")
# print(r.group())

# 预加载正则表达式
obj = re.compile(r"\d+")
ret = obj.finditer("我的电话号码是10086，10096")
for i in ret:
    print(i.group()) 



s = """
<div class='jay'><span id='1'>郭麒麟</span></div>
<div class='jj'><span id='2'>宋轶</span></div>
<div class='jolin'><span id='3'>大聪明</span></div>
<div class='sylar'><span id='4'>范思哲</span></div>
<div class='tory'><span id='5'>胡说八道</span></div>
"""

"""
(?P<wahaha>.*?)
分组

"""
obj = re.compile(r"<div class='.*?'><span id='(?P<id>\d+)'>(?P<wahaha>.*?)</span></div>",re.S) # re.S：让.能匹配换行符

result = obj.finditer(s)

for i in result:
    print(i.group("wahaha"))
    print(i.group("id"))
