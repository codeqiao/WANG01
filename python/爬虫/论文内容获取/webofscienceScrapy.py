
from base64 import encode
import encodings
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time


# 驱动器位置
location_driver = r'D:\资源\edgedriver_win64\msedgedriver.exe'


class WebOfScienceSpider(object):
    def __init__(self,username,password,out) -> None:
        # 登录网站的url
        self.login_url = 'https://webvpn.hfut.edu.cn/http/77726476706e69737468656265737421f3f652d22f367d44300d8db9d6562d/cas/login?service=https%3A%2F%2Fwebvpn.hfut.edu.cn%2Flogin%3Fcas_login%3Dtrue'
        # 浏览器对象,option是控制不自动关闭浏览器的
        self.driver = None
        # 登录用户名
        self.login_username = username
        # 登录密码
        self.login_password = password
        # 搜索次数
        self.num = 0
        self.out = out
        self.dealed_num = 0


    # 登录进入vpn
    def get_login_web(self):
        option = webdriver.EdgeOptions()
        option.add_experimental_option('detach',True)
        self.driver = webdriver.Edge(service=Service(location_driver),options=option)
        # 获取登录页面
        self.driver.get(self.login_url)
        time.sleep(0.5)
        # 输入登录用户名
        username_text = self.driver.find_element(By.XPATH,'//*[@id="username"]')
        username_text.send_keys(self.login_username)
        time.sleep(0.5)
        # 输入登陆密码
        password_text = self.driver.find_element(By.XPATH,'//*[@id="pwd"]')
        password_text.send_keys(self.login_password)
        time.sleep(0.5)
        # 点击登录按钮
        login_button = self.driver.find_element(By.XPATH,'//*[@id="sb2"]')
        login_button.click()
        time.sleep(0.5)

    # 进入web_of_science
    def goto_webofscience(self):
        # 滑动滚动条并进入图书馆
        self.driver.execute_script('window.scrollTo(0,1000)')
        time.sleep(1)
        library1 = self.driver.find_element(By.XPATH,'//*[@id="group-4"]/div[2]')
        #self.driver.execute_script("arguments[0].scroollIntoView();",library1)
        library1.click()
        time.sleep(1)

        # 切换窗口,到新的矿口来操作
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        
        #进入到数据库导航中
        ziyuan = self.driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[4]/ul[1]/li[1]')
        # 实例化，悬浮，点击
        ActionChains(self.driver).move_to_element(ziyuan).perform()
        time.sleep(2)
        datas_dirct = (By.XPATH,'/html/body/div[1]/div/div[4]/ul/li[1]/div/ul/li[2]/a')
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(datas_dirct))
        self.driver.find_element(*datas_dirct).click()
        time.sleep(0.5)

        # 进入webofscience
        self.driver.find_element(By.XPATH,'//*[@id="dbBiglist"]/div[2]/div[2]/table/tbody/tr[33]/td[1]/a').click()
        time.sleep(10)
        # 切换窗口,到新的矿口来操作
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
    
    # 搜素论文，并且获取页面源代码
    def get_html(self,search):
        # 清空输入栏的内容
        #self.driver.find_element(By.XPATH,'//*[@id="snSearchType"]/div[1]/app-search-row/div/div[2]/mat-form-field/div/div[1]/div[4]/div/button/mat-icon/svg/path').click()
        self.driver.find_element(By.XPATH,'//*[@id="snSearchType"]/div[3]/button[1]').click()
        #self.driver.find_element(By.XPATH,'//*[@id="snSearchType"]/div[4]/button[1]').click()
        # 输入查找的内容
        self.driver.find_element(By.XPATH,f'//*[@id="mat-input-{self.num}"]').send_keys(search)
        self.num+=1
        time.sleep(1)
        title = self.driver.title
        # 点击查找
        self.driver.find_element(By.XPATH,'//*[@id="snSearchType"]/div[3]/button[2]').click()
        time.sleep(1)
        title1 = self.driver.title
        if(title!=title1):
            # 点击进入第一个匹配选项     
            self.driver.execute_script('window.scrollTo(0,40)') 
            self.driver.find_element(By.XPATH,'/html/body/app-wos/div/div/main/div/div[2]/app-input-route/app-base-summary-component/div/div[2]/app-records-list/app-record[1]/div/div/div[2]/div[1]/app-summary-title/h3/a').click()
            search = search.replace('/','')
            filename = f'{self.out}/{search}.html'
            with open(filename,'w',encoding='utf-8') as f:
                f.write(self.driver.page_source)
            self.driver.back()
            time.sleep(2)
            #  # 切换窗口,到新的矿口来操作
            # windows = self.driver.window_handles
            # self.driver.switch_to.window(windows[-1])
            # print(self.driver.title)
            #print(self.driver.page_source)
            self.driver.back()
            time.sleep(2)
        else:
            with open(r"E:/code/learn/python/爬虫/论文内容获取/data/out/nosearch.txt",'a',encoding='utf-8') as f:
                f.write(search+'\n')
            print(search,"未搜到结果")
            self.driver.refresh()
            time.sleep(2)
            self.num = 0

    # 循环爬取表单
    def cricle_get(self, article_list:list):
        for article in article_list:
            self.dealed_num+=1
            self.get_html(article)
            time.sleep(2)
            print(self.dealed_num)
            # if(self.dealed_num%2==0):
            #     # self.driver.close()
            #     # time.sleep(2)
            #     # # 切换窗口,到新的矿口来操作
            #     # windows = self.driver.window_handles
            #     # self.driver.switch_to.window(windows[-1])
            #     # self.driver.close()
            #     # time.sleep(10)
            #     # windows = self.driver.window_handles
            #     # self.driver.switch_to.window(windows[-1])
            #     self.driver.quit()
            #     #self.driver.refresh()
            #     self.get_login_web()
            #     self.goto_webofscience()
            #     self.num = 0

        

    def run(self,article_list:list):
        self.get_login_web()
        self.goto_webofscience()
        self.cricle_get(article_list)
        self.driver.quit()





if __name__ == '__main__':
    tp = WebOfScienceSpider('2020214214','Yxm15255035272')
    article_list = [
        'peipei li',
        'peipei'
    ]
    tp.run(article_list)