import requests
from lxml import etree
from fake_useragent import UserAgent
import random
import os
import time

# ip池文件地址
ips_name = "E:\code\learn\python\爬虫\common\datas\ips.txt"


class DaliIP(object):

    def __init__(self) -> None:
        self.contents = self.append_url()

    def append_url(self):
        # self.contents = [
        #     ["http://ip.yqie.com/ipproxy.htm",'//*[@id="GridViewOrder"]/tr/td[1]/text()','//*[@id="GridViewOrder"]/tr/td[2]/text()'],
        #     ["http://www.ip3366.net/?stype=1&page=1",'//*[@id="list"]/table/tbody/tr/td[1]/text()','//*[@id="list"]/table/tbody/tr/td[2]/text()'],
        # ]
        # for i in range(2,11):
        #     url = f"http://www.ip3366.net/?stype=1&page={i}"
        #     temp = [url,'//*[@id="list"]/table/tbody/tr/td[1]/text()','//*[@id="list"]/table/tbody/tr/td[2]/text()']
        #     self.contents.append(temp)

        # for i in range(1,7):
        #     url = f"https://www.89ip.cn/index_{i}.html"
        #     temp = [url,'/html//body/div[3]/div[1]/div/div[1]/table/tbody/tr/td[1]/text()','/html/body/div[3]/div[1]/div/div[1]/table/tbody/tr/td[2]/text()']
        #     self.contents.append(temp)

        for i in range(1,4642):
            url = f"https://free.kuaidaili.com/free/inha/{i}"
            temp = [url,'//*[@id="list"]/table/tbody/tr/td[1]/text()','//*[@id="list"]/table/tbody/tr/td[2]/text()']
            yield temp
            
            

    def get_ip(self,url:str,ip_xpath:str,port_xpath:str)->list:
        ua = UserAgent()
        headers = {'User-Agent': ua.random}

        # rip = RandomIP() 
        # proxies = rip.random_proxies()
        # 获取页面源代码
        try:
            html = requests.get(url,headers=headers,timeout=5)
            # 解析页面获取IP和端口
            # print(html)
            tree = etree.HTML(html.text, etree.HTMLParser())
            ips = tree.xpath(ip_xpath)
            ports = tree.xpath(port_xpath)

            ips = [ips[i].strip() for i in range(len(ips))]
            ports = [ports[i].strip() for i in range(len(ports))]
            return ips,ports
        except Exception as e:
            return [],[]
     
    # 提取
    def generate_ip(self) -> None:
        """
        @Description:
            代理IP生成器
        @params:
        
        @Returns:
        """
        ips = []
        ports = []
        # 获取不同网站的IP
        for content in self.contents:
            ips1,ports1 = self.get_ip(content[0],content[1],content[2])
            ips.extend(ips1)
            ports.extend(ports1)
            # 降低访问速率防止被封IP
            time.sleep(1)


        for i in range(len(ips)):
            new_ip = ips[i] + ":" + ports[i]
            yield new_ip

    def generate_dailiip_datas(self) -> None:
        """
        @Description:
            生成代理IP库
        @params:

        @Returns:
        """
        with open(ips_name, 'a') as f:
            num = 1
            success = 0
            failed = 0
            for ip in self.generate_ip():
                print(f"第{num}个：",end='')
                num+=1
                if (self.check_ip(ip)):
                    success+=1
                    f.write(ip + '\n')
                else:
                    failed+=1
            
            print(f"总共{num}个IP，成功{success}个，失败{failed}个")

    # 测试IP是否可用
    def check_ip(self, ip: str) -> bool:
        testUrl = "http://www.baidu.com/"
        # testUrl = "https://www.bilibili.com/"
        ua = UserAgent()
        headers = {'User-Agent': ua.random}
        proxies = {'http': 'http://' + ip, 'https': 'https://' + ip}
        # proxies = {'https': 'https://' + ip}
        try:
            resp = requests.get(testUrl,
                                headers=headers,
                                proxies=proxies,
                                verify=False,
                                timeout=1)
            print(ip, "Success")
            return True
        except Exception as e:
            print(ip, "Failed")
            return False

class RandomIP(object):

    def __init__(self) -> None:
        self.ips = []
        self.read_ips()

    def read_ips(self) -> None:
        with open(ips_name, 'r') as f:
            for ip in f.readlines():
                self.ips.append(ip.strip())

    def random_proxies(self) -> dict:
        ip = random.sample(self.ips,1)[0]
        proxies = {
            'http':'http://'+ip,
            'https':'https://'+ip
        }
        return proxies

if __name__ == '__main__':
    test = DaliIP()
    test.generate_dailiip_datas()
    # ips,ports = test.get_ip(test.contents[11][0],test.contents[11][1],test.contents[11][2])
    # print(ips)
    # print(ports)
    # for i in range(len(ips)):
    #     print(ips[i]+":"+ports[i])

    # r = RandomIP()
    # for i in range(10):
    #     print(r.random_ip())
    # for i in test.get_ip():
    #     print(i)
    # print(os.path.abspath(__file__))

    # proxies = {
    # 'http':'http://39.106.223.134:80',
    # 'https':'https://39.106.223.134:80',
    # }
    # html = requests.get("https://free.kuaidaili.com/free/inha/1",verify=False,timeout=5).text
    #     # 解析页面获取IP和端口
    # tree = etree.HTML(html, etree.HTMLParser())
    # ips = tree.xpath('//*[@id="list"]/table/tbody/tr/td[1]/text()')
    # ports = tree.xpath('//*[@id="list"]/table/tbody/tr/td[2]/text()')
    # ips = [ips[i].strip() for i in range(len(ips))]
    # ports = [ports[i].strip() for i in range(len(ports))]
    # print(ips)
    # print(ports)
