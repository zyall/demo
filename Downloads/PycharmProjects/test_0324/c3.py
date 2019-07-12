class C1():

    def __init__(self,a,b,c):
        # 构造方法，初始化方法
        # 全局变量
    # def __init__(self,a=1,b=2,c=3):
        self.a = a
        self.b = b
        self.c = c

    def fish(self,type,name):
        if type == self.a or name == self.c and name != self.b:
            print("我是金鱼")
        else:
            print("我不是金鱼")


if __name__ =='__main__':
    # 实例化类时需要加参数
    # A 就是对象
    A = C1(1,2,3)
    # 如果有默认值的时候，实例化类时可以不需要加参数，使用默认值
    # A = C1()
    # 对象.调用方法
    A.fish(1,6)
