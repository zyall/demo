
from count import add


def add_bb():
    c = add()
    return c


# 这个方法下的程序不会被别人调用到
if __name__ == '__mian__':
    print(add_bb())
