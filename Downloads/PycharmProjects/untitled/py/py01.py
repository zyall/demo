import random,sys
name=input("输入姓名：")
n = 0
#用户输入姓名后生成1到100的随机数
target=random.randint(1,99)
print('I am thinking of a number between 1 and 100')
print(target)
#用户一共有5次猜测机会，5次没猜中游戏结束
while n < 5:
    n+=1
    while True:
        # 按q或Q退出游戏
        user_input =input("Take a guess or enter \"q\" to quit.\n")
        if user_input=='q' or user_input=='Q':
            sys.exit('Goodbye')
        # 实现输入validation，用户输入非数字的话要求重新输入
        if user_input.isdigit():
            user_input=int(user_input)
            break
        else:
            print("Invaild input")
    if user_input > target:
        print('your guess is too high')
    elif user_input < target:
        print('your guess is too low')
    else:
        print('Good job, the correct number is %s' %target)
        sys.exit(0)




