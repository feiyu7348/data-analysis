#!/usr/bin/env python
# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup

html_doc = '''
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title>1111111</title>
	</head>
	<body>
	    <ul>
	        <li><a href="a/b/c/java/">Java工程师</a></li>
	        <li><a href="a/b/c/python/">Python工程师</a></li>
	        <li><a href="a/b/c/ai/">AI工程师</a></li>
	    </ul>	
	</body>
</html>
'''
soup = BeautifulSoup(html_doc, 'lxml')
r = soup.title
print(r)

'''
通过tag标签对象获取文档数据
# soup.title     # title元素
# soup.p         # 第一个p元素
# soup.p['class']   # p元素的class属性
# soup.p.b          # p元素下的b元素
# soup.p.parent.name   # p元素的父节点的标签
'''




# 2、通过搜索获取 find  find_all
r = soup.find('title')
print(r.text)
print(r.get_text())

# 3、CSS选择器
r = soup.select('title')
