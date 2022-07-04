from unicodedata import name
from lxml import etree
import os


class DealData(object):

    def __init__(self) -> None:
        pass

    def get_info(self, html):
        tree = etree.HTML(html, etree.HTMLParser())
        # self.get_name(tree)
        # self.get_author(tree)
        # self.get_abstract(tree)
        lunwen_obj = f"{'{'}'论文标题':{self.get_name(tree)},'论文作者':{self.get_author(tree)},'论文摘要':{self.get_abstract(tree)}{'}'}"
        return lunwen_obj

        
    def get_name(self,tree):
        name = tree.xpath('//*[@id="snMainArticle"]/div[1]/div/div//h2/text()')
        return name
        
    def get_author(self,tree):
        author = tree.xpath('//*[@id="SumAuthTa-MainDiv-author-en"]/span//span/text()')
        return author

    def get_abstract(self,tree):
        abstract = tree.xpath('//*[@id="FullRTa-abstract-basic"]/p/text()')
        return abstract

    def run(self,inputfile,outfile):
        for file in os.listdir(inputfile):
            filename = f'{inputfile}/{file}'
            with open(filename,'r',encoding='utf-8') as f:
                html = f.read()
                if html == '':
                    continue
                lunwen = self.get_info(html)+"\n"
                with open(outfile,'a',encoding='utf-8') as f1:
                    f1.write(lunwen)
        # filename = 'E:/code/learn/python/爬虫/论文内容获取/data/out/html/10 Challenging Problems in Data Mining Research.html'
        # with open(filename,'r',encoding='utf-8') as f:
        #     html = f.read()
        #     lunwen  = eval(self.get_info(html))
        #     print(lunwen['论文摘要'])


if __name__ == '__main__':
    d = DealData()
    input = 'E:\code\learn\python\爬虫\论文html\\'
    out = "E:\code\learn\python\爬虫\out.txt"
    d.run(input,out)