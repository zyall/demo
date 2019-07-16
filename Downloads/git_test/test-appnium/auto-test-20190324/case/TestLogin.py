from page.PageLogin import PageLogin
import unittest
from ddt import ddt,data,unpack
from utils.common import get_data_csv
from utils.common import get_parent_path
from utils.logger import logger
import os

logger = logger(logger="TestLogin").getlog()

@ddt
class TestLogin(unittest.TestCase):
    #test_account = (("admin","123456","admin"),("admin1","123456","admin1"),("admin2","123456","admin2"))
    current_directory = os.path.dirname(os.path.abspath(__file__))
    root_path = get_parent_path(current_directory)
    test_account = get_data_csv(os.path.join(root_path, "data", "user.csv"))
    test_account_all = get_data_csv(os.path.join(root_path, "data", "user-all.csv"))
    test_account_failed = (("admin", "1234567", "指定的密码不正确"), ("", "1234516", "用户名一栏为空"), ("admin2", "", "密码一栏为空"))

     #test_account = get_data_csv()
    @classmethod
    def setUpClass(cls):
        cls.p_login = PageLogin()

    @data(*test_account)
    @unpack
    def test_login_pass(self,name,password,expect):
        self.p_login.driver.get("http://autotest/wordpress/wp-login.php")
        p_pannel = self.p_login.login(name,password)
        actual_msg= p_pannel.get_account_name()
        self.assertEqual(expect,actual_msg)



    @data(*test_account_failed)
    @unpack
    def test_login_failed(self,name,password,expect):
        self.p_login.driver.get("http://autotest/wordpress/wp-login.php")
        p_pannel = self.p_login.login(name,password)
        actual_name= self.p_login.get_error_msg()
        logger.info(actual_name)
        self.assertIn(expect,actual_name)

    @data(*test_account_all)
    @unpack
    def test_login_all(self,name,password,flag,expect):
        self.p_login.driver.get("http://autotest/wordpress/wp-login.php")
        p_pannel = self.p_login.login(name,password)
        if flag == "1":
            actual_name = p_pannel.get_account_name()
        else:
            actual_name = self.p_login.get_error_msg()
        self.assertIn(expect, actual_name)



if __name__=="__main__":
    unittest.main()