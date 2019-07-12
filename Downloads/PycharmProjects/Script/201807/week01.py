#
# 1.定义一个函数，找出2000-3200之间（包括左右边界），所有能被7整除但不能被5整除的数字。
# 数字与数字之间用逗号隔开。
# 提示：range()
'''
def number():
    l = []
    for i in range(2000, 3201):
        if i % 7 == 0 and i % 5 != 0:
            l.append(str(i))
    return ','.join(l)


print(number())

# def number():
#     test = ''
#     for i in range(2000, 3201):
#         if i % 7 == 0 and i % 5 != 0:
#             test += str(i) + ','
#     return test.strip(',')
#     # print(test)
#
#
# print(number())


# 2.定义一个函数，输入任意数字，输出该数字的阶乘运算结果。
# 例如输入8，函数返回8的阶乘结果：40320
# 提示：while循环 or 递归
def factorial(n):
    if (n <= 1):
        return 1
    else:
        return factorial(n - 1) * n


# n = int(input("请输入："))
print("结果:", factorial(8))


# def factorial():
#     n = int(input("请输入："))
#     su = 1
#     while n > 1:
#         su = su * n
#         n = n - 1
#     return su
#
#
# print("结果:", factorial())
# 3.找出列表中重复的元素

# l = [3, 3, 1, 2]
# a = []
# for i in l:
#     if l.count(i) == 2:
#         a.append(i)
# print(a)


排序算法
'''


def findSmallest(arr):
    smallest = arr[0]             #存储最小的值
    smallest_index = 0            #存储最小元素的索引
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):              #对数组进行排序
    newarr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)        #找出数组中最小的元素并将其加入到新数组中
        newarr.append(arr.pop(smallest))
    return newarr


arr = [5, 2, 3, 6, 7]
print(selectionSort(arr))
