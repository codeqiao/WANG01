

from re import M
import requests
from lxml import etree
url = "https://wuhu.zbj.com/sem/index?pmcode=130607455&utm_source=360pz&utm_medium=SEM"

resp = requests.get(url)

with open('a.html',mode='wb') as f:
    f.write(resp.content)
tree = etree.parse("a.html",etree.HTMLParser())
# tree = etree.HTML(resp.body())

divs = tree.xpath("/html/body/div[1]/div[5]/div[4]/div/div[4]/div[1]")
print(divs)
for div in divs:
    result = div.xpath("./div/div[2]/p/text()")
    print(result)