#open("abc.txt",'r')

#异常抛出
#FileNotFoundError

'''
try:
    open("abc.txt",'r')
except FileNotFoundError:
    print("file not found error!")
'''

try :
    print(aa)
except Exception as e:
    print(e)

#BaseException 是所有异常类父类
#Exception 继承BaseException，也可以看成有异常类父类