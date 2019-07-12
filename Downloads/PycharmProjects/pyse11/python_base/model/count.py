def add(a=1, b=2):
    '''用于计算（参数默认）a add b '''
    c = a + b
    return c


# 这个方法下的程序不会被别人调用到
if __name__ == '__mian__':
    print(add())
