# 单行注释
'''
多行注释


'''
#
# a = 1
# print(type(a))
#
# b = str(a)
#
# print(type(b))
#
# c = int(b)
# print(type(c))


# x = [1,2,3,4]
#
# print(len(x))
#
# print(x[0])
#
# print(x[3])
#
# for i in x :
#     print(i)
# 字典
#
# x = {'name':'zs','age':18}
#
# print(x['name'])

# 定义一个列表，立马包括学生的学号，性别，学历等信息

# 要求输出：


# l = ['周晴',1066999,'女','本科']
#
# print("我叫:%s,学号:%d,性别:%s,学历：%s" % (l[0], l[1], l[2],l[3]))

# # range(10)  0-9
#
# for i in range(10):
#     print(i,end=',')
#
# # range(1,10)  1-9
#
# for i in range(1,10):
#     print(i,end=',')
#
# # range(1,10,4)  (1,5,9)
# for i in range(1,10,4):
#     print(i,end=',')


# 1-50的奇数之和，偶数之和
# 奇数之和
'''
j = 0
o = 0
for i in range(1,51,2):
    # print(i, end=',')
    j += i

for x in range(2,51,2):
     # print(i,end = ',')
     o += x
print("奇数之和:%d,偶数之和:%d" %(j,o))



j = 0
o = 0
for i in range(1,51):
    if i % 2 == 0:
        o += i
    else:
        j += i
print("奇数之和:%d,偶数之和:%d" %(j,o))


# whlie 循环  
# 打印 1-10
a = 1
while(a<=10):
    print(a)
    a += 1

# 与或非
a = 5
b = 2
c = 'hello'
# and 连接的多个条件，同时成立，整个大的条件，才算成立
if a == 3 and b == 2:
    print(333)
# or 连接的多个条件，只要1个条件成立，那么大的条件就可以成立
if a > 3 or b < 3:
    print(444)
# not相反，如果连接的条件不成立，那么not+条件，就是成立
if not c == 'hell':
    print(555)

# 优先级 not > and > or
# if a > 2 and b < 3 or not c == 'hello':
# if (a > 2 and b < 3) or (not c == 'hello'):
#     print(666)

# for if ,将1-50 所有奇数之和，所有偶数之和打印
j = 0
o = 0

for i in range(1, 51):
    if i % 2 == 0:
        o += i
    else:
        j += i

print("奇数之和：%d，偶数之和：%d" % (j, o))

# 1- 10  少 8：
for i in range(1,11):
    if i == 8 :
        # continue : 终止本次循环，continue 下面的代码不再运行，继续下一轮循环
        continue
    print(i)

# 1-7
for i in range(1,11):
    if i == 8:
        # break:终止所有循环
        break
    print(i)



# try .... excpect
# 正常运行try里的代码， 如果try里出现代码异常，则异常下面的代码不运行
# 直接跳到except 中运行except里的代码
# try:
#     a = 1
#     b = 0
#     c = b/a
#     print(c)
# except:
#     print(111)


# 打印输出九九乘法表
# 几行  9行
for i in range(1,10):
    # 几列 第二行 2列
    for j in range(1,1+i):
        k = i * j
        print("%d*%d=%2d" % (i, j, i * j), end=' ')
        # print("{}*{}={}".format(i, j, k), end=' ')
    print()

# 冒泡排序

# 从键盘输入1个年份，判断是否为闰年
# x = input("输入1个年份:")  x为str类型
x = 1

while x <=3:
    try:
        years = int(input("输入1个年份:"))

        if years % 4 == 0 or years % 400 == 0 and years % 100 != 0:
            print("您输入的%d是闰年" % years)
            break
        else:
            print("您输入的%d不是闰年" % years)
            print("输入的不是闰年！您还有%d次机会" % (3 - x))
            x += 1
    except:
        print("输入有误，请输入一个数字！您还有%d次机会" % (3 - x))
    x += 1




for i in range(1, 6):
    # 先看几行
    # 空格 4，3，2，1，0  5 - i
    # *   1，3，5，7，9   2 * i - 1
    # i   1，2，3，4，5
    print(' ' * (5 - i), '*' * (2 * i - 1))

for i in range(1, 5):
    print(' ' * i, '*' * (9 - 2 * i))

# 给出一个字符串，有很多单词，单词之间用空格分隔，找出出现次数最高的单词

# "hello  how are you where are you from "

from collections import Counter
import operator
l = ('hello ,how are you where are you from : are').split(' ')
x = dict(Counter(l))
# # operator.itemgetter(1)：表示的是key : value 中的value
# # operator.itemgetter(0)：表示的是key : value 中的key
# # 用字典中的value去从大到小排序
y = sorted(x.items(),key=operator.itemgetter(1),reverse=True)
print(y[0][0])



def s(a,b):
    c = a + b
    return c

# 调用函数
x = s(1,2)

print(x)
'''

# 定义一个函数，实现功能

def s(a, b, c):
    if c == '*':
        l = a * b
    elif c == '+':
        l = a + b
    elif c == '/':
        try:
            l = a / b
        except:
            print("b不能为0")
            l = None
    elif c == '-':
        l = a - b
    else:
        raise NameError("输入有误")
    return l

x = s(1,0,'/')

print(x)