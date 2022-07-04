"""
xpath是XML文档中搜索内容的第一门语言
html是xml的一个子集
"""

# 安装lxml模块

# xpath解析
from lxml import etree

html = '''
<head>
    <div>什么</div>
</head>
'''

tree = etree.HTML(html)

# result = tree.xpath("head")  # /表示层级关系，第一个/是根节点

result = tree.xpath('//head/div')
print(result)
