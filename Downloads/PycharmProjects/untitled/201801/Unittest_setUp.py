# coding:utf-8
import requests
import unittest
class Test_kuaidi(unittest.TestCase):
    def setUp(self):   #前置
        self.url=""
        self.headers={

        }  # get方法其它加个ser-Agent就可以了

        self.s=requests.session()
    def test_kuaidi(self):
        r=self.s.get(self.url,headers=self.headers,verify=False)
        result=r.json()
        com_name=result['company'] #  获取公司名称
        data=result["data"]  # 获取data里面内容
        get_result=data[0]['context'] #获取已签收状态
        self.assertEqual(com_name,u"韵达快递")
        self.assertIn(u"已签收",get_result)
if __name__=="__main__"
    unittest.main()