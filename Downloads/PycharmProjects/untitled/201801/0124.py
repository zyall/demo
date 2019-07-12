# encoding:utf-8
#下载图片
#1.把所有图片拿到

import requests
r=requests.get('http://n9.cmsfile.pg0.cn/group4/M00/24/A2/CgpBUlkc-kyAVhnYAABzBwMSXXU758.jpg?enable=&w=550&h=348&cut=')

if r.status_code==200:
    with open('first.jpg','wb') as f:  #以二进制的方式写
        for  chunk in r.iter_content(1024):
            f.write(chunk)


