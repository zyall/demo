# #--coding:utf-8--
import xlrd
file = xlrd.open_workbook('test.xlsx')

print(file.sheet_names())

# 通过工作表名称获取excel
table = file.sheet_by_name('工作表1')
# 获取行数
nrows = table.nrows
# print(nrows)
# 获取列数
ncols = table.ncols
# print(ncols)
# 获取整行的值
# print(table.row_values(0))
# 获取整列的值
# print(table.col_values(0))
cls = []
for  i in range(nrows):
    if table.row_values(i)[0] != u'模块':
        cls.append(table.row_values(i))
print(cls)