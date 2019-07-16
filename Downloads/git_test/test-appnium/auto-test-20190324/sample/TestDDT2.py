import unittest
from ddt import ddt,data,unpack
import csv
import os
from utils.common import get_parent_path

def get_data_csv(filename):
    numbers = []
    with open(filename,'r',encoding='utf-8') as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            numbers.append(row)
    return numbers


@ddt
class TestDDT2(unittest.TestCase):
    print(os.getcwd())
    root_path = get_parent_path(os.getcwd())
    print(root_path)
    data_path = os.path.join(root_path, "data","numbers.csv")
    test_data = get_data_csv(data_path)
    @data(*test_data)
    @unpack
    def test_two_param(self,num1,num2,expect):
        int1= int(num1)
        int2 = int(num2)
        int_expect = int(expect)
        actual_result = self.my_add(int1,int2)
        self.assertEqual(actual_result,int_expect)
        print(num1, ' ', num2, ' ', expect)



    def my_add(self,a,b):
        return a + b

if __name__ == "__main__":
    unittest.main()