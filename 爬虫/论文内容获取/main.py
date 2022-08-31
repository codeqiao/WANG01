
import time
from dealhtml import DealData
from webofscienceScrapy import WebOfScienceSpider
import os

class ControlProgram(object):
    def __init__(self,username,password,formlisttxt,dealinput,htmlout,dealout) -> None:
        # 登录vpn用户名
        self.username = username
        # 登录vpn的密码
        self.password = password
        # 下载论文的表单
        self.formlisttxt = formlisttxt
        # 论文html文件夹
        self.dealinput = dealinput
        # 处理html后的输出文件
        self.dealout = dealout
        # 爬取的论文html的保存路径
        self.htmlout = htmlout

    def scrap_data(self):
        start = 0
        buchang = 70
        w = WebOfScienceSpider(self.username,self.password,self.htmlout)
        with open(self.formlisttxt,'r',encoding='utf-8') as f:
            formlist = f.readlines()
            formlist = [form.strip() for form in formlist]
            while start<len(formlist):
                w.run(formlist[start:(start+buchang):1])
                start+=buchang

    def deal_data(self):
        d = DealData()
        d.run(self.dealinput,self.dealout)

if __name__ == '__main__':
    username = '2020214214'
    password = 'Yxm15255035272'
    pwd = os.path.dirname(os.path.abspath(__file__))
    pwd = pwd.replace('\\','/')
    print(pwd)
    formlisttxt = f"{pwd}/out/piepie li.txt"
    dealinput = f'{pwd}/data/out/html/peipei li'
    dealout = f"{pwd}/data/out/out.txt"
    htmlout = f"{pwd}/data/out/html"
    c = ControlProgram(username,password,formlisttxt,dealinput,htmlout,dealout)
    c.scrap_data()

    # temp = set()
    # with open(f"{pwd}/data/out/out.txt", 'r', encoding='utf-8') as f:
    #     for i in f.readlines():
    #         temp.add(i)
    
    # with open(f"{pwd}/data/out/out.txt", 'w', encoding='utf-8') as f:
    #     for i in temp:
    #         f.write(i)

    # c.deal_data()

    






