# -*- coding: utf-8 -*-
#利用Python爬虫技术实现对给定URL的Instagram图片下载

import urllib.request
import re

def getHtml(url):
	req = urllib.request.Request(url)
	req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36')
	page = urllib.request.urlopen(req)
	html = page.read()
	html=html.decode('utf-8')   #Python3 必须有这句话！！
	return html

def getImg(html):
	reg = r'content="(.+?\.jpg)"'
	imgre = re.compile(reg)
	imglist = re.findall(imgre,html)
	x = 3
	for imgurl in imglist:
		urllib.request.urlretrieve(imgurl,'%s.jpg' % x)
		x+=1

html = getHtml("https://www.instagram.com/p/BUV2U-3BU4y/?taken-by=kimijuan&hl=zh-cn")
print(getImg(html))
print('Done')