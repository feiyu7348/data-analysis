#!/usr/bin/env python
# -*- coding:utf-8 -*-

from lxml import etree


# 第一种方式
text = '''
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
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

# 使用etree解析html字符串
# html = etree.HTML(text)

# 提取数据
# r = html.xpath('/html/body/ul/li/a/text()')
# print(r)   # ['Java工程师', 'Python工程师', 'AI工程师']
#
#
# r = html.xpath('/html/body/ul/li[1]/a/text()')
# print(r)


# 第二种方式
html = etree.parse('./text.html', etree.HTMLParser())
r = html.xpath('/html/body/ul/li[1]/a/text()')
print(r)
