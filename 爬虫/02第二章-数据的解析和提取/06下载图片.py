from email import header
import requests
from bs4 import BeautifulSoup

url = "https://wallhaven.cc/toplist"

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.44"
}

param = {
    "page" : "1"
}

image_number = 1
for i in range(100):
    print(f"正在解析第{i+1}页................................................................")
    param["page"]=i+1
    reps = requests.get(url,headers=headers,params=param)
    # 解析页面
    page = BeautifulSoup(reps.text,"html.parser")
    images = page.find_all("a",attrs={'class':'preview'})
    for image in images:
        herf = image.get("href") # 通过get函数拿到属性值
        child_page_resp = requests.get(herf)
        #print(child_page_resp.text)
        # 获取子页面解析页面对象
        child_page = BeautifulSoup(child_page_resp.text,"html.parser") 

        child_image = child_page.find("img",attrs={"id":"wallpaper"})
        # 获取src属性
        src = child_image.get("src")
        # 下载图片
        img_resp = requests.get(src)
        #将文件保存下来
        image_name = f"image{image_number}.jpg"
        with open(f"./images/{image_name}", 'wb') as f:
            f.write(img_resp.content) #img_resp.content()获取文件的二进制形式
        print(f"第{image_number}张图片下载完成......")
        image_number+=1
    reps.close()

