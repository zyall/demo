#!/usr/bin/env python
#coding:utf8
#

import re
import os
import urllib.request
#import urllib2

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

def getIma(html):
    reg = r'"objURL":"(.*?)"'
    imgre = re.compile(reg)
    print(imgre)

    imglist = re.findall(imgre,html)
    l = len(imglist)
    print(l)
    return imglist

def downLoad(urls,path):
    index = 1
    for url in urls:
        print("Downloading:",url)
        try:
            res = urllib2.Request(url)
            if str(res.status_code)[0] == "4":
                print("未下载成功:", url)
                continue
        except Exception as e:
            print("未下载成功:", url)
        filename = os.path.join(path,str(index) + ".jpg")
        urllib.urlretrieve(url,filename)
        index += 1

html = getHtml("https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result.txt&fr=&sf=1&fmq=1495865476197_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E8%98%91%E8%8F%87%E5%A4%B4%E8%A1%A8%E6%83%85%E5%8C%85")

savePath = "/root/mogutou_image"
downLoad(getIma(html),savePath)

