class C1():
    def abc(self):
        print("1111")

    def cat(self):
        print(222)

class C2():
    def sss(self):
        print(333)

# 调试用
if __name__ =='__main__':
    # 实例化类
    c = C1()
    # 对象.调用方法
    c.cat()
    # C1.cat()
    # TypeError: cat() missing 1 required positional argument: 'self'

    # 原因： 实例化时，少了括号，或者方法里参数个数不匹配