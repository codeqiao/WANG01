"""
1、拿到页面源代码
2、re提取源代码中我们想要的内容

注意：
    匹配（要注意要用[]将（括起来
"""
import re
import requests
import csv

url = "https://movie.douban.com/chart"

header ={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel)"
}
resp = requests.get(url,headers=header)


page_content = resp.text

# 解析数据
obj = re.compile(r' <td width="100" valign="top">.*?<a href=".*?class="">(?P<name>.*?)/ <span.*?>.*?<p class="pl">(?P<time>.*?)/.*?<span class="rating_nums">(?P<points>.*?)</span>',re.S)

result = obj.finditer(page_content)

for it in result:
    print(it.group("name").strip(),it.group("time").strip(),it.group("points").strip())

resp.close()