'''
21. 写一个小游戏：小机器人的初始坐标为(0, 0)，机器人可以接收指定的命令来移动位置。当游戏结束时，打印出小机器人所在的坐标。例如控制台一次性输入如下命令：
UP 5
LEFT 3
DOWN 3
UP 2
RIGHT 7

输出最后的坐标（4, 4）
'''
#
# def  game():
#     p = (0,0)i
#     l = []
#     while True:
#         s= input(" ").split()
#         if not s:
#             break
#         l.append(s)
#     result = {}
#     for data in l:
#         result[data[0]] = int(result.get(data[0],0) + int(data[1])) #将重复key的数据累计
#     x = p[0] + result['UP'] - result['DOWN']
#     y = p[1] + result['RIGHT'] - result['LEFT']
#     point =(x,y)
#     return point
#
# print(game())

#思路
# l = []
# s = ['UP 5', 'LEFT 3', 'DOWN 3', 'UP 2', 'RIGHT 7']
# result = {}
# for i in s:
#     a = i.split()
#     l.append(a)
# for data in l:
#     result[data[0]] = int(result.get(data[0], 0) + int(data[1]))
# print(result)


# class Game():
#     def __init__(self):
#         self.lines = []
#         self.getenter()
#
#     def getenter(self):
#         while True:
#             self.s = input("").split()
#             if self.s:
#                 self.lines.append(self.s)
#             else:
#                 break
#         return self.lines
#
#     def getresult(self):
#         p = (0, 0)
#         result = {}
#         for data in self.lines:
#             result[data[0]] = int(result.get(data[0], 0) + int(data[1]))  # 将重复key的value累计
#         x = p[0] + result['UP'] - result['DOWN']
#         y = p[1] + result['RIGHT'] - result['LEFT']
#         point = (x, y)
#         return point
#
#
# if __name__ == '__main__':
#     c = Game()
#     print(c.getresult())
#


'''
22. 写一个词频统计的小程序，要求控制台输入一串英文单词/数字，统计所有单词出现的次数，排序（列表的sort函数）后输出到控制台。
例如输入：New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
输出：
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1
'''

from  collections import Counter

def con():
    s = input("enter:").split()
    # print(s)
    s.sort()
    a = Counter(s)            #生成一个Counter类
    cnt = dict(a)             #将a中的键值转成字典
    result = []
    for k, v in cnt.items():   #调用items()实现字典的遍历
        b = k + ":" + str(v)
        result.append(b)
    return '\n'.join(result)

print(con())




# class A():
#     def __init__(self):
#         self.sortdict()
#
#     def sortdict(self):
#         li = input("enter:").split()
#         li.sort()
#         self.re = {}
#         for i in li:
#             a = li.count(i)
#             self.re[i] = a
#         return self.re
#
#     def printresult(self):
#         result = []
#         for k in self.re:
#             b = k + ":" + str(self.re[k])
#             result.append(b)
#         return '\n'.join(result)
#
#
# if __name__ == "__main__":
#     c = A()
#     print(c.printresult())
