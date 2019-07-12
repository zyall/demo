#coding=utf-8

''''
import re
import requests
def getHtml(url):
    page=urllib.request.urlopen(url)
    html=page.read()
    return html
html=getHtml("https://maam-dmzstg2.pingan.com.cn:9041/lottery/api/yaoyiyao/getYaoyiyaoServiceCfg.do")
print(html)




import urllib.request


url = 'https://maam-dmzstg2.pingan.com.cn:9041/lottery/api/yaoyiyao/getYaoyiyaoServiceCfg.do'

data = urllib.parse.urlencode({'userId': '', 'deviceId': 'value2','devieceType': 'ios', 'osVersion': '11','appId': 'PA00900000000_01_JKGJ',
          'appVersion': '4.4.0.0','sdkVersion': '4.1.0.42'})
data = data.encode('utf-8')

r=urllib.request.urlopen(url,data)
print(r.read().decode('utf-8'))
'''


import requests
class Person:
    def __init__(self,url,path,param):
        self.url=url
        self.path=path
        self.param=param

    def  test(self):
        r=requests.post(self.url+self.path,self.param)
        print(r.json())


if __name__ == "__main__":
    url="https://maam-dmzstg2.pingan.com.cn:9041"
    path = "/lottery/api/yaoyiyao/getYaoyiyaoServiceCfg.do"
    param = {'userId': '', 'deviceId': 'value2', 'devieceType': 'ios', 'osVersion': '11',
            'appId': 'PA00900000000_01_JKGJ',
            'appVersion': '4.4.0.0', 'sdkVersion': '4.1.0.42'}
    a=Person(url,path,param)
    a.test()
