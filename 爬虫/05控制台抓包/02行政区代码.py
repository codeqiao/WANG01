"""
反爬：
    会存在二级链接
    点击链接跳转到的页面不是点击的那个链接（点击那个链接后会跳转到js文件中，然后通过js文件跳转到一个新的链接）

"""

class GovSpider(object):
    def __init__(self) -> None:
        self.url = 'http://www.mca.gov.cn/article/sj/xzqh/2020/20201201.html'
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.44'}


    