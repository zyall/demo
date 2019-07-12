# for i in range(2):
#     print(i)

# # test = "abcde"
# # l_test = ["a", "b", "c", "d"]
# #
# # print(test[2])
#
# d={'name':'Tom','age':'22'}
# d['sex'] = 'man'
# print(d)
# items=[x for x in input("请输入：").split(',')]
# items.sort()
# print (','.join(items))


# items=input("请输入：").split(',')
# items.sort()
# print (','.join(items))


# for a in range(1,4):
#     print(a)


#
# def my_abs(x):
#     if not isinstance(x, (int, float)):
#         raise TypeError('bad operand type')
#     if x >= 0:

# l = []
# for i in range(20, 30):
#     if i % 2 == 0:
#         l.append(i)
#

# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         # print(b)
#         yield b
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
#
# f=fib(10)
# for i in f:
#     print(i)
#
# l=[1]
# while True:
#     l.append(0)
#     print(l)

#     l.append(0)

# from operator import  itemgetter
# l=[('Tom', '19', '80'), ('John', '20', '92'), ('Jony', '20', '94'), ('Jony', '20', '93'), ('Json', '21', '85')]
# t = sorted(l, key=itemgetter(0,2,1),reverse=False)
# print(t)



# import django

def sortdict():
    li = input("enter:").split(" ")
    li.sort()
    d = {}
    for i in li:
        a = li.count(i)
        d[i] = a
    return d

#
# A = sortdict()
# print(A)
a = {'2': 2, '3.': 1, '3?': 1, 'New': 1, 'Python': 5, 'Read': 1, 'and': 1, 'between': 1, 'choosing': 1, 'or': 2,
     'to': 1}
for key in a:
    print(key + ":" + str(a[key]))
