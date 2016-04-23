#coding=utf-8
import re
import urllib.request
import os

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    codec = page.info().get_param('charset')
    # print(codec)
    html = html.decode(codec)
    return html

def getImg(html):
    # reg = r'src="(.+?\.jpg)" pic_ext'       # r貌似没有区别
    # reg = 'src="(.+?\.jpg)" pic_ext'
    reg = r'src="(.+?\.jpg)"(?:\s>| size)'
    imgre = re.compile(reg)
    imglist = imgre.findall(html)
    return imglist

def saveImg(html):
    imglist = getImg(html)
    x = 0
    for imgurl in imglist:
        print(imgurl)
        temp = urllib.request.urlretrieve(imgurl, getSaveUrl(x))
        # print(temp)
        x += 1

def getSaveUrl(x):
    isExists = os.path.exists('pic')
    if not isExists:
        os.makedirs('pic')
    return 'pic/python%s.jpg' % x

# html = getHtml("http://tieba.baidu.com/p/2460150866")
html = getHtml("http://tieba.baidu.com/p/4490600900")
saveImg(html)