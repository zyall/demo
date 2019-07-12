'''
print(1)
# 常用的数据类型
# a 变量
a = 1
b = '1'
# <class 'str'>
print(type(b))
# <class 'int'>
print(type(a))
# 字符串的截取

a = "hello,world"

# print(a[0:5])
# print(a[:5])
#
# a1 = a.split(',')[0]
# print(a1)
a2 = a.split(',')[1]
print(a[-5:])
print(a2)

# a = " hello,world "
#
# a1 = a.strip()[:5]
#
# a2 = a.split(',')[0].strip()
a = " hello,,,,?world "

# a2 = a.split(',')[0].strip()    strip去掉空格
# print(a1)
# print(a2)
name = '张三'
age = 19
# print("my name is %s" % name)
print("my name is %s, i am %d years old" % (name, age))

# 列表
l = [1, 2, 3, 4, 5]

# print(l[0])
# 方法1
for i in l:
    print(i)
# 方法2
for i in range(len(l)):
    print(l[i])

# 列表元素添加
l = [1, 2, 3, 4, 5]
l.append(6)
print(l)

# 元组 tuple
tuple = (1,2,3,4,5)
print(tuple[0])

# 字典
dict1 = {'name':'zhangshan','age':18}
print(dict1['name'])

# 自定义一个列表，里面包含学生的姓名，籍贯，年龄等信息
# 输出一句话：我叫** 籍贯** 年龄**

# 列表
l = ['zhangshan', 'jiangxi', 18]
print("我叫:%s,籍贯:%s,年龄:%d" % (l[0], l[1], l[2]))
# 字典
d = {'name': 'zhangsan', 'jiguan': 'jiangxi', 'age': 19}
print("我叫:%s,籍贯:%s,年龄:%d" % (d['name'], d['jiguan'], d['age']))


# if .... else(条件判断）  一定要2个==
# 缩进：tab  反缩进：shift+tab
age = 18
if age > 18:
    print(111)
elif age == 18:
    print(222)
else:
    print(333)
# if ... if... if vs  if...elif esle 区别

# 与或非
a = 1
b = 2
c = 3
# and 与  连接的多个条件同时成立，整个条件才算成立
if a == 2 and b > 2:
    print(111)
# or 或 谅解的多个条件，只要有1个成立，那么整个条件就成立
if a > 3 or b < 3:
    print(222)
# != 表示不等于
# not 表示非
if not c != 3:
    print(333)
# 优先级 not > and > or
# if [(not a > 1) or (b != 2 and c > 5)]:
if not a > 1 or b != 2 and c > 5:
    print(444)
# range(10) 默认从0开始，比10小，每次加1
# 0-9
# for i in range(10):
#     print(i)
# # range(2,10) 从2开始，比10小，每次加1
# 2-9
# for i in range(2,10):
#     print(i)

# range(2,10,3) 表示从2开始，比10小，每次加3
# 2,5,8
# for i in range(2,10,3):
#     print(i)

# # 联系 打印 1 4 7 10 13 16 19 22 25
#
# for i in range(1, 26, 3):
#     print(i)
# 计算 1-100 所有的奇数之和，所有的偶数之和
# j = x = 0
# for i in range(1, 101):
#     # % 取余
#     if i % 2 == 1:
#         j += i
#     else:
#         x += i
#
# print("计算 1-100 所有的奇数之和：%d，所有的偶数之和：%d" % (j, x))
#输出 1-20 所有的数
# a = 1
# while (a <= 20):
#     print(a)
#     a += 1
# 使用while循环打印1，2，3，4，6，7，8，9，10
# 方法1
# a = 0
# while a <= 9:
#     a += 1
#     if a != 5:
#         print(a)
# a = 1
# while a <= 10:
#     if a != 5:
#         print(a)
#     a += 1

# #方法2 continue:结束本次循环，继续下一轮循环
# y = 0
# while(y<=9):
#     y += 1
#     if y == 5:
#         continue
#     #     下面的代码不会再执行
#     print(y)
# 打印1，2，3，4，6，7，8，9，10
# for i in range(1,11):
#     if i == 5:
#         continue
#     print(i)
# break:终止所有的循环  打印 1，2，3，4
# for i in range(1,11):
#     if i == 5:
#         break
#     print(i)
#打印 1，2，3，4，6，7，9，10，11，13，14，15，16，17，19，20，21，22，23，24，25，26
# 1-27 少了 5,8,12,18,23
# l = [5, 8, 12, 18, 23]
# for i in range(1, 27):
#     if i in l:
#         continue
#     print(i)
# 给出2个数a和b，计算a/b的值，如果b = 0 ,则打印"b 不能为0"
# 异常处理（方便定位问题）
# 方法1
# a = 4
# b = 2
# if b == 0:
#     print("b不能为0")
# else:
#     x = a / b
#     print("a/b的值：%r" % x)

# 方法2
# try:
#     a = 4
#     b = 0
#     x = a / b
#     print("a/b的值：%r" % x)
# except:
#     print("b不能为0")

# 类型转换
a = 1
# int -> str
b = str(a)
# <class 'int'>
print(type(a))
# <class 'str'>
print(type(b))
# str -> int
c = '1'
d = int(c)
print(type(c))
print(type(d))

# list -> tuple
l = [1, 2, 3]
l1 = tuple(l)
print(type(l))
print(type(l1))
# tuple -> list
z = (1, 2, 3)
z1 = list(z)
print(type(z))
print(type(z1))
# 自定义一个变量a，如果a变量是字符串类型，转换成int类型
a = '123'
#  判断变量a是否是str类型
if isinstance(a, str):
    b = int(a)
    print(int(b))
    # <class 'int'>
    print(type(b))
b = 123.0
# 判断变量b是否是float类型
if isinstance(b,float):
    c = int(b)
    print(c)
    # <class 'int'>
    print(type(c))

# 从键盘输入一个数字，随机生成1个数（1-100）
import random
j = random.randint(1, 100)
print("随机数是：%d" %j)
i = input("从键盘输入一个数字：")
if j > int(i):
    print(111)
elif j == int(i):
    print(222)
else:
    print(333)

#
# 如果键盘输入的数字>随机数，就退出程序
# 如果键盘输入的数字<随机数，或者输入的不是数字，就可以有3次连续输入的机会
import random
x = 1
while (x <= 3):
    try:
        j = random.randint(1, 100)
        i =int(input("从键盘输入一个数字："))
        print("随机数是：%d,键盘数是：%d" % (j, i))
        if j > i:
            print(111)
        elif j <= i:
            print("您当前输入键盘输入的数字<随机数，还有%d次机会" % (x, 3 - x))
            x += 1
        else:
            break
    except:
        print("您输入的不是数字！您当前输入的第%d次，还有%d次机会" % (x, 3 - x))
        x += 1

# 输入如下图形
'''
'''

*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''
'''
# 方法1
for i in range(1,10):
    if i <= 5:
        print('*' * i)
    else:
        print('*' * (10-i))

# 方法2
for i in range(1,6):
    print('*' * i)
for j in range(4):
    print('*' * (4-j))
'''
'''
*
***
*****
*******
*********
*******
*****
***
*

'''
# for i in range(1, 10, 2):
#     print('*' * i)
# for j in range(1, 8, 2):
#     print('*' * (8 - j))
# 打印等腰三角形
# for i in range(1, 6):
#     print(" " * (5 - i), '*' * (2 * i - 1))
# 1,2,3,4
# 7,5,3,1
# 打印菱形
# for i in range(1, 6):
#     print(" " * (5 - i), '*' * (2 * i - 1))
# for j in range(1,5):
#     print(" " * j , '*' * (9 - 2 * j))
# 打印九九乘法表
# 几行
# for i in range(1, 10):
#     # 几列
#     for j in range(1, 1 + i):
#         k = i * j
#         # 在某一行，所有列输出完之后，才能换行
#         print("{}*{}={}".format(i, j, k), end=' ')
#         # print("%d*%d=%2d"%(i, j, i * j), end=' ')
#     # 在某行所有列都输出完之后，才换行
#     print()

# 冒泡排序（相邻的2个数进行比较，将大的数放在后面，依次类推，从而达到从小到大排序的效果）
# 给出一组数，从小到大排序
# 第一轮 比较2次

# 第二轮 比较1次

# l = [3,2,1]
# for i in range(len(l)-1):
#     for j in range(len(l)-1-i):
#         if l[j] > l[j+1]:
#             l[j],l[j+1]=l[j+1],l[j]
# print(l)
# l = [3,2,1]
# # 从小到大排序
# # l.sort(reverse=False)
# # 从大到小
# # l.sort(reverse=True)
# b = sorted(l,reverse=False)
# # print(l)
# print(b)

# 给出一组数（很多重复数据），统计最大数的个数
# l = [5,7,4,8,8,8]
# l2 = sorted(l,reverse=True)
# x = 0
# for i in range(len(l)):
#     if l[i] == l2[0]:
#         x += 1
# print(x)

# 方法2
# max(a) 找出列表中a中最大数
# a.count(x)  在列表a中统计元素X出现的次数
# x = l.count(max(l))
# print(x)

# 给出一组数（很多重复数据）,按照出现的次数从多到少排序
# from collections import Counter
# import operator
# l = [5,7,4,8,8,8]
# # 转换为字典
# x = dict(Counter(l))
# print(x)
# # operator.itemgetter(1)：表示的是key : value 中的value
# # operator.itemgetter(0)：表示的是key : value 中的key
# # 用字典中的value去从大到小排序
# y = sorted(x.items(),key=operator.itemgetter(1),reverse=True)
# print(y)

# 给出一组数（很多重复数据）,去重
# 方法1
# l = [5,7,4,8,8,8]
# l2 =list(set(l))
# print(l2)
#方法2
# l2 =[]
# for i in l:
#     if i not in l2:
#         l2.append(i)
# print(l2)


# 从键盘输入1个年份，判断该年份是否是闰年
# x = 1
# while x <= 3:
#     try:
#         years = int(input("输入年份："))
#         if years % 4 == 0 or years % 400 == 0 and years % 100 != 0:
#             print("您输入的%d是闰年" %years)
#             break
#         else:
#             print("输入的不是闰年！您还有%d次机会" % (3 - x))
#             x += 1
#     except:
#         print("输入不是数字！您还有%d次机会" % (3 - x))
#         x += 1

# 查找某个子目录及其子目录下，打印输出所有包含某字符串的文件名
# 提示：os

import os

def search_file(path,str):
    # 列出path这个路径下所有的文件名或目录名
    files=os.listdir(path)
    print(files)
    for i in files:
        # 连接path和文件
        x = os.path.join(path,i)
        # 判断x是不是文件
        if os.path.isfile(x):
            if str in x:
                print(x)
        else:
            search_file(x,str)
if __name__ =='__main__':
    search_file('/Users/zq1/Downloads/PycharmProjects/test_0324/','5')


#
