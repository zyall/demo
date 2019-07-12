'''
认识异常
BaseException   所有异常类的父类 包含Exception
Exception   包含所以的异常类（NameError、FileNotFoundError）

try:
    open('abc.txt', 'r')

except FileNotFoundError as e:

    print(e)


try:
    print(a)

except NameError as e:

    print(e)

try:
    print(a)

except BaseException as e:

    print(e)

# 格式
try:
    print(a)
except Exception as e:
    print(e)
else:
    print("no error")
finally:
    print("没有异常，都会被执行")

'''

from random import randint

'''生成一个1到9之间的随机整数'''
num = randint(1, 9)

if num % 2 == 0:
    raise NameError("%d is even" % num)
