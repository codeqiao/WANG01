from lxml import etree




# result = tree3.xpath('/html')
tree = etree.parse("mybaidu.html",etree.HTMLParser())

result = tree.xpath('//*[@id="hotsearch-content-wrapper"]/li[4]/a')
print(result)