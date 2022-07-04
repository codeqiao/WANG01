"""
·定义
    1、定义：：代替你原来的IP地址去对接网路的IP地址
    2、作用：隐藏自身真实IP，避免被封

    高匿代理：高度匿名，web站点只能看到代理IP
    透明：web站点能看到代理IP和用户自身真实IP
    普通：web站点能看到代理IP和知道有人通过这个代理IP访问了，但是不知道用户真实IP

·用法：
    proxies = {
        'http':'http://IP:端口号',
        'https':'https://IP:端口号',
    }

http://httpbin.org/get 这个网站可以看见访问网站的IP

"""
import sys
sys.path.append(r"E:\\code\\learn\\python\\爬虫")
from common.dailiIP import RandomIP
import requests
from fake_useragent import UserAgent

url = "http://baidu.com/"
ua = UserAgent()
headers = {
    'User-Agent':ua.random
}
# 代理IP
ip = RandomIP()
proxies = ip.random_proxies()

try:     
    resp = requests.get(url,headers=headers,verify=False,proxies=proxies,timeout=8)
    print("Success")
except Exception as e:
    print("Failed")

