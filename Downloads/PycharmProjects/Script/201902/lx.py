# 统计在一个队列中的数字，有多少个正数，多少个负数，如[1, 3, 5, 7, 0, -1, -9, -4, -5, 8]
#
# # coding:utf-8
# a = [1, 3, 5, 7, 0, -1, -9, -4, -5, 8]
#
# # 用列表生成式，生成新的列表
# b = [i for i in a if i > 0]
# print("大于0的个数：%s" % len(b))
#
# c = [i for i in a if i < 0]
# print("小于0的个数：%s" % len(c))
#

#
# # 递归函数
#
# def fact(n):
#     if n == 1:
#         return 1
#     else:
#
#         return n * fact(n - 1)
#
#
# print(fact(5)


#冒泡排序

def  findsmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if arr[i]  < smallest:
            smallest = arr[i]
            smallest_index = i
    return  smallest_index

def  selctionsort(arr):
    newarr=[]
    for i in range (len(arr)):
        smallest = findsmallest(arr)
        newarr.append(arr.pop(smallest))
    return  newarr

l=[5,7,1,6]

print(selctionsort(l))







