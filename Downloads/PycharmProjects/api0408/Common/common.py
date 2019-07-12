import os
from xlrd import open_workbook
from xlwt import Workbook
from xlutils.copy import copy
from Common.Log import MyLog as Log
import readConfig as conf
from Common.configHttp import ConfigHttp
import logging

localConfigHttp = ConfigHttp()
log = Log.get_log()
logger = logging.getLogger()
class Excel():
    def __init__(self,xls_name,sheet_name):
        self.xlsPath = os.path.join(conf.proDir, "testFile", xls_name)
        self.sheet_name = sheet_name

    def get_xls(self):
        '''
        从excel文件中读取测试用例
        '''
        cls = []
        # get xls file's path
        # open xls file
        file = open_workbook(self.xlsPath)
        # get sheet by name
        sheet = file.sheet_by_name(self.sheet_name)
        # 获取行数
        nrows = sheet.nrows
        r = sheet.ncols
        # 获取列数
        # ncols = sheet.ncols
        # 读出每一行
        for i in range(1,nrows):
            cls.append(sheet.row_values(i))
        return cls
    def write_excel_xls(self,vlaue):
        index = len(vlaue)
        # 新建一个xls文件
        xls  = Workbook()
        sheet = xls.add_sheet(self.sheet_name)
        for i in range(0,index):
            for j in range(0,len(vlaue[i])):
                sheet.write(i,j,vlaue[i][j])
        xls.save(self.xlsPath)
        print("xls格式表格写入数据成功")
    def write_excel_xls_append_nclos(self,vlaue):
        index = len(vlaue)     #获取需要写入数据的行数
        xls = open_workbook(self.xlsPath)  # 打开工作薄
        sheets = xls.sheet_names()  # 获取工作薄中的所有表格
        worksheet = xls.sheet_by_name(sheets[0])  # 获取工作薄中所有表格中的第一个表格
        rows_old = worksheet.nrows  # 获取表格中已存在的数据的行数
        new_xls = copy(xls)  # 讲xlrd对象拷贝转换成xlwt对象
        new_worksheet = new_xls.get_sheet(0)  # 获取转化后工作薄中第一个表格
        for i in range(0, index):
            for j in range(1):
                new_worksheet.write(i+rows_old,5,vlaue[i][j])
        new_xls.save(self.xlsPath)
    def write_excel_xls_append_nrows(self,vlaue):
        index = len(vlaue)     #获取需要写入数据的行数
        xls = open_workbook(self.xlsPath)  # 打开工作薄
        sheets = xls.sheet_names()  # 获取工作薄中的所有表格
        worksheet = xls.sheet_by_name(sheets[0])  # 获取工作薄中所有表格中的第一个表格
        rows_old = worksheet.nrows  # 获取表格中已存在的数据的行数
        new_xls = copy(xls)  # 讲xlrd对象拷贝转换成xlwt对象
        new_worksheet = new_xls.get_sheet(0)  # 获取转化后工作薄中第一个表格
        for i in range(0, index):
            for j in range(0,len(vlaue[i])):
                new_worksheet.write(i+rows_old,j,vlaue[i][j])
        new_xls.save(self.xlsPath)

if __name__ == '__main__':
    A = Excel('sample.xls','test01')
    vlaue1 = [["sucess"],]

    A.write_excel_xls_append_nclos(vlaue1)






