import requests

url = "https://fanyi.baidu.com/sug"

s = input("输入翻译的单词：")

data  ={
    "kw": s
}
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Mobile Safari/537.36 Edg/102.0.1245.41"
}

# 发送post请求，发送的数据必须放在字典中，通过data参数进行传递
reps = requests.post(url=url, data=data, headers=headers)
print(reps.json()) # 将服务器返回的内容直接处理成json()

reps.close()
