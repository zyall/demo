#coding=utf-8

f=open('/Users/zq1/Downloads/sampleList.txt')
file=f.readlines()
f.close()
print(type(file))

''''
import sys


def cat(file_path):
    for path in file_path:
        with open(path,'rb') as f:
            print(f.read().decode('UTF-8'))

def cat_line(file_path):
    for path in file_path:
        with open(path,'rb') as f:
            start=1
            for line in f.readlines():
                print("%s %s" %(start,line.decode("UTF-8"))
                start=start+1
'''