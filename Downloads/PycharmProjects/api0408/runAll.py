import unittest
import HTMLTestRunner
from Common.Log import *
import  readConfig as conf
log = MyLog.get_log()
logger = logging.getLogger()
class excute():
    def set_case_list(self):
        self.caseList = []
        TxtPath = os.path.join(conf.proDir,'caselist.txt')
        fb = open(TxtPath)
        for value in fb.readlines():
            data = str(value)
            if data != '' and not data.startswith("#"):
                self.caseList.append(data.replace("\n", ""))
        fb.close()
        return self.caseList

    def set_case_suite(self):
        self.set_case_list()
        test_suite = unittest.TestSuite()
        suite_model = []

        for case in self.caseList:
            testCase_file = os.path.join(conf.proDir, "testCase/user")
            print(testCase_file )
            case_name = case.split("/")[-1]
            print(case_name+".py")
            discover = unittest.defaultTestLoader.discover(testCase_file , pattern=case_name + '.py', top_level_dir=None)
            suite_model.append(discover)

        if len(suite_model) > 0:
            for suite in suite_model:
                for test_name in suite:
                    test_suite.addTest(test_name)
        else:
            return None
        return test_suite

    def run(self):
        try:
            suit = self.set_case_suite()
            reportPath = os.path.join(resultPath, str(datetime.now().strftime("%Y%m%d")),'report.html')
            # print(reportPath)
            if suit is not None:
                logger.info("********TEST START********")
                fp = open(reportPath, 'wb')
                runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test Report', description='Test Description')
                runner.run(suit)
            else:
                logger.info("Have no case to test.")
        except Exception as ex:
            logger.error(str(ex))
        finally:
            logger.info("*********TEST END*********")
            # # send test report by email
            # if int(on_off) == 0:
            #     # self.email.send_email()
            #     pass
            # elif int(on_off) == 1:
            #     logger.info("Doesn't send report email to developer.")
            # else:
            #     logger.info("Unknow state.")


if __name__ =='__main__':
    A = excute()
    C =A.set_case_list()
    # A.set_case_suite()
    A.run()
