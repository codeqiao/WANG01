"""
安装bs4
"""

from tkinter import image_names
import requests
from bs4 import BeautifulSoup

url = "http://www.xinfadi.com.cn/getPriceData.html"
url1 ="http://www.xinfadi.com.cn/index.html"
resp = requests.get(url1)

# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.44"
# }

# data = {
#     'limit': '',
#     'current':'',
#     'pubDateStartTime':'' ,
#     'pubDateEndTime': '',
#     'prodPcatid': '',
#     'prodCatid': '',
#     'prodName': ''
# }

# for i in range(1, 16149):
#     data["current"] = i
#     reps = requests.post(url=url,headers=headers,data=data)
#     reps.close()
#     print(reps.json())



# bs4使用
# 1、将页面源代码给BeautifulSoup进行处理，生成bs对象

page = BeautifulSoup(resp.text, "html.parser") #参数2指定html解析器

# 2、从bs对象中查找数据
# find(标签，属性=值) 找一个
# fingall(标签，属性=值) 找所有

images = page.find_all("img",attrs={"class":"imgs"})
for image in images:
    print(image.text)# .text表示拿到被标签标记的内容



