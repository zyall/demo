#!/usr/bin/python
# -*- coding:utf-8 -*-

import os

from xlrd import open_workbook
from conf import *


class ExcelHelper():
    '''
    从excel中获取测试用例
    输出结果为[{列名1：第一列1，列名2：第一列2}, {列名1：第二列1，列名2：第二列2}...]
    '''
    def get_excel_by_list(self,xls_name,sheet_index):
        cls =[]
        try:
            # 打开excel
            file = open_workbook(xls_name)
            # 通过sheet_index，获取工作表
            table = file.sheet_by_index(sheet_index)
            # 获取行数
            nrows = table.nrows
            # 获取第一行数据
            fisrtncorls = table.row_values(0)
            # 获取列数
            nclos = table.ncols
            for i in range(1,nrows):
                row = table.row_values(i)
                if row:
                    excel_dict = {}
                    for i in range(nclos):
                        excel_dict[fisrtncorls[i]] = row[i]
                    cls.append(excel_dict)
            logger.info("Read Excel Successfully!")
            return cls
        except IOError as ex:
            logger.error(str(ex))


if __name__ == '__main__':
    xls_name = xlsPath+'/test.xlsx'
    A = ExcelHelper()
    x = A.get_excel_by_list(xls_name,0)
    print(x)


