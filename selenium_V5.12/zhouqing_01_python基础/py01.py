# -*- coding: utf-8 -*-

# 循环一个水仙花数

for a in range(100,1000):
    # 个位数
    b = a % 10
    # 十位数
    c = a // 10 % 10
    # 百位数
    d = a // 100
    if b ** 3 + c ** 3 + d ** 3 == a:
        print(a)

# 鸡兔同笼问题，一只笼子里有鸡和兔子，头的总数35个，腿的总数有94，使用循环求鸡有多少只，兔子有多少只
# 鸡 23  兔子 12
for x in range(35):
    y = 35 - x
    if 4 * x + 2 * y == 94:
        print("兔子%d只，鸡%d只" % (x, y))


class Phone():
    '''
    定义一个手机类，包含属性有品牌、颜色、屏幕尺寸大小，包含方法有打电话、发短信、听音乐，一个存在参数的返回值方法，打印手机的简介
    '''

    def __init__(self, Brand, color, Screen_size):
        self.Brand = Brand
        self.color = color
        self.Screen_size = Screen_size

    def call(self):
        call = '打电话'
        return call

    def send_message(self):
        SendMessage = '发短信'
        return SendMessage

    def listen_music(self):
        ListenMusic = '听音乐'
        return ListenMusic

    def introduction(self, call, SendMessage, ListenMusic):
        return ("品牌：%s,颜色：%s，屏幕尺寸大小：%s,手机功能：%s,%s,%s" % (
            self.Brand, self.color, self.Screen_size, call, SendMessage, ListenMusic))


if __name__ == '__main__':
    Phone = Phone('oppo', 'red', '1330')
    call = Phone.call()
    SendMessage = Phone.send_message()
    ListenMusic = Phone.listen_music()
    print(Phone.introduction(call, SendMessage, ListenMusic))
