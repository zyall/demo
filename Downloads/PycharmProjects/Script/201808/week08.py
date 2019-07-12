# 15. 控制台输入一位数的数字a，计算a+aa+aaa+aaaa的和作为结果输出。
# 例如输入：9
# 输出：11106
#
# a = str(input("输入："))
# b = a * 2
# c = a * 3
# d = a * 4
# sum2 = int(a) + int(c) + int(d) + int(b)
# print(sum2)
#
def num2():
    a = str(input("输入："))
    l = [a * i for i in range(1, 5)]
    s = sum(map(int, l))
    return s


print(num2())

# 16. 控制台输入一串以逗号隔开的数字，1. 筛选出其中的奇数，组成列表 2. 列表中的元素打印出来并以逗号隔开
# 要求：一共3行代码，控制台输入为一行，要求1为一行，要求2为一行。
# 例如输入：1,2,3,4,5,6,7,8,9
# 输出：1,3,5,7,9

s = input("输入：").split(',')
# l = list(filter(lambda i: int(i) % 2 != 0, s))
l = [i for i in s if int(i) % 2 != 0]
print("输出:{a}".format(a=','.join(l)))


