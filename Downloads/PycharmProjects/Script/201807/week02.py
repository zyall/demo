# 3. 定义一个函数，输入正整数a，输出一个字典，包含key为1到a, value为1到a的平方。
# 例如输入数字8，返回字典 {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}


def gather(a):
    d = {}
    for key in range(1, a):
        while key <= a:
            value = key * key
            d[key] = value
            key += 1
    return d


print(gather(8))


# 4. 把以英文冒号:隔开的字符串，按冒号分隔并转化为列表list和元祖tuple.
# 例如把字符串 this:is:a:test 转为["this", "is", "a", "test"] 和 ("this", "is", "a", “test")
str1='this:is:a:test'
print(str1.split(":"))
print(tuple(str1.split(":")))

# 题目：h
# 程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
# 在数学上，费波那契数列是以递归的方法来定义：
def fib(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a


print(fib(10))



