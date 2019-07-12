#coding=utf-8
#统计代码
''''
1.查看目录下所有的文件
2.遍历所有文件，打开每一个
3.统计所有文件的行数
'''
import os

'''
tmp=os.listdir('./')
#print(tmp)

all_codes=[f for f in tmp if f.split('.')[-1]=='py']
print(all_codes)

'''
class CodeStats:
    def __init__(self):
        self.code_lines=0
        self.blank_lines=0
        self.comment_lines=0


    def list_all_python_files(self):
        tmp=os.listdir('./')
        return [f for f in tmp if f.split('.')[-1]=='py']

    def stats(self):
        for d in self.list_all_python_files():
            with open(f,'rb') as file_handle:
                for line in file_handle.readlines():
                    striped_line=line.decode('utf-8').strip()
                    if striped_line == '':
                        self.blank_lines += 1
                    elif striped_line.startswith('#'):
                        seld.comment_lines += 1
                    else:
                        self.code_lines += 1
        return self


    def display(self):
        print("code lines: %s\nconment lines:%s\nblank lines:%s" %(self.code_lines))

