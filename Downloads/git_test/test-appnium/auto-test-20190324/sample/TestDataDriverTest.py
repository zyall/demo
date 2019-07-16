import unittest
from ddt import ddt,data

@ddt
class TestDataDriverTest(unittest.TestCase):

    @data(1,2,3,4,5)
    def test_aparam(self,num1):
    #def test_aparam(self):
        c = self.my_add(num1,2)
        print(c)
        #print(num1)

    def my_add(self,a,b):
        return a + b

if __name__ == "__main__":
    unittest.main()