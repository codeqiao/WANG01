"""
·浏览器F12抓包工具
·一级选项卡：
    Elements、Console、Sources、Network...
    二级选项卡：
    XHR 动态加载的文件（异步文件）

GET请求：参数在url地址中有显示
POST请求：Form表单提交数据


解密：
    找到js加密文件
    
"""
from unittest import result
import requests
import time
from hashlib import md5
import random


class YdSpider(object):
    def __init__(self) -> None:
        self.url = "https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
        self.headers = {
            'Accept':'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding':'gzip, deflate, br',
            'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Cache-Control':'no-cache',
            'Connection':'keep-alive',
            #'Content-Length':'241',
            'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie':'OUTFOX_SEARCH_USER_ID=111939407@10.108.160.105; OUTFOX_SEARCH_USER_ID_NCOO=1664042674.3196843; P_INFO=18355005847|1653369951|1|youdao_zhiyun2018|00&99|null&null&null#CN&null#10#0|&0|null|18355005847; fanyi-ad-id=306808; fanyi-ad-closed=1; ___rl__test__cookies=1656078520476',
            'Host':'fanyi.youdao.com',
            'Origin':'https://fanyi.youdao.com',
            'Pragma':'no-cache',
            'Referer':'https://fanyi.youdao.com/',
            'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="102", "Microsoft Edge";v="102"',
            'sec-ch-ua-mobile':'?0',
            'sec-ch-ua-platform':'"Windows"',
            'Sec-Fetch-Dest':'empty',
            'Sec-Fetch-Mode':'cors',
            'Sec-Fetch-Site':'same-origin',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.44',
            'X-Requested-With':'XMLHttpRequest'
        }
        self.data = {
            'i':'englise',
            'from':'AUTO',
            'to':'AUTO',
            'smartresult':'dict',
            'client':'fanyideskweb',
            'salt':'16560785204782',
            'sign':'1e5eb8772a296c18817aea43af4c188d',
            'lts':'1656078520478',
            'bv':'09e377475805a2fb71b566de21e0dc2b',
            'doctype':'json',
            'version':'2.1',
            'keyfrom':'fanyi.web',
            'action':'FY_BY_REALTlME'
        }

    # lts salt sign
    def get_lts_salt_sign(self,word) -> str:
        """
        @Description:
            
        @params:
            word: 搜索的单词
        @Returns:
        """
        lts = str(int(time.time()*1000))
        salt = lts + str(random.randint(0,9))
        string = "fanyideskweb" + word + salt + "Ygy_4c=r#e#4EX^NUGUc5"
            # 对string进行加密
        s = md5()
        s.update(string.encode('utf-8'))
        sign = s.hexdigest()
        return lts,salt,sign
        
    # 攻克有道
    def attack_yd(self,word:str):
        lts,salt,sign = self.get_lts_salt_sign(word)
        self.data['salt'] = salt
        self.data['lts'] = lts
        self.data['sign'] = sign
        self.data['i'] = word

        res = requests.post(url=self.url,headers=self.headers,data=self.data)
        html = res.json()
        result = html["translateResult"][0][0]['tgt']
        return result       

    def run(self):
        word = input('请输入要翻译的单词：')
        result = self.attack_yd(word=word)
        print('翻译结果为:' ,result)

if __name__ == '__main__':
    yd = YdSpider()
    yd.run()

# 第一步 找到url
# 第二步 找到form表单
# 看表单有没有加密参数、有道中的salt、sign、lts

"""
 var r = function(e) {
        var t = n.md5(navigator.appVersion)
          , r = "" + (new Date).getTime()
          , i = r + parseInt(10 * Math.random(), 10);
        return {
            ts: r,
            bv: t,
            salt: i,
            sign: n.md5("fanyideskweb" + e + i + "Ygy_4c=r#e#4EX^NUGUc5")
        }
    };

分析:
    r:
    js: r = "" + (new Date).getTime()
    pytho0n: r = str(int(time.time()*1000))

    i:
    js: i = r + parseInt(10 * Math.random(), 10)
    python: i = r + str(random.randint(0,9))

    e:
    翻译的单词
    
md5 加密用Python实现

生成sign：
    from hashlib import md5
    string = "fanyideskweb" + e + i + "Ygy_4c=r#e#4EX^NUGUc5"
    s = md5()
    s.update(string.encode())
    sign = s.hexdigest()
"""

# 第三步 找到request headers

