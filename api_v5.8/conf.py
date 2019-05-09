#!/usr/bin/python
# -*- coding:utf-8 -*-

import logging,os
from datetime import datetime


# ============================ Global parameter ==============================
baseurl = 'http://'
headers ={'content-Type':''}
timeout = 1.0

proDir = os.path.split(os.path.realpath(__file__))[0]
xlsPath = os.path.join(proDir, 'testFile')
testCasePath = os.path.join(proDir, 'testCase')
caseListPath = os.path.join(proDir,'caseList.txt')

# ============================ Logger config ==============================
resultPath = os.path.join(proDir,'result',str(datetime.now().strftime("%Y%m%d")))
if not os.path.exists(resultPath):
    os.mkdir(resultPath)
reportpath = os.path.join(resultPath,'report.html')
logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.FileHandler(os.path.join(resultPath,'output.log'))
formatter = logging.Formatter("%(asctime)s %(filename)s[line:%(lineno)d]-%(levelname)s %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

# ============================ email config ==============================
smtp_sever = "smtp.qq.com"
email_name = "1554754887@qq.com"
email_password = "123900600all"
email_To = "1554754887@qq.com"
