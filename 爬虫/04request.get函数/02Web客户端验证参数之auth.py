"""
1、针对需要web客户端用户名密码认证的网站
2、auth = （‘username’，‘pathword’）元组
requests.get()的outtime参数表示：
    访问网站超过那个时间就会抛出异常
    默认值为 180
    一般可以设置为3

其他知识：
    str.startwith()
    str.endwith()
"""




from email import header
import requests
from lxml import etree
# pip install fake_useragent --index-url https://pypi.douban.com/simple
from fake_useragent import UserAgent # 随机生成请求部头部

class CodeSpider(object):
    def __init__(self):
        self.url = ''
        self.auth = ('','')

    def get_headers(self):
        ua = UserAgent()
        return {'User-Agent':ua.random}

    def parse_html(self):
        # 获取html页面
        html = requests.get(self.url,auth=self.auth,headers=self.get_headers()).text
        # 解析页面
        parse_obj = etree.HTML(html,etree.HTMLParser())\
        
    def run(self):
        self.parse_html()

    def save_file(self,herf:str)->None:
        """
        @Description:
            下载文件
        @params:
            herf 下载链接
        @Returns:
            null
        """
        content = requests.get(herf,auth=self.auth,headers=self.get_headers()).content
        # 保存文件
        pass
        

        
        
        
        

if __name__ == '__main__':
    str1 = "a.txt"
    print(str1.startswith('a'))
    print(str1.endswith('.txt'))
    # spider = CodeSpider()
    # spider.run()

    arr = ['asd','dsf','sada']
    str2 = '/'.join(arr)+'/'
    print(str2)


