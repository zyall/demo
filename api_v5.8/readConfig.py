import os
import codecs
import configparser

# os.path.split分割文件名和路径
# os.path.realpath(__file__)返回path的真实路径
proDir = os.path.split(os.path.realpath(__file__))[0]

# os.path.join 将目录和文件合成一个路径
configpath = os.path.join(proDir,'config.ini')

class ReadConfig():
    def __init__(self):
        fd = open(configpath)
        data = fd.read()
        # remove BOM
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(configpath,'w')
            file.write(data)
            file.close()
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(configpath)
    def get_http(self,name):
        value = self.cf.get("HTTP",name)
        return value

if __name__=="__main__":
    A = ReadConfig()
    print(A.get_http('baseurl'))

