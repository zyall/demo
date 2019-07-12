# 19. 控制台（一次性）输入一组格式为“姓名(str)，年龄(int)，身高(int)”的数据，要求对这组数据按 姓名>身高>年龄 优先级排序，按格式输出到控制台。
# 例如输入：
# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85
#l=[('Tom', '19', '80'), ('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85')]
# 要求输出：
# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80’)]


from operator import itemgetter

l = []
while True:
    s = input("")
    if s:
        l.append(tuple(s.split(',')))
        t = sorted(l, key=itemgetter(0, 2, 1), reverse=False)
    else:
        break
print(t)

# 20. 定义一个函数，要求计算出0到指定入参x之间，能被7整除的数字迭代器（generator）。出参需要是一个迭代器
# 提示：可以用yield函数
# yield的作用就是把一个函数变成一个generator，带有yield的函数不再是一个普通函数。
# 在for循环执行时，每次循环都会执行fab函数内部的代码，执行导yield时，fab函数就会返回一个迭代值，下次迭代是代码从
# yield的下一条语句继续执行
# #
def triangles(x):
    for i in range(x + 1):
        if i % 7 == 0:
            yield i


# print(triangles(100))


for t in triangles(100):
    print(t)
