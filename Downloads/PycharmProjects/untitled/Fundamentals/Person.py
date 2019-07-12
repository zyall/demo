# encoding:utf-8
import requests
import json



class Person():
    def Senddata(self,url,param):
        r = requests.post(url,param)
        print("r:",r)
        r.code=r.status_code
        print(r.code)
        r.raise_for_status()
        print(r.json())

    def load_dict_from_file(self,filepath):
        param={}
        try:
            with open(filepath, 'r') as f:
                for line in f:
                    (key, value) = line.strip().split(':')
                    param[key] = value
                return param
        except IOError as ioerr:\
            print("文件 %s 不存在" %filepath)
    def Parjson(self):
        json_str=json.dumps(json_data)
        return json_str
    def jsonFile(self):
        fileObject = '/Users/zq1/PycharmProjects/untitled1/Fundamentals/json.txt'
        with open(fileObject, "w") as F:
            for idx in json_str:
                F.write(idx)
            return json_str

if __name__ == "__main__":
    url="https://maam-dmzstg2.pingan.com.cn:9041/lottery/api/yaoyiyao/getYaoyiyaoServiceCfg.do"
    filepath = 'param_file'
    param=Person().load_dict_from_file(filepath)
    json_data=Person().Senddata(url,param)
    #print(json_data)
    json_str=Person().Parjson()
    a=Person().jsonFile()
    print("param:", param)
    print(a)