# 7. 定义一个函数，控制台依次输入两个数字x, y，生成一个二维数组a（例：a=[[1,2], [3,4], [5,6]]，a[2][1]=6，即6这个值有2个维度）。数组中第x行第y列的值，为x*y
# 如：依次输入 3 和 5
# 中间计算：1. 横轴的值为0, 1, 2；纵轴的值为0, 1, 2, 3, 4；
# 2.得到具体长度的目标数组 [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]] （一维 len(a)长度为3，二维 len(a[1]) 长度为5）
# 输出结果：用纵轴横轴的各个值相乘，得出目标结果 [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
#
def arry():
    i = input("输入：").split(',')

    x = int(i[0])
    y = int(i[1])
    a = [[col * row for col in range(y)] for row in range(x)]    #二维数组
    # a = [[0 for col in y] for row in x]
    # for i in x:
    #     for j in y:
    #         a[i][j] = i * j
    return a
print(arry())

# 8. 控制台输入一串以逗号隔开的英文单词，要求把这些单词按字母表前后排序后作为结果输出。
# 如：输入 without,hello,bag,world
# 输出 bag,hello,without,world
#
# #
# def strt():
#     s = input("请输入：").split(',')
#     s.sort()
#     print(s)
#     # l = sorted(s, key=str.lower)
#     return ','.join(list(s))
#
# print(strt())
#
#
# def strt(s):
#     return s.sort()


s = input("请输入：").split(',')
s1 = map(sort, s)
print(s1)
print(s)



# # items=[x for x in raw_input().split(',')]
# # items.sort()
# # print (','.join(items))
#
# print(arry())
#
