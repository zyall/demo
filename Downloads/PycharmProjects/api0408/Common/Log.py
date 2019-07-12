import logging
import os
from datetime import datetime
import threading
import readConfig as conf

proDir = conf.proDir
resultPath = os.path.join(proDir, "result")

class Log():
    def __init__(self):
        global logPath, resultPath, proDir
        # create result file if it doesn't exist
        if not os.path.exists(resultPath):
            os.mkdir(resultPath)
        # defined test result file name by localtime
        logPath = os.path.join(resultPath, str(datetime.now().strftime("%Y%m%d")))
        # create test result file if it doesn't exist
        if not os.path.exists(logPath):
            os.mkdir(logPath)
        # 定义 logger对象
        self.logger = logging.getLogger()
        # 设置从哪个个等级开始提示
        self.logger.setLevel(logging.INFO)
        # 定义文件对象
        handler = logging.FileHandler(os.path.join(logPath, "output.log"))
        # 设置格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # defined formatter
        handler.setFormatter(formatter)
        # logger对象添加文件输出流
        self.logger.addHandler(handler)

class MyLog():
    log = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_log():

        if MyLog.log is None:
            MyLog.mutex.acquire()
            MyLog.log = Log()
            MyLog.mutex.release()

        return MyLog.log

if __name__ == '__main__':
    A = Log()
    print(A)