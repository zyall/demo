import unittest
from Common.configHttp import *
from Common.common import *
from Common.Log import MyLog as Log

s = ConfigHttp()
A = Excel('sample.xls','test01')
cls = A.get_xls()
class Case01(unittest.TestCase):
    def test_case_01(self):
        self.log = Log.get_log()
        self.logger = logging.getLogger()
        try:
            for i in cls:
                case_name = i[0]
                method = i[1]
                url = i[2]
                errmsg = i[3]
                status = i[4]
                print("******* Excute %s Start *******" % case_name)
                header = {'content-Type': 'application/json'}
                s.set_url(url)
                s.set_headers(header)
                if method == 'post':
                    resp = s.post()
                else:
                    resp = s.get()
                re = resp.json()
                # a代表实际结果，b代表预期结果，c代表 a!=b时的错误信息）
                # self.assertEqual(a,b,c)
                self.assertEqual(resp.status_code, 200)
                self.assertEqual(re.get('errmsg'), errmsg)
                self.assertEqual(re.get('status'), status)
                self.logger.info(resp.text)


                self.logger.info("******* Excute %s Start ******* " % case_name)
        except Exception as ex:
            print("Failed")
            self.logger.error(str(ex))
            self.logger.error('Failed')
