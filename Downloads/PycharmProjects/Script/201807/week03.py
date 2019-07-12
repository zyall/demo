# 5. 定义一个类，里面至少有2个功能函数：A函数接收控制台输入的字符串，B函数打印出A函数接收到字符串的大写字母
# 提示：可以用__init__函数定义一个公共参数

# class A():
#     def __init__(self):
#         self.s = ''
#         self.accpet()
#
#     def accpet(self):
#         self.s = input("请输入：")
#
#     def print1(self):
#         print("***打印字符串的大写字母***")
#         print(self.s.upper())
#
#     def print2(self):
#         print("***打印字符串中的大写字母***")
#         for i in self.s:
#             if i.isupper() == True:
#                 print(i, end='')
# if __name__ == "__main__":
#     A().print2()


# 6. 定义一个函数，输入一串以逗号隔开的数字，每个数字按固定公式计算出结果，以逗号隔开输出。
# 公式：X = [(2*C*D)/H] 再开平方根。其中C和H是常量，C=50，H=30
# 例子：输入：100,150,180 输出：18,22,24
# 提示：输出的结果如果是小数，应该向下取整收起

#
def numb():
    l = input("请输入：").split(',')
    C = 50
    H = 30
    test = ''
    #print(l)
    for i in l:
        x = ((2 * C * int(i)) / H) ** 0.5
        test += str(int(x)) + ','
    return test.strip(',')


print(numb())

# def numb():
#     l = input("请输入：").split(',')
#     C = 50
#     H = 30
#     test = []
#     for i in l:
#         x = ((2 * C * int(i)) / H) ** 0.5
#         test.append(str(int(x)))
#     return ','.join(test)




print(numb())
