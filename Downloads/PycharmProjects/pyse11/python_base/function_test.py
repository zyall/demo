'''
用引号
1.多行注释
2.类、方法、函数内部注释
'''


def add(a=1, b=2):
    '''用于计算（参数默认）a add b '''
    return a + b


# print(add(5, 7))

# print(help(add))

#类和方法
'''
class jisuan(object):

class jisuan():

class jisuan:



class A():
    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def add(self):
        return self.a + self.b

    def sub(self):
        '''调用add函数'''
        C = self.add()
        return C


class B(A):
    '''B继承A'''

    def __init__(self, a, b, c):
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)

    def add(self):
        return self.a + self.b + self.c


c = B(5, 7, 3).add()
print(c)
'''


