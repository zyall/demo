import unittest
from ddt import ddt,data,unpack

@ddt
class TestDDT(unittest.TestCase):
    test_data = ((100,1),(100,2),(100,3))
    @data(1,2,3,4,5)
    def test_aparam(self,num1):
        c = self.my_add(num1,2)
        print(c)

    @data((10,1),(10,2),(10,3))
    @unpack
    def test_two_param(self,num1,num2):
        print(self.my_add(num1,num2))

    @data(*test_data)
    @unpack
    def test_two_param2(self, num1, num2):
        print(self.my_add(num1, num2))

    def my_add(self,a,b):
        return a + b

if __name__ == "__main__":
    unittest.main()


