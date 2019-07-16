import  unittest
from page.PageYoudao import PageYoudao

class TestYoudaoFramework(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.yd = PageYoudao()

    def test_add_note(self):
        self.yd.add_note("title","content")
        expect_result = self.yd.get_save_toast()
        self.assertEqual("保存成功",expect_result)

    def test_delete_note(self):
        before_del = self.yd.get_note_fist_title_text()
        before_del1=self.yd.get_note_fist_title_text_by_id()
        self.yd.del_note()
        after_del = self.yd.get_note_fist_title_text()
        after_del1 =self.yd.get_note_fist_title_text_by_id()
        print(before_del,after_del)
        print(before_del1, after_del1)
        self.assertNotEqual(before_del,after_del)
        self.assertNotEqual(before_del1, after_del1)



if __name__ == "__main__":
    unittest.main()