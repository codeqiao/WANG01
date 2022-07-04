import re
import pymysql
from sqlalchemy import null
from sympy import EX

class MyDict(object):
    def __init__(self) -> None:
        self.db = pymysql.connect(host='localhost',
                    port=3306,
                    user='root',
                    password='',
                    database='dict',
                    charset='utf8')
        self.cur = self.db.cursor()

    def deal_data(self):
        sql = 'insert into words (word,trans) values(%s,%s)'
        with open('dict.txt','r',encoding='utf8') as f:
            text = f.read()
            compiles = re.compile(r'(?P<word>.*?)Trans:(?P<trans>.*?)#',re.S)    
            words = re.finditer(compiles,text)
            for w in words:    
                try:
                    self.cur.execute(sql,[w.group('word').strip(),w.group('trans').strip()])    
                    self.db.commit()
                except Exception as e:
                    self.db.rollback()
                    print(e)
               
    def search_word(self,word):
        sql = f"select trans from words where word='{word}'"
        self.cur.execute(sql)
        try:
            return self.cur.fetchone()[0]
        except Exception:
            return '没查到'

    def close(self):
        self.cur.close()
        self.db.close()

    def run(self):
        while True:
            word = input('你想要查询的单词：')
            print(f"{word}:{self.search_word(word)}")
        self.close()

if __name__=='__main__':
    d = MyDict()
    #d.deal_data()
    d.run()