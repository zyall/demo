#!/usr/bin/python
# -*- coding:utf-8 -*-


import logging
import os
import threading
from datetime import datetime

from config import readConfig as conf

proDir = conf.proDir

resultPath = os.path.join(proDir,"result")

class Log():
    def __init__(self):
        '''
        日志格式
        '''
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
    # 线程锁定
    mutex = threading.Lock()

    def __init__(self):
        pass
    @staticmethod
    def get_log():
        if MyLog.log is None:
            # 获取锁
            MyLog.mutex.acquire()
            MyLog.log = Log()
            # 释放锁
            MyLog.mutex.release()
        return MyLog.log

if __name__=='__main__':
    A = MyLog()
    A.get_log()