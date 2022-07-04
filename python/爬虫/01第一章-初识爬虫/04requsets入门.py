
"""
# 使用国内源下载工具包：
    pip install -i https://pypi.tuna.tsinghua.edu.cn/simple(清华大学镜像) requests

"""
import requests

url = "https://www.sogou.com/web?query=周杰伦"
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Mobile Safari/537.36 Edg/102.0.1245.41"
}

# 在地址栏里面的信息一律是get请求方式
reps = requests.get(url,headers=headers) #处理了一个小小的反爬机制

print(reps) # <Response [200]>表示这个响应没有问题
# print(reps.text) # 拿到页面源代码

with open("mybaidu.html", mode='w', encoding="utf-8") as f:
    f.write(reps.text) # 读取到网页源代码

reps.close()