#!/usr/bin/python
# -*- coding:utf-8 -*-

import os

from xlrd import open_workbook
from Common.Log import MyLog as Log
import readConfig as conf

log = Log.get_log().logger

class ExcelHelper():
    '''
    从excel中获取测试用例
    '''
    def get_excel_by_list(self,xls_name,sheet_index):
        self.cls =[]
        try:
            xlspath = os.path.join(conf.proDir,'testFile',xls_name)
            if not os.path.exists(xlspath):
                os.mkdir(xlspath)
            file = open_workbook(xlspath)
            sheet = file.sheet_by_index(sheet_index)
            nrows = sheet.nrows
            for i in range(1,nrows):
                self.cls.append(sheet.row_values(i))
            log.info("Read Excel Successfully!")
            return self.cls
        except IOError as ex:
            log.error(str(ex))


if __name__ == '__main__':
    A = ExcelHelper()
    print(A.get_excel_by_list('test.xlsx',0))
