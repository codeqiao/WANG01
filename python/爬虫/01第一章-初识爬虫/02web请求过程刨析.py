#-*- coding: utf-8 -*-
"""
过程：
    发起请求
    服务器返回页面

1、服务器渲染：在服务器那边直接把数据和html整合在一起，统一返回给浏览器
    在页面中能够找到数据

2、客户端渲染：在客户端（浏览器）上将数据和html整合在一起。
    在页面源代码中看不到数据
    第一次请求只要一个html骨架，第二次请求拿到数据，进行数据展示

3、学会熟练使用抓包工具
"""