# encoding:utf-8
import requests
import json

class Person():
    #'''
    def Get_param(self,filepath):
        print('*************** Get_param 函数开始 ***************')
        param={}
        try:
            with open(filepath, 'r') as f:
                for line in f:
                    (key, value) = line.strip().split(':')
                    param[key] = value
                return param
        except IOError as ioerr:
            print("文件 %s 不存在" %filepath)
    #'''
    def Senddata(self,url,param):
        print('*************** Senddata 函数开始 ***************')
        r = requests.post(url,param)
        Person.code=r.status_code     #获取请求状态响应码
        Person.res=r.json()       #JSON解码
        #paramstr=eval(param)
        #print("paramdumps",json.dumps(paramstr))
        #print("r:",r)
        print("Person.code",Person.code)
        print("Person.res:",Person.res)
        #r.raise_for_status()
        return Person.res
    def Check_request_code(self):
        print ('*************** Check_request_code 函数开始 ***************')
        assert (Person.code==200)   # 如果响应状态码不是 200，就主动抛出异常
    def Get_response_body(self):
        print('*************** Get_response_body 函数开始 ***************')
        Person.Get_response_body=Person.res[u'body']
        return Person.Get_response_body
    def Check_response_code(self):
        print('*************** Check_response_code 函数开始 ***************')
        Person.Check_response_code=Person.res[u'code']
        return Person.Check_response_code
        assert (Person.Check_response_code==0)    #如果code不是0，则主动抛出异常
    def Check_response_message(self):
        print('*************** Check_response_message 函数开始 ***************')
        json_data=Person.res
        Person.Check_response_message=json_data[u'message']
        return Person.Check_response_message
    def Get_icon(self):
        print('*************** Get_icon 函数开始 ***************')
        body=Person.Get_response_body
        body=body[0]
        Person.Get_icon=body[u'icon']
        return Person.Get_icon
if __name__ == "__main__":
    url="https://maam-dmzstg2.pingan.com.cn:9041/lottery/api/yaoyiyao/getYaoyiyaoServiceCfg.do"
    filepath = 'param_file'
    param=Person().Get_param(filepath)
    Person.res = Person().Senddata(url,param)
    print("param:",param)
    #a=Person().Get_response_body()