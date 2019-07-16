import unittest

class TestUnittest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("from setupclass")

    @classmethod
    def tearDownClass(cls):
        print("from teardown class ")


    def setUp(self):
        print("from setup as login")

    def tearDown(self):
        print("from teardown as logout")

    def test_testadd(self):
        self.assertEqual(1+1,2)
        print("from testcase1")

    def test_testadd2(self):
        self.assertEqual(1+2,3)
        print("from testcase2")

    def test_testadd3(self):
        self.assertEqual(1+2,3)
        print("from testcase3")

if __name__=="__main__":

    print("test end##############################################")
    unittest.main()
