#!/usr/bin/python
# -*- coding:utf-8 -*-


import logging
from datetime import datetime
import readConfig as conf
import threading,os

proDir = conf.proDir

resultPath = os.path.join(proDir,"result")

class Log():
    def __init__(self):
        global logpath,proDir,resultPath
        if not os.path.exists(resultPath):
            os.mkdir(resultPath)
        logpath = os.path.join(resultPath,str(datetime.now().strftime("%Y%m%d")))
        if not os.path.exists(logpath):
            os.mkdir(logpath)
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        handler = logging.FileHandler(os.path.join(logpath,'output.log'))
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
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

if __name__=='__main__':
    A = MyLog()
    A.get_log()