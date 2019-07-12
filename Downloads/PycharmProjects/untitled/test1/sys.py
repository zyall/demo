#coding=utf-8


import sys
sys.path.append('./test1') #将文件路径添加到环境变量
#print(sys.path)



from test1.jisuan2 import  add2 #从不同目录test1引用jisuan2

a=add2(3,5)

print(a)
'''
#python 引包机制
#同目录引用直接用import
import jisuan

寻找jisuan顺序

1.在当前目录下去找有没有jisuan
2.python 安装目录下找"C:\Python35\lib"目录下面找
3.PATH 目录下找

最后，都没有jisuan,这样一个模块的话，抛错

只需要做两步
1.把路径加过来
import sys
sys.path.append('./test1')
#print(sys.path)

2.创建一个空文件
./test1／__init__.py(python2需要做的)

'''
