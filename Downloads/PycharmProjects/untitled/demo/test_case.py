import requests
import unittest

class Case01(unittest.TestCase):
    def test_case_01(self):
        url = 'https://m.stock.pingan.com/hq/restapi/queryBondRate'
        response = requests.get(url=url, headers={'content-Type': 'application/json'})
        # 将请求结果转成json格式
        re = response.json()
        # a代表实际结果，b代表预期结果，c代表 a!=b时的错误信息）
        # self.assertEqual(a,b,c)
        self.assertEqual(response.status_code, 200, "请求失败")
        self.assertEqual(re.get('errmsg'), 'OK', 'eee')
        self.assertEqual(re.get('status'), 1, 'kkkkk')
        print(response.text)
        print("接口流程正确")

if __name__=='__main__':
    # 运行当前文件里的测试用例
    unittest.main()