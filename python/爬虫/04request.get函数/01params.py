import requests


url = 'http://tieba.baidu.com/f?'
params = {
    'kw':'赵丽颖',
    'ie':'utf-8',
    'pn':'50'
}

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.44"
}
res = requests.get(url,params=params,headers=headers)
res.encoding = 'utf-8'

print(res.url)


